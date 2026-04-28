
``swap_ranges``
===============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
------------------

二つの範囲または二つのランク1の ``View`` 間で、要素を入れ替えます。

インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType2 swap_ranges(const ExecutionSpace& ex, IteratorType1 first1,          (1)
                             IteratorType1 last1, IteratorType2 first2);

   template <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   auto swap_ranges(const ExecutionSpace& ex,                                         (2)
                    const ::Kokkos::View<DataType1, Properties1...>& source,
                    ::Kokkos::View<DataType2, Properties2...>& dest);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType2 swap_ranges(const std::string& label, const ExecutionSpace& ex,      (3)
                             IteratorType1 first1, IteratorType1 last1,
                             IteratorType2 first2);

   template <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   auto swap_ranges(const std::string& label, const ExecutionSpace& ex,               (4)
                    const ::Kokkos::View<DataType1, Properties1...>& source,
                    ::Kokkos::View<DataType2, Properties2...>& dest);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType1, class IteratorType2>
   KOKKOS_FUNCTION
   IteratorType2 swap_ranges(const TeamHandleType& teamHandle, IteratorType1 first1,  (5)
                             IteratorType1 last1, IteratorType2 first2);

   template <class TeamHandleType, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   auto swap_ranges(const TeamHandleType& teamHandle,                                 (6)
                    const ::Kokkos::View<DataType1, Properties1...>& source,
                    ::Kokkos::View<DataType2, Properties2...>& dest);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1 について、デフォルト文字列は、: "Kokkos::swap_ranges_iterator_api_default"

  - 2 について、デフォルト文字列は、: "Kokkos::swap_ranges_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first1``, ``last1``, ``first2``: 入れ替え対象の範囲を定義するイテレータ

  -  *ランダムアクセスイテレータ* でなければなりません。

  - 有効な範囲、つまり、 ``last1 >= first1`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``source``, ``dest``: 入れ替え対象のビュー

  - 必ずランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。


  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


戻り値
~~~~~~~~~~~~

- 1,3,5: ``first2 + Kokkos::Experimental::distance(first1, last1)`` に等しいイテレータ。

- 2,4,6: ``Kokkos::Experimental::begin(dest) +
  Kokkos::Experimental::distance(Kokkos::Experimental::begin(source), Kokkos::Experimental::end(source))`` に等しいイテレータ。 
  
