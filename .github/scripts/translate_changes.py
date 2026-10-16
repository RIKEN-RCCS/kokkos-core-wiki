#!/usr/bin/env python3
"""
Translate changed RST/MD files from main branch to Japanese using Claude API.

Only blocks (blank-line-separated chunks) that actually changed are sent to
Claude. Unchanged blocks retain their existing Japanese translation, preserving
any manual improvements.

Environment variables:
    AWS_BEARER_TOKEN_BEDROCK: Amazon Bedrock API key (required)
    AWS_DEFAULT_REGION: AWS region for bedrock-mantle (default: us-east-1)

Usage:
    python translate_changes.py \\
        --main-dir /path/to/main \\
        --japanese-dir /path/to/japanese \\
        --before-sha <sha>

    # Translate specific files (skips git diff, retranslates whole file):
    python translate_changes.py \\
        --main-dir /path/to/main \\
        --japanese-dir /path/to/japanese \\
        --files docs/source/foo.rst docs/source/bar.rst
"""

import argparse
import difflib
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from typing import Optional

from anthropic import AnthropicBedrockMantle

SYSTEM_PROMPT = """\
You are a technical documentation translator specializing in translating \
reStructuredText (RST) documentation from English to Japanese for the \
Kokkos C++ performance portability library.

Rules:
- Translate all natural language text to natural, professional Japanese.
- Preserve all RST markup exactly: directives, roles, hyperlinks, \
substitutions, footnotes, code blocks, tables, and indentation.
- Keep code blocks, function/class/variable names, and CLI syntax in English.
- Keep all URLs, file paths, and option names in English.
- For section title underlines/overlines, the underline must be as long as \
the display width of the title. CJK characters count as width 2; ASCII \
characters count as width 1. Adjust the underline length accordingly.
- RST inline markup (**strong**, *emphasis*, ``literal``, `interpreted text`, \
roles, and `references`_) requires whitespace or punctuation immediately \
before its opening marker and immediately after its closing marker. Japanese \
has no spaces between words, so a literal translation often glues a particle \
or word directly onto the marker (e.g. "**3月**に"), which breaks RST parsing. \
When natural Japanese phrasing would place a kana/kanji character directly \
against a markup delimiter, insert an escaped space — a backslash followed \
by a space, e.g. "**3月**\\ に" — right there. It satisfies the whitespace \
requirement without producing a visible space in the rendered output. The \
same problem occurs with a fullwidth bracket: a closing marker directly \
followed by an opening bracket like "（" (e.g. ":cpp:`x`（例）"), or a closing \
bracket like "）" directly followed by an opening marker, both need the same \
escaped-space treatment, e.g. ":cpp:`x`\\ （例）".
- Do not add explanations, comments, or extra blank lines outside the RST.
- Output only the translated RST content.\
"""

RST_UNDERLINE_CHARS = set("=-~^\"#+*`:./<>")

# If more than this fraction of old_en blocks can't be structurally aligned to
# a Japanese block, fall back to full-file retranslation.
BLOCK_DRIFT_THRESHOLD = 0.20


# ---------------------------------------------------------------------------
# RST utilities
# ---------------------------------------------------------------------------

def display_width(text: str) -> int:
    """Return terminal display width (CJK = 2, others = 1)."""
    return sum(
        2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
        for ch in text
    )


def _is_underline(line: str) -> bool:
    # Real section adornment lines are always flush-left; indented runs of a
    # single repeated character are list-table/bullet-list artifacts (e.g. a
    # bare "-" or "*" marking an empty cell), not title underlines.
    if not line or line[0] in (" ", "\t"):
        return False
    stripped = line.rstrip()
    return bool(stripped) and len(set(stripped)) == 1 and stripped[0] in RST_UNDERLINE_CHARS


def _is_title(line: str) -> bool:
    return bool(line.strip()) and line == line.lstrip() and not _is_underline(line)


