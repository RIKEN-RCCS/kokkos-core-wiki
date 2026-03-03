
# `exclusive_scan`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

//
// オーバーロードセット A
//
テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class ValueType>
OutputIteratorType exclusive_scan(const ExecutionSpace& exespace,                (1)
                                  InputIteratorType first,
                                  InputIteratorType last,
                                  OutputIteratorType first_dest,
                                  ValueType init_value);

テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class ValueType>
OutputIteratorType exclusive_scan(const std::string& label,                      (2)
                                  const ExecutionSpace& exespace,
                                  InputIteratorType first,
                                  InputIteratorType last,
                                  OutputIteratorType first_dest,
                                  ValueType init_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType>
auto exclusive_scan(const ExecutionSpace& exespace,                              (3)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    ValueType init_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType>
自動 exclusive_scan(const std::string& label, const ExecutionSpace& exespace,    (4)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    ValueType init_value);

//
// オーバーロードセット B
//
テンプレート <
 クラス ExecutionSpace, class InputIteratorType,
 クラス OutputIteratorType, class ValueType, class BinaryOpType
 >
OutputIteratorType exclusive_scan(const ExecutionSpace& exespace,                (5)
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest,
                                  ValueType init_value, BinaryOpType bin_op);


テンプレート <
  クラス ExecutionSpace, class InputIteratorType,
  クラス OutputIteratorType, class ValueType, class BinaryOpType
  >
OutputIteratorType exclusive_scan(const std::string& label,                      (6)
                                  const ExecutionSpace& exespace,
                                  InputIteratorType first_from,
                                  InputIteratorType last_from,
                                  OutputIteratorType first_dest,
                                  ValueType init_value, BinaryOpType bin_op);

テンプレート <
  クラス ExecutionSpace, class DataType1, class... Properties1,
  クラス DataType2, class... Properties2, class ValueType,
  クラス BinaryOpType>
自動 exclusive_scan(const ExecutionSpace& exespace,                              (7)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    ValueType init_value, BinaryOpType bin_op);

テンプレート <
  クラス ExecutionSpace, class DataType1, class... Properties1,
  クラス DataType2, class... Properties2, class ValueType,
  クラス BinaryOpType>
自動 exclusive_scan(const std::string& label, const ExecutionSpace& exespace,    (8)
                    const ::Kokkos::View<DataType1, Properties1...>& view_from,
                    const ::Kokkos::View<DataType2, Properties2...>& view_dest,
                    ValueType init_value, BinaryOpType bin_op);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

- 1,2,3,4: 範囲 `[first_from, last_from)` (1,2)または `view_from` (3,4)　について、
`init` を初期値として使用して、排他的累積　*和* を計算し、 結果を
`first_dest` (1,2)  から始まる範囲、または `view_dest` (3,4)に書き込みます。

- 5,6,7,8: `init` を初期値として使用して、 範囲 `[first_from, last_from)` (5,6)　または
  `view_from` (7,8)　を組み合わせるために、二項ファンクタ `bin_op`　を使用して排他的累積スキャンを計算し、
  結果を　`first_dest` (5,6) で始まる範囲、または `view_dest` (7,8)　に書き込みます。

排他的とは、i番目の入力は、i番目の和には含まれないことを意味します。

## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス
- `label`:
  - デバッグ目的で内部の並列カーネルに名付けるために使用
  - 1,2　について、デフォルト文字列は、: "Kokkos::exclusive_scan_iterator_api_default"
  - 5,6 について、デフォルト文字列は、: "Kokkos::exclusive_scan_view_api_default"
- `first_from`, `last_from`, `first_dest`:
  - 読み取り (`*_from`) および書き込む (`first_dest`)　要素の範囲
  -  *ランダムアクセスイテレータ*　でなければなりません。
  - 有効な範囲、つまり、 `last_from >= first_from` (デバッグモード確認済み)　を表す必要があります。
  -  `exespace`　からアクセス可能でなければなりません。
- `view_from`, `view_dest`:
  - `view_from` から要素を読み取り、 `view_dest`　にそれらを書き込むためのビュー。
  - 必ずランク-1であり、`LayoutLeft`, `LayoutRight`, or `LayoutStride` を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `bin_op`:
  - 要素のペアを組み合わせる演算を表す　*二項* ファンクタ。
  引数を引き渡された実行空間から呼び出されるために、有効でなければならず、
　型 (constの可能性) `value_type`　の2つの引数 `a,b`　を使って、呼び出し可能でなければなりません。そこでは、`value_type`　が　`InputIteratorType` (1,2,5,6　について) または、  `view_from` (3,4,7,8について)　の値型であり、 ``a,b``　を変更してはいけません。

  - 以下に一致しなければなりません:
  ```c++
  構造体 BinaryOp
  {
     KOKKOS_INLINE_FUNCTION
     return_type operator()(const value_type & a,
	                        const value_type & b) const {
       return /* ... */;
     }
  };
  ```
  戻り型 `return_type` は、(1,2,5,6)　について 型　`OutputIteratorType`　のオブジェクト、または
  `value_type` が (3,4,7,8) について　`view_dest`　の値型である、型 `value_type` のオブジェクトは、
   型 `return_type`　の値について、参照解除および割り当てが可能であるようでなければなりません。

## 戻し

最後の要素がコピーされた *後*　の宛先へのイテレータ。
