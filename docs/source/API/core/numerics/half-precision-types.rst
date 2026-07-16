.. _api-Half-precision-types:

半精度型
========

.. warning::
   ``half_t`` および ``bhalf_t`` は、まだ ``Kokkos::Experimental`` namespace 内にあります。

型
--

Kokkos はポータブルな半精度型を、 ``Kokkos::Experimental::half_t`` および ``Kokkos::Experimental::bhalf_t`` の名称で提供します。
 - ``half_t`` は、標準の半精度浮動小数点数を表し、1ビットの符号ビット、5ビットの指数部、10ビットの小数部で構成されます。
 - ``bhalf_t`` は、'brain half' として知られる型に対応し、1ビットの符号ビット、8ビットの指数部、7ビットの小数部を持ちます。

本型は、現在のバックエンド固有の型（例： Cuda上の ``__half`` ）にマッピングされるか、そのような型が存在しない場合は、 ``float`` にマッピングされます。

マクロ ``KOKKOS_HALF_T_IS_FLOAT`` および ``KOKKOS_BHALF_T_IS_FLOAT`` は、 ``half_t`` および ``bhalf_t`` が ``float`` にマッピングされる場合は ``true`` に、それ以外の場合は ``false`` に設定されます。

関数
----

以下の表は、 ``half_t`` および ``bhalf_t`` 型で使用可能な標準数学関数を一覧表示します。

さらに、Cuda、SYCL、および HIP バックエンドでは、マークされた関数は特定の半精度関数を使用して実行されるため、より高いパフォーマンスを発揮する可能性があります。
特定の関数が存在しない場合のデフォルト動作は、半精度浮動小数点数を ``float`` にキャストし、標準関数で演算を実行した後、結果を半精度に再キャストすることです。

.. csv-table::
   :header: "Function", "``half_t`` Cuda", "``bhalf_t`` Cuda", "``half_t`` SYCL", "``bhalf_t`` SYCL", "``half_t`` HIP", "``bhalf_t`` HIP"
   :widths: auto

   "abs", "X", "X", "X", , "X", "X"
   "fabs","X", "X", "X", "X", "X", "X"
   "fmod", , , "X", 
   "remainder", , , "X", 
   "fmax","X¹", "X¹", "X", "X", "X", "X"
   "fmin","X¹", "X¹", "X", "X", "X", "X"
   "fdim", "X", "X", "X", , "X", "X"
   "exp", "X", "X", "X", "X", "X", "X"
   "exp2", "X", "X", "X", "X", "X", "X"
   "expm1", , , "X", 
   "log", "X", "X", "X", "X", "X", "X"
   "log10", "X", "X", "X", "X", "X", "X"
   "log2", "X", "X", "X", "X", "X", "X"
   "log1p", , , "X", 
   "pow", , , "X", 
   "sqrt", "X", "X", "X", "X", "X", "X"
   "cbrt", , , "X", 
   "hypot", , , "X", 
   "sin", "X", "X", "X", "X", "X", "X"
   "cos", "X", "X", "X", "X", "X", "X"
   "tan", , , "X", 
   "asin", , , "X", 
   "acos", , , "X", 
   "atan", , , "X", 
   "atan2", , , "X", 
   "sinh", , , "X", 
   "cosh", , , "X", 
   "tanh", , , "X", 
   "asinh", , , "X", 
   "acosh", , , "X", 
   "atanh", , , "X", 
   "erf", , , "X", 
   "erfc", , , "X", 
   "tgamma", , , "X", 
   "lgamma", , , "X", 
   "ceil", "X", "X", "X", "X", "X", "X"
   "floor", "X", "X", "X", "X", "X", "X"
   "trunc", "X", "X", "X", "X", "X", "X"
   "round", , , "X", 
   "nearbyint", "X", "X", , 
   "logb", , , "X", 
   "nextafter", "X²", "X²", "X", "X", "X", "X"
   "copysign", , , "X", 
   "isfinite", , , "X", 
   "isinf", "X³", "X³", "X", , "X", "X"
   "isnan", "X", "X", "X", "X", "X", "X"
   "signbit", , , "X", 

   "abs", "X", "X", "X", 
   "fabs","X", "X", "X", "X"
   "fmod", , , "X", 
   "remainder", , , "X", 
   "fmax","X¹", "X¹", "X", "X"
   "fmin","X¹", "X¹", "X", "X"
   "fdim", "X", "X", "X", 
   "exp", "X", "X", "X", "X"
   "exp2", "X", "X", "X", "X"
   "expm1", , , "X", 
   "log", "X", "X", "X", "X"
   "log10", "X", "X", "X", "X"
   "log2", "X", "X", "X", "X"
   "log1p", , , "X", 
   "pow", , , "X", 
   "sqrt", "X", "X", "X", "X"
   "cbrt", , , "X", 
   "hypot", , , "X", 
   "sin", "X", "X", "X", "X"
   "cos", "X", "X", "X", "X"
   "tan", , , "X", 
   "asin", , , "X", 
   "acos", , , "X", 
   "atan", , , "X", 
   "atan2", , , "X", 
   "sinh", , , "X", 
   "cosh", , , "X", 
   "tanh", , , "X", 
   "asinh", , , "X", 
   "acosh", , , "X", 
   "atanh", , , "X", 
   "erf", , , "X", 
   "erfc", , , "X", 
   "tgamma", , , "X", 
   "lgamma", , , "X", 
   "ceil", "X", "X", "X", "X"
   "floor", "X", "X", "X", "X"
   "trunc", "X", "X", "X", "X"
   "round", , , "X", 
   "nearbyint", "X", "X", , 
   "logb", , , "X", 
   "nextafter", , , "X", 
   "copysign", , , "X", 
   "isfinite", , , "X", 
   "isinf", "X²", "X²", "X", 
   "isnan", "X", "X", "X", "X"
   "signbit", , , "X", 

² MSVC ではサポートされていません

³ --std=c++20 でコンパイルする際、nvcc-12.2 に対しては適用されません (https://docs.nvidia.com/cuda/archive/12.3.2/cuda-toolkit-release-notes/index.html#cuda-math-release-12-3)

² --std=c++20 (https://docs.nvidia.com/cuda/archive/12.3.2/cuda-toolkit-release-notes/index.html#cuda-math-release-12-3) を使ってコンパイルする際、nvcc-12.2 に対して、ではありません。

例
~~
.. code-block:: cpp

    #include<Kokkos_Core.hpp>
    #include<iostream>

    int main(int argc, char* argv[]) {
        Kokkos::ScopeGuard guard(argc, argv);
        const int N = 10;

        using half_type = Kokkos::Experimental::bhalf_t;

        Kokkos::View<half_type*> view("half view", N);

        Kokkos::parallel_for("parallel region",
          N,
          KOKKOS_LAMBDA(const int i) {
            // 利用可能な場合は `bhalf` 型に対して、そうでない場合は `float` 型に対して指数関数を実行します。
            view (i) = Kokkos::exp(half_type(i));
          });
    }

数値的特性
----------

以下の標準数値特性は ``half_t`` および ``bhalf_t`` を使って、使用可能です:
 - infinity
 - finite_min
 - finite_max
 - epsilon
 - round_error
 - norm_min
 - quiet_NaN
 - signaling_NaN
 - digits
 - digits10
 - radix
 - min_exponent
 - max_exponent

例
~~
.. code-block:: cpp

    #include<Kokkos_Core.hpp>
    #include<iostream>

    int main(int argc, char* argv[]) {
        Kokkos::ScopeGuard guard(argc, argv);
