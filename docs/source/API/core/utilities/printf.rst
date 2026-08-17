``printf``
==========

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Printf.hpp>``:sup:`Kokkos 4.2以降` で定義されており、``<Kokkos_Core.hpp>`` からインクルードされます

使い方
------

.. code-block:: cpp

   Kokkos::printf("Hello World!");
   Kokkos::printf("Pi is approx %.2f\n", 3.14159);
   Kokkos::printf("Value at index %d: %f\n", i, data[i]);

標準出力ストリーム（``stdout``）に書式化された出力を表示します。この関数は、
並列カーネル内を含め、ホストコードとデバイスコードの両方から呼び出すことが
できます。動作は ``std::printf`` に類似していますが、バックエンド間で一貫した
動作を保証するため、整数の代わりに ``void`` を返します。

インターフェース
----------------

.. cpp:function:: template <typename... Args> KOKKOS_FUNCTION void printf(const char* format, Args... args);

   .. versionadded:: 4.2

   :param format: 出力の書式化方法を指定するヌル終端文字列で、C の ``printf`` と
     互換性のある書式指定子を使用します
   :param args: 書式文字列に従って表示される値
   :returns: void（書き込まれた文字数を返す ``std::printf`` とは異なります）

書式指定子
^^^^^^^^^^

標準的な C の ``printf`` 書式指定子をサポートします。

* ``%d``, ``%i`` - 符号付き整数
* ``%u`` - 符号なし整数
* ``%f`` - 浮動小数点数
* ``%e``, ``%E`` - 科学表記
* ``%g``, ``%G`` - 最短表現
* ``%s`` - 文字列
* ``%p`` - ポインタ
* ``%x``, ``%X`` - 16進数
* 幅、精度、長さ修飾子（例：``%.2f``、``%10d``）

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
   
   カーネルから :cpp:func:`printf` を呼び出すと、レジスタの使用に影響を与え、
   パフォーマンスが低下する可能性があります。パフォーマンスが重要なコードでは
   控えめに使用してください。

関連項目
--------

.. seealso::

    :doc:`abort`
       エラーメッセージとともにプログラムを異常終了させます
    
    :doc:`assert`
       条件が false の場合に条件付きで中断します。デバッグに便利です
