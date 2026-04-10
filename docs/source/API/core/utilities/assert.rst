``KOKKOS_ASSERT``
=================

.. role:: cpp(code)
    :language: cpp

 ヘッダー ``<Kokkos_Core.hpp>`` に定義。

.. code-block:: cpp

    #if defined(NDEBUG) and not defined(KOKKOS_ENABLE_DEBUG)
    #  define KOKKOS_ASSERT(condition) ((void)0)
    #else
    #  define KOKKOS_ASSERT(condition) if (!bool(condition)) /*call Kokkos::abort()*/
    #endif

マクロ ``KOKKOS_ASSERT`` の定義は、他のマクロ、
``NDEBUG`` および ``KOKKOS_ENABLE_DEBUG``。

``NDEBUG`` が定義されず、 ``<Kokkos_Assert.hpp>`` または ``<Kokkos_Core.hpp>`` が含まれないソースコード内のポイントで
``KOKKOS_ENABLE_DEBUG`` が定義されない場合には、
アサートは何もできません。

``NDEBUG`` が定義されない、または ``KOKKOS_ENABLE_DEBUG`` が定義される場合には、
``KOKKOS_ASSERT`` は、``bool`` に変換されたその引数が、``false`` に決定されているかどうかを
確認します。 そうである場合には、 ``KOKKOS_ASSERT`` は、
事前定義されたマクロス  ``__FILE__`` and ``__LINE__`` のみならず、
式のテキストを含む、診断情報を使って、 ``Kokkos::abort`` を呼び出します。

例
-------

.. code-block:: cpp

    int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        KOKKOS_ASSERT(Kokkos::is_initialized());  // ホストから呼び出し可能

        Kokkos::parallel_for(1, KOKKOS_LAMBDA(int i) {
          KOKKOS_ASSERT(i == 0);  // デバイス側からも呼び出し可能
        });

        Kokkos::finalize();
        assert(Kokkos::is_finalized());  // ホスト上で、排他的に呼び出し可能


注意事項
-----

.. _KokkosAssert: https://github.com/kokkos/kokkos/blob/4.2.00/core/src/Kokkos_Assert.hpp

.. |KokkosAssert| replace:: ``<Kokkos_Assert.hpp>``

* バージョン 4.2以降、 |KokkosAssert|_ から ``KOKKOS_ASSERT`` もまた入手可能です。
* C++ 標準ライブラリからの `assert` とは対照的に、``KOKKOS_FUNCTION``から ``KOKKOS_ASSERT`` を呼び出すことは、合法的です。

以下も参照
--------
* `Kokkos::abort() <abort.html>`_ は、プログラムの異常終了を引き起こします。
