バージョンマクロ
================

.. list-table::
   :header-rows: 1
   :align: left

   * - バージョン整数マクロ
     - Kokkos バージョン 4.2.1 を想定した場合の値の例
   * - ``KOKKOS_VERSION``
     - ``40201``
   * - ``KOKKOS_VERSION_MAJOR``
     - ``4``
   * - ``KOKKOS_VERSION_MINOR``
     - ``2``
   * - ``KOKKOS_VERSION_PATCH``
     - ``1``

Kokkos のバージョンマクロは整数として定義されています。
``KOKKOS_VERSION`` は ``<MAJOR>*10000 + <MINOR>*100 + <PATCH>`` に等しくなります。
``40201`` は Kokkos 4.2.1 リリースバージョンに対応します。
パッチ番号 ``99`` は開発版を表します。つまり、``40199`` は
リリース 4.1 以降の Kokkos 開発版に対応します。

.. code-block:: c++

   #include <Kokkos_Core.hpp>
   #include <iostream>
   static_assert(KOKKOS_VERSION_MAJOR == KOKKOS_VERSION / 10000);
   static_assert(KOKKOS_VERSION_MINOR == KOKKOS_VERSION / 100 % 100);
   static_assert(KOKKOS_VERSION_PATCH == KOKKOS_VERSION % 100);
   #if KOKKOS_VERSION >= 30700
   // Kokkos version is at least 3.7
   #endif
   int main() {
     if (KOKKOS_VERSION_PATCH == 99)
       std::cout << "using development version of Kokkos"
     // ...
   }

.. warning:: Kokkos 4.1 までは、``KOKKOS_VERSION_MINOR`` と ``KOKKOS_VERSION_PATCH`` は ``0`` となるべき場合に定義されていませんでした。

比較ヘルパー
------------

.. list-table::
   :header-rows: 1
   :align: left

   * - 関数形式のバージョンヘルパーマクロ（Kokkos 4.1 以降）
   * - ``KOKKOS_VERSION_LESS(major, minor, patch)``
   * - ``KOKKOS_VERSION_LESS_EQUAL(major, minor, patch)``
   * - ``KOKKOS_VERSION_GREATER(major, minor, patch)``
   * - ``KOKKOS_VERSION_GREATER_EQUAL(major, minor, patch)``
   * - ``KOKKOS_VERSION_EQUAL(major, minor, patch)``

``KOKKOS_VERSION_<COMPARE>`` 関数形式マクロは、現在使用している Kokkos の
バージョンを、3 つの引数 ``major.minor.patch`` で指定されたバージョンと
比較した結果を返します。これらは Kokkos 4.1 以降で利用可能です。

.. code-block:: c++

   #include <Kokkos_Core.hpp>
   // sanity check for illustration
   static_assert(KOKKOS_VERSION_EQUAL(KOKKOS_VERSION_MAJOR,
                                      KOKKOS_VERSION_MINOR,
                                      KOKKOS_VERSION_PATCH));
   // set the minimum required version of Kokkos for a project or a file
   static_assert(KOKKOS_VERSION_GREATER_EQUAL(4, 5, 0));

   void do_work() {
     #if KOKKOS_VERSION_GREATER_EQUAL(4, 3, 0)
     // using the new rad functionality
     #else
     // falling back to the old boring stuff
     #endif
   }