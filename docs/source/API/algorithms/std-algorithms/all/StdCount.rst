``count``
=========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲内、またはランク1の　``ビュー``　において、指定されたターゲット値と等しい要素の数を返します。


インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType, class T>
   型名 IteratorType::difference_type count(const ExecutionSpace& exespace,
						IteratorType first,
						IteratorType last,                      (1)
						const T& value);

   テンプレート <class ExecutionSpace, class IteratorType, class T>
   型名 IteratorType::difference_type count(const std::string& label,
						const ExecutionSpace& exespace,
						IteratorType first,
						IteratorType last,                      (2)
						const T& value);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
   自動 count(const ExecutionSpace& exespace,                                           (3)
	      const ::Kokkos::View<DataType, Properties...>& view, const T& value);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
    count(const std::string& label, const ExecutionSpace& exespace,                 (4)
	      const ::Kokkos::View<DataType, Properties...>& view,
	      const T& value);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType, class T>
   KOKKOS_FUNCTION
   型名 IteratorType::difference_type count(const TeamHandleType& teamHandle,
						IteratorType first,
						IteratorType last,                      (5)
						const T& value);

   テンプレート <class TeamHandleType, class DataType, class... Properties, class T>
   KOKKOS_FUNCTION
   自動 count(const TeamHandleType& teamHandle,                                         (6)
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

- ``first, last``: range of elements to search in検索対象となる要素の範囲

  - `*ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``から返されなければなりません。

  - must represent a valid range, i.e., ``last >= first``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view``:

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

Return Value
~~~~~~~~~~~~

Returns the number of elements in the range ``first, last`` or in ``view`` that are equal to ``value``.
