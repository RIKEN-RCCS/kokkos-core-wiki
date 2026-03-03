
# `replace`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <class ExecutionSpace, class IteratorType, class T>
void replace(const ExecutionSpace& exespace,                                 (1)
             IteratorType first, IteratorType last,
             const T& old_value, const T& new_value);

テンプレート <class ExecutionSpace, class IteratorType, class T>
void replace(const std::string& label, const ExecutionSpace& exespace,       (2)
             IteratorType first, IteratorType last,
             const T& old_value, const T& new_value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
void replace(const ExecutionSpace& exespace,                                 (3)
             const Kokkos::View<DataType, Properties...>& view,
             const T& old_value, const T& new_value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
void replace(const std::string& label, const ExecutionSpace& exespace,       (4)
             const Kokkos::View<DataType, Properties...>& view,
             const T& old_value, const T& new_value);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

範囲 `[first, last)`（オーバーロード1,2）または `view`（オーバーロード3,4）内で、`old_value` と等しい全ての要素を `new_value` で置換します。等価性は `operator==` を使用して、確認されます。

## Parameters and Requirements

- `exespace`:
  - 実行空間インスタンス
- `label`:
  - デバッグ目的で実装カーネルを名付けるために使用
  - 1　について、デフォルト文字列は、: "Kokkos::replace_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::replace_view_api_default"
- `first, last`:
  - 検索対象の要素の範囲
  - 例えば、 ``Kokkos::Experimental::begin/end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。
  - 有効範囲、つまり、 ``last >= first``　を表す必要があります。（この条件はデバッグモードで確認されます）。
  - `exespace`　からアクセス可能でなければなりません。
- `view`:
  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。
- `old_value`, `new_value`:
  - 説明を要しません。


## 返し

無し


## 例

```c++
namespace KE = Kokkos::Experimental;
Kokkos::View<double*> a("a", 13);
//  a　を使用して何かを実行
// ...

const double oldValue{2};
const double newValue{34};
KE::replace(Kokkos::DefaultExecutionSpace(), KE::begin(a), KE::end(a), oldValue, newValue);

//　明示的にラベルと実行空間を設定します（アクティブであると仮定）
KE::replace("mylabel", Kokkos::OpenMP(), a, oldValue, newValue);
```
