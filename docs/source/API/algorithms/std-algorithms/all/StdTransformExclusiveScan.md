# `transform_exclusive_scan`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class ValueType,
  クラス BinaryOpType, class UnaryOpType>
OutputIteratorType transform_exclusive_scan(const ExecutionSpace& exespace,     (1)
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            ValueType init_value,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class ValueType,
  クラス BinaryOpType, class UnaryOpType>
OutputIteratorType transform_exclusive_scan(const std::string& label,           (2)
                                            const ExecutionSpace& exespace,
                                            InputIteratorType first_from,
                                            InputIteratorType last_from,
                                            OutputIteratorType first_dest,
                                            ValueType init_value,
                                            BinaryOpType binary_op,
                                            UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType, class BinaryOpType, class UnaryOpType>
auto transform_exclusive_scan(const ExecutionSpace& exespace,                   (3)
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              ValueType init_value, BinaryOpType binary_op,
                              UnaryOpType unary_op);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType, class BinaryOpType, class UnaryOpType>
自動 transform_exclusive_scan(const std::string& label,                         (4)
                              const ExecutionSpace& exespace,
                              const ::Kokkos::View<DataType1, Properties1...>& view_from,
                              const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                              ValueType init_value, BinaryOpType binary_op,
                              UnaryOpType unary_op);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

- 1,2:`unary_op` 演算子を用いて変換し、次に、  範囲 `[first_from, last_from)` 内の各要素を、
結果の範囲に対して、`binary_op` を使用して、エクスクルーシブプレフィックススキャン演算を計算し、
 `init` を初期値として使用して、 `first_dest`　で始まる範囲に結果を書き込みます。
i番目の入力要素を意味する　"exclusive" は、i番目の和には含まれません。

- 3,4: 要素が `view_from`　から読み込まれ、 `view_dest`　に書き込まれた要素である場合を除き、 (1,2) と同様です。

## パラメータおよび要件

- `exespace`, `first_from`, `first_last`, `first_dest`, `view_from`, `view_dest`:
  -  [`exclusive_scan`](./StdExclusiveScan)　と同様。
- `label`:
  - デバッグ目的で実装カーネルに名付けるために使用。
  - 1　について、デフォルト文字列は、: "Kokkos::transform_exclusive_scan_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::transform_exclusive_scan_view_api_default"
- `unary_op`:
  -要素に対して所望の変換演算を実行する *一項* ファンクタ。
  引数として渡された実行空間から呼び出されるためには、有効でなければならない、そして 型 (可能性のあるconst)　value_type　の引数　`v`　について、bool型に変換可能で、そこでは、value_type``　が、 `first_from` (1,2について)　の値型、または `view_from` (3,4について)　であり、 `v` 　を変更してはいけません。


  - 以下に一致ししなければなりません:
  ```c++
  構造体 UnaryOp {
	KOKKOS_FUNCTION
	constexpr value_type operator()(const value_type & v) const {
	  return /* ... */
	}
  };
  ```

## 返し

書き込まれた最後の要素 *後* の要素へのイテレータ。
