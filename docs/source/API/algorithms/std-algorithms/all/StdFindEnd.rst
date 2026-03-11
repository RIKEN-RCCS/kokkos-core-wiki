
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

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1,5: デフォルト文字列は、 "Kokkos::find_end_iterator_api_default".

  - 3,7: デフォルト文字列は、 "Kokkos::find_end_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索する要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。

  - 有効範囲、つまり、 ``last >= first``　を表さなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``s_first, s_last``: 検索を望む要素の範囲

  -  ``first, last``と同じ要件

- ``view``, ``s_view``: 検索対象および検索条件の、それぞれのビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``: 2つの引数が、 "等しい"　とみなされる場合、 ``真`` を返す　*二項* ファンクタ。

  ``pred(a,b)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして、それぞれ、 型　　 ``ValueType1`` および　``ValueType2``　の引数　``a,b`` のすべてのペアについて、ブール型に変換可能で、そこでは、``ValueType1`` および ``ValueType{1,2}``　が、``IteratorType{1,2}``　の値型、または ``(s_)view`` であり、 　``a,b``　を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     テンプレート <class ValueType1, class ValueType2 = ValueType1>
     構造体 IsEqualFunctor {
      KOKKOS_INLINE_FUNCTION
      ブール operator()(const ValueType1& a, const ValueType2& b) const {
        return (a == b);
      }
     };


戻り値
~~~~~~~~~~~~




範囲 ``[first, last)``　における シーケンス ``[s_first, s_last)``　の最後の発生の始め、または
  ``ビュー``　における　``s_view``　の最後の発生へのイテレータ。

``[s_first, s_last)`` または ``[first, last)`` が空である場合、 ``last`` が返されます。

``view`` または ``s_view`` が空である場合、 ``Kokkos::Experimental::end(view)`` が返されます。
