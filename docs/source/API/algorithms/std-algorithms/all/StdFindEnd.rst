
``find_end``
============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

指定された範囲またはランク1の　``ビュー``　において、対象となるシーケンスまたは値の　``ビュー``　の　*最後の*　出現箇所を検索します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType1 find_end(const ExecutionSpace& exespace,                                (1)
                          IteratorType1 first, IteratorType1 last,
			  IteratorType2 s_first, IteratorType2 s_last);

   テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType1 find_end(const std::string& label, const ExecutionSpace& exespace,
			  IteratorType1 first, IteratorType1 last,                       (2)
			  IteratorType2 s_first, IteratorType2 s_last);

   テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   自動 find_end(const ExecutionSpace& exespace,
		 const ::Kokkos::View<DataType1, Properties1...>& view,                  (3)
		 const ::Kokkos::View<DataType2, Properties2...>& s_view);

   テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   自動 find_end(const std::string& label, const ExecutionSpace& exespace,
		 const ::Kokkos::View<DataType1, Properties1...>& view,                  (4)
		 const ::Kokkos::View<DataType2, Properties2...>& s_view);

   テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   IteratorType1 find_end(const ExecutionSpace& exespace,                                (5)
                          IteratorType1 first, IteratorType1 last,
			  IteratorType2 s_first, IteratorType2 s_last,
			  const BinaryPredicateType& pred);

   テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   IteratorType1 find_end(const std::string& label, const ExecutionSpace& exespace,      (6)
			  IteratorType1 first, IteratorType1 last,
			  IteratorType2 s_first, IteratorType2 s_last,
			  const BinaryPredicateType& pred);

   テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicateType>
   自動 find_end(const ExecutionSpace& exespace,                                         (7)
		 const ::Kokkos::View<DataType1, Properties1...>& view,
		 const ::Kokkos::View<DataType2, Properties2...>& s_view,
		 const BinaryPredicateType& pred);

   テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicateType>
   自動 find_end(const std::string& label, const ExecutionSpace& exespace,               (8)
		 const ::Kokkos::View<DataType1, Properties1...>& view,
		 const ::Kokkos::View<DataType2, Properties2...>& s_view,
		 const BinaryPredicateType& pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType1, class IteratorType2>
   KOKKOS_FUNCTION
   IteratorType1 find_end(const TeamHandleType& teamHandle,                              (9)
                          IteratorType1 first, IteratorType1 last,
			  IteratorType2 s_first, IteratorType2 s_last);

   テンプレート <class TeamHandleType, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   自動 find_end(const TeamHandleType& teamHandle,                                      (10)
		 const ::Kokkos::View<DataType1, Properties1...>& view,
		 const ::Kokkos::View<DataType2, Properties2...>& s_view);

   テンプレート <class TeamHandleType, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   KOKKOS_FUNCTION
   IteratorType1 find_end(const TeamHandleType& teamHandle,                             (11)
                          IteratorType1 first, IteratorType1 last,
			  IteratorType2 s_first, IteratorType2 s_last,
			  const BinaryPredicateType& pred);

   テンプレート <class TeamHandleType, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicateType>
   KOKKOS_FUNCTION
    find_end(const TeamHandleType& teamHandle,                                      (12)
		 const ::Kokkos::View<DataType1, Properties1...>& view,
		 const ::Kokkos::View<DataType2, Properties2...>& s_view,
		 const BinaryPredicateType& pred);

オーバーロードセット詳細ディスクリプション
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 1,2,5,6:  ``operator ==`` (1,2) 経由または via ``pred`` (5,6)　経由で要素を比較する範囲　``[first, last)``　内のシーケンス ``[s_first, s_last)``　の最後の発生について検索します。

- 3,4,7,8: ``operator ==`` (3,4) 経由または ``pred`` (7,8)　経由で要素を比較する ``ビュー``　内の ``s_view`` の最後の発生について検索します。

パラメータおよび要件
---------------------------

- ``exespace``: 実行空間インス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1,5: デフォルト文字列は、 "Kokkos::find_end_iterator_api_default".

  - 3,7: デフォルト文字列は、 "Kokkos::find_end_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: range of elements to search in

  - must be *random access iterators*, e.g., returned from ``Kokkos::Experimental::(c)begin/(c)end``

  - must represent a valid range, i.e., ``last >= first``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``s_first, s_last``: range of elements that you want to search for

  - same requirements as ``first, last``

- ``view``, ``s_view``: views to search in and for, respectively

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``pred``: *binary* functor returning ``true`` if two arguments should be considered "equal".

  ``pred(a,b)`` must be valid to be called from the execution space passed, or
  the execution space associated with the team handle, and convertible to bool
  for every pair of arguments ``a,b`` of type ``ValueType1`` and ``ValueType2``,
  respectively, where ``ValueType1`` and ``ValueType{1,2}`` are the value types of
  ``IteratorType{1,2}`` or ``(s_)view``, and must not modify ``a,b``.

  - must conform to:

  .. code-block:: cpp

     template <class ValueType1, class ValueType2 = ValueType1>
     struct IsEqualFunctor {
      KOKKOS_INLINE_FUNCTION
      bool operator()(const ValueType1& a, const ValueType2& b) const {
        return (a == b);
      }
     };


Return Value
~~~~~~~~~~~~

Iterator to the beginning of the last occurrence of the sequence ``[s_first, s_last)``
in range ``[first, last)``, or the last occurrence of ``s_view`` in ``view``.

If ``[s_first, s_last)`` or ``[first, last)`` is empty, ``last`` is returned.

If ``view`` or ``s_view`` is empty, ``Kokkos::Experimental::end(view)`` is returned.
