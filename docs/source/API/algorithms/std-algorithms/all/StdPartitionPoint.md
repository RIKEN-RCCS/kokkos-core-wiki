
# `partition_point`

ヘッダーファイル: `<Kokkos_StdAlgorithms.hpp>`

```c++
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class IteratorType, class PredicateType>
IteratorType partition_point(const ExecutionSpace& exespace,                   (1)
                             IteratorType first, IteratorType last,
                             PredicateType pred);

template <class ExecutionSpace, class IteratorType, class PredicateType>
IteratorType partition_point(const std::string& label,                         (2)
                             const ExecutionSpace& exespace,
                             IteratorType first, IteratorType last,
                             PredicateType pred);

template <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
auto partition_point(const ExecutionSpace& exespace,
                     const ::Kokkos::View<DataType, Properties...>& view,      (3)
                     PredicateType pred);

template <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
auto partition_point(const std::string& label,                                 (4)
                     const ExecutionSpace& exespace,
                     const ::Kokkos::View<DataType, Properties...>& view,
                     PredicateType pred);

} //end namespace Experimental
} //end namespace Kokkos
```

## 説明

範囲  `[first, last)` または  `ビュー` を調べ、
`pred` を満たさない最初の要素を位置付けます。

範囲（またはビュー）は既にパーティション分割済みであると仮定します。


## パラメータおよび要件

- `exespace`, `first`, `last`, `view`, `pred`:  [`is_partitioned`](./StdIsPartitioned) と同様。
  - 実行空間インスタンス
- `label`:
  - デバッグ目的の実装カーネルに名付けるために使用されます。
  - 1について、デフォルト文字列は、 : "Kokkos::partition_point_iterator_api_default"
  - 3について、デフォルト文字列は、 : "Kokkos::partition_point_view_api_default"

## 戻り値

最初のパーティションにおける、最後の要素の *後* の要素へのイテレータ、またはすべての要素が
 `pred` を満たす場合、`last` へのイテレータ。
