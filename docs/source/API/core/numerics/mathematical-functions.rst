一般数学関数
=====================

.. role:: cpp(code)
    :language: cpp

.. role:: strike
    :class: strike

 モチベーションの例　(https://llvm.org/docs/CompileCudaWithLLVM.html#standard-library-support　より引用)

.. code-block:: cpp

    // 本関数のClangは問題ありません。
    __device__ void test() {
        std::sin(0.); // nvcc - ok
        std::sin(0);  // nvcc - エラー, std::sin(int) オーバーライドが利用できないため。 
        sin(0);       // nvcc - 上記に同じ。

        sinf(0.);       // nvcc - ok
        std::sinf(0.);  // nvcc - no such function
    }

Kokkos　の目標は、ホストとデバイスの両方で利用可能な一貫したオーバーロードセットを提供し、C++ 数値ライブラリの実践に従うことです。

------------

.. _text: https://github.com/kokkos/kokkos/blob/develop/core/src/Kokkos_MathematicalFunctions.hpp

.. |text| replace:: ``<Kokkos_MathematicalFunctions.hpp>``

 ``<Kokkos_Core.hpp>``　に含まれる ヘッダー |text|_ 　に定義。

.. _text2: https://en.cppreference.com/w/cpp/numeric/math

.. |text2| replace:: standard C mathematical functions from ``<cmath>``　からの標準数学関数

 |text2|_のほとんど、  例えば``fabs``、 ``sqrt``、 および ``sin``　を提供します。

数学関数は、バージョン3.7以降、Kokkos::namespace　で利用可能で、以前のバージョンでは、Kokkos::Experimental　において利用可能です。

一項数学関数の例として、``sqrt`` 関数のシノプシスは、以下の通りです。

.. code-block:: cpp

    namespace Kokkos {  // (バージョン　3.7以降)
        KOKKOS_FUNCTION float       sqrt ( float x );
        KOKKOS_FUNCTION float       sqrtf( float x );
        KOKKOS_FUNCTION double      sqrt ( double x );
                        long double sqrt ( long double x );
                        long double sqrtl( long double x );
        KOKKOS_FUNCTION double      sqrt ( IntegralType x );
    }

関数は、任意の算術型の引数に対して過負荷されます。　``float`` および　``long double``　に対応する、サフィックス　``f`` および　``l`` を伴う追加関数も利用可能です。なお、このデバイスには、 ``long double`` オーバーロードは利用できないことに注意してください。。

サポートされている一般数学関数の一覧については、以下で見られます。各機能の概要については、読者の cppreference.com を参照してください。

------------

``func*`` 以下の注意事項を参照。

.. _abs: https://en.cppreference.com/w/cpp/numeric/math/fabs

.. |abs| replace:: ``abs``

.. _fabs: https://en.cppreference.com/w/cpp/numeric/math/fabs

.. |fabs| replace:: ``fabs``

.. _fmod: https://en.cppreference.com/w/cpp/numeric/math/fmod

.. |fmod| replace:: ``fmod``

.. _remainder: https://en.cppreference.com/w/cpp/numeric/math/remainder

.. |remainder| replace:: ``remainder``

.. _remquo: https://en.cppreference.com/w/cpp/numeric/math/remquo

.. |remquo| replace:: ``remquo``

.. _fma*: https://en.cppreference.com/w/cpp/numeric/math/fma

.. |fma*| replace:: ``fma*``

.. _fmax: https://en.cppreference.com/w/cpp/numeric/math/fmax

.. |fmax| replace:: ``fmax``

.. _fmin: https://en.cppreference.com/w/cpp/numeric/math/fmin

.. |fmin| replace:: ``fmin``

.. _fdim: https://en.cppreference.com/w/cpp/numeric/math/fdim

.. |fdim| replace:: ``fdim``

.. _nan: https://en.cppreference.com/w/cpp/numeric/math/nan

.. |nan| replace:: ``nan``

**基本演算** |abs|_ |fabs|_ |fmod|_ |remainder|_ |fma*|_ |fmax|_ |fmin|_ |fdim|_ |nan|_ (現在は、 Kokkos: |remquo|_　によって提供されていません)

.. _exp: https://en.cppreference.com/w/cpp/numeric/math/exp

.. |exp| replace:: ``exp``

.. _exp2: https://en.cppreference.com/w/cpp/numeric/math/exp2

.. |exp2| replace:: ``exp2``

.. _expm1: https://en.cppreference.com/w/cpp/numeric/math/expm1

.. |expm1| replace:: ``expm1``

.. _log: https://en.cppreference.com/w/cpp/numeric/math/log

.. |log| replace:: ``log``

.. _log10: https://en.cppreference.com/w/cpp/numeric/math/log10

.. |log10| replace:: ``log10``

.. _log2: https://en.cppreference.com/w/cpp/numeric/math/log2

.. |log2| replace:: ``log2``

.. _log1p: https://en.cppreference.com/w/cpp/numeric/math/log1p

.. |log1p| replace:: ``log1p``

**指数関数** |exp|_ |exp2|_ |expm1|_ |log|_ |log10|_ |log2|_ |log1p|_

.. _pow: https://en.cppreference.com/w/cpp/numeric/math/pow

.. |pow| replace:: ``pow``

.. _sqrt: https://en.cppreference.com/w/cpp/numeric/math/sqrt

.. |sqrt| replace:: ``sqrt``

.. _cbrt: https://en.cppreference.com/w/cpp/numeric/math/cbrt

.. |cbrt| replace:: ``cbrt``

.. _hypot*: https://en.cppreference.com/w/cpp/numeric/math/hypot

.. |hypot*| replace:: ``hypot*``

**べき関数** |pow|_ |sqrt|_ |cbrt|_ |hypot*|_

.. _sin: https://en.cppreference.com/w/cpp/numeric/math/sin

.. |sin| replace:: ``sin``

.. _cos: https://en.cppreference.com/w/cpp/numeric/math/cos

.. |cos| replace:: ``cos``

.. _tan: https://en.cppreference.com/w/cpp/numeric/math/tan

.. |tan| replace:: ``tan``

.. _asin: https://en.cppreference.com/w/cpp/numeric/math/asin

.. |asin| replace:: ``asin``

.. _acos: https://en.cppreference.com/w/cpp/numeric/math/acos

.. |acos| replace:: ``acos``

.. _atan: https://en.cppreference.com/w/cpp/numeric/math/atan

.. |atan| replace:: ``atan``

.. _atan2: https://en.cppreference.com/w/cpp/numeric/math/atan2

.. |atan2| replace:: ``atan2``

**三角関数** |sin|_ |cos|_ |tan|_ |asin|_ |acos|_ |atan|_ |atan2|_

.. _sinh: https://en.cppreference.com/w/cpp/numeric/math/sinh

.. |sinh| replace:: ``sinh``

.. _cosh: https://en.cppreference.com/w/cpp/numeric/math/cosh

.. |cosh| replace:: ``cosh``

.. _tanh: https://en.cppreference.com/w/cpp/numeric/math/tanh

.. |tanh| replace:: ``tanh``

.. _asinh: https://en.cppreference.com/w/cpp/numeric/math/asinh

.. |asinh| replace:: ``asinh``

.. _acosh: https://en.cppreference.com/w/cpp/numeric/math/acosh

.. |acosh| replace:: ``acosh``

.. _atanh: https://en.cppreference.com/w/cpp/numeric/math/atanh

.. |atanh| replace:: ``atanh``

**双曲関数** |sinh|_ |cosh|_ |tanh|_ |asinh|_ |acosh|_ |atanh|_

.. _erf: https://en.cppreference.com/w/cpp/numeric/math/erf

.. |erf| replace:: ``erf``

.. _erfc: https://en.cppreference.com/w/cpp/numeric/math/erfc

.. |erfc| replace:: ``erfc``

.. _tgamma: https://en.cppreference.com/w/cpp/numeric/math/tgamma

.. |tgamma| replace:: ``tgamma``

.. _lgamma: https://en.cppreference.com/w/cpp/numeric/math/lgamma

.. |lgamma| replace:: ``lgamma``

**誤差関数とガンマ関数** |erf|_ |erfc|_ |tgamma|_ |lgamma|_

.. _ceil: https://en.cppreference.com/w/cpp/numeric/math/ceil

.. |ceil| replace:: ``ceil``

.. _floor: https://en.cppreference.com/w/cpp/numeric/math/floor

.. |floor| replace:: ``floor``

.. _trunc: https://en.cppreference.com/w/cpp/numeric/math/trunc

.. |trunc| replace:: ``trunc``

.. _round*: https://en.cppreference.com/w/cpp/numeric/math/round

.. |round*| replace:: ``round*``

.. _lround: https://en.cppreference.com/w/cpp/numeric/math/round

.. |lround| replace:: ``lround``

.. _llround: https://en.cppreference.com/w/cpp/numeric/math/round

.. |llround| replace:: ``llround``

.. _nearbyint*: https://en.cppreference.com/w/cpp/numeric/math/nearbyint

.. |nearbyint*| replace:: ``nearbyint*``

.. _rint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |rint| replace:: ``rint``

.. _lrint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |lrint| replace:: ``lrint``

.. _llrint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |llrint| replace:: ``llrint``

**最も近い整数浮動小数点演算** |ceil|_ |floor|_ |trunc|_ |round*|_ |nearbyint*|_ ( 現在　Kokkos　によっては、提供されていません: |lround|_ |llround|_ |rint|_ |lrint|_ |llrint|_)

.. _frexp: https://en.cppreference.com/w/cpp/numeric/math/frexp

.. |frexp| replace:: ``frexp``

.. _ldexp: https://en.cppreference.com/w/cpp/numeric/math/ldexp

.. |ldexp| replace:: ``ldexp``

.. _modf: https://en.cppreference.com/w/cpp/numeric/math/modf

.. |modf| replace:: ``modf``

.. _scalbn: https://en.cppreference.com/w/cpp/numeric/math/scalbn

.. |scalbn| replace:: ``scalbn``

.. _scalbln: https://en.cppreference.com/w/cpp/numeric/math/scalbln

.. |scalbln| replace:: ``scalbln``

.. _ilog: https://en.cppreference.com/w/cpp/numeric/math/ilog

.. |ilog| replace:: ``ilog``

.. _logb*: https://en.cppreference.com/w/cpp/numeric/math/logb

.. |logb*| replace:: ``logb*``

.. _nextafter*: https://en.cppreference.com/w/cpp/numeric/math/nextafter 

.. |nextafter*| replace:: ``nextafter*``

.. _nexttoward: https://en.cppreference.com/w/cpp/numeric/math/nexttoward

.. |nexttoward| replace:: ``nexttoward``

.. _copysign*: https://en.cppreference.com/w/cpp/numeric/math/copysign

.. |copysign*| replace:: ``copysign*``

**浮動小数点操作関数** |logb*|_ |nextafter*|_ |copysign*|_ (　現在　Kokkos　によっては、提供されていません: |frexp|_ |ldexp|_ |modf|_ |scalbn|_ |scalbln|_ |ilog|_ |nexttoward|_)

.. _fpclassify: https://en.cppreference.com/w/cpp/numeric/math/fpclassify

.. |fpclassify| replace:: ``fpclassify``

.. _isfinite: https://en.cppreference.com/w/cpp/numeric/math/isfinite

.. |isfinite| replace:: ``isfinite``

.. _isinf: https://en.cppreference.com/w/cpp/numeric/math/isinf

.. |isinf| replace:: ``isinf``

.. _isnan: https://en.cppreference.com/w/cpp/numeric/math/isnan

.. |isnan| replace:: ``isnan``

.. _isnormal: https://en.cppreference.com/w/cpp/numeric/math/isnormal

.. |isnormal| replace:: ``isnormal``

.. _signbit*: https://en.cppreference.com/w/cpp/numeric/math/signbit

.. |signbit*| replace:: ``signbit*``

.. _isgreater: https://en.cppreference.com/w/cpp/numeric/math/isgreater

.. |isgreater| replace:: ``isgreater``

.. _isgreaterequal: https://en.cppreference.com/w/cpp/numeric/math/isgreaterequal

.. |isgreaterequal| replace:: ``isgreaterequal``

.. _isless: https://en.cppreference.com/w/cpp/numeric/math/isless

.. |isless| replace:: ``isless``

.. _islessequal: https://en.cppreference.com/w/cpp/numeric/math/islessequal

.. |islessequal| replace:: ``islessequal``

.. _islessgreater: https://en.cppreference.com/w/cpp/numeric/math/islessgreater

.. |islessgreater| replace:: ``islessgreater``

.. _isunordered: https://en.cppreference.com/w/cpp/numeric/math/isunordered

.. |isunordered| replace:: ``isunordered``

**分類および比較** |isfinite|_ |isinf|_ |isnan|_ |signbit*|_ (　現在　Kokkos　によっては、提供されていません: |fpclassify|_ |isnormal|_ |isgreater|_ |isgreaterequal|_ |isless|_ |islessequal|_ |islessgreater|_ |isunordered|_)

------------

**　C++　標準ライブラリで提供されていないその他の数学関数**

``rsqrt(x)`` (すなわち computes \frac{1}{\sqrt(x)} を計算) (Kokkos 4.1以降)

------------

注意事項
-----

.. _openIssue: https://github.com/kokkos/kokkos/issues/new

.. |openIssue| replace:: **open an issue**

.. _issue4767: https://github.com/kokkos/kokkos/issues/4767

.. |issue4767| replace:: **Issue #4767**

.. _KnownIssues: ../../known-issues.html

.. |KnownIssues| replace:: known issues

* **現在実装されていない機能が必要な場合は**、**遠慮なく**   |openIssue|_  を実行してください。 |issue4767|_  はこれらを記録し、実装可能性に関するメモを掲載しています。**
*  SYCL　バックエンドでは、``nearbyint``　は利用できません
* ``round``、 ``logb``、 ``nextafter``、 ``copysign`` および ``signbit`` は、バージョン3.7以降利用可能です。
* ``hypot`` の3つの引数のバージョンは、4.0以降利用可能です。
* ``fma`` は、 4.0降利用可能です。
* ``namespace Kokkosを使う``　または、using　ダイレクティブには注意してください;無条件の数学関数呼び出しでコンパイルエラーを引き起こします。 代わりに、明示的条件( Kokkos::sqrt) または using-declaration を使ってください (  |KnownIssues|_　を参照)。
* 数学関数は、バージョン4.3の　``Kokkos::Experimental::``　内の名前空間からから削除されました。
* 四重精密浮動小数点数  ``__float128``のサポートは、``-DKokkos_ENABLE_LIBQUADMATH=ON``　によって有効化できます。

------------

以下も参照
--------

`数学定数 <mathematical-constants.html>`_

`数学特性 <numeric-traits.html>`_  
