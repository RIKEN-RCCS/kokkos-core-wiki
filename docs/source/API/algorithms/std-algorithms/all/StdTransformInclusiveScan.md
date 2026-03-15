
# `transform_inclusive_scan`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
namespace Kokkos{
namespace Experimental{

template <
  class ExecutionSpace, class InputIteratorType,
  class OutputIteratorType, class BinaryOpType, class UnaryOpType>
OutputIteratorType transform_inclusive_scan(const ExecutionSpace& exespace,       (1)
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op);

template <
  class ExecutionSpace, class InputIteratorType,
  class OutputIteratorType, class BinaryOpType, class UnaryOpType>
OutputIteratorType transform_inclusive_scan(const std::string& label,             (2)
                                            const ExecutionSpace& exespace,
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op);

template <
  class ExecutionSpace,
  class DataType1, class... Properties1,
  class DataType2, class... Properties2,
  class BinaryOpType, class UnaryOpType>
auto transform_inclusive_scan(const ExecutionSpace& exespace,                     (3)
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op,
                              UnaryOpType unary_op);

template <
  class ExecutionSpace,
  class DataType1, class... Properties1,
  class DataType2, class... Properties2,
  class BinaryOpType, class UnaryOpType>
auto transform_inclusive_scan(const std::string& label,                           (4)
                              const ExecutionSpace& exespace,
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op,
                              UnaryOpType unary_op);

template <
  class ExecutionSpace, class InputIteratorType,
  class OutputIteratorType, class BinaryOpType, class UnaryOpType,
  class ValueType>
OutputIteratorType transform_inclusive_scan(const ExecutionSpace& exespace,       (5)
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op,
                                            ValueType init_value);

template <
  class ExecutionSpace, class InputIteratorType,
  class OutputIteratorType, class BinaryOpType, class UnaryOpType,
  class ValueType>
OutputIteratorType transform_inclusive_scan(const std::string& label,             (6)
                                            const ExecutionSpace& exespace,
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op,
                                            ValueType init_value);

template <
  class ExecutionSpace,
  class DataType1, class... Properties1,
  class DataType2, class... Properties2,
  class BinaryOpType, class UnaryOpType, class ValueType>
auto transform_inclusive_scan(const ExecutionSpace& exespace,                     (7)
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op, UnaryOpType unary_op,
                              ValueType init_value);

template <
  class ExecutionSpace,
  class DataType1, class... Properties1,
  class DataType2, class... Properties2,
  class BinaryOpType, class UnaryOpType, class ValueType>
auto transform_inclusive_scan(const std::string& label,                           (8)
                              const ExecutionSpace& exespace,
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              BinaryOpType binary_op, UnaryOpType unary_op,
                              ValueType init_value);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

- 1,2: unary_op 演算子を用いて変換し、次に 範囲 [first_from, last_from)　内の各要素を、 結果の範囲に対して、`unary_op` を使用して、インクルーシブプレフィックススキャン演算を計算し、 `first_dest`　で始まる範囲に結果を書き込みます。 

- 3,4: 要素が `view_from`　から読み込まれ、 `view_dest`　に書き込まれた要素である場合を除き、 (1,2) と同様です。

- 5,6:  (1,2) と同様ですが、スキャンは、 `init_value` を示します。

- 7,8:　(3,4) と同様ですが、スキャンは、 `init_value` を示します。

インクルーシブは、i番目の入力要素が、i番目の和に含まれることを意味します。


## パラメータおよび要件

- `exespace`, `first_from`, `first_last`, `first_dest`, `view_from`, `view_dest`, `init_value`, `bin_op`, `unary_op`:
  -  [`transform_exclusive_scan`](./StdTransformExclusiveScan)　と同様。
- `label`:
  - デバッグ目的で実装カーネルに名付けるために使用。
  - 1,5 について、デフォルト文字列は、: "Kokkos::transform_inclusive_scan_iterator_api_default"
  - 3,7 について、デフォルト文字列は、: "Kokkos::transform_inclusive_scan_view_api_default"

## 返し

書き込まれた最後の要素 *後の* 要素へのイテレータ。
