
# `transform_reduce`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

//
// オーバーロードセット A
//
テンプレート <
  クラス ExecutionSpace, class IteratorType1,
  クラス IteratorType2, class ValueType>
ValueType transform_reduce(const ExecutionSpace& exespace,                      (1)
                           IteratorType1 first1, IteratorType1 last1,
                           IteratorType2 first2,
                           ValueType init_reduction_value);

テンプレート <
  クラス ExecutionSpace, class IteratorType1,
  クラス IteratorType2, class ValueType>
ValueType transform_reduce(const std::string& label,                            (2)
                           const ExecutionSpace& exespace,
                           IteratorType1 first1, IteratorType1 last1,
                           IteratorType2 first2,
                           ValueType init_reduction_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType>
ValueType transform_reduce(const ExecutionSpace& exespace,                      (3)
                           const ::Kokkos::View<DataType1, Properties1...>& first_view,
                           const ::Kokkos::View<DataType2, Properties2...>& second_view,
                           ValueType init_reduction_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType>
ValueType transform_reduce(const std::string& label,                            (4)
                           const ExecutionSpace& exespace,
                           const ::Kokkos::View<DataType1, Properties1...>& first_view,
                           const ::Kokkos::View<DataType2, Properties2...>& second_view,
                           ValueType init_reduction_value);

//
// オーバーロードセット B
//
テンプレート <
  クラス ExecutionSpace,
  クラス IteratorType1, class IteratorType2,
  クラス ValueType,
  クラス BinaryJoinerType, class BinaryTransform>
ValueType transform_reduce(const ExecutionSpace& exespace,                      (5)
                           IteratorType1 first1,
                           IteratorType1 last1, IteratorType2 first2,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           BinaryTransform binary_transformer);

テンプレート <
  クラス ExecutionSpace,
  クラス IteratorType1, class IteratorType2,
  クラス ValueType,
  クラス BinaryJoinerType, class BinaryTransform>
ValueType transform_reduce(const std::string& label,                            (6)
                           const ExecutionSpace& exespace,
                           IteratorType1 first1, IteratorType1 last1,
                           IteratorType2 first2,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           BinaryTransform binary_transformer);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス ValueType,
  クラス BinaryJoinerType, class BinaryTransform>
ValueType transform_reduce(const ExecutionSpace& exespace,                      (7)
                           const ::Kokkos::View<DataType1, Properties1...>& first_view,
                           const ::Kokkos::View<DataType2, Properties2...>& second_view,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           BinaryTransform binary_transformer);

テンプレート <
   クラス ExecutionSpace,
   クラス DataType1, class... Properties1,
   クラス DataType2, class... Properties2,
   クラス ValueType,
   クラス BinaryJoinerType, class BinaryTransform>
ValueType transform_reduce(const std::string& label,                            (8)
                           const ExecutionSpace& exespace,
                           const ::Kokkos::View<DataType1, Properties1...>& first_view,
                           const ::Kokkos::View<DataType2, Properties2...>& second_view,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           BinaryTransform binary_transformer);

//
// オーバーロードセット C
//
テンプレート <
  クラス ExecutionSpace,
  クラス IteratorType, class ValueType,
  クラス BinaryJoinerType, class UnaryTransform>
ValueType transform_reduce(const ExecutionSpace& exespace,                      (9)
                           IteratorType first1, IteratorType last1,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           UnaryTransform unary_transformer);

テンプレート <
  クラス ExecutionSpace,
  クラス IteratorType, class ValueType,
  クラス BinaryJoinerType, class UnaryTransform>
ValueType transform_reduce(const std::string& label,
                           const ExecutionSpace& exespace,                      (10)
                           IteratorType first1, IteratorType last1,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           UnaryTransform unary_transformer);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType, class... Properties, class ValueType,
  クラス BinaryJoinerType, class UnaryTransform>
ValueType transform_reduce(const ExecutionSpace& exespace,                      (11)
                           const ::Kokkos::View<DataType, Properties...>& first_view,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           UnaryTransform unary_transformer);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType, class... Properties, class ValueType,
  クラス BinaryJoinerType, class UnaryTransform>
ValueType transform_reduce(const std::string& label,                            (12)
                           const ExecutionSpace& exespace,
                           const ::Kokkos::View<DataType, Properties...>& first_view,
                           ValueType init_reduction_value,
                           BinaryJoinerType joiner,
                           UnaryTransform unary_transformer);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

- (1,2): 範囲 `[first1, last1)` 内の各要素と、`first2` から始まる範囲の要素との間で、
*積*（`演算子*` 経由）を実行し、結果を初期値 `init_reduction_value` と共に還元します。
  
- (3,4): performs the *product* (via `operator*`) between each pair
  of elements in `first_view` and `second_view`,　`first_view`　と　`second_view`　の各要素ペア間で
*積*（`演算子*` 経由）を実行し、結果を初期値 `init_reduction_value` と共に還元します。

- (5,6): ファンクタ　`binary_transformer` を、
範囲 `[first1, last1)` および `first2` から始まる範囲内の各要素のペアに適用し、
  結合演算を *バイナリ* ファンクタ `joiner` を通じて実行して、結果を初期値
  `init_reduction_value` と共に還元します。

- (7,8): ファンクタ　`binary_transformer` を、
`first_view` および `second_view` 範囲内の各要素のペアに適用し、
  結合演算を *バイナリ* ファンクタ `joiner` を通じて実行して、結果を初期値
  `init_reduction_value` と共に還元します。


- (9,10):  ファンクタ　`unary_transformer` を範囲 `[first, last)` の各要素に適用し、
  結合演算を *バイナリ* ファンクタ `joiner` を通じて実行して、結果を初期値
  `init_reduction_value` と共に還元します。

- (11,12): `view`　内の各要素に対してファンクタ　`unary_transformer`　を適用し、 
  結合演算を *バイナリ* ファンクタ `joiner` を通じて実行して、結果を初期値
  `init_reduction_value` と共に還元します。


## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス
- `label`:
  - デバッグ目的で実装カーネルに名付けるために使用。
  - 1,5,9　について、デフォルト文字列は、: "Kokkos::transform_reduce_iterator_api_default"
  - 3,7,11　について、デフォルト文字列は、: "Kokkos::transform_reduce_view_api_default"
- `first1`, `last1`, `first2`:
  - 変換および還元対象の要素の範囲
  - 　*ランダムアクセスイテレータ*　でなければなりません。
  - 有効な範囲を表す必要があり、つまり、 `last1 >= first1` (デバッグモードで確認済み)でなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `first_view`, `second_view`:
  - 変換および還元対象のビュー
  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `init_reduction_value`:
  - 使用する初期還元値
- `joiner`:
  - 2つの要素結合のために所望の変換演算を実行する *二項* ファンクタ。
  　引数として渡された実行空間から呼び出されるためには、有効でなければならない、そして 型 (可能性のあるconst)　`ValueType`  の2つの引数　`a,b`　を使って、呼び出し可能であり、 `a,b` を変更してはいけません。
  - 以下に一致しなければなりません:
  ```c++
  構造体 JoinFunctor {
	KOKKOS_FUNCTION
	constexpr ValueType operator()(const ValueType& a,
                                 const ValueType& b) const {
	  返し /* ... */
	}
  };
  ```
  - `joiner` 演算が、結合法則または交換法則に従わない場合、その挙動は非決定的です。

- `binary_transformer`:
  - 還元 *前* に、要素の各ペアに適用される　*二項* ファンクタ。
  引数として渡された実行空間から呼び出されるためには、有効でなければならない、そして 型 (可能性のあるconst)　`value_type_a`　および `value_type_b` の2つの引数　`a,b`　を使って、呼び出し可能であり、ここで、
  `value_type_{a,b}` は、 `first1` および `first2` (1,2,5,6について)　の値型であり、または
 `first_view` および　`second_view` (3,4,7,8について)　の値型であり、  `a,b` を変更してはいけません。
  - 以下に一致しなければなりません:
  ```c++
  struct BinaryTransformer {
	KOKKOS_FUNCTION
	constexpr return_type operator()(const value_type_a & a, const value_type_b & b) const {
	  返し /* ... */
	}
  };
  ```
  - `return_type`  は、それが　`joiner`により受け入れ可能であるという条件下にあります。

- `unary_transformer`:
  - 要素に対して所望の演算を実行する　*一項* ファンクタ。
  引数として渡された実行空間から呼び出されるためには、有効でなければならない、そして 型 (可能性のあるconst)　`value_type`　の引数　`v`　を使って呼び出し可能で、そこでは、`value_type`　が、 `first1` (9,10について)　の値型、または  `first_view` (11,12について)　であり、`v` を変更してはいけません。
  - 以下に一致しなければなりません:
  ```c++
  構造体 UnaryTransformer {
	KOKKOS_FUNCTION
	constexpr value_type operator()(const value_type & v) const {
	  return /* ... */
	}
  };
  ```

## 返し

還元結果。
