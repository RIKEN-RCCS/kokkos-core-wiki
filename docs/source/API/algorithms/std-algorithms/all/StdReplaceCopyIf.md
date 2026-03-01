
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

`pred` が `真`　を返すすべての要素を `new_value` と置換して、 範囲 `[first_from, last_from)` の要素を、別の範囲
`first_to` から始まる範囲（オーバーロード 1,2）または `view_from` から `view_to` までの範囲
（オーバーロード 3,4）にコピーします。


## パラメータおよび要件

- `exespace`, `first_from`, `last_from`, `first_to`, `view_from`, `view_to`, `new_value`:
  -  [`replace_copy`](./StdReplaceCopy)　と同様。
- `label`:
  - 1　について、デフォルト文字列は、: "Kokkos::replace_copy_if_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::replace_copy_if_view_api_default"
- `pred`:
  - *一項* 述語：置換対象の必須要素に対して「真」を返す述語; ``pred(v)``　は、引数として渡された実行空間から呼び出されるためには、有効でなければならず、そ 型　value_type　すべての引数　``v``　（constの可能性）について、bool型に変換可能で、そこでは、``value_type``　が、　 `InputIteratorType`  (1,2,について) の値型、または `view_from` (3,4について)　の値型であり、  ``v``　を変更してはいけません。
  -  [`replace_if`](./StdReplaceIf)　について示されたのと同じAPIを持つ必要があります。


## 返し

コピーされた最後の要素の *後* の要素へのイテレータ。
