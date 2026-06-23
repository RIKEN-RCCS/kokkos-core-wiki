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
- Do not add explanations, comments, or extra blank lines outside the RST.
- Output only the translated RST content.\
"""

RST_UNDERLINE_CHARS = set("=-~^\"#+*`:./<>")

# If the ratio of block counts between old_en and ja differs by more than this,
# fall back to full-file retranslation.
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
    stripped = line.strip()
    return bool(stripped) and len(set(stripped)) == 1 and stripped[0] in RST_UNDERLINE_CHARS


def fix_underlines(content: str) -> str:
    """Ensure every RST title underline/overline matches the title's display width."""
    lines = content.split("\n")
    result = list(lines)

    for i, line in enumerate(lines):
        if not _is_underline(line):
            continue
        char = line.strip()[0]
        # Overline pattern: [i] overline, [i+1] title, [i+2] underline
        if i + 2 < len(lines) and _is_underline(lines[i + 2]) and lines[i + 1].strip():
            width = display_width(lines[i + 1].strip())
            result[i] = char * width
            result[i + 2] = char * width
        # Underline pattern: [i-1] title, [i] underline
        elif i > 0 and lines[i - 1].strip() and not _is_underline(lines[i - 1]):
            width = display_width(lines[i - 1].strip())
            result[i] = char * width

    return "\n".join(result)


# ---------------------------------------------------------------------------
# Block splitting
# ---------------------------------------------------------------------------

def split_blocks(content: str) -> list[str]:
    """Split RST/MD content into non-empty blocks separated by blank lines."""
    return [b.strip() for b in re.split(r"\n{2,}", content.strip()) if b.strip()]


def join_blocks(blocks: list[str]) -> str:
    return "\n\n".join(blocks) + "\n"


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def get_changed_files(repo_dir: str, before_sha: str, after_sha: str = "HEAD") -> list[str]:
    """Return relative paths of RST/MD files changed between two commits."""
    if before_sha == "0" * 40:
        # First push or force push — translate all tracked RST/MD files
        out = subprocess.run(
            ["git", "ls-files", "--", "*.rst", "*.md"],
            cwd=repo_dir, capture_output=True, text=True, check=True,
        ).stdout
    else:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACM",
             before_sha, after_sha, "--", "*.rst", "*.md"],
            cwd=repo_dir, capture_output=True, text=True, check=True,
        ).stdout
    return [p for p in out.strip().splitlines() if p]


def get_file_at_commit(repo_dir: str, rel_path: str, sha: str) -> Optional[str]:
    """Return file content at the given commit, or None if it didn't exist."""
    try:
        return subprocess.run(
            ["git", "show", f"{sha}:{rel_path}"],
            cwd=repo_dir, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return None


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
        result[int(m.group(1))] = m.group(2).strip()
    return result


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

    Falls back to full-file retranslation when the block structure of old_en
    and current_ja diverge by more than BLOCK_DRIFT_THRESHOLD.
    """
    old_blocks = split_blocks(old_en)
    new_blocks = split_blocks(new_en)
    ja_blocks = split_blocks(current_ja)

    # Structural alignment check
    if old_blocks:
        drift = abs(len(old_blocks) - len(ja_blocks)) / len(old_blocks)
        if drift > BLOCK_DRIFT_THRESHOLD:
            print(
                f"    [warn] block count mismatch "
                f"(old_en={len(old_blocks)}, ja={len(ja_blocks)}, drift={drift:.0%}) "
                "→ full retranslation"
            )
            result = translate_whole_file(client, new_en, current_ja, rel_path)
            return fix_underlines(result)

    # Diff old_en blocks vs new_en blocks
    sm = difflib.SequenceMatcher(None, old_blocks, new_blocks, autojunk=False)

    # Build a plan: either a literal block string or an index into to_translate
    to_translate: list[tuple[str, Optional[str]]] = []  # (new_en_block, prev_ja_block|None)
    plan: list[str | int] = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                ja_idx = i1 + k
                plan.append(ja_blocks[ja_idx] if ja_idx < len(ja_blocks) else new_blocks[j1 + k])

        elif tag in ("replace", "insert"):
            for k in range(j2 - j1):
                new_block = new_blocks[j1 + k]
                prev_ja = (
                    ja_blocks[i1 + k]
                    if tag == "replace" and (i1 + k) < len(ja_blocks)
                    else None
                )
                plan.append(len(to_translate))
                to_translate.append((new_block, prev_ja))

        # tag == "delete": omit those ja blocks

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

    return fix_underlines(join_blocks(result_blocks))


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
        changed = args.files
        use_diff = False
    elif args.before_sha:
        changed = get_changed_files(args.main_dir, args.before_sha, args.after_sha)
        use_diff = args.before_sha != "0" * 40
    else:
        parser.error("Provide either --before-sha or --files.")

    if not changed:
        print("No RST/MD files changed.")
        return

    print(f"Files to process ({len(changed)}):")
    for f in changed:
        print(f"  {f}")

    errors: list[tuple[str, Exception]] = []

    for rel_path in changed:
        main_file = Path(args.main_dir) / rel_path
        japanese_file = Path(args.japanese_dir) / rel_path

        if not main_file.exists():
            print(f"[skip] deleted: {rel_path}")
            continue

        new_en = main_file.read_text(encoding="utf-8")
        current_ja = japanese_file.read_text(encoding="utf-8") if japanese_file.exists() else None

        print(f"[translate] {rel_path} ...", flush=True)
        try:
            if use_diff and current_ja and args.before_sha:
                old_en = get_file_at_commit(args.main_dir, rel_path, args.before_sha)
                if old_en:
                    result = translate_with_diff(client, old_en, new_en, current_ja, rel_path)
                else:
                    # File is new in this push
                    result = fix_underlines(
                        translate_whole_file(client, new_en, None, rel_path)
                    )
            else:
                result = fix_underlines(
                    translate_whole_file(client, new_en, current_ja, rel_path)
                )

            japanese_file.parent.mkdir(parents=True, exist_ok=True)
            japanese_file.write_text(result, encoding="utf-8")
            print(f"    written: {japanese_file}")
        except Exception as exc:
            print(f"    ERROR: {exc}")
            errors.append((rel_path, exc))

    if errors:
        print("\nFailed files:")
        for path, err in errors:
            print(f"  {path}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