def fix_underlines(content: str, rel_path: str) -> str:
    """Ensure every RST title underline/overline matches the title's display width.

    No-op for non-.rst files: in Markdown a run of identical characters is
    often a code fence (```) rather than a title underline, and "fixing" it
    would corrupt the fence.
    """
    if not rel_path.lower().endswith(".rst"):
        return content

    lines = content.split("\n")
    result = list(lines)

    for i, line in enumerate(lines):
        if not _is_underline(line):
            continue
        char = line.strip()[0]
        # Overline pattern: [i] overline, [i+1] title, [i+2] underline
        if i + 2 < len(lines) and _is_underline(lines[i + 2]) and _is_title(lines[i + 1]):
            width = display_width(lines[i + 1].strip())
            result[i] = char * width
            result[i + 2] = char * width
        # Underline pattern: [i-1] title, [i] underline
        elif i > 0 and _is_title(lines[i - 1]):
            width = display_width(lines[i - 1].strip())
            result[i] = char * width

    return "\n".join(result)


# RST requires whitespace or punctuation immediately outside an inline-markup
# delimiter; a Hiragana/Katakana/Kanji letter butted directly against one
# breaks that rule (see docutils' start_string_prefix / end_string_suffix).
# Punctuation like "、"/"。" is already accepted by docutils, so only flag
# actual CJK *letters* — this also keeps the check from ever firing inside
# real code (which is ASCII), so it can't corrupt a literal block.
def _is_cjk_letter(ch: Optional[str]) -> bool:
    if ch is None:
        return False
    return (
        unicodedata.category(ch) in ("Lo", "Lm")
        and unicodedata.east_asian_width(ch) in ("W", "F")
    )


# docutils' start_string_prefix additionally accepts an *opening* bracket
# immediately before an opening delimiter (e.g. "(**foo**"), and its
# end_string_suffix accepts a *closing* bracket immediately after a closing
# delimiter (e.g. "**foo**)"). The other pairing is not accepted: a fullwidth
# closing bracket right before an opening delimiter ("）**foo**") or a
# fullwidth opening bracket right after a closing delimiter ("**foo**（") both
# break RST parsing the same way a bare CJK letter does. Scoped to the common
# Japanese bracket pairs rather than all Unicode punctuation, to keep the
# false-positive risk (accidentally rewriting real code) low.
_FULLWIDTH_OPENERS = "（「『【〔《〈｛［"
_FULLWIDTH_CLOSERS = "）」』】〕》〉｝］"


def _needs_prefix_escape(ch: Optional[str]) -> bool:
    """Whether `ch`, sitting immediately before an opening delimiter, needs
    an escaped space inserted after it."""
    return _is_cjk_letter(ch) or (ch is not None and ch in _FULLWIDTH_CLOSERS)


def _needs_suffix_escape(ch: Optional[str]) -> bool:
    """Whether `ch`, sitting immediately after a closing delimiter, needs
    an escaped space inserted before it."""
    return _is_cjk_letter(ch) or (ch is not None and ch in _FULLWIDTH_OPENERS)


# Matches **strong**, ``literal``, *emphasis*, and `interpreted text`/`role`/
# `reference`_/`anonymous reference`__ spans (longest delimiter tried first
# via the backreference). Requires no whitespace just inside either
# delimiter and no blank line inside the body, mirroring docutils' own
# start-/end-string rules closely enough to avoid matching bullet-list "* "
# markers or spanning across paragraph breaks.
_INLINE_MARKUP_RE = re.compile(
    r"(?P<delim>\*\*|``|\*|`)(?!\s)"
    r"(?:(?!(?P=delim))[^\n]|\n(?!\n))+?"
    r"(?<!\s)(?P=delim)(?:__|_)?"
)


