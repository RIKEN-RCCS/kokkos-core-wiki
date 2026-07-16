一般数学関数
============

.. role:: cpp(code)
    :language: cpp

.. role:: strike
    :class: strike

モチベーションの例 (https://llvm.org/docs/CompileCudaWithLLVM.html#standard-library-support より引用)

.. code-block:: cpp

    // 本関数のClangは問題ありません。
    __device__ void test() {
        std::sin(0.); // nvcc - ok
        std::sin(0);  // nvcc - エラー, std::sin(int) オーバーライドが利用できないため。 
        sin(0);       // nvcc - 上記に同じ。

        sinf(0.);       // nvcc - ok
        std::sinf(0.);  // nvcc - no such function
    }

Kokkos の目標は、ホストとデバイスの両方で利用可能な一貫したオーバーロードセットを提供し、C++ 数値ライブラリの実践に従うことです。

------------

.. _text: https://github.com/kokkos/kokkos/blob/develop/core/src/Kokkos_MathematicalFunctions.hpp

.. |text| replace:: ``<Kokkos_MathematicalFunctions.hpp>``

``<Kokkos_Core.hpp>`` に含まれる ヘッダー |text|_  に定義。

.. _text2: https://en.cppreference.com/w/cpp/numeric/math

.. |text2| replace:: ``<cmath>`` からの標準C数学関数

|text2|_ のほとんど、  例えば``fabs``、 ``sqrt``、 および ``sin`` を提供します。

一項数学関数の例として、 ``sqrt`` 関数の概要は、以下の通りです。

.. code-block:: cpp

    namespace Kokkos {
        KOKKOS_FUNCTION float       sqrt ( float x );
        KOKKOS_FUNCTION float       sqrtf( float x );
        KOKKOS_FUNCTION double      sqrt ( double x );
                        long double sqrt ( long double x );
                        long double sqrtl( long double x );
        KOKKOS_FUNCTION double      sqrt ( IntegralType x );
    }

関数は、任意の算術型の引数に対して過負荷されます。 ``float`` および ``long double`` に対応する、サフィックス ``f`` および ``l`` を伴う追加関数も利用可能です。なお、このデバイスには、 ``long double`` オーバーロードは利用できないことに注意してください。

サポートされている一般数学関数の一覧については、以下で見られます。各機能の概要については、読者の cppreference.com を参照してください。

------------

.. [#since_kokkos_4_0] (Kokkos 4.0以降)
.. [#since_kokkos_4_1] (Kokkos 4.1以降)
.. [#since_kokkos_5_1] (Kokkos 5.1以降)
.. [#not_available_with_sycl] (SYCLでは利用できません)

基本演算
^^^^^^^^

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

.. _fma: https://en.cppreference.com/w/cpp/numeric/math/fma

.. |fma| replace:: ``fma``

.. _fmax: https://en.cppreference.com/w/cpp/numeric/math/fmax

.. |fmax| replace:: ``fmax``

.. _fmin: https://en.cppreference.com/w/cpp/numeric/math/fmin

.. |fmin| replace:: ``fmin``

.. _fdim: https://en.cppreference.com/w/cpp/numeric/math/fdim

.. |fdim| replace:: ``fdim``

.. _nan: https://en.cppreference.com/w/cpp/numeric/math/nan

.. |nan| replace:: ``nan``

.. list-table::
   :align: left

   * - |abs|_
       |fabs|_
     - 浮動小数点値の絶対値 (:math:`|x|`)
   * - |fmod|_
     - 浮動小数点除算演算の剰余
   * - |remainder|_
     - 除算演算の符号付き剰余
   * - |remquo|_ [#since_kokkos_5_1]_
     - 符号付き剰余および除算演算の下位3ビット
   * - |fma|_ [#since_kokkos_4_0]_
     - 融合積和演算
   * - |fmax|_
     - 2つの浮動小数点値のうち大きい方
   * - |fmin|_
     - 2つの浮動小数点値のうち小さい方
   * - |fdim|_
     - 2つの浮動小数点値の正の差 (:math:`\max(0, x-y)`)
   * - |nan|_
     - 非数 (NaN)

指数関数
^^^^^^^^

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

.. list-table::
   :align: left

   * - |exp|_
     - :math:`e` を指定されたべき乗した値を返す (:math:`e^x`)
   * - |exp2|_
     - :math:`2` を指定されたべき乗した値を返す (:math:`2^x`)
   * - |expm1|_
     - :math:`e` を指定されたべき乗した値から :math:`1` を引いた値を返す (:math:`e^x-1`)
   * - |log|_
     - 指定された数の底 :math:`e` の対数 (:math:`\log(x)`)
   * - |log10|_
     - 指定された数の底 :math:`10` の対数 (:math:`\log_{10}(x)`)
   * - |log2|_
     - 指定された数の底 :math:`2` の対数 (:math:`\log_{2}(x)`)
   * - |log1p|_
     - 指定された数に1を加えた値の自然対数 (底 :math:`e`) (:math:`\ln(1+x)`)

べき関数
^^^^^^^^

.. _pow: https://en.cppreference.com/w/cpp/numeric/math/pow

.. |pow| replace:: ``pow``

.. _sqrt: https://en.cppreference.com/w/cpp/numeric/math/sqrt

.. |sqrt| replace:: ``sqrt``

.. _cbrt: https://en.cppreference.com/w/cpp/numeric/math/cbrt

.. |cbrt| replace:: ``cbrt``

.. _hypot: https://en.cppreference.com/w/cpp/numeric/math/hypot

.. |hypot| replace:: ``hypot``

.. list-table::
   :align: left

   * - |pow|_
     - 数を指定されたべき乗する (:math:`x^y`)
   * - |sqrt|_
     - 平方根を計算する (:math:`\sqrt{x}`)
   * - |cbrt|_
     - 立方根を計算する (:math:`\sqrt[3]{x}`)
   * - |hypot|_ [#3_argument_overload_since_kokkos_4_0]_
     - 斜辺を計算する (:math:`\sqrt{x^2 + y^2}` および :math:`\sqrt{x^2 + y^2 + z^2}`)

.. [#3_argument_overload_since_kokkos_4_0] 3引数のオーバーロードはKokkos 4.0以降利用可能

三角関数
^^^^^^^^

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

.. list-table::
   :align: left

   * - |sin|_
     - 正弦を計算する (:math:`\sin(x)`)
   * - |cos|_
     - 余弦を計算する (:math:`\cos(x)`)
   * - |tan|_
     - 正接を計算する (:math:`\tan(x)`)
   * - |asin|_
     - 逆正弦を計算する (:math:`\arcsin(x)`)
   * - |acos|_
     - 逆余弦を計算する (:math:`\arccos(x)`)
   * - |atan|_
     - 逆正接を計算する (:math:`\arctan(x)`)
   * - |atan2|_
     - 符号を使って象限を決定する逆正接

双曲線関数
^^^^^^^^^^

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

.. list-table::
   :align: left

   * - |sinh|_
     - 双曲線正弦を計算する (:math:`\sinh(x)`)
   * - |cosh|_
     - 双曲線余弦を計算する (:math:`\cosh(x)`)
   * - |tanh|_
     - 双曲線正接を計算する (:math:`\tanh(x)`)
   * - |asinh|_
     - 逆双曲線正弦を計算する (:math:`\text{arsinh}(x)`)
   * - |acosh|_
     - 逆双曲線余弦を計算する (:math:`\text{arcosh}(x)`)
   * - |atanh|_
     - 逆双曲線正接を計算する (:math:`\text{artanh}(x)`)

誤差関数とガンマ関数
^^^^^^^^^^^^^^^^^^^^

.. _erf: https://en.cppreference.com/w/cpp/numeric/math/erf

.. |erf| replace:: ``erf``

.. _erfc: https://en.cppreference.com/w/cpp/numeric/math/erfc

.. |erfc| replace:: ``erfc``

.. _tgamma: https://en.cppreference.com/w/cpp/numeric/math/tgamma

.. |tgamma| replace:: ``tgamma``

.. _lgamma: https://en.cppreference.com/w/cpp/numeric/math/lgamma

.. |lgamma| replace:: ``lgamma``

.. list-table::
   :align: left

   * - |erf|_
     - 誤差関数
   * - |erfc|_
     - 相補誤差関数
   * - |tgamma|_
     - ガンマ関数
   * - |lgamma|_
     - ガンマ関数の自然対数

最も近い整数への浮動小数点演算
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _ceil: https://en.cppreference.com/w/cpp/numeric/math/ceil

.. |ceil| replace:: ``ceil``

.. _floor: https://en.cppreference.com/w/cpp/numeric/math/floor

.. |floor| replace:: ``floor``

.. _trunc: https://en.cppreference.com/w/cpp/numeric/math/trunc

.. |trunc| replace:: ``trunc``

.. _round: https://en.cppreference.com/w/cpp/numeric/math/round

.. |round| replace:: ``round``

.. _lround: https://en.cppreference.com/w/cpp/numeric/math/round

.. |lround| replace:: ``lround``

.. _llround: https://en.cppreference.com/w/cpp/numeric/math/round

.. |llround| replace:: ``llround``

.. _nearbyint: https://en.cppreference.com/w/cpp/numeric/math/nearbyint

.. |nearbyint| replace:: ``nearbyint``

.. _rint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |rint| replace:: ``rint``

.. _lrint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |lrint| replace:: ``lrint``

.. _llrint: https://en.cppreference.com/w/cpp/numeric/math/rint

.. |llrint| replace:: ``llrint``

.. list-table::
   :align: left

   * - |ceil|_
     - 指定された値以上の最も近い整数
   * - |floor|_
     - 指定された値以下の最も近い整数
   * - |trunc|_
     - 指定された値の絶対値を超えない最も近い整数
   * - |round|_
       |lround|_ [#since_kokkos_5_1]_ [#not_available_with_sycl]_
       |llround|_ [#since_kokkos_5_1]_ [#not_available_with_sycl]_
     - 最も近い整数、中間の場合は0から離れる方向に丸める
   * - |nearbyint|_ [#not_available_with_sycl]_
     - 現在の丸めモードを使用した最も近い整数
   * - |rint|_ [#since_kokkos_5_1]_
       |lrint|_ [#since_kokkos_5_1]_ [#not_available_with_sycl]_
       |llrint|_ [#since_kokkos_5_1]_ [#not_available_with_sycl]_
     - 現在の丸めモードを使用した最も近い整数、結果が異なる場合は例外を発生する

浮動小数点操作関数
^^^^^^^^^^^^^^^^^^

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

.. _ilogb: https://en.cppreference.com/w/cpp/numeric/math/ilogb

.. |ilogb| replace:: ``ilogb``

.. _logb: https://en.cppreference.com/w/cpp/numeric/math/logb

.. |logb| replace:: ``logb``

.. _nextafter: https://en.cppreference.com/w/cpp/numeric/math/nextafter 

.. |nextafter| replace:: ``nextafter``

.. 次の行はタイプミスではありません。nexttoward は nextafter と同じページに記載されています。
.. _nexttoward: https://en.cppreference.com/w/cpp/numeric/math/nextafter

.. |nexttoward| replace:: ``nexttoward``

.. _copysign: https://en.cppreference.com/w/cpp/numeric/math/copysign

.. |copysign| replace:: ``copysign``

.. list-table::
   :align: left

   * - |frexp|_ [#since_kokkos_5_1]_
     - 数を仮数部と底 :math:`2` の指数部に分解する
   * - |ldexp|_ [#since_kokkos_5_1]_
     - 数に :math:`2` を整数乗した値を掛ける
   * - |modf|_ [#since_kokkos_5_1]_
     - 数を整数部と小数部に分解する
   * - |scalbn|_ [#since_kokkos_5_1]_
       |scalbln|_ [#since_kokkos_5_1]_
     - 数に ``FLT_RADIX`` をべき乗した値を掛ける
   * - |ilogb|_ [#since_kokkos_5_1]_
     - 数の指数部を抽出する
   * - |logb|_
     - 数の指数部を抽出する
   * - |nextafter|_
       |nexttoward|_ [#since_kokkos_5_1]_
     - 指定された値に向かう次の表現可能な浮動小数点値
   * - |copysign|_
     - 浮動小数点値の符号をコピーする

分類および比較
^^^^^^^^^^^^^^

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

.. _signbit: https://en.cppreference.com/w/cpp/numeric/math/signbit

.. |signbit| replace:: ``signbit``

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

.. list-table::
   :align: left

   * - |fpclassify|_ [#since_kokkos_5_1]_
     - 指定された浮動小数点値を分類する
   * - |isfinite|_
     - 指定された数が有限の値を持つかどうかを確認する
   * - |isinf|_
     - 指定された数が無限大であるかどうかを確認する
   * - |isnan|_
     - 指定された数がNaNであるかどうかを確認する
   * - |isnormal|_ [#since_kokkos_5_1]_
     - 指定された数が正規化数であるかどうかを確認する
   * - |signbit|_
     - 指定された数が負であるかどうかを確認する
   * - |isgreater|_ [#since_kokkos_5_1]_
     - 1番目の浮動小数点引数が2番目より大きいかどうかを確認する
   * - |isgreaterequal|_ [#since_kokkos_5_1]_
     - 1番目の浮動小数点引数が2番目以上であるかどうかを確認する
   * - |isless|_ [#since_kokkos_5_1]_
     - 1番目の浮動小数点引数が2番目より小さいかどうかを確認する
   * - |islessequal|_ [#since_kokkos_5_1]_
     - 1番目の浮動小数点引数が2番目以下であるかどうかを確認する
   * - |islessgreater|_ [#since_kokkos_5_1]_
     - 1番目の浮動小数点引数が2番目より小さいか大きいかどうかを確認する
   * - |isunordered|_ [#since_kokkos_5_1]_
     - 2つの浮動小数点値が順序付けできないかどうかを確認する

------------

その他（非標準）の関数
^^^^^^^^^^^^^^^^^^^^^^

.. note:: これらの関数はC++標準ライブラリでは提供されていません。

.. list-table::
   :align: left

   * - ``rsqrt`` [#since_kokkos_4_1]_
     - 平方根の逆数を計算する (:math:`1/\sqrt{x}`)
   * - ``rcp`` [#since_kokkos_5_1]_
     - 逆数を計算する (:math:`1/x`)

------------

注意事項
--------

.. _openIssue: https://github.com/kokkos/kokkos/issues/new

.. |openIssue| replace:: **open an issue**

.. _issue4767: https://github.com/kokkos/kokkos/issues/4767

.. |issue4767| replace:: **Issue #4767**

.. _KnownIssues: ../../known-issues.html

.. |KnownIssues| replace:: known issues

* **現在実装されていない関数のいずれかが必要な場合は、遠慮なく** |openIssue|_ **してください。** |issue4767|_ **がこれらを記録しており、実装可能性に関するメモを掲載しています。**
* using ディレクティブ ``using namespace Kokkos;`` は、数学関数への非修飾呼び出しでコンパイルエラーを引き起こすことに注意してください。代わりに明示的な修飾（``Kokkos::sqrt``）または using 宣言（``using
  Kokkos::sqrt;``）を使用してください。（|KnownIssues|_ を参照）
* 数学関数は、バージョン4.3で ``Kokkos::Experimental::`` 名前空間から削除されました。
* 四倍精度浮動小数点 ``__float128`` のサポートは、``-DKokkos_ENABLE_LIBQUADMATH=ON`` によって有効化できます。

------------

以下も参照
----------

`数学定数 <mathematical-constants.html>`_

`数学特性 <numeric-traits.html>`_  
