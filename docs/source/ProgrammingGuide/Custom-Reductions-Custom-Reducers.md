# カスタムリデューサー

カスタムの任意の縮約は、縮約クラスと "縮約" クラスを用いて実装されます。 "reduced" クラスは、 [Built-In Reducers with Custom Scalar Types](Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types) で使われるカスタムスカラータイプに非常に似ており、リダクションクラスは、[ReducerConcept](../API/core/builtinreducers/ReducerConcept) を実装しています。

 "reduced" クラスについては、以下の要件を満たす必要があります
     
   * 適用縮約クラスに必要な演算子を実装する必要があります
   * クラス/構造体はデフォルトのコピーコンストラクタを使用するか、特定のコピーコンストラクタを実装している必要があります。

縮約クラスについては、以下の要件を満たす必要があります
     
   * 型定義リデューサー、value_type および result_view_type は、定義される必要があります。詳細については、 [ReducerConcept](../API/core/builtinreducers/ReducerConcept) を参照してください。
   * リデューサーの概念手法は、実装される必要があります。
   * 露出 result_view_type は、オブジェクトが使用されるメモリ空間内で、定義されなければなりません 

注意事項: タグ付き縮約の場合でも、すなわちポリシー内でタグを指定する場合であっても、潜在的な `init`/`join`/`final` メンバ関数は `WorkTag` 引数を選択してははいけません。

## 例

本例では、カスタムクラスとリデューサーを使って、配列上でカスタム縮約を実行します。

```c++
#include <Kokkos_Core.hpp>

namespace sample {

template <class ScalarType, int N>
struct array_type {
  ScalarType myArray[N];

  KOKKOS_INLINE_FUNCTION
  array_type() { init(); }

  KOKKOS_INLINE_FUNCTION
  array_type(const array_type& rhs) {
    for (int i = 0; i < N; i++) {
      myArray[i] = rhs.myArray[i];
    }
  }

  KOKKOS_INLINE_FUNCTION  // myArray を 0 に初期化します
      void
      init() {
    for (int i = 0; i < N; i++) {
      myArray[i] = 0;
    }
  }

  KOKKOS_INLINE_FUNCTION
  array_type& operator+=(const array_type& src) {
    for (int i = 0; i < N; i++) {
      myArray[i] += src.myArray[i];
    }
     return *this;
  }
};

template <class T, class Space, int N>
struct SumMyArray {
 public:
  // 必要とされます
  typedef SumMyArray reducer;
  typedef array_type<T, N> value_type;
  typedef Kokkos::View<value_type*, Space, Kokkos::MemoryUnmanaged>
      result_view_type;

 private:
  value_type& value;

 public:
  KOKKOS_INLINE_FUNCTION
  SumMyArray(value_type& value_) : value(value_) {}

  // 必要とされます
  KOKKOS_INLINE_FUNCTION
  void join(value_type& dest, const value_type& src) const {
    dest += src;
  }

  KOKKOS_INLINE_FUNCTION
  void init(value_type& val) const { val.init(); }

  KOKKOS_INLINE_FUNCTION
  value_type& reference() const { return value; }

  KOKKOS_INLINE_FUNCTION
  result_view_type view() const { return result_view_type(&value, 1); }

  KOKKOS_INLINE_FUNCTION
  bool references_scalar() const { return true; }
};
}  // 名前空間サンプル

int main(int argc, char* argv[]) {
  Kokkos::initialize(argc, argv);
  {
    int E = 1024;

    typedef sample::array_type<int, 4> ValueType;
    typedef sample::SumMyArray<int, Kokkos::HostSpace, 4> ArraySumResult;

    ValueType tr;

    Kokkos::parallel_reduce(
        E,
        KOKKOS_LAMBDA(const int i, ValueType& upd) {
          int ndx = i % 4;  // sum all of the i%4 entries (divide total by 4)
          upd.myArray[ndx] += 1;
        },
        ArraySumResult(tr));

    // 出力結果。
    printf("  Computed result %d, %d, %d, %d \n", tr.myArray[0], tr.myArray[1],
           tr.myArray[2], tr.myArray[3]);
  }
  Kokkos::finalize();
}
```
 
