イテレータ
==========

.. role:: cpp(code)
    :language: cpp

``Kokkos::Experimental::{begin, cbegin, end, cend}``
----------------------------------------------------

ヘッダーファイル: ``<Kokkos_StdAlgorithms.hpp>`` (Kokkos 5.2 まで)、``<Kokkos_Core.hpp>`` (Kokkos 5.2 以降)

`Iterators (Core) <../../core/view/iterators.html>`__ を参照してください。

------------------

``Kokkos::Experimental::distance``
----------------------------------

ヘッダーファイル: ``<Kokkos_StdAlgorithms.hpp>`` (Kokkos 5.2 まで)、``<Kokkos_Core.hpp>`` (Kokkos 5.2 以降)

`Iterators (Core) <../../core/view/iterators.html>`__ を参照してください。

------------------

``Kokkos::Experimental::iter_swap``
-----------------------------------

ヘッダーファイル: ``<Kokkos_StdAlgorithms.hpp>``

.. cpp:function:: template <class IteratorType> void iter_swap(IteratorType first, IteratorType last);

   指定されたイテレータが指す要素の値を入れ替えます。

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~

* ``first, last``: 入れ替えるためのイテレータ

注意事項
~~~~~~~~

現在、操作がデフォルトの実行スペースで実行されるため、API には実行スペースパラメータがありません。この操作はデフォルトの実行領域をフェンスします。

戻り値
~~~~~~

無し

例
~~

.. code-block:: cpp

    namespace KE = Kokkos::Experimental;
    Kokkos::View<double*> a("a", 13);

    auto it1 = KE::begin(a);
    auto it2 = it1 + 4;
    KE::swap(it1, it2);
