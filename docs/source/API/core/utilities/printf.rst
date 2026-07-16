``Kokkos::printf``
==================

.. role:: cpp(code)
    :language: cpp

.. _KokkosPrintf: https://github.com/kokkos/kokkos/blob/4.2.00/core/src/Kokkos_Printf.hpp

.. |KokkosPrintf| replace:: ``<Kokkos_Printf.hpp>``

``<Kokkos_Core.hpp>`` に含まれる ヘッダー |KokkosPrintf|_ に定義。

.. code-block:: cpp

    template <typename... Args>
    KOKKOS_FUNCTION void printf(const char* format, Args... args);  // (バージョン 4.2以降)

``format`` および ``args...`` で指定されたデータを ``stdout`` に出力します。
この動作は、 ``std::printf`` に類似していますが、
戻り値の型は、バックエンド間で一貫した動作を保証するため、 ``void`` です。

例
~~

.. code-block:: cpp

    #include <Kokkos_Core.hpp>

    int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        Kokkos::parallel_for(4, KOKKOS_LAMBDA(int i) {
            Kokkos::printf("hello world from thread %d\n", i);
        });
        Kokkos::finalize();
    }

注意事項
~~~~~~~~
* ``Kokkos::printf()`` 関数は、リリース 4.2 で追加されました。
* カーネルから  ``Kokkos::printf()`` を呼び出すことは、レジスタの使用に影響を与え、パフォーマンスに影響を与える可能性があります。
