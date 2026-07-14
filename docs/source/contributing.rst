コントリビュート
================

.. toctree::
   :maxdepth: 1
   :hidden:

templates/index
   developer-guides/index
   testing-and-issue-tracking

外部からの貢献を歓迎します。変更内容について、まず `イシューを開いて
<https://github.com/kokkos/kokkos/issues>`_ 議論してください（特に大規模な機能については重要です）。その後、``develop`` ブランチに対してプルリクエストを送信してください。
イシューを開くべきか迷う場合は、最初のフィードバックを得るために気軽に `Slack で連絡
<https://kokkos.org/community/chat/#slack>`__ してください。

法的要件
----------
ライセンス
^^^^^^^^^^
Kokkos Core に貢献することにより、あなたは **Apache License 2.0
with LLVM Exception** に同意することに注意してください。これにより、あなたの貢献はクローズドソースの商用の文脈でも利用できるようになります。詳細については `LICENSE <license.html>`__ を参照してください。著者は自身の貢献に対する著作権を保持します。

開発者原産地証明（DCO）
^^^^^^^^^^^^^^^^^^^^^^^
オープンソースソフトウェアの明確な管理の連鎖を確保するために、すべての貢献が `開発者原産地証明
<https://developercertificate.org/>`_ に従って「サインオフ」されることを要求します。

コミットメッセージに ``Signed-off-by`` 行を追加することで、あなたはプロジェクトのライセンスの下でその作業を提出する権利を持っていることを証明します。これはコミット時に ``-s`` フラグを使用することで自動化できます。

.. code-block:: bash

git commit -s -m "My informative commit message"

文書投稿
--------

文書構築に関する指示全般については、`README <https://github.com/kokkos/kokkos-core-wiki/blob/main/README.md>`_ を参照してください。

簡単に API 文書へコントリビュートできるように、:doc:`こちら <templates/index>` に文書テンプレートを用意しています。

ディベロッパーコーナー
----------------------

* :doc:`ディベロッパーガイド  <developer-guides/index>`

* :doc:`Kokkos 計画および試験 <testing-and-issue-tracking>`
