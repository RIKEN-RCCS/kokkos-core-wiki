ユーティリティ
==============

エラー処理と診断
----------------
Kokkos は、ホストコードとデバイスコードの両方で一貫して動作する、エラー処理、デバッグ、および出力のためのユーティリティ関数を提供します。

.. list-table::
   :align: left
   :widths: 30 70

   * - :doc:`utilities/abort`
     - エラーメッセージとともにプログラムを直ちに終了します。
   * - :doc:`utilities/assert`
     - ユーザーが指定した条件が ``true`` でない場合にプログラムを中断します。
       動作は ``NDEBUG`` および ``KOKKOS_ENABLE_DEBUG`` マクロに依存します。
   * - :doc:`utilities/printf`
     - 標準出力ストリームにフォーマット済みの出力を表示します。

.. toctree::
   :hidden:
   :maxdepth: 1

   ./utilities/abort
   ./utilities/assert
   ./utilities/printf

実行時とデバイスの情報
----------------------
Kokkos は、Kokkos 実行環境に関する実行時情報を照会するためのユーティリティ関数を提供します。

.. list-table::
   :align: left
   :widths: 30 70

   * - :doc:`utilities/device_id`
     - ``DefaultExecutionSpace`` が使用するデバイスの id を返します。
   * - :doc:`utilities/num_devices`
     - Kokkos が利用可能なデバイスの数を返します。
   * - :doc:`utilities/num_threads`
     - ``DefaultHostExecutionSpace`` が使用するスレッドの数を返します。
   * - :doc:`utilities/print_configuration`
     - Kokkos のコンパイル時および実行時の構成を出力ストリームに出力します。

.. toctree::
   :hidden:
   :maxdepth: 1

   ./utilities/device_id
   ./utilities/num_devices
   ./utilities/num_threads
   ./utilities/print_configuration

その他
------
.. toctree::
   :maxdepth: 1

   ./utilities/min_max_clamp
   ./utilities/swap
   ./utilities/timer
