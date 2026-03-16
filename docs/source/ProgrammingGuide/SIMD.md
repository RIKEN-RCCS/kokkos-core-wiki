# SIMD 型

## 背景

CPU　を使った高性能計算の歴史の中で、コンパイラの自動ベクトル化を通じて、CPU　ベクトルレジスタや命令を効果的に活用するソフトウェアを得ることは苦労してきました。 この葛藤について興味深い考察はこのブログで見ることができ、Intel　コンパイラの自動ベクトル化がNVIDIA GPUs　用の　CUDA　のようなモデルと比べてどのように欠点があるかを示しています。 スタンフォード大学のティム・フォーリーに帰せられる重要な引用には「自動ベクトル化はプログラミングモデルではない」と記されています。 これが本質的な問題の核心です。自動ベクトル化はプログラマーと機械の間の双方向の対話ではありません。むしろ、ほとんど常に機能しないブラックボックスのようなものです。 SimD　型を推進した主要な推進力の一人である　Matthias Kretzの論文　[dissertation](https://www.researchgate.net/profile/Matthias_Kretz2/publication/295253746_Extending_C_for_Explicit_Data-Parallel_Programming_via_SIMD_Vector_Types/links/56c8c99208ae5488f0d6ffa0.pdf)でも、C++　言語の　ISO 標準 に提案された動機が説明されています。 Kokkos はベクター対応　CPU で　高性能を追求するプログラミングモデルであり、  代替手法の制約を考慮するとこれらの　SIMD タイプを提供するのは理にかなっています。

## 基本理念

SIMD 型の考え方は、Intel　の内在呼び出しを手作業でコーディングする抽象化の層を一段階進めることです。 SIMD 型の設計は、多くのCPUベンダーが提供するベクトルの本質がかなり似ていること、そしてユーザーが一度に特定のベンダー向けに手作業でコーディングしたくないことを認識しています。 

したがって、SIMD 型は  ベクトルレジスタの　C++　表現であり、そのメソッドはベンダー固有のベクトル内在命令を明示的に呼び出します。 
ベンダー固有の部分はテンプレートパラメータを通じてユーザーコードから抽象化されます。

SIMD 型が高性能なコードを生成するのに非常に効果的な理由は、ユーザーが望むベクトル並列性を直接表現し、期待するベクトル命令を確実に生成できる形で行えるからです。
SIMD　型を使用する場合、コンパイラは自動ベクトル化を失敗することはありません。なぜなら自動ベクトル化は状況の一部ではないためです。 
ユーザーは、オートベクトリザではほとんどできない方法で、コード内の並列性をより明確に推論できるようになります。 
ユーザーが、ベンダーロックインや異なるベンダー命令セットの奇妙な特性から守りつつ、ベクトル化の実行方法を直接制御できることで、SIMD　型は CPU および　GPU　間で、パフォーマンス用ポータブルコードを書くことを可能にします。

## 例

CPU　ベクトル化を利用したい次のループがあると仮定します:

```c++
double* x;
double* y;
double* z;
double* r;
int n;
for (int i = 0; i < n; ++i) {
  r[i] = sqrt(x[i] * x[i] + y[i] * y[i] + z[i] * z[i]);
}
```

このようなループを　Kokkos　のSIMD　型タイプに変換する方法を、以下に示します:

```c++
#include <Kokkos_SIMD.hpp>

using simd_type = Kokkos::Experimental::simd<double>;
constexpr int width = int(simd_type::size());
assert(n % width == 0);
for (int i = 0; i < n; i += width) {
  simd_type sx(x + i, Kokkos::Experimental::simd_flag_default);
  simd_type sy(y + i, Kokkos::Experimental::simd_flag_default);
  simd_type sz(z + i, Kokkos::Experimental::simd_flag_default);
  simd_type sr = Kokkos::sqrt(sx * sx + sy * sy + sz * sz);
  sr.copy_to(r + i, Kokkos::Experimental::simd_flag_default);
}
```

`Kokkos::Experimental::simd<double>は、64ビット浮動小数点型の値を含むベクトルレジスタの基本的なSIMD　型です。 ポインタ(およびアラインメントタグ)　を与えられたものを構成すると、ベクトル化されたロード命令が実行され、copy_to　はベクトル化されたストア命令を生成します。 多くの場合、これらの命令がCPUからメモリ帯域幅をフルに引き出す唯一の方法です。 SIMD　型は  基本的な数学演算子を提供しているため、3回の掛け算と2回の加算は乗算と加算のためのベクトル命令に変換されることが保証されます。  Kokkos::sqrtのオーバーロードは、CPU　が対応すれば値の平方根を計算するためのベクトル命令を呼び出します。

換言すれば、ベンダー固有のものは含まれていませんが、Kokkos　がどの　CPU　型　(　KOKKOS_ARCH　構成)にコンパイルされているかに応じて、正確なベンダーベクター命令を確実に出す　C++　コードが手に入っています。 
また、特に数学演算を扱う部分はかなり読みやすいです。

CPU　が、256ビットベクトルレジスタをサポートしている場合、このコードは4つのダブル(幅=4)を同時に処理し、状況に応じて約　4X　の高速化を実現します。

## 剰余の対処

上記の例では、扱うデータ　`n`　のサイズがベクトル幅で均等に割られると主張することで、厄介な落とし穴を一掃ました。 
この問題に対処するには少なくとも三つの主要なアプローチがあります:

1. データサイズは常にベクトル幅の倍数であることを強制します。その一つの方法がパディングで、必要以上に割り当てて倍数になるまで割り当て、余分な値は無視することです。
   もう一つの方法は、同じサイズの型を保存する方法で、同じ　SIMD　型を使うことで可能です:


   ```c++
   #include <Kokkos_SIMD.hpp>
   
   simd_type = Kokkos::Experimental::simd<double>　を使用;
   simd_type* x;
   simd_type* y;
   simd_type* z;
   simd_type* r;
   int n;
   for (int i = 0; i < n; ++i) {
     r[i] = sqrt(x[i] * x[i] + y[i] * y[i] + z[i] * z[i]);
   }
   ```
   
   Kokkos　は、このユースケースをさらにサポートし、　Kokkos::View　との相互運用性を可能にするために特別なストレージタイプを追加しようと取り組んでいます。

   本アプローチは例の中では見た目がきれいですが、元のデータ型が変更され、大規模なコードベースの他の箇所でも変更が必要になる可能性があるため、広範な影響を及ぼす可能性があります。

3. 剰余については、例えば、非ベクトル化コードのループを使って残りの値を計算する等、違う方法で対処しましょう。:

   ```c++
   #include <Kokkos_SIMD.hpp>
 
   using simd_type = Kokkos::Experimental::simd<double>;
   constexpr int width = int(simd_type::size());
   for (int i = 0; i + width <= n; i += width) {
     simd_type sx(x + i, Kokkos::Experimental::simd_flag_default);
     simd_type sy(y + i, Kokkos::Experimental::simd_flag_default);
     simd_type sz(z + i, Kokkos::Experimental::simd_flag_default);
     simd_type sr = Kokkos::sqrt(sx * sx + sy * sy + sz * sz);
     sr.copy_to(r + i, Kokkos::Experimental::simd_flag_default);
   }
   for (; i < n; ++i) {
     r[i] = sqrt(x[i] * x[i] + y[i] * y[i] + z[i] * z[i]);
   }
   ```
  
   本アプローチの主な欠点は、コードを重複や繰り返しすることです。

4. 各イテレーションでマスクを使用:

   ```c++
   #include <Kokkos_SIMD.hpp>
 
   using simd_type = Kokkos::Experimental::simd<double>;
   using mask_type = Kokkos::Experimental::simd_mask<double>;
   constexpr int width = int(simd_type::size());
   for (int i = 0; i < n; i += width) {
     mask_type mask([] (std::size_t lane) { return i + int(lane) < n; });
     simd_type sx;
     simd_type sy;
     simd_type sz;
     where(mask, sx).copy_from(x + i, Kokkos::Experimental::simd_flag_default);
     where(mask, sy).copy_from(y + i, Kokkos::Experimental::simd_flag_default);
     where(mask, sz).copy_from(z + i, Kokkos::Experimental::simd_flag_default);
     simd_type sr = Kokkos::sqrt(sx * sx + sy * sy + sz * sz);
     where(mask, sr).copy_to(r + i, Kokkos::Experimental::simd_flag_default);
   }
   ```
  
   本方法の主な欠点は、マスクされたロードやストアを使う際のわずかなオーバーヘッドですが、パディングも変更もされていないソースからのデータを、コードの繰り返しなしにうまく処理できます。

## ライブラリコードのベクトル化

テンプレートを使うことで、複雑な数学ライブラリコードも変更せずに、ベクトル化の効果を、自動で最大限に活用できます:

```c++
テンプレート <class T>
KOKKOS_FUNCTION void quadratic_formula(
    T const& a,
    T const& b,
    T const& c,
    T& x1,
    T& x2)
{
  T 判別関数 = b * b - 4 * a * c;
  T sqrt_discriminant = Kokkos::sqrt(discriminant);
  x1 = (-b + sqrt_discriminant) / (2 * a);
  x2 = (-b - sqrt_discriminant) / (2 * a);
}
```

`T=double`　でインスタンス化すると、この関数は古典的で馴染み深い直列的な意味で振る舞います。 もし単に `T=Kokkos::Experimental::simd<double>　でインスタンス化しても、コンパイルはほぼ同じですが、すべての数学演算が必ずベクトル命令を出すことが保証され、関数は256ビットベクトル　CPU　上で同時に4つの二次式を計算できます。

Kokkos は、ダブルでできることが、SIMD　型でも実行できること、例えばこの例コードの整数リテラル `4` および `2` による掛け算を含め、すべてが実現できるように特別な配慮を行っていることに注意してください。

## 条件文

### 条件付き代入

SIMD　型で扱う中で最も難しいことの一つが条件付き論理です。 次のコードを考えます。これは値 `x` が負でないことを保証する役割を担います(この議論では最大関数の存在は、簡単な例としては無視します):

```c++
double x;
if (x < 0) x = 0;
```

このシナリオでは、単純に　SIMD　型を使うことはできません。なぜなら、 `x < 0` はブール値ではなく、複数のブール値を表現する　simd_mask<double, Abi>　オブジェクトだからです。

```c++
Kokkos::Experimental::simd<double> x;
if (x < 0 /* <- this is not a boolean */) x = 0;
```

ISO C++　の一貫した解決策は、ここで次の式を用いることです:

```c++
Kokkos::Experimental::simd<double> x;
where(x < 0, x) = 0;
```

### 三項演算子

この書き込み辞典では、SIMD　の意味での三項条件演算子 `a ? b : c` の挙動を模倣する関数を使うのも一般的な慣行です。 つまり、以下のものは機能的に同値です:

```c++
bool a;
double b;
double c;
auto d = a ? b : c;
```

```c++
Kokkos::Experimental::simd_mask<double> a;
Kokkos::Experimental::simd<double> b;
Kokkos::Experimental::simd<double> c;
auto d = Kokkos::Experimental::condition(a, b, c);
```

```c++
Kokkos::Experimental::simd_mask<double> a;
Kokkos::Experimental::simd<double> b;
Kokkos::Experimental::simd<double> c;
auto d = c;
where(a, d) = b;
```

三項演算子に関するロードマップは、次の通りです:　ISO C++　は後のバージョンでこの演算子をオーバーロードする機能を追加する可能性が高く、標準ライブラリの　SIMD　型はこれを過負荷にします

Kokkos SIMD　型を使用する際は、`条件付き`　ロジックで、できるだけ多くの式を使用することが推奨されます。これは、まだ利用されていない非標準関数や言語機能に依存しない、現在提案されている　ISO C++　のライブラリソリューションと整合しているからです。

### パフォーマンスのための還元

上記の条件付き論理の解法で、厄介な点の一つは、計算がスキップされるのではなく、単にマスクアウトされていることです。次の直列論理を考えます:

```c++
bool a;
double b = 1.0;
if (a) b = very_expensive_function(c, d, e);
```

　`if`　文を使用する場合、  `a` が `真`　でない限り、very_expensive_function　は実行されません。しかし、SIMDモードでは:

```c++
Kokkos::Experimental::simd_mask<double> a;
Kokkos::Experimental::simd<double> b = 1.0;
where(a, b) = very_expensive_function(c, d, e);
```

今や、`very_expensive_function`　は、常に実行されています。 ある存在が真である確率が非常に低いとしたらどうでしょうか?　可能であれば　`very_expensive_function`　の計算を省略したいと考えています。

このため、マスク間のブール還元を `all_of`, `none_of`, and `any_of`　と呼びます:

```c++
Kokkos::Experimental::simd_mask<double> a;
Kokkos::Experimental::simd<double> b = 1.0;
if (Kokkos::Experimental::any_of(a)) {
  where(a, b) = very_expensive_function(c, d, e);
}
```

マスク `a`　のブール値のいずれかが `真`　である場合にのみ、　`very_expensive_function`　が実行されます。 `a`　のすべてのブール値が、 `偽`　であることが多いのであれば、　`very_expensive_function`　にかかる時間は、はるかに短くなります。
