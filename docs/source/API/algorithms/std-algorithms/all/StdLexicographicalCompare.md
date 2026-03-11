
# `lexicographical_compare`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```cpp
名前空間 Kokkos{
名前空間 実験的{

テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2>
ブール lexicographical_compare(const ExecutionSpace& exespace, IteratorType1 first1,
                             IteratorType1 last1, IteratorType2 first2,              (1)
                             IteratorType2 last2);

テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2>
ブール lexicographical_compare(const std::string& label, const ExecutionSpace& exespace,
                             IteratorType1 first1, IteratorType1 last1,              (2)
                             IteratorType2 first2, IteratorType2 last2);

テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2>
ブール lexicographical_compare(
    const ExecutionSpace& exespace,
    const ::Kokkos::View<DataType1, Properties1...>& view1,                          (3)
    ::Kokkos::View<DataType2, Properties2...>& view2);

テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2>
ブール lexicographical_compare(
    const std::string& label, const ExecutionSpace& exespace,
    const ::Kokkos::View<DataType1, Properties1...>& view1,                          (4)
    ::Kokkos::View<DataType2, Properties2...>& view2);

テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2,
          class ComparatorType>
ブール lexicographical_compare(const ExecutionSpace& exespace, IteratorType1 first1,
                             IteratorType1 last1, IteratorType2 first2,              (5)
                             IteratorType2 last2, ComparatorType comp);

テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2,
          class ComparatorType>
ブール lexicographical_compare(const std::string& label, const ExecutionSpace& exespace,
                             IteratorType1 first1, IteratorType1 last1,              (6)
                             IteratorType2 first2, IteratorType2 last2,
                             ComparatorType comp);

テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2, class ComparatorType>
ブール lexicographical_compare(
    const ExecutionSpace& exespace,
    const ::Kokkos::View<DataType1, Properties1...>& view1,
    ::Kokkos::View<DataType2, Properties2...>& view2, ComparatorType comp);          (7)


テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2, class ComparatorType>
ブール lexicographical_compare(
    const std::string& label, const ExecutionSpace& exespace,
    const ::Kokkos::View<DataType1, Properties1...>& view1,                          (8)
    ::Kokkos::View<DataType2, Properties2...>& view2, ComparatorType comp);

} //エンド　名前空間 実験的
} //エンド　名前空間 Kokkos
```

## ディスクリプション

第1の範囲 [first1, last1) が、第2の範囲 [first2, last2)　よりも順序の上で、小さい場合に、(1,2,5,6) について、`真`　を返します。
`view1` の要素が `view2`における要素よりも順序の上で、小さい場合に、(3,4,7,8) について、`真`　を返します。
Elements (1,2,3,4) are compared using the `<` operator.
Elements (5,6,7,8) are compared using `comp`.

## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス

- `ラベル`:
    - 1,5: デフォルト文字列は、 "Kokkos::lexicographical_compare_iterator_api_default".
    - 3,7: デフォルト文字列は、 "Kokkos::lexicographical_compare_view_api_default".

- `first1`, `last1`, `first2`, `last2`　:
  - 比較対象の要素の範囲
  - *ランダムアクセスイテレータ*　でなければなりません。
  - 有効な範囲、つまり `last1 >= first1` および `last2 >= first2`　を表さなければなりません。
  - `exespace`からアクセス可能でなければなりません。

- `view1`, `view2`:
  - 比較対象のビュー
  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - ``exespace``　からアクセス可能でなければなりません。

- `pred` -  [`equal`](./StdEqual)　と同様。


