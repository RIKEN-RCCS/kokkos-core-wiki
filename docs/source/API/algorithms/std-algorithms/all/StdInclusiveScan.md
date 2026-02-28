
# `inclusive_scan`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 実験的{

//
// オーバーロードセット A
//
テンプレート <class ExecutionSpace, class InputIteratorType, class OutputIteratorType>
OutputIteratorType inclusive_scan(const ExecutionSpace& exespace,                 (1)
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest);

テンプレート <class ExecutionSpace, class InputIteratorType, class OutputIteratorType>
OutputIteratorType inclusive_scan(const std::string& label,                       (2)
                                  const ExecutionSpace& exespace,
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2>
自動 inclusive_scan(const ExecutionSpace& exespace,                               (3)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2>
自動 inclusive_scan(const std::string& label, const ExecutionSpace& exespace,     (4)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest);

//
// オーバーロードセット B
//
テンプレート <
 クラス ExecutionSpace, class InputIteratorType,
 クラス OutputIteratorType, class BinaryOpType
 >
OutputIteratorType inclusive_scan(const ExecutionSpace& exespace,                 (5)
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest,
                                  BinaryOpType bin_op);

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class BinaryOpType
  >
OutputIteratorType inclusive_scan(const std::string& label,                       (6)
                                  const ExecutionSpace& exespace,
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest,
                                  BinaryOpType bin_op);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType>
自動 inclusive_scan(const ExecutionSpace& exespace,                               (7)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    BinaryOpType bin_op);

テンプレート <
  クラス ExecutionSpace, class DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType>
自動 inclusive_scan(const std::string& label, const ExecutionSpace& exespace,     (8)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    BinaryOpType bin_op);

//
// オーバーロードセット C
//
テンプレート <
 クラス ExecutionSpace,
 クラス InputIteratorType, class OutputIteratorType,
 クラス BinaryOpType, class ValueType
 >
OutputIteratorType inclusive_scan(const ExecutionSpace& exespace,                 (9)
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest,
                                  BinaryOpType bin_op,
                                  ValueType init_value);

テンプレート <
  クラス ExecutionSpace, クラス InputIteratorType,
  クラス OutputIteratorType, クラス BinaryOpType, クラス ValueType
  >
OutputIteratorType inclusive_scan(const std::string& label,                       (10)
                                  const ExecutionSpace& exespace,
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest,
                                  BinaryOpType bin_op,
                                  ValueType init_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType, class ValueType>
自動 inclusive_scan(const ExecutionSpace& exespace,                               (11)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    BinaryOpType bin_op,
                    ValueType init_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス BinaryOpType, class ValueType>
自動 inclusive_scan(const std::string& label, const ExecutionSpace& exespace,     (12)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    BinaryOpType bin_op,
                    ValueType init_value);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## Descriptionディスクリプション

- 1,2,3,4: 二つの要素を結合するために、二項演算子 `bin_op` を用いて、範囲 `[first_from, last_from)` (1,2) に対して、
- あるいは view_from` (3,4) に対して、インクルーシブプレフィックススキャンを計算し、
 `first_dest` (1,2) の範囲の始め、または `view_dest` (3,4)　に結果を書き込みます。

- 5,6,7,8: 二つの要素を結合するために、二項演算子 `bin_op` を用いて、範囲 `[first_from, last_from)` (5,6) に対して、
- あるいは view_from` (7,8) に対して、インクルーシブプレフィックススキャンを計算し、
 `first_dest` (5,6) の範囲の始め、または `view_dest` (7,8)　に結果を書き込みます。

- 9,10,11,12: 二つの要素および初期値としての `init`　を結合するために、二項演算子 `bin_op` を用いて、範囲 `[first_from, last_from)` (9,10) に対して、
- あるいは view_from` (11,12) に対して、インクルーシブプレフィックススキャンを計算し、
 `first_dest` (9,10) の範囲の始め、または `view_dest` (11,12)　に結果を書き込みます。

インクルーシブとは、i番目の入力要素が、i番目の和に含まれることを意味します。

## Parameters and Requirementsパラメータおよび要件

- `exespace`, `first_from`, `first_last`, `first_dest`, `view_from`, `view_dest`, `bin_op`:
  -  [`exclusive_scan`](./StdExclusiveScan)　と同様。
- `ラベル`:
  - デバッグ目的で実装カーネルに名付けるために使用
  - 1,5,9　について、デフォルト文字列は、 : "Kokkos::inclusive_scan_iterator_api_default"
  - 3,7,11　について、デフォルト文字列は、 : "Kokkos::inclusive_scan_iterator_api_default"

## 戻り値

最後の要素がコピーされた *後*　の宛先へのイテレータ。
