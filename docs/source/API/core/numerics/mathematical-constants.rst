数学定数
======================

.. role:: cpp(code)
    :language: cpp

.. _text: https://github.com/kokkos/kokkos/blob/develop/core/src/Kokkos_MathematicalConstants.hpp

.. |text| replace:: ``<Kokkos_MathematicalConstants.hpp>``

ヘッダー |text|_ に定義。``<Kokkos_Core.hpp>`` に含まれます。

.. _text2: https://en.cppreference.com/w/cpp/numeric/constants

.. |text2| replace:: ``<numbers>``

|text2|_ ( C++20 以降) からのすべての数学定数を提供します。

すべての定数は  バージョン4.0以降の Kokkos::numbers:: namespace で定義されており、以前のバージョンでは、 Kokkos::Experimental で定義されています。

**数学定数**

``e``
``log2e``
``log10e``
``pi``
``inv_pi``
``inv_sqrtpi``
``ln2``
``ln10``
``sqrt2``
``sqrt3``
``inv_sqrt3``
``egamma``
``phi``

------------

注意事項
--------

.. _KnownIssues: ../../../known-issues.html#mathematical-constants

.. |KnownIssues| replace:: 既知の問題

* 	数学定数は ``Kokkos::Experimental::`` において、Kokkos 3.6以降利用可能です。
* 	4.0では``Kokkos::numbers`` namespace に「昇格」し、4.3では、 ``Kokkos::Experimental::`` から削除されています。
*  数学定数を参照で渡す、またはデバイスコード内でアドレスを取得することは、一部のツールチェーンではサポートされておらず、したがって移植性がありません。 (参照 |KnownIssues|_)。
*  四重精密浮動小数点 ``__float128`` のサポートは、-DKokkos_ENABLE_LIBQUADMATH=ON により、有効化できます。

------------

例
-------

.. code-block:: cpp

    KOKKOS_FUNCTION void example() {
        constexpr auto pi = Kokkos::numbers::pi_v<float>;
        auto const x = Kokkos::sin(pi/6);
    }

------------

以下も参照
----------

`一般数学関数 <mathematical-functions.html>`_

`数値特性 <numeric-traits.html>`_
