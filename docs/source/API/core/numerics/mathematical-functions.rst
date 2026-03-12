一般数学関数
=====================

.. role:: cpp(code)
    :language: cpp

.. role:: strike
    :クラス: ストライク

 モチベーションの例　(https://llvm.org/docs/CompileCudaWithLLVM.html#standard-library-support　より引用)

.. code-block:: cpp

    // 本関数のClangは問題ありません。
    __device__ void test() {
        std::sin(0.); // nvcc - ok
        std::sin(0);  // nvcc - error, because no std::sin(int) override is available.
        sin(0);       // nvcc - same as above.

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

数学関数は、バージョン3.7以降、Kokkos::namespace　で利用可能で、以前のバージョンではKokkos::Experimental　において利用可能です。

一項数学関数の例として、``sqrt`` 関数のシノプシスは、以下の通りです。

.. code-block:: cpp

    名前空間 Kokkos {  // ( 3.7以降)
        KOKKOS_FUNCTION float       sqrt ( float x );
        KOKKOS_FUNCTION float       sqrtf( float x );
        KOKKOS_FUNCTION double      sqrt ( double x );
                        long double sqrt ( long double x );
                        long double sqrtl( long double x );
        KOKKOS_FUNCTION double      sqrt ( IntegralType x );
    }

関数は、任意の算術型の引数に対して過負荷されます。　``float`` および　``long double``に対応する、サフィックス　``f`` および　``l`` を伴う追加関数も利用可能です。なお、このデバイスには、 ``long double`` オーバーロードは利用できないことに注意してください。。

サポートされている一般数学関数の一覧については、以下で見られます。各機能の概要については、読者の cppreference.com を参照してください。

------------

``func*`` 以下の注意事項を参照。

.. _abs: https://en.cppreference.com/w/cpp/numeric/math/fabs

.. |abs| replace:: ``abs``

.. _fabs: https://en.cppreference.com/w/cpp/numeric/math/fabs

.. |fabs| 置換:: ``fabs``

.. _fmod: https://en.cppreference.com/w/cpp/numeric/math/fmod

.. |fmod| 置換:: ``fmod``

.. _remainder: https://en.cppreference.com/w/cpp/numeric/math/remainder

.. |remainder| 置換:: ``remainder``

.. _remquo: https://en.cppreference.com/w/cpp/numeric/math/remquo

.. |remquo| 置換:: ``remquo``

.. _fma*: https://en.cppreference.com/w/cpp/numeric/math/fma

.. |fma*| 置換:: ``fma*``

.. _fmax: https://en.cppreference.com/w/cpp/numeric/math/fmax

.. |fmax| 置換:: ``fmax``

.. _fmin: https://en.cppreference.com/w/cpp/numeric/math/fmin

.. |fmin| 置換:: ``fmin``

.. _fdim: https://en.cppreference.com/w/cpp/numeric/math/fdim

.. |fdim| 置換:: ``fdim``

.. _nan: https://en.cppreference.com/w/cpp/numeric/math/nan

.. |nan| 置換:: ``nan``

**基本演算** |abs|_ |fabs|_ |fmod|_ |remainder|_ |fma*|_ |fmax|_ |fmin|_ |fdim|_ |nan|_ (現在は、 Kokkos: |remquo|_　によって提供されていません)

.. _exp: https://en.cppreference.com/w/cpp/numeric/math/exp

.. |exp| 置換:: ``exp``

.. _exp2: https://en.cppreference.com/w/cpp/numeric/math/exp2

.. |exp2| 置換:: ``exp2``

.. _expm1: https://en.cppreference.com/w/cpp/numeric/math/expm1

.. |expm1| 置換:: ``expm1``

.. _log: https://en.cppreference.com/w/cpp/numeric/math/log

.. |log| 置換:: ``log``

.. _log10: https://en.cppreference.com/w/cpp/numeric/math/log10

.. |log10| 置換:: ``log10``

.. _log2: https://en.cppreference.com/w/cpp/numeric/math/log2

.. |log2| 置換:: ``log2``

.. _log1p: https://en.cppreference.com/w/cpp/numeric/math/log1p

.. |log1p| 置換:: ``log1p``

**指数関数** |exp|_ |exp2|_ |expm1|_ |log|_ |log10|_ |log2|_ |log1p|_

.. _pow: https://en.cppreference.com/w/cpp/numeric/math/pow

.. |pow| 置換:: ``pow``

.. _sqrt: https://en.cppreference.com/w/cpp/numeric/math/sqrt

.. |sqrt| 置換:: ``sqrt``

.. _cbrt: https://en.cppreference.com/w/cpp/numeric/math/cbrt

.. |cbrt| 置換:: ``cbrt``

.. _hypot*: https://en.cppreference.com/w/cpp/numeric/math/hypot

.. |hypot*| 置換:: ``hypot*``

**べき関数** |pow|_ |sqrt|_ |cbrt|_ |hypot*|_

.. _sin: https://en.cppreference.com/w/cpp/numeric/math/sin

.. |sin| 置換:: ``sin``

.. _cos: https://en.cppreference.com/w/cpp/numeric/math/cos

.. |cos| 置換:: ``cos``

.. _tan: https://en.cppreference.com/w/cpp/numeric/math/tan

.. |tan| 置換:: ``tan``

.. _asin: https://en.cppreference.com/w/cpp/numeric/math/asin

.. |asin| 置換:: ``asin``

.. _acos: https://en.cppreference.com/w/cpp/numeric/math/acos

.. |acos| 置換:: ``acos``

.. _atan: https://en.cppreference.com/w/cpp/numeric/math/atan

.. |atan| 置換:: ``atan``

.. _atan2: https://en.cppreference.com/w/cpp/numeric/math/atan2

.. |atan2| 置換:: ``atan2``

**三角関数** |sin|_ |cos|_ |tan|_ |asin|_ |acos|_ |atan|_ |atan2|_

.. _sinh: https://en.cppreference.com/w/cpp/numeric/math/sinh

.. |sinh| 置換:: ``sinh``

.. _cosh: https://en.cppreference.com/w/cpp/numeric/math/cosh

.. |cosh| 置換:: ``cosh``

.. _tanh: https://en.cppreference.com/w/cpp/numeric/math/tanh

.. |tanh| 置換:: ``tanh``

.. _asinh: https://en.cppreference.com/w/cpp/numeric/math/asinh

.. |asinh| 置換:: ``asinh``

.. _acosh: https://en.cppreference.com/w/cpp/numeric/math/acosh

.. |acosh| 置換:: ``acosh``

.. _atanh: https://en.cppreference.com/w/cpp/numeric/math/atanh

.. |atanh| 置換:: ``atanh``

**双曲関数** |sinh|_ |cosh|_ |tanh|_ |asinh|_ |acosh|_ |atanh|_

.. _erf: https://en.cppreference.com/w/cpp/numeric/math/erf

.. |erf| 置換:: ``erf``

.. _erfc: https://en.cppreference.com/w/cpp/numeric/math/erfc

.. |erfc| 置換:: ``erfc``

.. _tgamma: https://en.cppreference.com/w/cpp/numeric/math/tgamma

.. |tgamma| 置換:: ``tgamma``

.. _lgamma: https://en.cppreference.com/w/cpp/numeric/math/lgamma

.. |lgamma| 置換:: ``lgamma``

**誤差関数とガンマ関数** |erf|_ |erfc|_ |tgamma|_ |lgamma|_

.. _ceil: https://en.cppreference.com/w/cpp/numeric/math/ceil

.. |ceil| 置換:: ``ceil``

.. _floor: https://en.cppreference.com/w/cpp/numeric/math/floor

.. |floor| 置換:: ``floor``

.. _trunc: https://en.cppreference.com/w/cpp/numeric/math/trunc

.. |trunc| 置換:: ``trunc``

.. _round*: https://en.cppreference.com/w/cpp/numeric/math/round

.. |round*| 置換:: ``round*``

.. _lround: https://en.cppreference.com/w/cpp/numeric/math/round

.. |lround| 置換:: ``lround``

.. _llround: https://en.cppreference.com/w/cpp/numeric/math/round

.. |llround| 置換:: ``llround``

.. _nearbyint*: https://en.cppreference.com/w/cpp/numeric/math/nearbyint

.. |nearbyint*| 置換:: ``nearbyint*``

.. _rint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |rint| 置換:: ``rint``

.. _lrint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |lrint| 置換:: ``lrint``

.. _llrint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |llrint| 置換:: ``llrint``

**最も近い整数浮動小数点演算** |ceil|_ |floor|_ |trunc|_ |round*|_ |nearbyint*|_ ( 現在　Kokkos　によっては、提供されていません: |lround|_ |llround|_ |rint|_ |lrint|_ |llrint|_)

.. _frexp: https://en.cppreference.com/w/cpp/numeric/math/frexp

.. |frexp| 置換:: ``frexp``

.. _ldexp: https://en.cppreference.com/w/cpp/numeric/math/ldexp

.. |ldexp| 置換:: ``ldexp``

.. _modf: https://en.cppreference.com/w/cpp/numeric/math/modf

.. |modf| 置換:: ``modf``

.. _scalbn: https://en.cppreference.com/w/cpp/numeric/math/scalbn

.. |scalbn| 置換:: ``scalbn``

.. _scalbln: https://en.cppreference.com/w/cpp/numeric/math/scalbln

.. |scalbln| 置換:: ``scalbln``

.. _ilog: https://en.cppreference.com/w/cpp/numeric/math/ilog

.. |ilog| 置換:: ``ilog``

.. _logb*: https://en.cppreference.com/w/cpp/numeric/math/logb

.. |logb*| 置換:: ``logb*``

.. _nextafter*: https://en.cppreference.com/w/cpp/numeric/math/nextafter 

.. |nextafter*| 置換:: ``nextafter*``

.. _nexttoward: https://en.cppreference.com/w/cpp/numeric/math/nexttoward

.. |nexttoward| 置換:: ``nexttoward``

.. _copysign*: https://en.cppreference.com/w/cpp/numeric/math/copysign

.. |copysign*| 置換:: ``copysign*``

**浮動小数点操作関数** |logb*|_ |nextafter*|_ |copysign*|_ (　現在　Kokkos　によっては、提供されていません: |frexp|_ |ldexp|_ |modf|_ |scalbn|_ |scalbln|_ |ilog|_ |nexttoward|_)

.. _fpclassify: https://en.cppreference.com/w/cpp/numeric/math/fpclassify

.. |fpclassify| 置換:: ``fpclassify``

.. _isfinite: https://en.cppreference.com/w/cpp/numeric/math/isfinite

.. |isfinite| 置換:: ``isfinite``

.. _isinf: https://en.cppreference.com/w/cpp/numeric/math/isinf

.. |isinf| 置換:: ``isinf``

.. _isnan: https://en.cppreference.com/w/cpp/numeric/math/isnan

.. |isnan| 置換:: ``isnan``

.. _isnormal: https://en.cppreference.com/w/cpp/numeric/math/isnormal

.. |isnormal| 置換:: ``isnormal``

.. _signbit*: https://en.cppreference.com/w/cpp/numeric/math/signbit

.. |signbit*| 置換:: ``signbit*``

.. _isgreater: https://en.cppreference.com/w/cpp/numeric/math/isgreater

.. |isgreater| 置換:: ``isgreater``

.. _isgreaterequal: https://en.cppreference.com/w/cpp/numeric/math/isgreaterequal

.. |isgreaterequal| 置換:: ``isgreaterequal``

.. _isless: https://en.cppreference.com/w/cpp/numeric/math/isless

.. |isless| 置換:: ``isless``

.. _islessequal: https://en.cppreference.com/w/cpp/numeric/math/islessequal

.. |islessequal| 置換:: ``islessequal``

.. _islessgreater: https://en.cppreference.com/w/cpp/numeric/math/islessgreater

.. |islessgreater| 置換:: ``islessgreater``

.. _isunordered: https://en.cppreference.com/w/cpp/numeric/math/isunordered

.. |isunordered| 置換:: ``isunordered``

**分類および比較** |isfinite|_ |isinf|_ |isnan|_ |signbit*|_ (　現在　Kokkos　によっては、提供されていません: |fpclassify|_ |isnormal|_ |isgreater|_ |isgreaterequal|_ |isless|_ |islessequal|_ |islessgreater|_ |isunordered|_)

------------

**　C++　標準ライブラリで提供されていないその他の数学関数**

``rsqrt(x)`` (　すなわち computes \frac{1}{\sqrt(x)} を計算　) ( Kokkos 4.1以降)

------------

注意事項
-----

.. _openIssue: https://github.com/kokkos/kokkos/issues/new

.. |openIssue| 置換:: **open an issue**

.. _issue4767: https://github.com/kokkos/kokkos/issues/4767

.. |issue4767| 置換:: **Issue #4767**

.. _KnownIssues: ../../known-issues.html

.. |KnownIssues| 置換:: known issues既知の問題

* **現在実装されていない機能が必要な場合は**、**遠慮なく**   |openIssue|_  を実行してください。 |issue4767|_  はこれらを記録し、実装可能性に関するメモを掲載しています。**
*  SYCL　バックエンドでは、``nearbyint``　は利用できません
* ``round``、 ``logb``、 ``nextafter``、 ``copysign`` および ``signbit`` は、バージョン3.7以降利用可能です。
* ``hypot`` の3つの引数のバージョンは、4.0以降利用可能です。
* ``fma`` は、 4.0降利用可能です。
* ``namespace Kokkosを使う``　または、using-directive には注意してください;無条件の数学関数呼び出しでコンパイルエラーを引き起こします。 代わりに、明示的条件( Kokkos::sqrt) または using-declaration を使ってください (  |KnownIssues|_　を参照)。
* 数学関数は、バージョン4.3の　``Kokkos::Experimental::``　内の名前空間からから削除されました。
* 四重精密浮動小数点数  ``__float128``のサポートは、``-DKokkos_ENABLE_LIBQUADMATH=ON``　によって有効化できます。

------------

以下も参照
--------

`数学定数 <mathematical-constants.html>`_

`数学特性 <numeric-traits.html>`_  
