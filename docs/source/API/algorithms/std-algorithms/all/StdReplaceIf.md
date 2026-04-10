
# `replace_if`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class IteratorType, class UnaryPredicateType, class T>
void replace_if(const ExecutionSpace& exespace,                              (1)
                IteratorType first, IteratorType last,
                UnaryPredicateType pred, const T& new_value);

template <class ExecutionSpace, class IteratorType, class UnaryPredicateType, class T>
void replace_if(const std::string& label, const ExecutionSpace& exespace,    (2)
                IteratorType first, IteratorType last,
                UnaryPredicateType pred, const T& new_value);

template <class ExecutionSpace, class DataType, class... Properties, class UnaryPredicateType, class T>
void replace_if(const ExecutionSpace& exespace,                              (3)
                const Kokkos::View<DataType, Properties...>& view,
                UnaryPredicateType pred, const T& new_value);

template <class ExecutionSpace, class DataType, class... Properties, class UnaryPredicateType, class T>
void replace_if(const std::string& label, const ExecutionSpace& exespace,    (4)
                const Kokkos::View<DataType, Properties...>& view,
                UnaryPredicateType pred, const T& new_value);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

範囲 `[first, last)`（オーバーロード 1,2）または `view`（オーバーロード 3,4）において、`pred` が `true` となる全ての要素を `new_value` と置き換えます。

## パラメータおよび要件

- `exespace`, `first`, `last`, `view`, `new_value`:  [`replace`](./StdReplace) と同様。
- `label`:
  - 1 について、デフォルト文字列は、: "Kokkos::replace_if_iterator_api_default"
  - 3 について、デフォルト文字列は、: "Kokkos::replace_if_view_api_default"
- `pred`:
  - *一項* 述語：置換対象の必須要素に対して「真」を返す述語; ``pred(v)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならず、 型 value_type すべての引数 ``v`` （constの可能性）について、ブール型に変換可能で、そこでは、``value_type`` が、  `InputIteratorType`  (1,2,について) の値型、または  `view`  (3,4について) の値型であり、  ``v`` を変更してはいけません。
  - 以下に一致しなければなりません:
  ```c++
  struct Predicate
  {
     KOKKOS_INLINE_FUNCTION
     bool operator()(const value_type & v) const { return /* ... */; }

     // または、また有効

     KOKKOS_INLINE_FUNCTION
     bool operator()(value_type v) const { return /* ... */; }
  };
  ```


## 返し

無し

## 例

```c++
template <class ValueType>
struct IsPositiveFunctor {
  KOKKOS_INLINE_FUNCTION
  bool operator()(const ValueType val) const { return (val > 0); }
};
// ---

namespace KE = Kokkos::Experimental;
Kokkos::View<double*> a("a", 13);
// a を使って何かを実行
// ...

const double oldValue{2};
const double newValue{34};
KE::replace_if(Kokkos::DefaultExecutionSpace(), KE::begin(a), KE::end(a),
   IsPositiveFunctor<double>(), newValue);

// 明示的にラベルおよび実行空間を設定（アクティブであると仮定）
KE::replace_if("mylabel", Kokkos::OpenMP(), a,
   IsPositiveFunctor<double>(), newValue);
```
