
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

## Parameters and Requirements

- `exespace`:
  - execution space instance

- `label`:
    - 1,5: The default string is "Kokkos::lexicographical_compare_iterator_api_default".
    - 3,7: The default string is "Kokkos::lexicographical_compare_view_api_default".

- `first1`, `last1`, `first2`, `last2`:
  - range of elements to compare
  - must be *random access iterators*
  - must represent valid ranges, i.e., `last1 >= first1` and `last2 >= first2` 
  - must be accessible from `exespace`

- `view1`, `view2`:
  - views to compare
  - must be rank-1, and have `LayoutLeft`, `LayoutRight`, or `LayoutStride`
  - must be accessible from `exespace`

- `pred` - similar to [`equal`](./StdEqual)


