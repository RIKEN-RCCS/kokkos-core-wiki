``count``
=========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
------------------

範囲内、またはランク1の ``ビュー`` において、指定されたターゲット値と等しい要素の数を返します。


インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType, class T>
   typename IteratorType::difference_type count(const ExecutionSpace& exespace,
						IteratorType first,
						IteratorType last,                      (1)
						const T& value);

   template <class ExecutionSpace, class IteratorType, class T>
   typename IteratorType::difference_type count(const std::string& label,
						const ExecutionSpace& exespace,
						IteratorType first,
						IteratorType last,                      (2)
						const T& value);

   template <class ExecutionSpace, class DataType, class... Properties, class T>
   auto count(const ExecutionSpace& exespace,                                           (3)
	      const ::Kokkos::View<DataType, Properties...>& view, const T& value);

   template <class ExecutionSpace, class DataType, class... Properties, class T>
   auto count(const std::string& label, const ExecutionSpace& exespace,           (4)
	      const ::Kokkos::View<DataType, Properties...>& view,
	      const T& value);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType, class T>
   KOKKOS_FUNCTION
   typename IteratorType::difference_type count(const TeamHandleType& teamHandle,
						IteratorType first,
						IteratorType last,                      (5)
						const T& value);

   template <class TeamHandleType, class DataType, class... Properties, class T>
   KOKKOS_FUNCTION
   auto count(const TeamHandleType& teamHandle,                                         (6)
	      const ::Kokkos::View<DataType, Properties...>& view,
	      const T& value);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::count_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::count_view_api_default".

  - 注意事項: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

- ``first, last``: 検索対象となる要素の範囲

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、 last >= first を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``:

  - 必ずランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

戻り値
~~~~~~~~~~~~

範囲 ``first, last`` または ``値`` に等しい ``ビュー`` の中にある要素数を返します。
