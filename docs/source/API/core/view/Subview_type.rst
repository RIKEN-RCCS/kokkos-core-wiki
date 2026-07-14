``Kokkos::Subview``
===================

.. role:: cpp(code)
   :language: cpp

.. _subviewfunc: subview.html

.. |subviewfunc| replace:: ``Kokkos::subview()``

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

説明
------------------

|subviewfunc|_ 関数を、指定の引数により呼び出した際に、返される型を推論するためのエイリアステンプレートです。

インターフェイス
----------------

.. code-block:: cpp

   template <class ViewType, class... Args>
   using Subview = IMPL_DETAIL; // ソースビューの特性からサブビューのタイプを推論します。

``Kokkos::subview(ViewType view_arg, Args .... args)`` の結果の型。

必要要件
------------

以下を必要とします:

- ``ViewType`` は、 ``Kokkos::View`` の仕様です。

- ``Args...`` は、 |subviewfunc|_ で定義されているスライス指定子です。

- ``sizeof... (Args) == ViewType::rank()``.


例
--------

.. code-block:: cpp

   using view_type = Kokkos::View<double ***[5]>;
   view_type a("A",N0,N1,N2);

   struct subViewHolder {
   Kokkos::Subview<view_type,
                   std::pair<int,int>,
                   int,
                   decltype(Kokkos::ALL),
                   int> s;
   } subViewHolder;

   subViewHolder.s  = Kokkos::subview(a,
                                      std::pair<int,int>(3,15),
                                      5,
                                      Kokkos::ALL,
                                      3);
