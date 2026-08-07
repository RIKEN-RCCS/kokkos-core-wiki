``abort``
=========

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Abort.hpp>``:sup:`Kokkos 4.2 以降` に定義。このヘッダーは ``<Kokkos_Core.hpp>`` からインクルードされます。

使用法
------

.. code-block:: cpp

    Kokkos::abort("helpful error message");

異常なプログラム終了が発生し、標準エラーストリームにエラーメッセージが表示されます。
この関数は、並列カーネル内を含め、ホストコードとデバイスコードの両方から呼び出すことができます。

インターフェイス
----------------

.. cpp:function:: KOKKOS_FUNCTION void abort(const char * msg);

   :param msg: プロセスを中止する前に表示するエラーメッセージを含む、ヌル終端文字列。
   :returns: 返しません

注意事項
--------

バージョン履歴
^^^^^^^^^^^^^^
* すべての Kokkos バージョンで利用可能
* 細粒度のヘッダー ``<Kokkos_Abort.hpp>`` はバージョン 4.2 で追加されました

バックエンド固有の動作
^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   **SYCL バックエンド:** SYCL バックエンドで並列領域から :cpp:func:`abort` を呼び出し、かつ ``NDEBUG`` が定義されている場合、この関数は異常終了を **引き起こしません** 。その代わりに、標準出力ストリームに表示してプログラムの実行を継続します。
   :ref:`既知の問題 <known-issues-sycl-abort>` を参照してください。

.. warning::
   **NextSilicon バックエンド:** NextSilicon バックエンドで並列領域から :cpp:func:`abort` を呼び出す場合、この関数は異常なプログラム終了を引き起こしますが、領域がアクセラレータにオフロードされている場合はメッセージを表示しません。

例
--

.. code-block:: cpp

    KOKKOS_FUNCTION void validate_input(int value) {
      if (value < 0) {
        Kokkos::abort("Error: negative value not allowed");
      }
    }

    // 並列領域で使用可能
    Kokkos::parallel_for("check_data", n, KOKKOS_LAMBDA(int i) {
      if (data(i) > threshold) {
        Kokkos::abort("Data value exceeds threshold");
      }
    });

関連項目
--------

.. seealso::

   :doc:`assert`
      条件が偽の場合に条件付きで中止します。リリースビルドでは無効化できます
   
   :doc:`printf`
      実行を終了せずにフォーマットされた出力を表示します
