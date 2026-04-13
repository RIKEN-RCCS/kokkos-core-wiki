
``equal``
=========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------
2つの範囲または2つのランク1 ``ビュー`` が等しい場合、真を返します。

インターフェイス
---------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   bool equal(const ExecutionSpace& exespace,                                        (1)
              IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   bool equal(const std::string& label, const ExecutionSpace& exespace,              (2)
	      IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   bool equal(const ExecutionSpace& exespace,                                        (3)
              IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2,
	      BinaryPredicateType predicate);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   bool equal(const std::string& label, const ExecutionSpace& exespace,              (4)
	      IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2,
	      BinaryPredicateType predicate);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   bool equal(const ExecutionSpace& exespace, IteratorType1 first1,                  (5)
              IteratorType1 last1, IteratorType2 first2,
	      IteratorType2 last2);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2>
   bool equal(const std::string& label, const ExecutionSpace& exespace,              (6)
	      IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2, IteratorType2 last2);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   bool equal(const ExecutionSpace& exespace,                                        (7)
	      IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2, IteratorType2 last2,
	      BinaryPredicateType predicate);

   template <class ExecutionSpace, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   bool equal(const std::string& label, const ExecutionSpace& exespace,              (8)
	      IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2, IteratorType2 last2,
	      BinaryPredicateType predicate);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   bool equal(const ExecutionSpace& exespace,                                        (9)
	      const Kokkos::View<DataType1, Properties1...>& view1,
              const Kokkos::View<DataType2, Properties2...>& view2);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   bool equal(const std::string& label, const ExecutionSpace& exespace,             (10)
	      const Kokkos::View<DataType1, Properties1...>& view1,
	      const Kokkos::View<DataType2, Properties2...>& view2);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicate>
   bool equal(const ExecutionSpace& exespace,                                       (11)
	      const Kokkos::View<DataType1, Properties1...>& view1,
	      const Kokkos::View<DataType2, Properties2...>& view2,
	      BinaryPredicate pred);

   template <class ExecutionSpace, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicate>
   bool equal(const std::string& label, const ExecutionSpace& exespace,             (12)
	      const Kokkos::View<DataType1, Properties1...>& view1,
	      const Kokkos::View<DataType2, Properties2...>& view2,
	      BinaryPredicate pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType1, class IteratorType2>
   KOKKOS_FUNCTION
   bool equal(const TeamHandleType& teamHandle,                                     (13)
              IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2);

   template <class TeamHandleType, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   KOKKOS_FUNCTION
   bool equal(const TeamHandleType& teamHandle,                                     (14)
              IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2,
	      BinaryPredicateType predicate);

   template <class TeamHandleType, class IteratorType1, class IteratorType2>
   KOKKOS_FUNCTION
   bool equal(const TeamHandleType& teamHandle,                                     (15)
              IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2, IteratorType2 last2);

   template <class TeamHandleType, class IteratorType1, class IteratorType2,
	     class BinaryPredicateType>
   KOKKOS_FUNCTION
   bool equal(const TeamHandleType& teamHandle,                                     (16)
              IteratorType1 first1, IteratorType1 last1,
	      IteratorType2 first2, IteratorType2 last2,
	      BinaryPredicateType predicate);

   template <class TeamHandleType, class DataType1, class... Properties1,
	     class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   bool equal(const TeamHandleType& teamHandle,                                     (17)
	      const Kokkos::View<DataType1, Properties1...>& view1,
	      const Kokkos::View<DataType2, Properties2...>& view2);

   template <class TeamHandleType, class DataType1, class... Properties1,
	     class DataType2, class... Properties2, class BinaryPredicate>
   KOKKOS_FUNCTION
   bool equal(const TeamHandleType& teamHandle,                                     (18)
	      const Kokkos::View<DataType1, Properties1...>& view1,
	      const Kokkos::View<DataType2, Properties2...>& view2,
	      BinaryPredicate pred);


オーバーロードセット詳細ディスクリプション
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- (1,2,3,4,13,14): 範囲 ``[first1, last1)`` が
  範囲 ``[first2, first2 + (last1 - first1))`` に等しい場合には、真を返し、そうでない場合には、偽を返します。

- (5,6,7,8,15,16): 範囲 ``[first1, last1)`` が 範囲 ``[first2, last2)`` に等しい場合には、真を返し、そうでない場合には、偽を返します。

- (9,10,11,12,17,18): ``view1`` および ``view2`` が等しい場合には、真を返し、そうでない場合には、偽を返します。

- 該当する場合、二項述語 ``pred`` は、二つの要素間の等価性を確認するために使用されます。
そうでない場合には、``operator ==`` が使用されます。

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - (1,3,5,7): デフォルト文字列は、 "Kokkos::equal_iterator_api_default"。

  - (9,11):  デフォルト文字列は、"Kokkos::equal_view_api_default"。

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first1``, ``last1``, ``first2``, ``last2``: 読み取りおよび比較を行う範囲を定義するイテレータ

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、 ``last1 >= first1`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view1``, ``view2``: 比較するためのビュー

  - 必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``: 二つの引数が "等しい" と見なされる場合に ``真`` を返す *二項* ファンクタ。

  ``pred(a,b)`` は、引数として渡された実行空間から呼び出されるために、有効でなければならず、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型 ``ValueType1`` および ``ValueType2`` の引数が、それぞれ  のすべてのペアについて、ブール型に変換可能で、そこでは、``ValueType1`` および ``ValueType{1,2}`` が、 ``IteratorType{1,2}`` または ``view{1,2}`` の値型、または ``view`` であり、  ``a,b`` を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     template <class ValueType1, class ValueType2 = ValueType1>
     struct IsEqualFunctor {
      KOKKOS_INLINE_FUNCTION
      bool operator()(const ValueType1& a, const ValueType2& b) const {
        return (a == b);
      }
     };

戻り値
~~~~~~~~~~~~

2つの範囲またはビューの要素が等しい場合には、``真`` を返し、そうでない場合には、 ``偽`` を返します。

 ``偽`` が返される特殊なケース:

- ビューを受け入れるすべてのオーバーロードについて、``view1.extent(0) != view2.extent(1)`` である場合。

- 範囲 ``[first1, last)`` の長さが、 ``[first2,last2)`` の長さに等しくない場合。


例
-------

.. code-block:: cpp

   名前空間 KE = Kokkos::Experimental;

   template <class ValueType1, class ValueType2 = ValueType1>
   struct IsEqualFunctor {
     KOKKOS_INLINE_FUNCTION
     bool operator()(const ValueType1& a, const ValueType2& b) const {
       return (a == b);
     }
   };

   auto exespace = Kokkos::DefaultExecutionSpace;
   using view_type = Kokkos::View<exespace, int*>;
   view_type a("a", 15);
   view_type b("b", 15);
   // 何らかの方法で a,b を満たす

   // ファンクタを作成
   IsEqualFunctor<int,int> p();

   bool isEqual = KE::equal(exespace, KE::begin(a), KE::end(a),
                            KE::begin(b), KE::end(b) p);

   // ホスト上で明示的に実行（aとbがホスト上でアクセス可能であることを想定）
   bool isEqual = KE::equal(Kokkos::DefaultHostExecutionSpace(), KE::begin(a), KE::end(a),
                            KE::begin(b), KE::end(b), p);
