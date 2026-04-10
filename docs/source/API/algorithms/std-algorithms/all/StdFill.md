
# `fill`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class IteratorType, class T>
void fill(const ExecutionSpace& exespace,                                    (1)
          IteratorType first, IteratorType last,
          const T& value);

template <class ExecutionSpace, class IteratorType, class T>
void fill(const std::string& label, const ExecutionSpace& exespace,          (2)
          IteratorType first, IteratorType last,
          const T& value);

template <class ExecutionSpace, class DataType, class... Properties, class T>
void fill(const ExecutionSpace& exespace,                                    (3)
          const Kokkos::View<DataType, Properties...>& view,
          const T& value);

template <class ExecutionSpace, class DataType, class... Properties, class T>
void fill(const std::string& label, const ExecutionSpace& exespace,          (4)
          const Kokkos::View<DataType, Properties...>& view,
          const T& value);

} //end namespace Experimental
} //end namespace Kokkos
```

## ディスクリプション

範囲 `[first, last)` (オーバーロード 1,2) 内、または
 `ビュー` (オーバーロード 3,4) 内に、各要素を代入します。


## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス
- `label`:
  - デバッグ目的で実装カーネルに名付けるために使用
  - 1 について、 デフォルト文字列は、: "Kokkos::fill_iterator_api_default"
  - 3 について、 デフォルト文字列は、: "Kokkos::fill_view_api_default"
- `first, last`:
  - 割当先の要素の範囲
  - 例えば、 `Kokkos::Experimental::begin/end` など、*ランダムアクセスイテレータ* でなければなりません。
  - 有効な範囲、つまり、``last_from >= first_from`` を表さなければなりません。 (デバッグモードで確認済み)
  - `exespace` からアクセス可能でなければなりません。
- `view`:
  - 必ずランク-1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。
  - `exespace` からアクセス可能でなければなりません。
- `value`:
  - 各要素に割り当てる値


## 戻り値

無し

## 例

```c++
namespace KE = Kokkos::Experimental;
Kokkos::View<double*> a("a", 13);

KE::fill(Kokkos::DefaultExecutionSpace(), KE::begin(a), KE::end(a), 4.);

// ビューを直接渡します
KE::fill(Kokkos::DefaultExecutionSpace(), a, 22.);

// 明示的に実行空間を設定します（アクティブと仮定）
KE::fill(Kokkos::OpenMP(), KE::begin(a), KE::end(a), 14.);
```
