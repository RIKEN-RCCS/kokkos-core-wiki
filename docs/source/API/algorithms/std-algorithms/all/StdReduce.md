
# `reduce`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間　実験的 {

//
// オーバーロードセット A
//
テンプレート <class ExecutionSpace, class IteratorType>
型名 IteratorType::value_type reduce(const ExecutionSpace& exespace,        (1)
                                         IteratorType first,
                                         IteratorType last);

テンプレート <class ExecutionSpace, class IteratorType>
型名 IteratorType::value_type reduce(const std::string& label,              (2)
                                         const ExecutionSpace& exespace,
                                         IteratorType first,
                                         IteratorType last);

テンプレート <class ExecutionSpace, class DataType, class... Properties>
自動 reduce(const ExecutionSpace& exespace,                                     (3)
            const ::Kokkos::View<DataType, Properties...>& view);

テンプレート <class ExecutionSpace, class DataType, class... Properties>
自動 reduce(const std::string& label, const ExecutionSpace& exespace,           (4)
            const ::Kokkos::View<DataType, Properties...>& view);

//
// オーバーロードセット B
//
テンプレート <class ExecutionSpace, class IteratorType, class ValueType>
ValueType reduce(const ExecutionSpace& exespace,                                (5)
                 IteratorType first, IteratorType last,
                 ValueType init_reduction_value);

テンプレート <class ExecutionSpace, class IteratorType, class ValueType>
ValueType reduce(const std::string& label, const ExecutionSpace& exespace,      (6)
                 IteratorType first, IteratorType last,
                 ValueType init_reduction_value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class ValueType>
ValueType reduce(const ExecutionSpace& exespace,                                (7)
                 const ::Kokkos::View<DataType, Properties...>& view,
                 ValueType init_reduction_value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class ValueType>
ValueType reduce(const std::string& label,                                      (8)
                 const ExecutionSpace& exespace,
                 const ::Kokkos::View<DataType, Properties...>& view,
                 ValueType init_reduction_value);

//
// オーバーロードセット C
//
テンプレート <
  クラス ExecutionSpace, class IteratorType, class ValueType,
  クラス BinaryOp>
ValueType reduce(const ExecutionSpace& exespace,                                (9)
                 IteratorType first, IteratorType last,
                 ValueType init_reduction_value,
                 BinaryOp joiner);

テンプレート <
  クラス ExecutionSpace, class IteratorType, class ValueType,
  クラス BinaryOp>
ValueType reduce(const std::string& label, const ExecutionSpace& exespace,      (10)
                 IteratorType first, IteratorType last,
                 ValueType init_reduction_value,
                 BinaryOp joiner);

テンプレート <
  クラス ExecutionSpace, class DataType, class... Properties,
  クラス ValueType, class BinaryOp>
ValueType reduce(const ExecutionSpace& exespace,                                (11)
                 const ::Kokkos::View<DataType, Properties...>& view,
                 ValueType init_reduction_value,
                 BinaryOp joiner);

テンプレート <
  クラス ExecutionSpace, class DataType, class... Properties,
  クラス ValueType, class BinaryOp>
ValueType reduce(const std::string& label, const ExecutionSpace& exespace,      (12)
                 const ::Kokkos::View<DataType, Properties...>& view,
                 ValueType init_reduction_value,
                 BinaryOp joiner);

} //エンド　名前空間 実験的
} //エンド　名前空間 Kokkos
```

## ディスクリプション

- オーバーロードセット A (1,2,3,4): 範囲 `[first, last)` (1,2) または `ビュー` (3,4)　における要素の還元を実行します。

- オーバーロードセット B (5,6,7,8): 初期値 `init_reduction_value`　を説明する、範囲 `[first, last)` (5,6) または `ビュー` (7,8) における要素の還元を実行します。

- オーバーロードセット C (9,10,11,12): 還元演算の間にオペランドを結合するための、ファンクタ　`ジョイナー`　を使って、初期値 `init_reduction_value`　を説明する、範囲　`[first, last)` (9,10)　または `ビュー` (11,12) における要素の還元を実行します。


## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス
- `ラベル`デバッグ目的の実装カーネルに名付けるために使用されます。
  - デバッグ目的の実装カーネルに名付けるために使用されます。
  - 1,5,9について、デフォルト文字列は、: "Kokkos::reduce_iterator_api_default"
  - 3,7,11について、デフォルト文字列は、: "Kokkos::reduce_view_api_default"
- `first`, `last`:
  - 還元する要素の範囲
  - *ランダムアクセスイテレータ*　でなければなりません。
  - 有効な範囲、つまり、 ``last >= first``　を表す必要があります　（デバッグモードで確認済）。
  -  `exespace`　からアクセス可能でなければなりません。
- `view`:
  - 還元対象のビュー
  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `init_reduction_value`:
  - 使用する初期還元値
- `joiner`:
  -  *二項*　ファンクタであり、2つの要素を結合するために所望の演算を実行します。
  引数として渡された実行空間、またはチームハンドルに関連付けられた実行空間から呼び出されるために、有効でなければならず、 型 (可能性のあるconst)　`ValueType`　の2つの引数　で呼び出し可能であり、 `a,b`　を変更してはいけません。

  - 以下に一致しなければなりません:
  ```c++
  構造体 JoinFunctor {
	KOKKOS_FUNCTION
	constexpr ValueType operator()(const ValueType& a, const ValueType& b) const {
	  return /* ... */
	}
  };
  ```
  - `join`　演算が、結合法則または交換法則を満たさない場合、
その動作は非決定的です


## 戻し

還元結果。
