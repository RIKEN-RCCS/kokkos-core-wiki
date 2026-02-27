
# `fill`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <class ExecutionSpace, class IteratorType, class T>
void fill(const ExecutionSpace& exespace,                                    (1)
          IteratorType first, IteratorType last,
          const T& value);

テンプレート <class ExecutionSpace, class IteratorType, class T>
void fill(const std::string& label, const ExecutionSpace& exespace,          (2)
          IteratorType first, IteratorType last,
          const T& value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
void fill(const ExecutionSpace& exespace,                                    (3)
          const Kokkos::View<DataType, Properties...>& view,
          const T& value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
void fill(const std::string& label, const ExecutionSpace& exespace,          (4)
          const Kokkos::View<DataType, Properties...>& view,
          const T& value);

} //end namespace Experimental
} //end namespace Kokkos
```

## ディスクリプション

範囲 `[first, last)` (オーバーロード 1,2)　内、または
 `ビュー` (オーバーロード 3,4)　内に、各要素を代入します。


## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス
- `ラベル`:
  - デバッグ目的で実装カーネルに名付けるために使用
  - for 1, the default string is: "Kokkos::fill_iterator_api_default"
  - for 3, the default string is: "Kokkos::fill_view_api_default"
- `first, last`:
  - range of elements to assign to
  - must be *random access iterators*, e.g., `Kokkos::Experimental::begin/end`
  - must represent a valid range, i.e., `last >= first` (checked in debug mode)
  - must be accessible from `exespace`
- `view`:
  - must be rank-1, and have `LayoutLeft`, `LayoutRight`, or `LayoutStride`
  - must be accessible from `exespace`
- `value`:
  - value to assign to each element


## Return

None

## Example

```c++
namespace KE = Kokkos::Experimental;
Kokkos::View<double*> a("a", 13);

KE::fill(Kokkos::DefaultExecutionSpace(), KE::begin(a), KE::end(a), 4.);

// passing the view directly
KE::fill(Kokkos::DefaultExecutionSpace(), a, 22.);

// explicitly set execution space (assuming active)
KE::fill(Kokkos::OpenMP(), KE::begin(a), KE::end(a), 14.);
```
