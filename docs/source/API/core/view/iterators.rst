イテレータ
==========

.. role:: cpp(code)
    :language: cpp

``Kokkos::Experimental::{begin, cbegin, end, cend}``
----------------------------------------------------

ヘッダーファイル: ``<Kokkos_StdAlgorithms.hpp>`` (Kokkos 5.2まで)、``<Kokkos_Core.hpp>`` (Kokkos 5.2以降)


.. cpp:function:: template <class DataType, class... Properties> KOKKOS_INLINE_FUNCTION auto begin(const Kokkos::View<DataType, Properties...>& view);

   ``view`` の先頭を指すKokkosの **ランダムアクセス** イテレータを返します

.. cpp:function:: template <class DataType, class... Properties> KOKKOS_INLINE_FUNCTION auto cbegin(const Kokkos::View<DataType, Properties...>& view);

   ``view`` の先頭を指すKokkosのconst修飾された **ランダムアクセス** イテレータを返します

.. cpp:function:: template <class DataType, class... Properties> KOKKOS_INLINE_FUNCTION auto end(const Kokkos::View<DataType, Properties...>& view);

   ``view`` の末尾の次の要素を指すKokkosの **ランダムアクセス** イテレータを返します

.. cpp:function:: template <class DataType, class... Properties> KOKKOS_INLINE_FUNCTION auto cend(const Kokkos::View<DataType, Properties...>& view);

   ``view`` の末尾の次の要素を指すconst修飾されたKokkosの **ランダムアクセス** イテレータを返します

注意事項
~~~~~~~~

* 返されるイテレータは、パフォーマンス上の理由から **ランダムアクセス** です

* ``view`` は ``const`` として受け取られます。これは、各関数内でビュー自体を変更しないためです。返されるイテレータは、ビューの構造を変更することなく操作します。

* イテレータのデリファレンスは、``view`` にアクセス可能な実行空間内で行う必要があります

パラメータと要件
~~~~~~~~~~~~~~~~

* ``view``: ``LayoutLeft``、``LayoutRight``、または ``LayoutStride`` を持つランク1のビューでなければなりません

例
~~

.. code-block:: cpp

    namespace KE = Kokkos::Experimental;
    using view_type = Kokkos::View<int*>;
    view_type a("a", 15);

    auto it = KE::begin(a);
    // (適切な実行空間内で) デリファレンスされた場合、`a` の内容を変更できます

    auto itc = KE::cbegin(a);
    // (適切な実行空間内で) デリファレンスされた場合、`a` の内容を読み取ることのみができます

------------------

``Kokkos::Experimental::distance``
----------------------------------

ヘッダーファイル: ``<Kokkos_StdAlgorithms.hpp>`` (Kokkos 5.2まで)、``<Kokkos_Core.hpp>`` (Kokkos 5.2以降)

.. cpp:function:: template <class IteratorType> KOKKOS_INLINE_FUNCTION constexpr typename IteratorType::difference_type distance(IteratorType first, IteratorType last);

   ``first`` から ``last`` まで進むために必要なステップ数を返します。

パラメータと要件
~~~~~~~~~~~~~~~~

* ``first, last``: 距離を計算する範囲

戻り値
~~~~~~

``first`` から ``last`` まで進むために必要なステップ数。
ランダムアクセスイテレータを使用する場合、値は負になることがあります。


例
~~

.. code-block:: cpp

    namespace KE = Kokkos::Experimental;
    Kokkos::View<double*> a("a", 13);

    auto it1 = KE::begin(a);
    auto it2 = it1 + 4;
    const auto stepsA = KE::distance(it1, it2);
    // stepsA は 4 と等しくなるはずです

    const auto stepsB = KE::distance(it2, it1);
    // stepsB は -4 と等しくなるはずです