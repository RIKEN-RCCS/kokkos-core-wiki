
# `for_each_n`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```cpp
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <class ExecutionSpace, class InputIterator, class SizeType, class UnaryFunctorType>
UnaryFunctorType for_each_n(const ExecutionSpace& exespace,
                      InputIterator first, SizeType n,
                      UnaryFunctorType functor);                                     (1)

テンプレート <class ExecutionSpace, class InputIterator, class SizeType, class UnaryFunctorType>
UnaryFunctorType for_each_n(const std::string& label, const ExecutionSpace& exespace,
                      InputIterator first, SizeType n
                      UnaryFunctorType functor);                                     (2)

テンプレート <class ExecutionSpace, class DataType, class... Properties, class SizeType, class UnaryFunctorType>
UnaryFunctorType for_each_n(const ExecutionSpace& exespace,
             const Kokkos::View<DataType, Properties...>& view, SizeType n,
             UnaryFunctorType functor);                                              (3)

テンプレート <class ExecutionSpace, class DataType, class... Properties, class SizeType, class UnaryFunctorType>
UnaryFunctorType for_each_n(const std::string& label, const ExecutionSpace& exespace,
             const Kokkos::View<DataType, Properties...>& view, SizeType n,
             UnaryFunctorType func);                                                 (4)

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

(1,2) について、各イテレータの参照解除結果に適用し、 (3,4) 内では、ファンクタを、ビューの最初の `n` 個の要素に適用します。

- (1,2): イテレータを受け入れるオーバーロードセット
- (3,4): ビューを受け入れるオーバーロードセット

## パラメータおよび要件

- `exespace`, `first`, `view`, `func` :  [`for_each`](./StdForEach)　において同様。

- `label`:
  - 1　について、デフォルト文字列は、: "Kokkos::for_each_n_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::for_each_n_view_api_default"

- `n`:
  - 演算対象となる要素数

## 戻り値

`func`
