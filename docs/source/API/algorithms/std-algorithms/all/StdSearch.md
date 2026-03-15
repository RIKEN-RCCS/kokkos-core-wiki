
# `search`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```cpp
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class IteratorType1, class IteratorType2>
IteratorType1 search(const ExecutionSpace& exespace, IteratorType1 first,
                     IteratorType1 last, IteratorType2 s_first,                      (1)
                     IteratorType2 s_last);

template <class ExecutionSpace, class IteratorType1, class IteratorType2>
IteratorType1 search(const std::string& label, const ExecutionSpace& exespace,
                     IteratorType1 first, IteratorType1 last,                        (2)
                     IteratorType2 s_first, IteratorType2 s_last);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2>
auto search(const ExecutionSpace& exespace,
            const ::Kokkos::View<DataType1, Properties1...>& view,                   (3)
            const ::Kokkos::View<DataType2, Properties2...>& s_view);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2>
auto search(const std::string& label, const ExecutionSpace& exespace,
            const ::Kokkos::View<DataType1, Properties1...>& view,                   (4)
            const ::Kokkos::View<DataType2, Properties2...>& s_view);

// オーバーロードセット 2: 引き渡された二項述語
template <class ExecutionSpace, class IteratorType1, class IteratorType2,
          class BinaryPredicateType>
IteratorType1 search(const ExecutionSpace& exespace, IteratorType1 first,                  (5)
                     IteratorType1 last, IteratorType2 s_first,
                     IteratorType2 s_last, const BinaryPredicateType& pred);

template <class ExecutionSpace, class IteratorType1, class IteratorType2,
          class BinaryPredicateType>
IteratorType1 search(const std::string& label, const ExecutionSpace& exespace,
                     IteratorType1 first, IteratorType1 last,                        (6)
                     IteratorType2 s_first, IteratorType2 s_last,
                     const BinaryPredicateType& pred);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2, class BinaryPredicateType>
auto search(const ExecutionSpace& exespace,
            const ::Kokkos::View<DataType1, Properties1...>& view,                   (7)
            const ::Kokkos::View<DataType2, Properties2...>& s_view,
            const BinaryPredicateType& pred);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2, class BinaryPredicateType>
auto search(const std::string& label, const ExecutionSpace& exespace,
            const ::Kokkos::View<DataType1, Properties1...>& view,                   (8)
            const ::Kokkos::View<DataType2, Properties2...>& s_view,
            const BinaryPredicateType& pred)

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

 (1,2,5,6)　における、[s_first, s_last)　の要素列が、範囲　[first, last)　の内での最初の出現を検索します。
 (3,4,7,8)　における、要素列 `s_view` の最初の出現を検索します。
 (1,2,3,4) 内の要素は、 `==` を使用して比較され、 (5,6,7,8) 内の要素は、 `pred`　を使用して比較されます。

## パラメータおよび要件

- `exespace`, `s_first`, `s_last`, `first`, `last`, `s_view` および `view` は、 [`mismatch`](./StdMismatch)　と同様です。

- `label`:
    - 1,5: デフォルト文字列は、"Kokkos::search_iterator_api_default".
    - 3,7: デフォルト文字列は、 "Kokkos::search_view_api_default".

- `pred` -  [`equal`](./StdEqual) と同様。
