数学定数
========

.. role:: cpp(code)
    :language: cpp

.. _source_math_constants: https://github.com/kokkos/kokkos/blob/develop/core/src/Kokkos_MathematicalConstants.hpp

.. |source_math_constants| replace:: ``<Kokkos_MathematicalConstants.hpp>``

ヘッダー |source_math_constants|_ に定義されており、``<Kokkos_Core.hpp>`` からインクルードされます。

.. attention::
   **推奨事項:** Kokkos 5.X は C++20 を必要とするため、ユーザーは標準ライブラリの定数
   (``std::numbers::*``) を直接使用することが推奨されます。``Kokkos::numbers``
   namespace は後方互換性のために維持されており、標準ライブラリの定数の `using 宣言
   <https://en.cppreference.com/w/cpp/language/namespace.html#Using-declarations>`__
   を介して実装されています。

使用法
------

.. code-block:: cpp

   auto const x = Kokkos::numbers::pi_v<float>;
   auto const y = Kokkos::numbers::sqrt2_v<float>;

.. _cpp_reference_numbers: https://en.cppreference.com/w/cpp/numeric/constants

.. |cpp_reference_numbers| replace:: ``<numbers>``

標準ライブラリの C++20 |cpp_reference_numbers|_ ヘッダーで定義されている数学定数へのアクセスを提供します。

すべての定数は ``Kokkos::numbers::`` namespace で定義されています。

変数テンプレート
----------------
以下は、標準の浮動小数点型 (``float``、``double``、``long double``) に対して定義された変数テンプレートです。

.. list-table::
   :align: left
   :header-rows: 1

   * - テンプレート名
     - 数学記号
     - 説明
   * - ``e_v``
     - :math:`e`
     - 自然対数の底
   * - ``log2e_v``
     - :math:`\log_{2}{e}`
     - e の底 2 の対数
   * - ``log10e_v``
     - :math:`\log_{10}{e}`
     - e の底 10 の対数
   * - ``pi_v``
     - :math:`\pi`
     - 円周の直径に対する比
   * - ``inv_pi_v``
     - :math:`\frac{1}{\pi}`
     - pi の逆数
   * - ``inv_sqrtpi_v``
     - :math:`\frac{1}{\sqrt{\pi}}`
     - pi の平方根の逆数
   * - ``ln2_v``
     - :math:`\ln{2}`
     - 2 の自然対数
   * - ``ln10_v``
     - :math:`\ln{10}`
     - 10 の自然対数
   * - ``sqrt2_v``
     - :math:`\sqrt{2}`
     - 2 の平方根
   * - ``sqrt3_v``
     - :math:`\sqrt{3}`
     - 3 の平方根
   * - ``inv_sqrt3_v``
     - :math:`\frac{1}{\sqrt{3}}`
     - 3 の平方根の逆数
   * - ``egamma_v``
     - :math:`\gamma`
     - オイラー・マスケローニ定数
   * - ``phi_v``
     - :math:`\varphi`
     - 黄金比定数 :math:`\frac{1+\sqrt{5}}{2}`

利便性のための定数 (``double``)
-------------------------------
上記に列挙された各変数テンプレートについて、Kokkos は ``_v`` サフィックスのない
``inline constexpr double`` 定数を提供します。これらは ``double`` 特殊化の省略形です。

* ``Kokkos::numbers::pi`` は ``Kokkos::numbers::pi_v<double>`` と等価です
* ``Kokkos::numbers::e`` は ``Kokkos::numbers::e_v<double>`` と等価です

------------

注意事項
--------

.. _KnownIssues: ../../../known-issues.html#mathematical-constants

.. |KnownIssues| replace:: 既知の問題

.. important::
   **移植性:** 数学定数を参照で渡すこと、またはデバイスコード内でそのアドレスを取得することは、
   一部のツールチェーンではサポートされておらず、したがって移植性がありません。 (|KnownIssues|_ を参照)

.. note::
   **四倍精度:** 四倍精度浮動小数点 ``__float128`` のサポートは、``-DKokkos_ENABLE_LIBQUADMATH=ON``
   により有効化できます。

------------

例
--

.. code-block:: cpp

    KOKKOS_FUNCTION void example() {
        // 推奨される C++20 の使用法
        constexpr auto pi_f = std::numbers::pi_v<float>;
        
        // Kokkos namespace の使用法 (後方互換性)
        constexpr auto pi = Kokkos::numbers::pi_v<float>;

        auto const x = Kokkos::sin(pi_f / 6);
    }

------------

以下も参照
----------

.. seealso::
   `一般数学関数 <mathematical-functions.html>`_
   
   `数値特性 <numeric-traits.html>`_
