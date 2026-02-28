``max_element``
===============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

2つの要素の比較には、``operator<``　を使用するか、ユーザーが提供する比較演算子を使用して、範囲内またはランク1の ``ビュー`` 内で最大の要素を検索します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType>
   自動 max_element(const ExecutionSpace& exespace,                        (1)
                    IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class IteratorType>
   自動 max_element(const std::string& label,                              (2)
                    const ExecutionSpace& exespace,
                    IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   自動 max_element(const ExecutionSpace& exespace,                        (3)
                    IteratorType first, IteratorType last,
                    ComparatorType comp);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   自動 max_element(const std::string& label,                              (4)
                    const ExecutionSpace& exespace,
                    IteratorType first, IteratorType last,
                    ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 max_element(const ExecutionSpace& exespace,                        (5)
                    const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 max_element(const std::string& label,                              (6)
                    const ExecutionSpace& exespace,
                    const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class DataType, class ComparatorType, class... Properties>
   自動 max_element(const ExecutionSpace& exespace,                        (7)
                    const ::Kokkos::View<DataType, Properties...>& view,
                    ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class ComparatorType, class... Properties>
   自動 max_element(const std::string& label,                              (8)
                    const ExecutionSpace& exespace,
                    const ::Kokkos::View<DataType, Properties...>& view,
                    ComparatorType comp);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   自動 max_element(const TeamHandleType& teamHandle,                      (9)
                    IteratorType first, IteratorType last);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   自動 max_element(const TeamHandleType& teamHandle,                      (10)
                    const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class TeamHandleType, class IteratorType, class ComparatorType>
   KOKKOS_FUNCTION
   自動 max_element(const TeamHandleType& teamHandle,                      (11)
                    IteratorType first, IteratorType last,
                    ComparatorType comp);

   テンプレート <class TeamHandleType, class DataType, class ComparatorType,
             class... Properties>
   KOKKOS_FUNCTION
   自動 max_element(const TeamHandleType& teamHandle,                      (12)
                    const ::Kokkos::View<DataType, Properties...>& view,
                    ComparatorType comp);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _min_element_link: ./StdMinElement.html

.. |min_element_link| replace:: ``min_element``

- ``exespace``, ``first``, ``last``, ``view``, ``comp``:  |min_element_link|_　におけるのと同様。
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _min_element_link: ./StdMinElement.html

.. |min_element_link| replace:: ``min_element``

- ``exespace``, ``first``, ``last``, ``view``, ``comp``:  |min_element_link|_　におけるのと同様。

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1 および 3: デフォルト文字列は、 "Kokkos::max_element_iterator_api_default".

  - 5 および 7: デフォルト文字列は、 "Kokkos::max_element_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

戻り値
~~~~~~~~~~~~

最大要素へのイテレータ。

以下の特例が適用されます:

- 複数の要素が最大の要素と同等である場合、そのような要素のうち *最初* の要素へのイテレータを返します。

- 範囲 ``[first, last)`` が空である場合、それは ``last``　を返します。

- ``ビュー`` が空である場合、 それは ``Kokkos::Experimental::end(view)``　を返します。

例
~~~~~~~

.. code-block:: cpp

   名前空間 KE = Kokkos::Experimental;
   Kokkos::View<double*> a("a", 13);
   //  a を何らかの方法で満たす

   自動 res = KE::max_element(Kokkos::DefaultExecutionSpace(), KE::begin(a), KE::end(a));

   // ビューを直接渡す
   auto res = KE::max_element(Kokkos::DefaultExecutionSpace(), a);


   // カスタムコンパレータを使用
   テンプレート <class ValueType1, class ValueType2 = ValueType1>
   構造体 CustomLessThanComparator {
     KOKKOS_INLINE_FUNCTION
     bool operator()(const ValueType1& a,
                     const ValueType2& b) const {
       // ここでは　<　を使用していますが、a　が　b　より小さい場合に、真を返すような任意のカスタムロジックを実装することも可能です。
       return a < b　を返す;
     }

     KOKKOS_INLINE_FUNCTION
     CustomLessThanComparator() {}
   };

   // ビューを直接渡す
   自動 res = KE::max_element(Kokkos::DefaultExecutionSpace(), a, CustomLessThanComparator<double>());
