並列実行/ディスパッチ
===========================

並列パターン
-----------------

アルゴリズムを構成するための並列実行パターン。

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - 関数
     - 説明
   * - `parallel_for <parallel-dispatch/parallel_for.html>`__
     - ユーザーコードを並列に実行
   * - `parallel_reduce <parallel-dispatch/parallel_reduce.html>`__
     - 並列で削減を実行するためにユーザーコードを実行
   * - `parallel_scan <parallel-dispatch/parallel_scan.html>`__
     - 並列で接頭和を生成するユーザーコードを実行
   * - `fence <parallel-dispatch/fence.html>`__
     - 実行領域をフェンス

チームポリシー計算用タグ
---------------------------------

以下の並列パターンタグは、チーム規模計算の適切なオーバーロードを呼び出すために使用されます(team_size_max,team_size_recommended):

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - タグ
     - パターン
   * - `ParallelForTag <parallel-dispatch/ParallelForTag.html>`__
     - parallel_for
   * - `ParallelReduceTag <parallel-dispatch/ParallelReduceTag.html>`__
     - parallel_reduce
   * - `ParallelScanTag <parallel-dispatch/ParallelScanTag.html>`__
     - parallel_scan

.. toctree::
   :hidden:
   :maxdepth: 1

   ./parallel-dispatch/parallel_for
   ./parallel-dispatch/parallel_reduce
   ./parallel-dispatch/parallel_scan
   ./parallel-dispatch/fence
   ./parallel-dispatch/ParallelForTag
   ./parallel-dispatch/ParallelReduceTag
   ./parallel-dispatch/ParallelScanTag