def fix_inline_markup_spacing(content: str, rel_path: str) -> str:
    """Insert an escaped space (``\\ ``) around RST inline markup whose
    delimiter directly touches a CJK letter or an unpaired fullwidth bracket,
    e.g. turn ``**3月**に`` into ``**3月**\\ に``, or
    ``:cpp:`x`（例）`` into ``:cpp:`x`\\ （例）``. Without it, Sphinx's ``-W``
    build fails with "Inline strong/interpreted text start-string without
    end-string" (or, inside a C++ role, an "Unparseable C++ cross-reference").

    This is a backstop for translations that don't follow the escaped-space
    instruction in SYSTEM_PROMPT. No-op for non-.rst files, matching
    fix_underlines: Markdown has no such adjacency rule.
    """
    if not rel_path.lower().endswith(".rst"):
        return content

    def repl(m: re.Match) -> str:
        start, end = m.span()
        before = content[start - 1] if start > 0 else None
        after = content[end] if end < len(content) else None
        prefix = "\\ " if _needs_prefix_escape(before) else ""
        suffix = "\\ " if _needs_suffix_escape(after) else ""
        return prefix + m.group(0) + suffix

    return _INLINE_MARKUP_RE.sub(repl, content)


def postprocess_rst(content: str, rel_path: str) -> str:
    """Run all deterministic, non-LLM RST fixups on translated content."""
    content = fix_underlines(content, rel_path)
    content = fix_inline_markup_spacing(content, rel_path)
    return content


# ---------------------------------------------------------------------------
# Block splitting
# ---------------------------------------------------------------------------

def split_blocks(content: str) -> list[str]:
    """Split RST/MD content into non-empty blocks separated by blank lines.

    Only strips leading/trailing newlines, not spaces: many blocks (literal
    blocks, indented list continuations, block quotes) are meaningfully
    indented on their first line, and str.strip() would eat that indentation.
    """
    return [b.strip("\n") for b in re.split(r"\n{2,}", content.strip("\n")) if b.strip()]


def join_blocks(blocks: list[str]) -> str:
    return "\n\n".join(blocks) + "\n"


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def get_changed_files(
    repo_dir: str, before_sha: str, after_sha: str = "HEAD"
) -> list[tuple[Optional[str], Optional[str]]]:
    """Return (old_rel_path, new_rel_path) pairs for RST/MD files added,
    modified, copied, deleted, or renamed between two commits.
    old_rel_path is None for additions/copies; new_rel_path is None for
    deletions; both are set (and may differ) for renames."""
    if before_sha == "0" * 40:
        # First push or force push — translate all tracked RST/MD files
        out = subprocess.run(
            ["git", "ls-files", "--", "*.rst", "*.md"],
            cwd=repo_dir, capture_output=True, text=True, check=True,
        ).stdout
        return [(None, p) for p in out.strip().splitlines() if p]

    out = subprocess.run(
        ["git", "diff", "--name-status", "-M", "--diff-filter=ACMDR",
         before_sha, after_sha, "--", "*.rst", "*.md"],
        cwd=repo_dir, capture_output=True, text=True, check=True,
    ).stdout

    changes: list[tuple[Optional[str], Optional[str]]] = []
    for line in out.strip().splitlines():
        if not line:
            continue
        fields = line.split("\t")
        status = fields[0]
        if status.startswith("R"):
            changes.append((fields[1], fields[2]))
        elif status.startswith("C"):
            changes.append((None, fields[2]))
        elif status == "D":
            changes.append((fields[1], None))
        else:  # A or M
            changes.append((fields[1] if status == "M" else None, fields[1]))
    return changes


