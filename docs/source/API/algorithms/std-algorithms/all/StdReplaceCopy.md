
# `replace_copy`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <class ExecutionSpace, class InputIteratorType, class OutputIteratorType, class T>
OutputIteratorType replace_copy(const ExecutionSpace& exespace,               (1)
                                InputIteratorType first_from,
                                InputIteratorType last_from,
                                OutputIteratorType first_to,
                                const T& old_value, const T& new_value);

テンプレート <class ExecutionSpace, class InputIteratorType, class OutputIteratorType, class T>
OutputIteratorType replace_copy(const std::string& label,                     (2)
                                const ExecutionSpace& exespace,
                                OutputIteratorType first_to,
                                const T& old_value, const T& new_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス T
>
自動 replace_copy(const ExecutionSpace& exespace,                             (3)
                  const Kokkos::View<DataType1, Properties1...>& view_from,
                  const Kokkos::View<DataType2, Properties2...>& view_to,
                  const T& old_value, const T& new_value);

テンプレート <
  クラス ExecutionSpace,
  クラス DataType1, class... Properties1,
  クラス DataType2, class... Properties2,
  クラス T
>
自動 replace_copy(const std::string& label,
                  const ExecutionSpace& exespace,                             (4)
                  const Kokkos::View<DataType1, Properties1...>& view_from,
                  const Kokkos::View<DataType2, Properties2...>& view_to,
                  const T& old_value, const T& new_value);

} //エンド 名前空間 Experimental
} //エンド 名前空間 Kokkos
```

## ディスクリプション

`old_value` と等しいすべての要素を `new_value` で置換して、範囲 `[first_from, last_from)` の要素を、別の範囲
`first_to` から始まる範囲（オーバーロード 1,2）または `view_from` から `view_to` までの範囲
（オーバーロード 3,4）にコピーします。`operator==`　を使用して、要素間の比較を実行します。

## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス
- `label`:
  - デバッグ目的で実装カーネルに名付けるために使用。
  - 1　について、デフォルト文字列は、: "Kokkos::replace_copy_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::replace_copy_view_api_default"
- `first_from, last_from`:
  - コピー元への要素の範囲
  - *ランダムアクセスイテレータ*　でなければなりません。
  - 有効範囲、つまり、 ``last >= first``　を表さなければなりません。 (デバッグモードで確認済み)
  - `exespace`　からアクセス可能でなければなりません。
- `first_to`:
  - コピー先への範囲の始め
  - *ランダムアクセスイテレータ*　でなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `view_from`, `view_to`:
  - ソースおよび宛先のビュー
  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `old_value`, `new_value`:
  - 説明を要しません。


## 返し

コピーされた最後の要素の *後* の要素へのイテレータ。
