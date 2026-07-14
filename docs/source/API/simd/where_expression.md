# `Experimental::where_expression`

（Kokkos 5.0 以降非推奨）

ヘッダーファイル: `Kokkos_SIMD.hpp`

使用方法

`Kokkos::Experimental::where_expression` は、ベクトルレジスタ内の値のサブセットを参照します。どの値がサブセット内に含まれるかは、マスクによって記述されます。したがって、`where_expression` は、ベクトル値に対するマスク操作の基礎を形成します。

## インターフェイス

```c++
namespace Experimental {
template <class M, class T>
class const_where_expression;
template <class M, class T>
class where_expression : public const_where_expression;
}
```

### テンプレートパラメータ
第1のテンプレートパラメータ `M` はマスクの型を表し、クラス型テンプレート `Kokkos::Experimental::simd_mask` のインスタンス、または `bool` である必要があります。
第2のテンプレートパラメータ `T` は値の型であり、クラス型テンプレート `Kokkos::Experimental::simd` のインスタンス、または `double` などの基本型である必要があります。

### Where 関数
オブジェクトは、非メンバメソッド `Kokkos::Experimental::where` を呼び出すことによってのみ構築されます。:
 * `template <class T, class Abi> where_expression<simd_mask<T, Abi>, simd<T, Abi>>
    where(const simd_mask<T, Abi>&, simd<T, Abi>&)`: `simd_mask`引数によって選択された `simd` 引数の値を参照する、非定数の where 式を作成します。
 * `template <class T, class Abi> const_where_expression<simd_mask<T, Abi>, simd<T, Abi>>
    where(const simd_mask<T, Abi>&, const simd<T, Abi>&)`: `simd_mask` 引数によって選択された `simd` 引数の値を参照する `where` 式を定数として作成します。

### 負荷/格納メソッド
 * `template<class U, class Flags> void const_where_expression::copy_to(U* mem, Flags) const`: マスク付きストア操作を実行します。マスク値 `i` が真の場合に限り、ベクトル値 `i` を `mem[i]` に格納します。`Flags` は、アドレス `mem` におけるアライメントを記述するために使用される `simd_flags` 型のものです。
 * `template<class U, class Flags> void where_expression::copy_from(const U* mem, Flags)`: マスク付きロード操作を実行します。マスク値 `i` が真の場合に限り、ベクトル値 `i` を `mem[i]` から読み込みます。 `Flags` は、アドレス `mem` におけるアラインメントを記述するために使用される `simd_flags` 型の変数です。

#### Simd フラッグ
 * 利用可能な `simd_flags` は、 `simd_flag_default` および `simd_flag_aligned`。
 * 下位互換性のため、`Kokkos::Experimental::element_aligned_tag` および `Kokkos::Experimental::vector_aligned_tag` の型が利用可能です。
 * `Kokkos::Experimental::element_aligned_tag` は `decltype(simd_flag_default)` の型エイリアスであり、`Kokkos::Experimental::vector_aligned_tag` は `decltype(simd_flag_aligned)` の型エイリアスです。

### 収集/分散メソッド
 これらのメソッドは、 Kokkos によって追加されたものであり、ISO C++ のプロポーザルには含まれておりません。
 * `void const_where_expression::scatter_to(double* mem, simd<std::int32_t, Abi> const& index) const`: 値型 `T` が `Kokkos::Experimental::simd<double, Abi>` の場合、本関数はマスク値 `i` が真であるとき、値を `mem[index[i]]` に分散します。
 * `void where_expression::gather_from(const double* mem, simd<std::int32_t, Abi> const& index)`: 値型 `T` が `Kokkos::Experimental::simd<double, Abi>` の場合、本関数は、マスク値 `i` が真であるとき、`mem[index[i]]` から値を収集します。

### 代入
 * `template<class U> void where_expression::operator=(U&& x)`:  マスク値 `i` が真の場合にのみ、ベクトル値 `i` に `x[i]` の値を代入します。

## 例

```c++
#include <Kokkos_SIMD.hpp>
#include <cstdio>

int main(int argc, char* argv[]) {
  Kokkos::initialize(argc,argv);
  {
    using simd_type = Kokkos::Experimental::simd<double>;
    // この後、ベクトル a の最初の値は負になります
    simd_type a([] (std::size_t i) { return 1.0 * i - 1.0; });
    // where 式を使用して、負の値を 0.0 に設定することができます
    where(a < 0.0, a) = 0.0;
    // 現在では、関数の呼び出しにドメイン制限を設ける方が安全かもしれません
    auto b = Kokkos::sqrt(a);
  }
  Kokkos::finalize();
}
```
