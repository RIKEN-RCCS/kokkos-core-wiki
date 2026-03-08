# `Experimental::simd`

ヘッダーファイル: `Kokkos_SIMD.hpp`

使用例: 

`Kokkos::Experimental::simd` は、プラットフォーム固有のベクトルデータ型を抽象化であり、プラットフォーム固有のベクトルイントリンシックを呼び出します。
それは、[this document](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/n4808.pdf)　で　ISO C++　向けに提案されている　`simd`　型に基づいています。

## インターフェイス

```c++
名前空間 実験的 {
テンプレート <class T, class Abi>
クラス basic_simd;
}
```

### テンプレートパラメータ

最初のテンプレートパラメータ `T` は、現在のプラットフォームがベクトル組み込み関数をサポートする C++ の基本型である必要があります。Kokkos は `T` に対して以下の型をサポートしています：
 - `float`
 - `double`
 - `std::int32_t`
 - `std::int64_t`
 - `std::uint32_t`
 - `std::uint64_t`

2つ目のテンプレートパラメータ `Abi` は、名前空間 `Kokkos::Experimental::simd_abi` 内で事前定義された ABI 型のいずれかです。本型はベクトルのサイズと、どのアーキテクチャ固有の組み込み関数が使用されるかを決定します。以下の型は、その名前空間において常に利用可能です：
 - `scalar`: フォールバックABIは、常にベクトルサイズが1であり、特別な組み込み関数を使用しません。
 - `native`: Kokkosがコンパイルされたアーキテクチャ向けの "最適な" ABIです。 ( Kokkos 4.6以降非推奨)

### 型定義

 *  `value_type`:  `T`　に等しいです。
 *  `reference`: この型は `value_type` に変換可能である必要があり、`value_type` は `reference` に代入可能である必要があります。これは単純な参照である場合もあれば、1つのベクトルのレーンを抽出または埋めるためにベクトル固有関数を呼び出す実装定義の型である場合もあります。 ( Kokkos 4.6以降削除)
 *  `mask_type`:  `simd_mask<T, Abi>`　に等しいです。
 *  `abi_type`:  `Abi`　に等しいです。

### 幅

 * `static constexpr std::size_t size()`: `simd<T, Abi>::size()` は、ベクトルの幅、すなわちベクトル内の型 `T` の値の数を表すコンパイル時定数です。

### コンストラクタ

  * `simd()`: デフォルトコンストラクタ。 本コンストラクタではベクトル値は初期化されません。
  * `テンプレート <class U> simd(U&&)`: 単一値コンストラクタです。引数は、`value_type`　型に変換され、ベクトル内の全ての値がその値に設定されます。
  * `テンプレート <class G> simd(G&& gen)`: ジェネレータコンストラクタ。ジェネレータ `gen` は、`std::integral_constant<std::size_t, i>()` を引数として受け取り、`value_type` に変換可能な値を返すことができる呼び出し可能型（例：ファンクタ）である必要があります。 ベクトルレーン `i` は、`gen(std::integral_constant<std::size_t, i>())` の値で初期化されます。

### 負荷/格納メソッド

  * `テンプレート <class U, class Flags> void copy_from(const U* mem, Flags flags)`: アドレス `mem` から始まる連続した値のベクトル全体を読み込みます。 `Flags` は、アドレス `mem` におけるアラインメントを記述するために使用される `simd_flags` です。
  * `テンプレート <class U, class Flags> void copy_to(U* mem, Flags flags)`: アドレス `mem` から始まる連続した値の完全なベクトルを格納します。 `Flags` は、アドレス `mem` におけるアラインメントを記述するために使用される `simd_flags` です。

#### Simdフラッグ

  * 利用可能な `simd_flags` は、`simd_flag_default` および `simd_flag_aligned`　です。
  * 下位互換性のため、`Kokkos::Experimental::element_aligned_tag` および `Kokkos::Experimental::vector_aligned_tag` の型が利用可能です。
  * ‘Kokkos：：Experimental：`Kokkos::Experimental::element_aligned_tag` は、 `decltype(simd_flag_default)` の型エイリアスであり、`Kokkos::Experimental::vector_aligned_tag` は、 `decltype(simd_flag_aligned)` の型エイリアスです。

### 値へのアクセス方法
  * `value_type operator[](std::size_t) const`: ベクトル値 `i`　を返します。
  * `reference operator[](std::size_t)`: 変更可能なベクトル値 `i` への参照を返します。 ( Kokkos 4.6以降で削除)

### 算術演算子
  * `simd simd::operator-() const`
  * `simd operator+(const simd& lhs, const simd& rhs)`
  * `simd operator-(const simd& lhs, const simd& rhs)`
  * `simd operator*(const simd& lhs, const simd& rhs)`
  * `simd operator/(const simd& lhs, const simd& rhs)`
  * `simd simd::operator~() const`
  * `simd operator&(const simd& lhs, const simd& rhs)`
  * `simd operator|(const simd& lhs, const simd& rhs)`
  * `simd operator^(const simd& lhs, const simd& rhs)`
  * `simd operator>>(const simd& lhs, const simd& rhs)`
  * `simd operator>>(const simd& lhs, int rhs)`
  * `simd operator<<(const simd& lhs, const simd& rhs)`
  * `simd operator<<(const simd& lhs, int rhs)`

