# カスタムスカラータイプを備えた内蔵リデューサー

組み込みの還元を持つカスタムスカラータイプを使用するには、以下の要件を満たす必要があります。

   * 初期化関数は、Kokkos::reduction_identity<T>　クラスの特殊化を通じて、提供されなければなりません。 
   * 適用還元クラスに必要な演算子を、実装する必要があります。
   * クラス/構造体は、デフォルトのコピーコンストラクタを使用するか、特定のコピーコンストラクタを実装している必要があります。 

## 例

 本例では、組み込みの [`Sum`](../API/core/builtinreducers/Sum) リデューサーを使って配列に対してカスタム還元を行います。

```c++
namespace sample {  // 名前空間は、還元識別子における名前解決に役立ちます 
   template< class ScalarType, int N >
   struct array_type {
     ScalarType the_array[N];
  
     KOKKOS_INLINE_FUNCTION   // デフォルトコンストラクタ -  0's　に初期化します
     array_type() { 
       for (int i = 0; i < N; i++ ) { the_array[i] = 0; }
     }
     KOKKOS_INLINE_FUNCTION   // コピーコンストラクタ
     array_type(const array_type & rhs) { 
        for (int i = 0; i < N; i++ ){
           the_array[i] = rhs.the_array[i];
        }
     }
     KOKKOS_INLINE_FUNCTION   // 演算子を追加します
     array_type& operator += (const array_type& src) {
       for ( int i = 0; i < N; i++ ) {
          the_array[i]+=src.the_array[i];
       }
       return *this;
     }
   };
   typedef array_type<int,4> ValueType;  // 以下のコードの簡易化に使用されます
}
namespace　Kokkos { //reduction identity 還元識別は、Kokkos namespace　に定義されなければなりません
   template<>
   struct reduction_identity< sample::ValueType > {
      KOKKOS_FORCEINLINE_FUNCTION static sample::ValueType sum() {
         return sample::ValueType();
      }
   };
}
int main( int argc, char* argv[] )
{
  int E = 1024;
  Kokkos::initialize( argc, argv );
  {
     sample::ValueType tr;         
     Kokkos::parallel_reduce( E, KOKKOS_LAMBDA (const int& i, 
                                                sample::ValueType & upd) {
        int ndx =i%4;  // i%4 入力のすべてを総計します (総計を　4　で割ります)
        upd.the_array[ndx] += 1; 
     }, Kokkos::Sum<sample::ValueType>(tr) );
     printf( "  Computed result for %d is %d, %d, %d, %d \n", 
             E, tr.the_array[0], tr.the_array[1], 
                tr.the_array[2], tr.the_array[3] );
  }
  Kokkos::finalize();

  return 0;
}
```
