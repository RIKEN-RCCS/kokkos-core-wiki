コントリビュート
================

.. toctree::
   :maxdepth: 1
   :hidden:

   templates/index
   developer-guides/index
   testing-and-issue-tracking

外部からの貢献を歓迎します。変更内容について、まず `イシューを開いて
<https://github.com/kokkos/kokkos/issues>`_ 議論してください—特に大規模な機能については—そして
``develop`` ブランチに対してプルリクエストを発行してください。
イシューを開くべきか迷う場合は、`Slack で気軽に問い合わせて
<https://kokkos.org/community/chat/#slack>`__ 初期フィードバックを得てください。

法的要件
----------
ライセンス
^^^^^^^^^^
Kokkos Core に貢献することにより、あなたは自身の貢献が **Apache License 2.0
with LLVM Exception** の下でライセンスされることに同意したものとみなされます。この例外により、
エンドユーザーが Kokkos のライセンス文を配布することなく、Kokkos をバイナリ(クローズドソースの
商用ソフトウェアを含む)にコンパイル・リンクできます。詳細については
`LICENSE <license.html>`__ を参照してください。貢献者(またはその雇用主)は、自身の貢献に対する著作権を保持します。

Developer Certificate of Origin (DCO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
オープンソースソフトウェアの明確な管理履歴を確保するために、私たちはすべての
貢献が `Developer Certificate of
Origin <https://developercertificate.org/>`_ に従って「サインオフ」されることを求めています。

コミットメッセージに ``Signed-off-by`` 行を追加することにより、あなたは
プロジェクトのライセンスの下でその成果物を投稿する権利を有していることを証明します。

コマンドラインを使用する場合は、 ``-s`` フラグを付けることでこれを自動化できます:

.. code-block:: bash

   git commit -s -m "My informative commit message"

Git の GUI や Web インターフェースを使用する場合は、コミットの説明の末尾に次の行を手動で入力する必要があります:

.. code-block:: text

   Signed-off-by: Jane Doe <jane.doe@example.com>

生成 AI と Assisted-By による貢献
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Kokkos のコードを書く際に生成 AI ツール(GitHub Copilot、ChatGPT、Claude などのモデル)を
補助的に使用することは、人間による監督と透明性という厳格な条件の下で認められています。

**人間の説明責任:**
AI が生成したコードには、微妙なロジックのバグ、セキュリティ上のリスク、ライセンス遵守上の問題が
含まれていることがよくあります。AI ツールは Developer Certificate of Origin (DCO) に署名できないため、
投稿するすべてのコード行に対する責任は **あなた** が全面的に負います。AI の補助を受けた貢献は、
投稿前に十分にレビュー・テストし、内容を理解しておく必要があります。

**帰属と開示:**
コードがどのように書かれたかの履歴を明確かつ透明に保つため、AI ツールによって生成された、
または大幅に変更されたコードを相当量含むコミットには、コミットメッセージに ``Assisted-By``
トレーラーを含める必要があります。

このトレーラーには使用したツール名とバージョンを記載し、 ``Signed-off-by`` 行のすぐ隣に置いてください。

.. code-block:: text

   Fix out-of-bounds error in View layout initialization

   Detailed explanation of the fix goes here...

   Assisted-By: Copilot:gpt-4o
   Signed-off-by: Jane Doe <jane.doe@example.com>

人間による積極的な監督とコードレビューを経ずに、自動化された AI エージェントだけで生成された投稿は固く禁じられています。

文書投稿
--------

文書構築に関する指示全般については、`README <https://github.com/kokkos/kokkos-core-wiki/blob/main/README.md>`_ を参照してください。

簡単に API 文書へコントリビュートできるように、:doc:`こちら <templates/index>` に文書テンプレートを用意しています。

ディベロッパーコーナー
----------------------

* :doc:`ディベロッパーガイド  <developer-guides/index>`

* :doc:`Kokkos 計画および試験 <testing-and-issue-tracking>`
