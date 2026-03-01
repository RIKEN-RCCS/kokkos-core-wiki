
# `replace_copy_if`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <
  クラス ExecutionSpace,
  クラス InputIteratorType, class OutputIteratorType,
  クラス UnaryPredicateType, class T
>
OutputIteratorType replace_copy_if(const ExecutionSpace& exespace,              (1)
                                   InputIteratorType first_from,
                                   InputIteratorType last_from,
                                   OutputIteratorType first_to,
                                   UnaryPredicateType pred, const T& new_value);

テンプレート <
  クラス ExecutionSpace,
  クラス InputIteratorType,  class OutputIteratorType,
  クラス UnaryPredicateType, class T
>
OutputIteratorType replace_copy_if(const std::string& label,                    (2)
                                   const ExecutionSpace& exespace,
                                   InputIteratorType first_from,
                                   InputIteratorType last_from,
                                   OutputIteratorType first_to,
                                   UnaryPredicateType pred, const T& new_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス UnaryPredicateType, class T
>
自動 replace_copy_if(const ExecutionSpace& exespace,                            (3)
                     const Kokkos::View<DataType1, Properties1...>& view_from,
                     const Kokkos::View<DataType2, Properties2...>& view_to,
                     UnaryPredicateType pred, const T& new_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス UnaryPredicateType, class T
>
自動 replace_copy_if(const std::string& label,                                  (4)
                     const ExecutionSpace& exespace,
                     const Kokkos::View<DataType1, Properties1...>& view_from,
                     const Kokkos::View<DataType2, Properties2...>& view_to,
                     UnaryPredicateType pred, const T& new_value);

} //エンド 名前空間 Experimental
} //エンド 名前空間 Kokkos
```

## ディスクリプション

Copies the elements from range `[first_from, last_from)` to another range
beginning at `first_to` (overloads 1,2) or from `view_from` to `view_to`
(overloads 3,4) replacing with `new_value` all elements for which `pred` returns `true`.


## Parameters and Requirements

- `exespace`, `first_from`, `last_from`, `first_to`, `view_from`, `view_to`, `new_value`:
  - same as in [`replace_copy`](./StdReplaceCopy)
- `label`:
  - for 1, the default string is: "Kokkos::replace_copy_if_iterator_api_default"
  - for 3, the default string is: "Kokkos::replace_copy_if_view_api_default"
- `pred`:
  - unary predicate which returns `true` for the required element; `pred(v)`
  must be valid to be called from the execution space passed, and convertible to bool for every
  argument `v` of type (possible const) `value_type`, where `value_type`
  is the value type of `InputIteratorType` (for 1,2) or of `view_from` (for 3,4),
  and must not modify `v`.
  - should have the same API as that shown for [`replace_if`](./StdReplaceIf)


## Return

Iterator to the element *after* the last element copied.
