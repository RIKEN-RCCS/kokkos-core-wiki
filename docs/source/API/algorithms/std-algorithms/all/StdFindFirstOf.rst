
``find_first_of``
=================

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

対象範囲または　``ビュー``　内のいずれかの要素について、別の範囲または　``ビュー``　を検索します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType1 find_first_of(const ExecutionSpace& exespace,                           (1)
                               IteratorType1 first, IteratorType1 last,
			       IteratorType2 s_first, IteratorType2 s_last);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType1 find_first_of(const std::string& label, const ExecutionSpace& exespace, (2)
			       IteratorType1 first, IteratorType1 last,
			       IteratorType2 s_first, IteratorType2 s_last);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   auto find_first_of(const ExecutionSpace& exespace,                                    (3)
		      const ::Kokkos::View<DataType1, Properties1...>& view,
		      const ::Kokkos::View<DataType2, Properties2...>& s_view);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   auto find_first_of(const std::string& label, const ExecutionSpace& exespace,          (4)
		      const ::Kokkos::View<DataType1, Properties1...>& view,
		      const ::Kokkos::View<DataType2, Properties2...>& s_view);

   // オーバーロードセット 2: 引き渡された二項述語
   template <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   IteratorType1 find_first_of(const ExecutionSpace& exespace,                           (5)
                               IteratorType1 first, IteratorType1 last,
			       IteratorType2 s_first, IteratorType2 s_last,
			       const BinaryPredicateType& pred);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   IteratorType1 find_first_of(const std::string& label, const ExecutionSpace& exespace, (6)
			       IteratorType1 first, IteratorType1 last,
			       IteratorType2 s_first, IteratorType2 s_last,
			       const BinaryPredicateType& pred);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicateType>
   auto find_first_of(const ExecutionSpace& exespace,                                    (7)
		      const ::Kokkos::View<DataType1, Properties1...>& view,
		      const ::Kokkos::View<DataType2, Properties2...>& s_view,
		      const BinaryPredicateType& pred);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicateType>
   auto find_first_of(const std::string& label, const ExecutionSpace& exespace,          (8)
		      const ::Kokkos::View<DataType1, Properties1...>& view,
		      const ::Kokkos::View<DataType2, Properties2...>& s_view,
		      const BinaryPredicateType& pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType1, class IteratorType2>
   KOKKOS_FUNCTION
   IteratorType1 find_first_of(const TeamHandleType& teamHandle,                         (9)
                               IteratorType1 first, IteratorType1 last,
			       IteratorType2 s_first, IteratorType2 s_last);

   template <class TeamHandleType, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   auto find_first_of(const TeamHandleType& teamHandle,                                 (10)
		      const ::Kokkos::View<DataType1, Properties1...>& view,
		      const ::Kokkos::View<DataType2, Properties2...>& s_view);

   // オーバーロードセット 2: 引き渡された二項述語
   template <class TeamHandleType, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   KOKKOS_FUNCTION
   IteratorType1 find_first_of(const TeamHandleType& teamHandle,                        (11)
                               IteratorType1 first, IteratorType1 last,
			       IteratorType2 s_first, IteratorType2 s_last,
			       const BinaryPredicateType& pred);

   template <class TeamHandleType, class DataType1, class... Properties1,
	     クラス DataType2, class... Properties2, class BinaryPredicateType>
   KOKKOS_FUNCTION
   自動 find_first_of(const TeamHandleType& teamHandle,                                 (12)
		      const ::Kokkos::View<DataType1, Properties1...>& view,
		      const ::Kokkos::View<DataType2, Properties2...>& s_view,
		      const BinaryPredicateType& pred);

詳細ディスクリプション
~~~~~~~~~~~~~~~~~~~~

- 1,2,5,6,9,10: ``operator ==``　経由 または ``pred``　経由で、要素を比較する範囲 ``[s_first, s_last)`` 内のいずれかの要素について、範囲 ``[first, last)`` を検索します。

- 3,4,7,8,11,12: ``operator ==``　経由 または ``pred``　経由で、要素を比較する ``s_view``　内のいずれかの要素について、 ``ビュー`` を検索します。

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicy　使用時に、並列領域内部で提供されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

    - 1,5: デフォルト文字列は、 "Kokkos::find_first_of_iterator_api_default".

    - 3,7: デフォルト文字列は、 "Kokkos::find_first_of_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索対象となる要素の範囲

  - 　*ランダムアクセスイテレータ*　である必要があり、例えば、``Kokkos::Experimental::(c)begin/(c)end``から返されなければなりません。

  - 有効な範囲を表す必要があり、つまり、``last >= first`` でなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``s_first, s_last``: 検索を望む要素の範囲

  - ``first, last``　と同じ要件。

- ``view``, ``s_view``: 検索対象および検索条件の、それぞれのビュー

  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``: 2つの引数が、 "等しい"　とみなされる場合、 ``真`` を返す　*二項* ファンクタ。

  ``pred(a,b)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして、それぞれ、 型　　 ``ValueType1`` および　``ValueType2``　の引数　``a,b``　のすべてのペアについて、ブール型に変換可能で、そこでは、``ValueType1`` および ``ValueType{1,2}``　が、``IteratorType{1,2}``　の値型、または ``(s_)view``　であり、 　``a,b``　を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     template <class ValueType1, class ValueType2 = ValueType1>
     struct IsEqualFunctor {
      KOKKOS_INLINE_FUNCTION
      bool operator()(const ValueType1& a, const ValueType2& b) const {
        return (a == b);
      }
     };
