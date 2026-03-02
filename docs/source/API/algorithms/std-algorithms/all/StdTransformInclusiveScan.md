
# `transform_inclusive_scan`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class BinaryOpType, class UnaryOpType>
OutputIteratorType transform_inclusive_scan(const ExecutionSpace& exespace,       (1)
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class BinaryOpType, class UnaryOpType>
OutputIteratorType transform_inclusive_scan(const std::string& label,             (2)
                                            const ExecutionSpace& exespace,
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType, class UnaryOpType>
自動 transform_inclusive_scan(const ExecutionSpace& exespace,                     (3)
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op,
                              UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  class BinaryOpType, class UnaryOpType>
自動 transform_inclusive_scan(const std::string& label,                           (4)
                              const ExecutionSpace& exespace,
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op,
                              UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class BinaryOpType, class UnaryOpType,
  クラス ValueType>
OutputIteratorType transform_inclusive_scan(const ExecutionSpace& exespace,       (5)
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op,
                                            ValueType init_value);

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class BinaryOpType, class UnaryOpType,
  クラス ValueType>
OutputIteratorType transform_inclusive_scan(const std::string& label,             (6)
                                            const ExecutionSpace& exespace,
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op,
                                            ValueType init_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType, class UnaryOpType, class ValueType>
自動 transform_inclusive_scan(const ExecutionSpace& exespace,                     (7)
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op, UnaryOpType unary_op,
                              ValueType init_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType, class UnaryOpType, class ValueType>
自動 transform_inclusive_scan(const std::string& label,                           (8)
                              const ExecutionSpace& exespace,
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op, UnaryOpType unary_op,
                              ValueType init_value);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

- 1,2: transforms each element in the range `[first_from, last_from)`
with `unary_op`, then computes an inclusive prefix scan operation using `binary_op`
over the resulting range, and writes the results to the range beginning at `first_dest`. unary_op 演算子を用いて変換し、次に 範囲 [first_from, last_from)　内の各要素を、 結果の範囲に対してbinary_op を使用してプレフィックススキャン演算を計算し、 init を初期値として使用して、 first_dest　で始まる範囲に結果を書き込みます。 i番目の入力要素を意味する　"exclusive" は、i番目の和には含まれません。

- 3,4: same as (1,2) except that the elements are read from `view_from`
and written to `view_dest`

- 5,6: same as (1,2) but the scan accounts for the `init_value`.

- 7,8: same as (3,4) but the scan accounts for the `init_value`.

Inclusive means that the i-th input element is included in the i-th sum.

## Parameters and Requirements

- `exespace`, `first_from`, `first_last`, `first_dest`, `view_from`, `view_dest`, `init_value`, `bin_op`, `unary_op`:
  - same as [`transform_exclusive_scan`](./StdTransformExclusiveScan)
- `label`:
  - used to name the implementation kernels for debugging purposes
  - for 1,5 the default string is: "Kokkos::transform_inclusive_scan_iterator_api_default"
  - for 3,7 the default string is: "Kokkos::transform_inclusive_scan_view_api_default"

## Return

Iterator to the element *after* the last element written.
