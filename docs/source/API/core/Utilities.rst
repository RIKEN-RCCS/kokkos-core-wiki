ユーティリティ
==============

エラー処理と診断
----------------

Kokkos は、ホストコードとデバイスコードの間で一貫して動作する、エラー処理、デバッグ、および出力のためのユーティリティ関数を提供します。

.. list-table::
   :align: left
   :widths: 30 70

   * - :doc:`utilities/abort`
     - エラーメッセージを表示して直ちにプログラムを終了します。
   * - :doc:`utilities/assert`
     - ユーザーが指定した条件が ``true`` でない場合にプログラムを中断します。
       動作は ``NDEBUG`` および ``KOKKOS_ENABLE_DEBUG`` マクロに依存します。
   * - :doc:`utilities/printf`
     - 標準出力ストリームに書式化された出力を表示します。

.. toctree::
   :hidden:
   :maxdepth: 1

   ./utilities/abort
   ./utilities/assert
   ./utilities/printf

その他
------

.. toctree::
   :maxdepth: 1

   ./utilities/all
   ./utilities/min_max_clamp
   ./utilities/swap
   ./utilities/timer
   ./utilities/device_id
   ./utilities/num_devices
   ./utilities/num_threads
   ./utilities/experimental
