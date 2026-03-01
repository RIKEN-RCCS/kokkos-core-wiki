
# `search_n`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```cpp
名前空間 Kokkos{
名前空間 実験的E{

テンプレート <class ExecutionSpace, class IteratorType, class SizeType,
          class ValueType>
IteratorType search_n(const ExecutionSpace& exespace, IteratorType first,
                      IteratorType last, SizeType count,                             (1)
                      const ValueType& value);

テンプレート <class ExecutionSpace, class IteratorType, class SizeType,
          class ValueType>
IteratorType search_n(const std::string& label, const ExecutionSpace& exespace,
                      IteratorType first, IteratorType last, SizeType count,         (2)
                      const ValueType& value);

テンプレート <class ExecutionSpace, class DataType, class... Properties,
          class SizeType, class ValueType>
自動 search_n(const ExecutionSpace& exespace,
              const ::Kokkos::View<DataType, Properties...>& view,                   (3)
              SizeType count, const ValueType& value);

テンプレート <class ExecutionSpace, class DataType, class... Properties,
          class SizeType, class ValueType>
自動 search_n(const std::string& label, const ExecutionSpace& exespace,
              const ::Kokkos::View<DataType, Properties...>& view,                   (4)
              SizeType count, const ValueType& value);

// オーバーロードセット 2: 引き渡された二項述語
テンプレート <class ExecutionSpace, class IteratorType, class SizeType,
          class ValueType, class BinaryPredicateType>
IteratorType search_n(const ExecutionSpace& exespace, IteratorType first,
                      IteratorType last, SizeType count, const ValueType& value,     (5)
                      const BinaryPredicateType& pred);

テンプレート <class ExecutionSpace, class IteratorType, class SizeType,
          class ValueType, class BinaryPredicateType>
IteratorType search_n(const std::string& label, const ExecutionSpace& exespace,
                      IteratorType first, IteratorType last, SizeType count,         (6)
                      const ValueType& value, const BinaryPredicateType& pred);

テンプレート <class ExecutionSpace, class DataType, class... Properties,
          class SizeType, class ValueType, class BinaryPredicateType>
自動 search_n(const ExecutionSpace& exespace,
              const ::Kokkos::View<DataType, Properties...>& view,                   (7)
              SizeType count, const ValueType& value,
              const BinaryPredicateType& pred);

テンプレート <class ExecutionSpace, class DataType, class... Properties,
          class SizeType, class ValueType, class BinaryPredicateType>
auto search_n(const std::string& label, const ExecutionSpace& exespace,
              const ::Kokkos::View<DataType, Properties...>& view,                   (8)
              SizeType count, const ValueType& value,
              const BinaryPredicateType& pred);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

範囲 [first, last) を、`count` 要素の範囲について、それぞれ `value`   (1,2)　と等しいかどうかを比較して、検索します。
`count` 要素の範囲について、それぞれ `value`  (3,4) と等しいかどうかを比較して、 `view` を検索します。
 (5,6)　における `value` について、 `pred` が真を返す`count` 要素の範囲について、範囲 [first, last) を検索します。
 (7,8)　における `value` について、 `pred` が真を返す`count` 要素の範囲について、 `view` を検索します。

## パラメータおよび要件

- `exespace`, `first`, `last`, `view` および `count` は、 [`for_each_n`](./StdForEachN)　と同様。

- `label`:
    - 1,5: デフォルト文字列は、 "Kokkos::search_n_iterator_api_default".
    - 3,7: デフォルト文字列は、 "Kokkos::search_n_view_api_default".

- `pred` -  [`equal`](./StdEqual) と同様。
