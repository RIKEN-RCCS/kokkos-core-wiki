# CLAUDE.md

このリポジトリは Kokkos のドキュメンテーションサイト(https://kokkos.github.io/kokkos-core-wiki/)のソースです。
このファイルは、このリポジトリで作業する Claude Code インスタンスのためのプロジェクト概要です。

## リポジトリ構成

- `docs/source/` — ドキュメント本体(`.rst` / `.md` 混在、Sphinx + MyST でビルド)
- `docs/Makefile` — ビルド定義(下記参照)
- `docs/generated_docs/` — ビルド成果物(`make clean` で削除される、通常はコミットしない)
- `build_requirements.txt` — ローカルビルド用の Python 依存関係(`pip install -r build_requirements.txt`)
- `.github/workflows/auto-translate.yml` — `main` → `Japanese` ブランチへの自動翻訳ワークフロー
- `.github/scripts/translate_changes.py` — 上記ワークフローが呼ぶ翻訳スクリプト本体。詳細は [skills.md](skills.md) を参照

## ブランチ構成

- `main` — 英語の正本(ソース・オブ・トゥルース)
- `Japanese` — `main` の内容を自動翻訳した日本語ブランチ。`auto-translate.yml` が `main` への push を検知し、`translate_changes.py` で差分翻訳した上で `Japanese` 向けの PR を自動作成する
- リモートは2つ:
  - `origin` = `RIKEN-RCCS/kokkos-core-wiki`(このフォーク。日本語翻訳の運用元)
  - `upstream` = `kokkos/kokkos-core-wiki`(本家)

`Japanese` ブランチへの変更(翻訳スクリプトの修正など)は、まず `Japanese` 上でコミットし、スクリプト自体の修正など `main` にも反映すべき変更は個別に `main` へもコミット・push する(このリポジトリでは `main` への直接 push が可能で、PR 必須のブランチ保護はかかっていない)。

## ビルドとテスト

```sh
cd docs
make html   # sphinx-build -b html ./source/ ./generated_docs/ -W --keep-going
make clean  # rm -rf ./generated_docs/
```

- `-W` により **Sphinx の警告はすべてビルドエラー**になる(`build finished with problems, N warning(s) (with warnings treated as errors)`)。
- **注意**: `generated_docs/`(や Sphinx の doctree キャッシュ)が残っていると、実際には存在する警告が再ビルド時に再現しないことがある。警告の有無を正確に確認したいときは必ず `make clean && make html` でクリーンビルドすること。
- `make html` は sphinx-build の後に `python3 ./source/edit_button_handler.py` を実行し、各生成 HTML に GitHub 編集ボタンを埋め込む(この過程で大量の `=> Processing: ...` ログが出る。これは翻訳/ビルドの失敗ではない)。

## 既知の落とし穴: RST インライン記法と CJK 文字の隣接

日本語訳の RST で `**強調**` などの直後に読点等を挟まず日本語の文字(かな/漢字)が直接続くと、docutils が閉じ記号を認識できず
`WARNING: Inline strong start-string without end-string.` となり、`-W` ビルドが失敗する。
この問題のクラスと、翻訳スクリプト側での恒久対策は [skills.md](skills.md) に詳しくまとめてある。