### Compound Assignment Operators
  * `simd operator+=(simd& lhs, const simd& rhs)`
  * `simd operator-=(simd& lhs, const simd& rhs)`
  * `simd operator*=(simd& lhs, const simd& rhs)`
  * `simd operator/=(simd& lhs, const simd& rhs)`
  * `simd operator&=(simd& lhs, const simd& rhs)`
  * `simd operator|=(simd& lhs, const simd& rhs)`
  * `simd operator^=(simd& lhs, const simd& rhs)`
  * `simd operator>>=(simd& lhs, const simd& rhs)`
  * `simd operator<<=(simd& lhs, const simd& rhs)`

### 複合代入演算子
  * `mask_type operator==(const simd& lhs, const simd& rhs)`
  * `mask_type operator!=(const simd& lhs, const simd& rhs)`
  * `mask_type operator>=(const simd& lhs, const simd& rhs)`
  * `mask_type operator<=(const simd& lhs, const simd& rhs)`
  * `mask_type operator>(const simd& lhs, const simd& rhs)`
  * `mask_type operator<(const simd& lhs, const simd& rhs)`

### 丸め関数
  * `simd Kokkos::floor(const simd& lhs)`
  * `simd Kokkos::ceil(const simd& lhs)`
  * `simd Kokkos::round(const simd& lhs)`
  * `simd Kokkos::trunc(const simd& lhs)`

### 最小/最大関数
  * `simd Kokkos::min(const simd& lhs, const simd& rhs)`
  * `simd Kokkos::max(const simd& lhs, const simd& rhs)`

### Reductions 
  * `T Kokkos::Experimental::reduce(const simd& lhs, const simd_mask& mask)`
  * `T Kokkos::Experimental::reduce(const simd& lhs, Op binary_op)`
  * `T Kokkos::Experimental::reduce_min(const simd& lhs, const simd_mask& mask)`
  * `T Kokkos::Experimental::reduce_min(const simd& lhs)`
  * `T Kokkos::Experimental::reduce_max(const simd& lhs, const simd_mask& mask)`
  * `T Kokkos::Experimental::reduce_max(const simd& lhs)`

### `<cmath>` 関数
  * `simd Kokkos::abs(const simd& lhs)`
  * `simd Kokkos::exp(const simd& lhs)`
  * `simd Kokkos::exp2(const simd& lhs)`
  * `simd Kokkos::log(const simd& lhs)`
  * `simd Kokkos::log10(const simd& lhs)`
  * `simd Kokkos::sqrt(const simd& lhs)`
  * `simd Kokkos::cbrt(const simd& lhs)`
  * `simd Kokkos::sin(const simd& lhs)`
  * `simd Kokkos::cos(const simd& lhs)`
  * `simd Kokkos::tan(const simd& lhs)`
  * `simd Kokkos::asin(const simd& lhs)`
  * `simd Kokkos::acos(const simd& lhs)`
  * `simd Kokkos::atan(const simd& lhs)`
  * `simd Kokkos::sinh(const simd& lhs)`
  * `simd Kokkos::cosh(const simd& lhs)`
  * `simd Kokkos::tanh(const simd& lhs)`
  * `simd Kokkos::asinh(const simd& lhs)`
  * `simd Kokkos::acosh(const simd& lhs)`
  * `simd Kokkos::atanh(const simd& lhs)`
  * `simd Kokkos::erf(const simd& lhs)`
  * `simd Kokkos::erfc(const simd& lhs)`
  * `simd Kokkos::tgamma(const simd& lhs)`
  * `simd Kokkos::lgamma(const simd& lhs)`
  * `simd Kokkos::pow(const simd& lhs, const simd& rhs)`
  * `simd Kokkos::hypot(const simd& x, const simd& y)`
  * `simd Kokkos::hypot(const simd& x, const simd& y, const simd& z)`
  * `simd Kokkos::atan2(const simd& x, const simd& y)`
  * `simd Kokkos::copysign(const simd& mag, const simd& sgn)`
  * `simd Kokkos::fma(const simd& x, const simd& y, const simd& z)`

  以下の関数は、 `value_type=float` および `value_type=double`　について `AVX2` and `AVX512` においてのみ定義されます。
  * `simd Kokkos::cbrt(simd& lhs)`
  * `simd Kokkos::exp(simd& lhs)`
  * `simd Kokkos::log(simd& lhs)`


### グローバル型定義
  * `template <class T> Kokkos::Experimental::native_simd`:  `Kokkos::Experimental::simd<T、 Kokkos::Experimental::simd_abi::native<T>>`　の別名 ( Kokkos 4.6以降非推奨)
  * `テンプレート <class T, int N> Kokkos::Experimental::simd`: `Kokkos::Experimental::basic_simd<T, ...>`　の別名 ( Kokkos 4.6以降)
  * `Kokkos::Experimental::element_aligned_tag`:  `Kokkos::Experimental::simd_flags<>`　の別名
  * `Kokkos::Experimental::vector_aligned_tag`: `Kokkos::Experimental::simd_flags<simd_alignment_vector_aligned>`　の別名

## 例

```c++
#include <Kokkos_SIMD.hpp>
#include <cstdio>

int main(int argc, char* argv[]) {
  Kokkos::initialize(argc,argv);
  {
    simd_type = Kokkos::Experimental::simd<double>　を使用;
    simd_type a([] (std::size_t i) { return 0.1 * i; });
    simd_type b(2.0);
    simd_type c = Kokkos::sqrt(a * a + b * b);
    for (std::size_t i = 0; i < simd_type::size(); ++i) {
      printf("[%zu] = %g\n", i, c[i]);
    }
  }
  Kokkos::finalize();
}
```
