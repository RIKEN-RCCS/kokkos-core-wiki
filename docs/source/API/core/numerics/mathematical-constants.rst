数学定数
======================

.. role::cpp(code)
    :language: cpp

.. _text: https://github.com/kokkos/kokkos/blob/develop/core/src/Kokkos_MathematicalConstants.hpp

.. |text| replace:: ``<Kokkos_MathematicalConstants.hpp>``

ヘッダー |text|_　に定義。
 ``<Kokkos_Core.hpp>``　に含まれます。

.. _text2: https://en.cppreference.com/w/cpp/numeric/constants

.. |text2| 置換:: ``<numbers>``

 |text2|_ ( C++20　以降)　からのすべての数学定数を提供します。

すべての定数は  バージョン4.0以降の　Kokkos::numbers:: namespace　で定義されており、以前のバージョンでは、　Kokkos::Experimental　で定義されています。

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
-----

.. _KnownIssues: ../../../known-issues.html#mathematical-constants

.. |KnownIssues| 置換:: known issues

* The mathematical constants are available in ``Kokkos::Experimental::`` since Kokkos 3.6
* They were "promoted" to the ``Kokkos::numbers`` namespace in 4.0 and removed from ``Kokkos::Experimental::`` in 4.3
* Passing mathematical constants by reference or taking their address in device code is not supported by some toolchains and hence not portable.  (See |KnownIssues|_)
* Support for quadruple precision floating-point ``__float128`` can be enabled
  via ``-DKokkos_ENABLE_LIBQUADMATH=ON``.

------------

例
-------

.. code-block:: cpp

    KOKKOS_FUNCTION void example() {
        constexpr auto pi = Kokkos::numbers::pi_v<float>;
        auto const x = Kokkos::sin(pi/6);
    }

------------

See also
--------

`Common mathematical functions <mathematical-functions.html>`_

`Numeric traits <numeric-traits.html>`_
