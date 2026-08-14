``printf``
==========

.. role:: cpp(code)
    :language: cpp

``<Kokkos_Core.hpp>`` からインクルードされるヘッダー ``<Kokkos_Printf.hpp>``:sup:`Kokkos 4.2以降` で定義されています。

使い方
------

.. code-block:: cpp

   Kokkos::printf("Hello World!");
   Kokkos::printf("Pi is approx %.2f\n", 3.14159);
   Kokkos::printf("Value at index %d: %f\n", i, data[i]);

フォーマットされた出力を標準出力ストリーム（ ``stdout`` ）に出力します。
この関数は、並列カーネル内を含め、ホストコードとデバイスコードの両方から呼び出すことができます。
動作は ``std::printf`` に類似していますが、バックエンド間で一貫した動作を保証するため、整数ではなく ``void`` を返します。

インターフェース
----------------

.. cpp:function:: template <typename... Args> KOKKOS_FUNCTION void printf(const char* format, Args... args);

   .. versionadded:: 4.2

   :param format: 出力のフォーマット方法を指定するヌル終端文字列。C の ``printf`` と互換性のあるフォーマット指定子を使用します。
   :param args: フォーマット文字列に従って出力される値
   :returns: void（書き込まれた文字数を返す ``std::printf`` とは異なります）

フォーマット指定子
^^^^^^^^^^^^^^^^^^

標準の C ``printf`` フォーマット指定子をサポートします。

* ``%d``, ``%i`` - 符号付き整数
* ``%u`` - 符号なし整数
* ``%f`` - 浮動小数点数
* ``%e``, ``%E`` - 科学的記数法
* ``%g``, ``%G`` - 最短表現
* ``%s`` - 文字列
* ``%p`` - ポインタ
* ``%x``, ``%X`` - 16進数
* 幅、精度、および長さの修飾子（例: ``%.2f``, ``%10d``）

例
--

基本的な使い方
^^^^^^^^^^^^^^
.. code-block:: cpp

    #include <Kokkos_Core.hpp>

    int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        {
          Kokkos::printf("Starting computation\n");       

          Kokkos::parallel_for("hello", 4, KOKKOS_LAMBDA(int i) {
              Kokkos::printf("hello world from thread %d\n", i);
          });
          Kokkos::fence();

          Kokkos::printf("Computation complete\n");
        }
        Kokkos::finalize();
    }

値のデバッグ
^^^^^^^^^^^^

.. code-block:: cpp

    Kokkos::parallel_for("debug", n, KOKKOS_LAMBDA(int i) {
        if (i < 5) {  // Limit output for large arrays
            Kokkos::printf("data[%d] = %.6f\n", i, data(i));
        }
        if (data(i) < 0) {
            Kokkos::printf("Warning: negative value at index %d: %f\n", i, data(i));
        }
    });

注意事項
--------
.. warning::
   
   カーネルから :cpp:func:`printf` を呼び出すと、レジスタの使用に影響を与え、パフォーマンスが低下する可能性があります。
   パフォーマンスが重要なコードでは控えめに使用してください。

関連項目
--------

.. seealso::

    :doc:`abort`
       エラーメッセージを伴ってプログラムを異常終了させます。
    
    :doc:`assert`
       条件が偽の場合に条件付きで中断します。デバッグに便利です。