def get_file_at_commit(repo_dir: str, rel_path: str, sha: str) -> Optional[str]:
    """Return file content at the given commit, or None if it didn't exist."""
    try:
        return subprocess.run(
            ["git", "show", f"{sha}:{rel_path}"],
            cwd=repo_dir, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return None


def read_main_file(main_dir: str, rel_path: str, ref: Optional[str]) -> Optional[str]:
    """Read a main-branch file's content.

    When ref is given, read it via `git show ref:path` so the content
    reflects that exact commit regardless of what's currently checked out in
    main_dir (main_dir just needs to be a clone of main with enough history
    to contain ref — this keeps translation results independent of whichever
    commit happens to be checked out, e.g. an older SHA targeted by a manual
    workflow_dispatch re-run). Otherwise read directly from the working tree
    (used by --files, which has no associated commit).
    """
    if ref is None:
        path = Path(main_dir) / rel_path
        return path.read_text(encoding="utf-8") if path.exists() else None
    return get_file_at_commit(main_dir, rel_path, ref)


# ---------------------------------------------------------------------------
# Translation via Claude API
# ---------------------------------------------------------------------------

def _call_claude(client: AnthropicBedrockMantle, user_message: str) -> str:
    response = client.messages.create(
        model="anthropic.claude-opus-4-8",
        max_tokens=8192,
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def translate_whole_file(
    client: AnthropicBedrockMantle,
    new_en: str,
    current_ja: Optional[str],
    rel_path: str,
) -> str:
    """Translate an entire file (used for new files or when block mapping fails)."""
    if current_ja:
        msg = (
            f"The file `{rel_path}` has been updated in the English (main) branch.\n"
            "Translate the new English version to Japanese.\n"
            "The existing Japanese translation is provided for reference to maintain "
            "consistency in terminology and style.\n\n"
            f"<existing_japanese>\n{current_ja}\n</existing_japanese>\n\n"
            f"<new_english>\n{new_en}\n</new_english>\n\n"
            "Output only the complete translated RST content."
        )
    else:
        msg = (
            f"Translate the following RST file `{rel_path}` from English to Japanese.\n\n"
            f"<english>\n{new_en}\n</english>\n\n"
            "Output only the complete translated RST content."
        )
    return _call_claude(client, msg)


def _leading_spaces(line: str) -> str:
    return line[: len(line) - len(line.lstrip(" "))]


def _reapply_first_line_indent(source_block: str, translated_block: str) -> str:
    """Claude frequently drops the leading whitespace on just the first line
    of a translated block (right after the `<t id="N">` tag) even though it
    faithfully keeps the indentation on every other line of the same block.
    Restore it from the source block's own first-line indent when that
    mismatch is detected."""
    src_indent = _leading_spaces(source_block.split("\n", 1)[0])
    if not src_indent:
        return translated_block
    lines = translated_block.split("\n")
    if not lines[0].startswith(src_indent):
        lines[0] = src_indent + lines[0].lstrip(" ")
    return "\n".join(lines)


def translate_blocks_batch(
    client: AnthropicBedrockMantle,
    items: list[tuple[str, Optional[str]]],  # (new_en_block, prev_ja_block | None)
    rel_path: str,
) -> dict[int, str]:
    """
    Translate a list of changed blocks in a single API call.
    Returns {index: translated_block}.
    """
    parts = []
    for i, (en, prev_ja) in enumerate(items):
        part = f'<b id="{i}">\n<en>\n{en}\n</en>\n'
        if prev_ja:
            part += f"<prev>\n{prev_ja}\n</prev>\n"
        part += "</b>"
        parts.append(part)

    msg = (
        f"Translate the following RST blocks from English to Japanese for `{rel_path}`.\n"
        "The <prev> tag (if present) is the previous Japanese translation of that block; "
        "use it only for terminology consistency.\n"
        'Output each translation as: <t id="N">translated content</t>\n\n'
        + "\n\n".join(parts)
    )
    text = _call_claude(client, msg)

    result: dict[int, str] = {}
    for m in re.finditer(r'<t id="(\d+)">(.*?)</t>', text, re.DOTALL):
        idx = int(m.group(1))
        translated = m.group(2).strip("\n")
        if 0 <= idx < len(items):
            translated = _reapply_first_line_indent(items[idx][0], translated)
        result[idx] = translated
    return result


# ---------------------------------------------------------------------------
# Block alignment (old_en <-> current_ja)
# ---------------------------------------------------------------------------

# Directives whose argument is code/paths rather than prose, so it survives
# translation unchanged and can tell e.g. overloaded cpp:function blocks apart.
# Domain directives (anything with ":" in the name, e.g. cpp:function) are
# included as well.
_VERBATIM_ARG_DIRECTIVES = {
    "code-block", "code", "sourcecode", "literalinclude", "include",
    "image", "figure", "highlight", "role",
}
_DIRECTIVE_RE = re.compile(r"\.\.\s+([\w:.-]+)::\s*(.*)")
_SUBST_DEF_RE = re.compile(r"\.\.\s+(\|[^|]+\|)")
_LIST_MARKER_RE = re.compile(r"(?:([-*+])|\d+[.)]|#\.|\(\d+\))\s")
_INLINE_LITERAL_RE = re.compile(r"``(?!\s)(.+?)(?<!\s)``")


def _block_key(block: str) -> tuple[str, str]:
    """Return (coarse, fine) structural signatures of a block that are
    (normally) identical for an English block and its Japanese translation.

    coarse is the indentation plus the block category (directive, title,
    list, text, ...). fine adds the directive name and any verbatim parts
    such as C++ signatures, link targets, and the set of ``literals`` in the
    block. Prose itself is deliberately left out of both.
    """
    lines = block.split("\n")
    first = lines[0]
    indent = len(_leading_spaces(first))
    s = first.strip()

    if s == ".." or s.startswith(".. "):
        if s.startswith(".. _"):
            category, detail = "target", s  # hyperlink target: entirely verbatim
        elif (m := _SUBST_DEF_RE.match(s)):
            category, detail = "subst", m.group(1)
        elif (m := _DIRECTIVE_RE.match(s)):
            name, arg = m.groups()
            verbatim = ":" in name or name in _VERBATIM_ARG_DIRECTIVES
            category, detail = "directive", name + (f" {arg}" if verbatim else "")
        else:
            category, detail = "comment", ""
    elif len(lines) > 1 and _is_title(first) and _is_underline(lines[1]):
        category, detail = "title", lines[1][0]
    elif len(lines) > 2 and _is_underline(first) and _is_underline(lines[2]):
        category, detail = "overtitle", first[0]
    elif s.startswith("#"):  # Markdown heading
        category, detail = "md-heading", s.split(" ", 1)[0]
    elif s.startswith("```"):  # Markdown code fence
        category, detail = "md-fence", s
    else:
        m = _LIST_MARKER_RE.match(s)
        category = "list" if m else "text"
        detail = (m.group(1) or "enum") if m else ""
        # Translation reflows lines, so collect literals from the whole block.
        literals = sorted(set(_INLINE_LITERAL_RE.findall(block)))
        if literals:
            detail += " " + " ".join(literals)

    coarse = f"{indent}|{category}"
    return coarse, f"{coarse} {detail}"


def align_blocks(
    old_blocks: list[str], ja_blocks: list[str]
) -> tuple[list[list[int]], list[int]]:
    """Map each old_en block to the Japanese block(s) that translate it.

    Blocks are matched by _block_key with difflib, rather than by position:
    a manually edited translation can merge or split blocks (e.g. a missing
    or extra blank line), and a positional mapping silently shifts every
    later block by one.

    Returns (groups, prefix). groups[i] lists the ja block indices owned by
    old block i: the ja block structurally matched to it, followed by any
    unmatched ja blocks up to the next match. groups[i] is empty when old
    block i matched nothing. prefix lists unmatched ja blocks before the
    first match.
    """
    old_keys = [_block_key(b) for b in old_blocks]
    ja_keys = [_block_key(b) for b in ja_blocks]
    sm = difflib.SequenceMatcher(
        None, [k[1] for k in old_keys], [k[1] for k in ja_keys], autojunk=False
    )
    owner_of_ja: dict[int, int] = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            pairs = zip(range(i1, i2), range(j1, j2))
        elif (
            tag == "replace"
            and i2 - i1 == j2 - j1
            and all(old_keys[i1 + k][0] == ja_keys[j1 + k][0] for k in range(i2 - i1))
        ):
            # Same number and kinds of blocks whose details differ (e.g. a
            # stale or hand-edited translation): pair them up in order.
            pairs = zip(range(i1, i2), range(j1, j2))
        else:
            continue
        for i, j in pairs:
            owner_of_ja[j] = i

    groups: list[list[int]] = [[] for _ in old_blocks]
    prefix: list[int] = []
    current: Optional[int] = None
    for j in range(len(ja_blocks)):
        if j in owner_of_ja:
            current = owner_of_ja[j]
        (prefix if current is None else groups[current]).append(j)
    return groups, prefix


def build_diff_plan(
    old_blocks: list[str], new_blocks: list[str], ja_blocks: list[str]
) -> "tuple[list[str | int], list[tuple[str, Optional[str]]]] | str":
    """Plan the Japanese output for a diff-based translation.

    Returns (plan, to_translate): plan items are either a Japanese block to
    keep verbatim or an index into to_translate, whose entries are
    (new_en_block, prev_ja_block | None). Returns a reason string instead
    when the change can't be applied safely and the caller should
    retranslate the whole file.
    """
    groups, prefix = align_blocks(old_blocks, ja_blocks)

    unmatched = sum(1 for g in groups if not g)
    if old_blocks and unmatched / len(old_blocks) > BLOCK_DRIFT_THRESHOLD:
        return (
            f"block structure mismatch ({unmatched} of {len(old_blocks)} "
            "old_en blocks have no Japanese counterpart)"
        )

    def is_clean(i: int) -> bool:
        """Old block i corresponds to exactly one Japanese block."""
        return len(groups[i]) == 1

    def is_safe_change(i1: int, i2: int) -> bool:
        """Whether old[i1:i2] can be replaced (or a block inserted at i1)
        without touching Japanese text that belongs to other blocks."""
        if i1 == 0 and prefix:
            return False
        # The changed blocks and the block just before them must each map to
        # exactly one Japanese block: a removed block may otherwise share its
        # Japanese text with a kept neighbour, or the change may land on the
        # wrong side of an unmatched Japanese block.
        if not all(is_clean(i) for i in range(max(i1 - 1, 0), i2)):
            return False
        # The block just after only needs a counterpart of its own, i.e. it
        # wasn't merged into the Japanese text of a changed block.
        return i2 == len(old_blocks) or bool(groups[i2])

    sm = difflib.SequenceMatcher(None, old_blocks, new_blocks, autojunk=False)

    to_translate: list[tuple[str, Optional[str]]] = []
    plan: list[str | int] = [ja_blocks[j] for j in prefix]

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for i in range(i1, i2):
                plan.extend(ja_blocks[j] for j in groups[i])
            continue

        if not is_safe_change(i1, i2):
            return f"cannot locate changed old_en blocks {i1}-{i2} in the Japanese file"

        for k in range(j2 - j1):
            prev_ja = ja_blocks[groups[i1 + k][0]] if i1 + k < i2 else None
            plan.append(len(to_translate))
            to_translate.append((new_blocks[j1 + k], prev_ja))
        # tag == "delete": the Japanese blocks of old[i1:i2] are dropped

    return plan, to_translate


# ---------------------------------------------------------------------------
# Core: diff-based translation
# ---------------------------------------------------------------------------

def translate_with_diff(
    client: AnthropicBedrockMantle,
    old_en: str,
    new_en: str,
    current_ja: str,
    rel_path: str,
) -> str:
    """
    Translate only the blocks that changed between old_en and new_en.
    Unchanged blocks are taken directly from current_ja.

    Falls back to full-file retranslation when the changed blocks can't be
    located safely in current_ja (see build_diff_plan).
    """
    new_blocks = split_blocks(new_en)
    built = build_diff_plan(split_blocks(old_en), new_blocks, split_blocks(current_ja))
    if isinstance(built, str):
        print(f"    [warn] {built} → full retranslation")
        result = translate_whole_file(client, new_en, current_ja, rel_path)
        return postprocess_rst(result, rel_path)
    plan, to_translate = built

    if not to_translate:
        print("    no changed blocks detected")
        return current_ja

    total = len(new_blocks)
    changed = len(to_translate)
    print(f"    translating {changed} changed block(s) (of {total} total)")

    translations = translate_blocks_batch(client, to_translate, rel_path)

    result_blocks: list[str] = []
    for item in plan:
        if isinstance(item, str):
            result_blocks.append(item)
        else:
            translated = translations.get(item)
            if translated is None:
                # Fallback: keep English if Claude failed to produce a translation
                translated, _ = to_translate[item]
            result_blocks.append(translated)

    return postprocess_rst(join_blocks(result_blocks), rel_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate changed RST/MD blocks to Japanese."
    )
    parser.add_argument("--main-dir", default=".", help="Path to main branch checkout")
    parser.add_argument("--japanese-dir", required=True, help="Path to Japanese branch checkout")
    parser.add_argument("--before-sha", default="", help="Git SHA before the push")
    parser.add_argument("--after-sha", default="HEAD", help="Git SHA after the push")
    parser.add_argument(
        "--files", nargs="+", metavar="FILE",
        help="Specific files to translate (whole-file retranslation; skips git diff)"
    )
    args = parser.parse_args()

    client = AnthropicBedrockMantle(
        aws_region=os.environ.get("AWS_DEFAULT_REGION", "us-east-1"),
    )

    if args.files:
        changed = [(f, f) for f in args.files]
        use_diff = False
        after_ref: Optional[str] = None
    elif args.before_sha:
        changed = get_changed_files(args.main_dir, args.before_sha, args.after_sha)
        use_diff = args.before_sha != "0" * 40
        after_ref = args.after_sha
    else:
        parser.error("Provide either --before-sha or --files.")

    if not changed:
        print("No RST/MD files changed.")
        return

    print(f"Files to process ({len(changed)}):")
    for old_rel_path, new_rel_path in changed:
        if new_rel_path is None:
            print(f"  {old_rel_path} (deleted)")
        elif old_rel_path and old_rel_path != new_rel_path:
            print(f"  {old_rel_path} -> {new_rel_path} (renamed)")
        else:
            print(f"  {new_rel_path}")

    errors: list[tuple[str, Exception]] = []

    for old_rel_path, new_rel_path in changed:
        if new_rel_path is None:
            # Deleted from main — remove the corresponding Japanese file.
            japanese_file = Path(args.japanese_dir) / old_rel_path
            if japanese_file.exists():
                japanese_file.unlink()
                print(f"[delete] {old_rel_path} removed from main; deleted {japanese_file}")
            else:
                print(f"[skip] deleted: {old_rel_path} (no Japanese file to remove)")
            continue

        japanese_file = Path(args.japanese_dir) / new_rel_path

        new_en = read_main_file(args.main_dir, new_rel_path, after_ref)
        if new_en is None:
            print(f"[skip] missing in main: {new_rel_path}")
            continue

        renamed = old_rel_path is not None and old_rel_path != new_rel_path
        if renamed:
            old_japanese_file = Path(args.japanese_dir) / old_rel_path
            if old_japanese_file.exists() and not japanese_file.exists():
                japanese_file.parent.mkdir(parents=True, exist_ok=True)
                old_japanese_file.rename(japanese_file)
                print(f"[move] {old_japanese_file} -> {japanese_file}")
            elif old_japanese_file.exists():
                # A file already exists at the new path — drop the stale duplicate.
                old_japanese_file.unlink()

        current_ja = japanese_file.read_text(encoding="utf-8") if japanese_file.exists() else None

        print(f"[translate] {new_rel_path} ...", flush=True)
        try:
            if use_diff and current_ja and old_rel_path:
                old_en = get_file_at_commit(args.main_dir, old_rel_path, args.before_sha)
                if old_en:
                    result = translate_with_diff(client, old_en, new_en, current_ja, new_rel_path)
                else:
                    # File is new in this push
                    result = postprocess_rst(
                        translate_whole_file(client, new_en, None, new_rel_path),
                        new_rel_path,
                    )
            else:
                result = postprocess_rst(
                    translate_whole_file(client, new_en, current_ja, new_rel_path),
                    new_rel_path,
                )

            japanese_file.parent.mkdir(parents=True, exist_ok=True)
            japanese_file.write_text(result, encoding="utf-8")
            print(f"    written: {japanese_file}")
        except Exception as exc:
            print(f"    ERROR: {exc}")
            errors.append((new_rel_path, exc))

    if errors:
        print("\nFailed files:")
        for path, err in errors:
            print(f"  {path}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
