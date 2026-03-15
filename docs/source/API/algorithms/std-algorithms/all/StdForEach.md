
# `for_each`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```cpp
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class InputIterator, class UnaryFunctorType>
void for_each(const ExecutionSpace& exespace,                            (1)
              InputIterator first, InputIterator last,
              UnaryFunctorType functor);

template <class ExecutionSpace, class InputIterator, class UnaryFunctorType>
void for_each(const std::string& label, const ExecutionSpace& exespace,  (2)
              InputIterator first, InputIterator last,
              UnaryFunctorType functor);

template <class ExecutionSpace, class DataType, class... Properties, class UnaryFunctorType>
void for_each(const ExecutionSpace& exespace,
              const Kokkos::View<DataType, Properties...>& view,                      (3)
              UnaryFunctorType functor);

template <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
void for_each(const std::string& label, const ExecutionSpace& exespace,
              const Kokkos::View<DataType, Properties...>& view,                      (4)
              UnaryFunctorType func);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

UnaryFunctorType `func` を、`[first,last)` の各イテレータの参照解除結果（(1,2) の場合）およびビュー要素（(3,4) の場合）に適用します。

## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス

- `label`:
  - 1　について、デフォルト文字列は、: "Kokkos::for_each_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::for_each_view_api_default"

- `first, last`:
  - 演算対象の要素の範囲
  - *ランダムアクセスイテレータ*　でなければなりません。
  - 有効な範囲、つまり `last >= first` を表さなければなりません　(この条件は、デバッグモード内で確認されます)
  - `exespace` からアクセス可能でなければなりません。

- `view`:
  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。

- `func`:
  - すべての要素上で呼び出される関数オブジェクト;
  - 関数のシグネチャは `func(v)` である必要があります。
  - 渡された実行空間から呼び出されるためには有効である必要があり、型 `value_type`（定数である可能性があります）の引数 `v` をすべて受け入れる必要がありますが、 ここでは、 `value_type` は、`InputIterator`　の値型であり、  `v`を変更してはいけません。
    
  - 以下に一致しなければなりません:
  ```cpp
  struct func
  {
     KOKKOS_INLINE_FUNCTION
     void operator()(const /*type needed */ & operand) const { /* ... */; }

     // または、また有効

     KOKKOS_INLINE_FUNCTION
     void operator()(/*type needed */ operand) const { /* ... */; }
  };
  ```

## 戻り値

(無し)


## 例
```cpp
namespace KE = Kokkos::Experimental;

template<class ValueType>
struct IncrementValsFunctor
{
  const ValueType m_value;
  IncrementValsFunctor(ValueType value) : m_value(value){}

  KOKKOS_INLINE_FUNCTION
  void operator()(const ValueType & operand) const {
    operand += m_value;
  }
};

auto exespace = Kokkos::DefaultExecutionSpace;
using view_type = Kokkos::View<exespace, int*>;
view_type a("a", 15);
// 何らかの方法で "a" を満たす

// ファンクタを作成
IncrementValsFunctor<int> p(5);

//  "a" における各要素を　5 増す。
KE::for_each(exespace, KE::begin(a), KE::end(a), p);

// OpenMPが有効になっていると仮定すれば、明示的に以下のように呼び出すことも可能です
KE::for_each(Kokkos::OpenMP(), KE::begin(a), KE::end(a), p);
```
