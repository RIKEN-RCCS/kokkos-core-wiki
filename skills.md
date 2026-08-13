# skills.md

`Japanese` ブランチの自動翻訳パイプラインと、そこで発生する Sphinx ビルド警告の調査・修正に関する知見をまとめる。

## 全体像

1. `main` に `docs/source/**/*.rst` または `*.md` の変更が push される
2. `.github/workflows/auto-translate.yml` が起動し、`main` と `Japanese` を別ディレクトリにチェックアウト
3. `.github/scripts/translate_changes.py` が `before_sha`〜`after_sha` 間で変更されたブロック(空行区切りの段落単位)のみを Claude(AWS Bedrock 経由)で翻訳し、未変更ブロックは既存の日本語訳をそのまま流用する
4. 結果を `Japanese` ブランチ上でコミットし、`auto-translate/main-<after_sha>` ブランチを作成・push し、`Japanese` 向けに PR を自動作成する

`translate_changes.py` は `main` と `Japanese` の両ブランチに同一内容で存在する。スクリプト自体の修正は原則として両ブランチに反映する。

## Sphinx ビルド警告(`-W` エラー)の調査手順

1. **まずクリーンビルドする**。`docs/generated_docs/` や Sphinx の doctree キャッシュが残っていると警告が再現しないことがある。
   ```sh
   cd docs && make clean && make html
   ```
2. 警告行から対象ファイルと行番号を特定する(例: `.../release-process.rst:18: WARNING: Inline strong start-string without end-string. [docutils]`)。
3. 疑わしい行を `docutils.core.publish_doctree` に直接渡して最小再現させると、Sphinx 全体をビルドし直さずに高速に切り分けられる:
   ```python
   from docutils.core import publish_doctree
   publish_doctree("該当行のテキスト", settings_overrides={'report_level': 1})
   ```
   これを使って文字列を少しずつ削り、原因の文字位置をピンポイントで特定できる(print と警告の出力先が stdout/stderr で異なるため、順序を確認したい場合は都度 `sys.stdout.flush()` / `sys.stderr.flush()` を挟むこと)。

## RST インライン記法 vs CJK 文字隣接問題

### 原因

docutils はインライン記法(`**strong**` / `*emphasis*` / `` `literal` `` / `` `interpreted text` `` / `` `reference`_ `` など)の**開始記号の直前**と**終了記号の直後**に、空白または特定の句読点が来ることを要求する(`docutils.parsers.rst.states.Inliner` の `start_string_prefix` / `end_string_suffix` 正規表現で規定)。

日本語は分かち書きをしないため、翻訳結果が `**11 月**に` のように助詞や単語を記号へ直接接続してしまいやすい。「、」「。」などの句読点は docutils の許可リストに含まれるため問題ないが、かな・漢字などの通常の文字が直接続くと**終了記号として認識されず**、
`Inline strong start-string without end-string.`(または interpreted text / phrase reference の同種警告)になる。

### 修正方法

問題箇所の記号の直後(または直前)に **エスケープ空白** `\ `(バックスラッシュ+半角スペース)を挿入する。これは構文上は空白として扱われて記号を正しく終端させるが、レンダリング結果には見えないスペースとして出力される(見た目上の余計な空白を作らずに済む)。

```rst
Kokkos は、**3 月**、**7 月**、**11 月**\ にリリースを行う、...
```

### 恒久対策(`translate_changes.py`)

1. `SYSTEM_PROMPT` にこのルールと `\ ` によるエスケープ空白の使い方を明記し、Claude が翻訳時点でこの問題を作らないよう誘導している。
2. それでも漏れた場合の決定的なバックストップとして `fix_inline_markup_spacing()` を実装済み(`fix_underlines()` と同じ「LLM 出力への非LLM後処理」パターン)。
   - `**strong**` / `*emphasis*` / `` `interpreted` `` / `` `reference`_ `` / `` `reference`__ `` / ``` ``literal``` ``` のスパンを検出
   - 記号の外側に隣接する文字が `unicodedata.category(ch) in ("Lo", "Lm")` かつ `east_asian_width(ch) in ("W", "F")`(＝ひらがな・カタカナ・漢字)のときだけ `\ ` を自動挿入する
   - 句読点(`、` `。` など)や ASCII・コードには反応しないため、リスト項目のマーカー(`* `)や実際のコードブロックを誤って書き換えるリスクは低い
   - `fix_underlines()` と合わせて `postprocess_rst()` にまとめられており、翻訳結果を書き込む全箇所(`translate_with_diff` の全量再翻訳フォールバック、差分翻訳結果、`main()` 内の新規/全量翻訳の2箇所)がこれを通る
   - `.md` ファイルには適用しない(Markdown にはこの隣接ルールが存在しないため。`fix_underlines()` と同じ理由)

### この対策の既知の限界

- 対象は「かな・カタカナ・漢字がインライン記法の記号に直接接触するケース」に絞ってある。全角数字・記号など他の Unicode 幅広文字への隣接は意図的にスコープ外(誤検知でコード片を壊すリスクを避けるため)。
- 段落(空行区切りブロック)をまたぐマッチはしないよう正規表現側で制御しているが、完全な RST パーサーではないため、複雑な入れ子構造では取りこぼす可能性がある。実運用上問題が見つかれば `fix_inline_markup_spacing()`(`.github/scripts/translate_changes.py`)を拡張する。
