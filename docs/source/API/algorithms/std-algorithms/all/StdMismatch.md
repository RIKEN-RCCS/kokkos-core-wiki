
# `mismatch`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```cpp
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class IteratorType1, class IteratorType2>
Kokkos::pair<IteratorType1, IteratorType2> mismatch(const ExecutionSpace& exespace,
                  IteratorType1 first1,
                  IteratorType1 last1,                                               (1)
                  IteratorType2 first2,
                  IteratorType2 last2);

template <class ExecutionSpace, class IteratorType1, class IteratorType2>
Kokkos::pair<IteratorType1, IteratorType2> mismatch(
                const std::string& label,
                const ExecutionSpace& exespace,
                IteratorType1 first1,
                IteratorType1 last1,                                                 (2)
                IteratorType2 first2,
                IteratorType2 last2)

template <class ExecutionSpace, class IteratorType1, class IteratorType2, class BinaryPredicate>
Kokkos::pair<IteratorType1, IteratorType2> mismatch(const ExecutionSpace& exespace,
                  IteratorType1 first1,
                  IteratorType1 last1,                                               (3)
                  IteratorType2 first2,
                  IteratorType2 last2, BinaryPredicate pred);

template <class ExecutionSpace, class IteratorType1, class IteratorType2, class BinaryPredicate>
Kokkos::pair<IteratorType1, IteratorType2> mismatch(const std::string& label,
                  const ExecutionSpace& exespace,
                  IteratorType1 first1,
                  IteratorType1 last1,                                               (4)
                  IteratorType2 first2,
                  IteratorType2 last2, BinaryPredicate pred);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2>
auto mismatch(const ExecutionSpace& exespace,
              const Kokkos::View<DataType1, Properties1...>& view1,                  (5)
              const Kokkos::View<DataType2, Properties2...>& view2);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2>
auto mismatch(const std::string& label, const ExecutionSpace& exespace,
              const Kokkos::View<DataType1, Properties1...>& view1,                  (6)
              const Kokkos::View<DataType2, Properties2...>& view2);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2, class BinaryPredicateType>
auto mismatch(const ExecutionSpace& exespace,
              const Kokkos::View<DataType1, Properties1...>& view1,                  (7)
              const Kokkos::View<DataType2, Properties2...>& view2,
              BinaryPredicateType&& predicate);

template <class ExecutionSpace, class DataType1, class... Properties1,
          class DataType2, class... Properties2, class BinaryPredicateType>
auto mismatch(const std::string& label, const ExecutionSpace& exespace,
              const Kokkos::View<DataType1, Properties1...>& view1,                  (8)
              const Kokkos::View<DataType2, Properties2...>& view2,
              BinaryPredicateType&& predicate);

} //エンド 名前空間 実験的
} //エンド 名前空間 Kokkos
```

## ディスクリプション

2つの範囲から最初の不一致ペアを返します:  (1,2,3,4)　については、1つは [first1, last1) により定義され、もう1つは [first2,last2) によって定義されます。
(5,6,7,8)において、2つのビュー `view1` および `view2` から、最初の不一致ペアを返します。
(1,2,5,6)において、 `operator==` を使って、要素を比較します。
(3,4,7,8) における要素を、 BinaryPredicate `pred`　を使用して比較します。

## パラメータおよび要件

- `exespace`:
  - 実行空間インスタンス

- `label`:
  - 1,3については、 デフォルト文字列は: "Kokkos::mismatch_iterator_api_default"
  - 5,7については、 デフォルト文字列は: "Kokkos::mismatch_view_api_default"

- `first1`, `last1`, `first2`, `last2`:
  - 比較対象の要素の範囲
  - *ランダムアクセスイテレータ*　でなければなりません
  - 有効な範囲、つまり、 `last1 >= first1` および `last2 >= first2` を表さなければなりません。
  -  `exespace`　からアクセス可能でなければなりません。

- `view1`, `view2`:
  - 比較対象のビュー
  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。
  - `exespace`　からアクセス可能でなければなりません。

- `pred`
  ```cpp
  template <class ValueType1, class ValueType2 = ValueType1>
  struct IsEqualFunctor {

  KOKKOS_INLINE_FUNCTION
  Kokkos::pair<ValueType1, ValueType2> operator()(const ValueType1& a, const ValueType2& b) const {
    return (a == b);
    }
  };
 ```

## 返し

- (1,2) - Kokkos::pair, ここでは、 `.first` および `.second` が `operator==` が偽に評価される　IteratorType1 および IteratorType2 インスタンスです。 
- (3,4) - Kokkos::pair, ここでは、 `.first` および `.second` が `pred` が偽に評価され IteratorType1 およに IteratorType2  インスタンスです。

## 例 

```cpp
namespace KE = Kokkos::Experimental;

template <class ValueType1, class ValueType2 = ValueType1>
struct MismatchFunctor {

  KOKKOS_INLINE_FUNCTION
  Kokkos::pair<ValueType1, ValueType2> operator()(const ValueType1& a, const ValueType2& b) const {
    if(a != b)
        return (Kokkos::pair<ValueType1, ValueType2> (a,b));
  }
};

auto exespace = Kokkos::DefaultExecutionSpace;
using view_type = Kokkos::View<exespace, int*>;
view_type a("a", 15);
view_type b("b", 15);
// 何らかの方法で a,b を満たす

// ファンクタ作成
MismatchFunctor<int, int> p();

Kokkos::pair<int,int> mismatch_index = KE::mismatch(exespace, KE::begin(a), KE::end(a), KE::begin(b), KE::end(b) p);

// OpenMP が有効であると仮定すると、以下を明示的に呼び出すことが可能です
Kokkos::pair<int,int> mismatch_index = KE::mismatch(Kokkos::OpenMP(), KE::begin(a), KE::end(a), KE::begin(b), KE::end(b), p);
```
