``BadAlloc``
============

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Core.hpp>`` で定義されています。

.. warning::

   ``BadAlloc`` は ``Kokkos::Experimental`` 名前空間に含まれるため、今後のリリースで
   予告なく変更される可能性があります。

使い方
------

.. code-block:: cpp

    try {
      void* ptr = Kokkos::kokkos_malloc(huge_size);
    } catch (Kokkos::Experimental::BadAlloc const& e) {
      std::cerr << "Allocation failed: " << e.what() << '\n';
    }

Kokkos がメモリの確保に失敗したときにスローされる例外型です。例えば
:cpp:func:`kokkos_malloc`、:cpp:func:`kokkos_realloc` から、あるいは
:cpp:class:`View` を確保するときにスローされます。

インターフェース
----------------

.. cpp:class:: Experimental::BadAlloc : public std::runtime_error

   .. versionadded:: 5.2

備考
----

バージョン履歴
^^^^^^^^^^^^^^
* Kokkos 4.4 より前では、確保の失敗は ``Experimental::RawMemoryAllocationFailure``
  のようなバックエンド固有の型をスローしていました。これらの型はもう存在しません。
* Kokkos 4.4 から 5.1 までは、確保の失敗は ``std::runtime_error`` をスローします。
* Kokkos 5.2 以降では、確保の失敗は ``Experimental::BadAlloc`` をスローします。
  これは ``std::runtime_error`` から派生しているため、``std::runtime_error`` を
  キャッチするコードは引き続き動作します。