``ALL``
=======

ヘッダー ``<Kokkos_Core.hpp>`` で定義

.. code-block:: cpp

   namespace Kokkos{
     constexpr UNSPECIFIED_TYPE ALL = IMPLEMENTATION_DETAIL;
   }

``Kokkos::ALL`` は、ある次元のすべての要素を選択するために使用される、未規定の型の定数です。

例
--

.. code-block:: cpp

   Kokkos::View<double**[5]> a("A",N0,N1);
   auto s  = Kokkos::subview(a,
                 5,
                 Kokkos::ALL,
                 Kokkos::ALL);