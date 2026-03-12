数値特性
==============

.. ロール::cpp(code)
    :language: cpp

.. ロール:: ストライク
    :クラス: ストライク

.. _KokkosNumericTraits: https://github.com/kokkos/kokkos/blob/3.5.00/core/src/Kokkos_NumericTraits.hpp

.. |KokkosNumericTraits| 置換:: ``<Kokkos_NumericTraits.hpp>``

 ``<Kokkos_Core.hpp>``　に含まれる ヘッダー |KokkosNumericTraits|_　に定義。

.. _NumericLimits: https://en.cppreference.com/w/cpp/types/numeric_limits

.. |NumericLimits| 置換:: 標準ライブラリヘッダー ``<limits>``　からの ``numeric_limits``。

.. _P1841 : http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p1841r2.pdf

.. |P1841| 置換:: P1841

 |NumericLimits|_　の代替えを提供します。  C++23標準ライブラリに追加される新しい機能を実装し、モノリシックな ``numeric_limits`` クラステンプレートを個別のトレイトテンプレートに分割します。 詳細については、標準ライブラリヘッダー からの |P1841|_.numeric_limit　を参照してください。

数値特性は、Kokkos 3.5以降に、``Kokkos::Experimental`` namespace　で定義されています。

以下に利用可能な特性のリストを記載します。

------------

　Kokkos 3.6 に追加された``特性*`` を示しています。

:strike:`trait*` は、 Kokkos 4.0　において削除された特性を示しています。

**数値的顕著価値**
``infinity``
``finite_min``
``finite_max``
``epsilon``
``round_error``
``norm_min``
``denorm_min*``
:strike:`reciprocal_overflow_threshold*`
``quiet_NaN*``
``signaling_NaN*``

**数値的特徴トレイト**
``digits``
``digits10``
``max_digits10``
``radix``
``min_exponent``
``min_exponent10``
``max_exponent``
``max_exponent10``

------------

+---------------------------------------------------------+------------------------------------------------+
| 標準ライブラリ                                        | 　　C++17  を伴うKokkos                            |
+=========================================================+================================================+
| ``std::numeric_limits<Integral>::min()``                | ``finite_min_v<Integral>``                     |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::min()``           | ``norm_min_v<FloatingPoint>``                  |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<Arithmetic>::lowest()``           | ``finite_min_v<Arithmetic>``                   |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<Arithmetic>::max()``              | ``finite_max_v<Arithmetic>``                   |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::epsilon()``       | ``epsilon_v<FloatingPoint>``                   |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::round_error()``   | ``round_error_v<FloatingPoint>``               |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::infinity()``      | ``infinity_v<FloatingPoint>``                  |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::quiet_NaN()``     | ``quiet_NaN_v<FloatingPoint>`` (バージョン 3.6以降)     |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::signaling_NaN()`` | ``signaling_NaN_v<FloatingPoint>`` (バージョン 3.6以降) |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::denorm_min()``    | ``denorm_min_v<FloatingPoint>`` (バージョン　3.6以降)    |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<Arithmetic>::digits``             | ``digits_v<Arithmetic>``                       |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<Arithmetic>::digits10``           | ``digits10_v<Arithmetic>``                     |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::max_digits10``    | ``max_digits10_v<FloatingPoint>``              |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<Arithmetic>::radix``              | ``radix_v<Arithmetic>``                        |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::min_exponent``    | ``min_exponent_v<FloatingPoint>``              |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::min_exponent10``  | ``min_exponent10_v<FloatingPoint>``            |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::max_exponent``    | ``max_exponent_v<FloatingPoint>``              |
+---------------------------------------------------------+------------------------------------------------+
| ``std::numeric_limits<FloatingPoint>::max_exponent10``  | ``max_exponent10_v<FloatingPoint>``            |
+---------------------------------------------------------+------------------------------------------------+

個々の特性には、C++14　で使用できる値メンバー定数があります  (例:  ``epsilon<float>::value``)。

------------

個々の特性は、SFINAE　に配慮した、価値の存在/不在を検出できます。

.. code-block:: cpp

    テンプレート <class T>
    constexpr auto has_infinity(T)
            -> decltype(Kokkos::Experimental::infinity<T>::value, std::true_type{}) {
        return {};
    }

    constexpr std::false_type has_infinity(...) { return {}; }

    テンプレート <クラス T>
    KOKKOS_FUNCTION constexpr std::enable_if_t<has_infinity(T{}), T>
    legacy_std_numeric_limits_infinity() {
        return Kokkos::Experimental::infinity<T>::value;
    }

    テンプレート <class T>
    KOKKOS_FUNCTION constexpr std::enable_if_t<!has_infinity(T{}), T>
    legacy_std_numeric_limits_infinity() {
        返し T();
    }

------------

**以下も参照**

.. _MathematicalConstants : mathematical-constants.html

.. |MathematicalConstants| replace:: Mathematical constants

.. _CommonMathematicalFunctions : mathematical-functions.html 

.. |CommonMathematicalFunctions| 置換:: 一般数学関数

|MathematicalConstants|_

|CommonMathematicalFunctions|_
