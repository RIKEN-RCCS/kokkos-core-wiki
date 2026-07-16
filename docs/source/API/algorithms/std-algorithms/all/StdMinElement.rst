``min_element``
===============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
----

2つの要素の比較には、 ``operator<`` を使用するか、ユーザーが提供する比較演算子を使用して、範囲内またはランク1の ``ビュー`` 内で最小の要素を検索します。

インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType>
   auto min_element(const ExecutionSpace& exespace,                        (1)
                    IteratorType first, IteratorType last);

   template <class ExecutionSpace, class IteratorType>
   auto min_element(const std::string& label,                              (2)
                    const ExecutionSpace& exespace,
                    IteratorType first, IteratorType last);

   template <class ExecutionSpace, class IteratorType, class ComparatorType>
   auto min_element(const ExecutionSpace& exespace,                        (3)
                    IteratorType first, IteratorType last,
                    ComparatorType comp);

   template <class ExecutionSpace, class IteratorType, class ComparatorType>
   auto min_element(const std::string& label,                              (4)
                    const ExecutionSpace& exespace,
                    IteratorType first, IteratorType last,
                    ComparatorType comp);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto min_element(const ExecutionSpace& exespace,                        (5)
                    const ::Kokkos::View<DataType, Properties...>& view);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto min_element(const std::string& label,                              (6)
                    const ExecutionSpace& exespace,
                    const ::Kokkos::View<DataType, Properties...>& view);

   template <class ExecutionSpace, class DataType, class ComparatorType, class... Properties>
   auto min_element(const ExecutionSpace& exespace,                        (7)
                    const ::Kokkos::View<DataType, Properties...>& view,
                    ComparatorType comp);

   template <class ExecutionSpace, class DataType, class ComparatorType, class... Properties>
   auto min_element(const std::string& label,                              (8)
                    const ExecutionSpace& exespace,
                    const ::Kokkos::View<DataType, Properties...>& view,
                    ComparatorType comp);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   auto min_element(const TeamHandleType& teamHandle,                      (9)
                    IteratorType first, IteratorType last);

   template <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   auto min_element(const TeamHandleType& teamHandle,                      (10)
                    const ::Kokkos::View<DataType, Properties...>& view);

   template <class TeamHandleType, class IteratorType, class ComparatorType>
   KOKKOS_FUNCTION
   auto min_element(const TeamHandleType& teamHandle,                      (11)
                    IteratorType first, IteratorType last,
                    ComparatorType comp);

   template <class TeamHandleType, class DataType, class ComparatorType,
             class... Properties>
   KOKKOS_FUNCTION
   auto min_element(const TeamHandleType& teamHandle,                      (12)
                    const ::Kokkos::View<DataType, Properties...>& view,
                    ComparatorType comp);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1 および 3: デフォルト文字列は、 "Kokkos::min_element_iterator_api_default".

  - 5 および 7: デフォルト文字列は、 "Kokkos::min_element_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first``, ``last``: 検証対象の要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されるなど、*ランダムアクセスイテレータ* でなければなりません。

  - 有効範囲、つまり、 ``last >= first`` を表さなければなりません。（デバッグモードで確認済み）

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``: 検証対象の Kokkos ビュー

  - 必ずランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``comp``:

  - 第1の引数が、第2の引数 *より小さい* 場合に ``真`` を返す *二項* ファンクタ;
    ``comp(a,b)`` は、 渡された実行空間から呼び出されるためには有効である必要があり、そして、 型 ``value_type`` の引数 ``a,b`` のすべてのペアについて、ブール型に変換可能で、そこでは、 ``value_type`` が ``IteratorType`` (1,2,3,4について) の値型、または ``ビュー`` (5,6,7,8について) の値型であり、 ``a,b`` を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     struct Comparator
     {
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & a, const value_type & b) const {
         return /* "より小さい" という論理に基づき、a が b より小さい場合 */;
       }
     };

戻り値
~~~~~~

イテレータを最小要素に返します。

以下の特例が適用されます:

- 複数の要素が最小の要素と同等である場合、そのような要素のうち *最初* の要素へのイテレータを返します。

- 範囲 ``[first, last)`` が空である場合、それは ``last`` を返します。

- ``ビュー`` が空である場合、 それは ``Kokkos::Experimental::end(view)`` を返します。


例
~~

.. code-block:: cpp

   namespace KE = Kokkos::Experimental;
   Kokkos::View<double*> a("a", 13);
   // a を何らかの方法で満たす

   auto res = KE::min_element(Kokkos::DefaultExecutionSpace(), KE::begin(a), KE::end(a));

   // ビューを直接渡す
   auto res = KE::min_element(Kokkos::DefaultExecutionSpace(), a);


   // カスタムコンパレータを使用
   template <class ValueType1, class ValueType2 = ValueType1>
   struct CustomLessThanComparator {
     KOKKOS_INLINE_FUNCTION
     bool operator()(const ValueType1& a,
                     const ValueType2& b) const {
       // ここでは < を使用していますが、a が b より小さい場合に、 a < b を返すような任意のカスタムロジックを実装することも可能です。;
     }

     KOKKOS_INLINE_FUNCTION
     CustomLessThanComparator() {}
   };

   // ビューを直接渡す
   auto res = KE::min_element(Kokkos::DefaultExecutionSpace(), a, CustomLessThanComparator<double>());
