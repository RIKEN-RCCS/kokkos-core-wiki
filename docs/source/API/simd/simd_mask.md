# `Experimental::simd_mask`

ヘッダーファイル: `Kokkos_SIMD.hpp`

使用例: 

 `Kokkos::Experimental::simd_mask` は、プラットフォーム固有のベクトルマスクを抽象化したものであり、プラットフォーム固有のベクトル固有関数を呼び出します。
これは、 [this document](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/n4808.pdf) における ISO C++ 向けに提案された `simd_mask` 型に基づいています。

## インターフェイス

```c++
namespace Experimental {
template <class T, class Abi>
class basic_simd_mask;
}
```

### テンプレートパラメータ

最初のテンプレート引数 `T` は、現在のプラットフォームがベクトルインストリプリズンをサポートする C++ の基本型である必要があります。 Kokkos は、 `T` について、以下の型をサポートしています:
 - `float`
 - `double`
 - `std::int32_t`
 - `std::int64_t`
 - `std::uint32_t`
 - `std::uint64_t`

2つ目のテンプレートパラメータ `Abi` は、名前空間 Kokkos::Experimental::simd_abi 内で事前定義された ABI 型のいずれかです。本型はベクトルのサイズと、どのアーキテクチャ固有のインストリプリズンが使用されるかを決定します。 以下の型は、その名前空間において常に利用可能です：
 - `scalar`: フォールバックABIは、常にベクトルサイズが1であり、特別なインストリプリズンを使用しません。
 - `native`: Kokkos がコンパイルされたアーキテクチャ向けの "最適な" ABIです。 ( Kokkos 4.6以降非推奨)

### 型定義

 *  `value_type`: Equal to `bool` に等しいです。
 *  `reference`:  本型は `value_type` に変換可能である必要があり、`value_type` は `reference` に代入可能である必要があります。これは単純な参照である場合もあれば、1つのベクトルのレーンを抽出または埋めるためにベクトルインストリプリズンを呼び出す実装定義の型である場合もあります。 ( Kokkos 4.6以降削除)
 *  `simd_type`:  `simd<T, Abi>` に等しいです。
 *  `abi_type`: `Abi` に等しいです。

### 幅

 * `static constexpr std::size_t size()`: `simd_mask<T, Abi>::size()` は、ベクトルの幅、すなわちベクトル内の型 `T` の値の数を表すコンパイル時定数です。

### コンストラクタ

  * `simd_mask()`: デフォルトコンストラクタ。 本コンストラクタではベクトル値は初期化されません。
  * `simd_mask(bool)`: 単一値コンストラクタです。引数は、`value_type` 型に変換され、マスク内の全ての値が、引数の値に設定されます。
 * `template <class G> simd_mask(G&& gen)`: ジェネレータコンストラクタ。ジェネレータ `gen` は、`std::integral_constant<std::size_t, i>()` を引数として受け取り、`bool` に変換可能な値を返すことができる呼び出し可能型（例：ファンクタ）である必要があります。 ベクトルマスク値 `i` は、`gen(std::integral_constant<std::size_t, i>())` の値に初期化されます。

### 値アクセスメソッド
  * `bool operator[](std::size_t) const`: マスク値 `i` を返します。
  * `reference operator[](std::size_t)`: 変更可能なマスク値 `i` に参照を返します。 ( Kokkos 4.6において削除)

### ブール値演算
  * `simd_mask simd_mask::operator!() const`
  * `simd_mask operator&&(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator||(const simd_mask& lhs, const simd_mask& rhs)`

### ビット単位演算
  * `simd_mask simd_mask::operator~() const`
  * `simd_mask operator&(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator|(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator^(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator&=(simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator|=(simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator^=(simd_mask& lhs, const simd_mask& rhs)`

### 比較演算子
  * `simd_mask operator==(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator!=(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator>=(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator<=(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator>(const simd_mask& lhs, const simd_mask& rhs)`
  * `simd_mask operator<(const simd_mask& lhs, const simd_mask& rhs)`

### 還元
  * `bool all_of(const simd_mask&)`: マスク内のベクトル値すべてが真である場合にのみ、真を返します
  * `bool any_of(const simd_mask&)`: マスク内のベクトル値のいずれかが真である場合にのみ、真を返します
  * `bool none_of(const simd_mask&)`: マスク内のベクトル値のいずれも真ではない場合にのみ、真を返します

### グローバル型定義
  * `template <class T> Kokkos::Experimental::native_simd_mask`: Alias for `Kokkos::Experimental::simd_mask<T, Kokkos::Experimental::simd_abi::native<T>>`. (Kokkos 4.6以降非推奨)
  * `template <class T, int N> Kokkos::Experimental::simd_mask`: Alias for `Kokkos::Experimental::basic_simd_mask<T, ...>`. (Kokkos 4.6以降)

## 例

```c++
#include <Kokkos_SIMD.hpp>
#include <cstdio>

int main(int argc, char* argv[]) {
  Kokkos::initialize(argc,argv);
  {
    using mask_type = Kokkos::Experimental::simd_mask<double>;
    mask_type a([] (std::size_t i) { return i == 0; });
    mask_type b([] (std::size_t i) { return i == 1; });
    mask_type c([] (std::size_t i) { return i == 0 || i == 1; });
    if (all_of(c == (a || b))) {
      printf("Kokkos simd_mask works as expected!");
    }
  }
  Kokkos::finalize();
}
```
