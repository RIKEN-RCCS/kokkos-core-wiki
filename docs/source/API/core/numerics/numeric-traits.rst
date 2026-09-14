数値特性
========

.. role:: cpp(code)
    :language: cpp

.. _source_numeric_traits: https://github.com/kokkos/kokkos/blob/5.2.0/core/src/Kokkos_NumericTraits.hpp

.. |source_numeric_traits| replace:: ``<Kokkos_NumericTraits.hpp>``

``<Kokkos_Core.hpp>`` からインクルードされるヘッダー |source_numeric_traits|_ に定義されています。

.. note::
   数値トレイトは、`P2551
   <https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2551r2.pdf>`__
   でなされた明確化に従い、`P1841
   <http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p1841r2.pdf>`__
   において当初 C++ 標準ライブラリ向けに提案された機能を実装しています。
   いずれの提案も C++ 標準には採用されておらず、現時点で切り替え可能な標準ライブラリの
   同等物は存在しません。``Kokkos`` namespace のトレイトは、``std::numeric_limits``
   が使用できない可能性のあるデバイスコードでの使用を意図しています。

使い方
------

.. code-block:: cpp

   constexpr auto inf = Kokkos::infinity<float>::value;
   auto x = Kokkos::finite_min_v<float>;

.. _cpp_reference_numeric_limits: https://en.cppreference.com/w/cpp/types/numeric_limits

.. |cpp_reference_numeric_limits| replace:: ``std::numeric_limits``

標準ライブラリヘッダー ``<limits>`` の |cpp_reference_numeric_limits|_ の代替を提供します。これはデバイスコードでも動作し、モノリシックな ``numeric_limits`` クラステンプレートを個別のトレイトテンプレートに分割します。

数値トレイトは、Kokkos 5.2 以降は ``Kokkos`` namespace で、それ以前のバージョンでは ``Kokkos::Experimental`` namespace で定義されています。

個々のトレイト
--------------
以下のトレイトは、静的な constexpr の ``value`` メンバーを持つクラステンプレートです。
各トレイトは、それが意味を持つ引数型に対してのみ定義されます (以下の表における `floating-point` または `arithmetic`)。

数値的な特別な値のトレイト
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :align: left
   :header-rows: 1

   * - トレイト名
     - 説明
     - 有効な型
   * - ``infinity``
     - 正の無限大を表す値
     - floating-point 型
   * - ``finite_min``
     - 最小の有限値
     - arithmetic 型
   * - ``finite_max``
     - 最大の有限値
     - arithmetic 型
   * - ``epsilon``
     - 1 と、1 より大きい次に表現可能な値との差
     - floating-point 型
   * - ``round_error``
     - 最大の丸め誤差
     - floating-point 型
   * - ``norm_min``
     - 最小の正の正規化値
     - floating-point 型
   * - ``denorm_min``
     - 最小の正の非正規化値。非正規化数がサポートされていない場合は
       最小の正の正規化値
     - floating-point 型
   * - ``quiet_NaN``
     - quiet (非シグナリング) NaN 値
     - floating-point 型
   * - ``signaling_NaN``
     - シグナリング NaN 値
     - floating-point 型

数値的特徴のトレイト
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :align: left
   :header-rows: 1

   * - トレイト名
     - 説明
     - 有効な型
   * - ``digits``
     - 変化なく表現できる基数の桁数
     - arithmetic 型
   * - ``digits10``
     - 変化なく表現できる 10 進数の桁数
     - arithmetic 型
   * - ``max_digits10``
     - すべての異なる値を表現するために必要な 10 進数の桁数
     - floating-point 型
   * - ``radix``
     - 表現に使用される底 (基数)
     - arithmetic 型
   * - ``min_exponent``
     - ``radix`` をその冪乗した値が正規化値となるような、最小の負の指数
     - floating-point 型
   * - ``min_exponent10``
     - 10 をその冪乗した値が正規化値となるような、最小の負の指数
     - floating-point 型
   * - ``max_exponent``
     - ``radix`` をその冪乗した値が表現可能な有限値となるような、最大の正の指数
     - floating-point 型
   * - ``max_exponent10``
     - 10 をその冪乗した値が表現可能な有限値となるような、最大の正の指数
     - floating-point 型

変数テンプレート
----------------
上記の各トレイトに対して、Kokkos は ``_v`` サフィックスを持つ変数テンプレートを提供します。これらはトレイトの ``value`` メンバーの短縮形です。

* ``Kokkos::epsilon_v<T>`` は ``Kokkos::epsilon<T>::value`` と等価です
* ``Kokkos::infinity_v<T>`` は ``Kokkos::infinity<T>::value`` と等価です

標準ライブラリとの対応
----------------------
各トレイトは、|cpp_reference_numeric_limits|_ の対応するメンバーを反映しています。

.. _numlim_infinity: https://en.cppreference.com/w/cpp/types/numeric_limits/infinity
.. _numlim_lowest: https://en.cppreference.com/w/cpp/types/numeric_limits/lowest
.. _numlim_max: https://en.cppreference.com/w/cpp/types/numeric_limits/max
.. _numlim_epsilon: https://en.cppreference.com/w/cpp/types/numeric_limits/epsilon
.. _numlim_round_error: https://en.cppreference.com/w/cpp/types/numeric_limits/round_error
.. _numlim_min: https://en.cppreference.com/w/cpp/types/numeric_limits/min
.. _numlim_denorm_min: https://en.cppreference.com/w/cpp/types/numeric_limits/denorm_min
.. _numlim_quiet_NaN: https://en.cppreference.com/w/cpp/types/numeric_limits/quiet_NaN
.. _numlim_signaling_NaN: https://en.cppreference.com/w/cpp/types/numeric_limits/signaling_NaN
.. _numlim_digits: https://en.cppreference.com/w/cpp/types/numeric_limits/digits
.. _numlim_digits10: https://en.cppreference.com/w/cpp/types/numeric_limits/digits10
.. _numlim_max_digits10: https://en.cppreference.com/w/cpp/types/numeric_limits/max_digits10
.. _numlim_radix: https://en.cppreference.com/w/cpp/types/numeric_limits/radix
.. _numlim_min_exponent: https://en.cppreference.com/w/cpp/types/numeric_limits/min_exponent
.. _numlim_min_exponent10: https://en.cppreference.com/w/cpp/types/numeric_limits/min_exponent10
.. _numlim_max_exponent: https://en.cppreference.com/w/cpp/types/numeric_limits/max_exponent
.. _numlim_max_exponent10: https://en.cppreference.com/w/cpp/types/numeric_limits/max_exponent10

.. |numlim_infinity| replace:: ``std::numeric_limits<FloatingPoint>::infinity()``
.. |numlim_lowest| replace:: ``std::numeric_limits<Arithmetic>::lowest()``
.. |numlim_max| replace:: ``std::numeric_limits<Arithmetic>::max()``
.. |numlim_epsilon| replace:: ``std::numeric_limits<FloatingPoint>::epsilon()``
.. |numlim_round_error| replace:: ``std::numeric_limits<FloatingPoint>::round_error()``
.. |numlim_min| replace:: ``std::numeric_limits<FloatingPoint>::min()``
.. |numlim_denorm_min| replace:: ``std::numeric_limits<FloatingPoint>::denorm_min()``
.. |numlim_quiet_NaN| replace:: ``std::numeric_limits<FloatingPoint>::quiet_NaN()``
.. |numlim_signaling_NaN| replace:: ``std::numeric_limits<FloatingPoint>::signaling_NaN()``
.. |numlim_digits| replace:: ``std::numeric_limits<Arithmetic>::digits``
.. |numlim_digits10| replace:: ``std::numeric_limits<Arithmetic>::digits10``
.. |numlim_max_digits10| replace:: ``std::numeric_limits<FloatingPoint>::max_digits10``
.. |numlim_radix| replace:: ``std::numeric_limits<Arithmetic>::radix``
.. |numlim_min_exponent| replace:: ``std::numeric_limits<FloatingPoint>::min_exponent``
.. |numlim_min_exponent10| replace:: ``std::numeric_limits<FloatingPoint>::min_exponent10``
.. |numlim_max_exponent| replace:: ``std::numeric_limits<FloatingPoint>::max_exponent``
.. |numlim_max_exponent10| replace:: ``std::numeric_limits<FloatingPoint>::max_exponent10``

.. list-table::
   :align: left
   :header-rows: 1

   * - トレイト名
     - 等価物
   * - ``infinity``
     - |numlim_infinity|_
   * - ``finite_min``
     - |numlim_lowest|_
   * - ``finite_max``
     - |numlim_max|_
   * - ``epsilon``
     - |numlim_epsilon|_
   * - ``round_error``
     - |numlim_round_error|_
   * - ``norm_min``
     - |numlim_min|_
   * - ``denorm_min``
     - |numlim_denorm_min|_
   * - ``quiet_NaN``
     - |numlim_quiet_NaN|_
   * - ``signaling_NaN``
     - |numlim_signaling_NaN|_
   * - ``digits``
     - |numlim_digits|_
   * - ``digits10``
     - |numlim_digits10|_
   * - ``max_digits10``
     - |numlim_max_digits10|_
   * - ``radix``
     - |numlim_radix|_
   * - ``min_exponent``
     - |numlim_min_exponent|_
   * - ``min_exponent10``
     - |numlim_min_exponent10|_
   * - ``max_exponent``
     - |numlim_max_exponent|_
   * - ``max_exponent10``
     - |numlim_max_exponent10|_

.. note::
   ``Arithmetic`` は任意の整数型または浮動小数点型 (すなわち ``std::is_arithmetic_v``
   が ``true`` となる任意の型) を表し、``FloatingPoint`` は任意の浮動小数点型
   (すなわち ``std::is_floating_point_v`` が ``true`` となる任意の型) を表します。
   これらは上記の表の「有効な型」列に対応します。Kokkos のトレイトはそれらの型に対して
   のみ特殊化されています。これは |cpp_reference_numeric_limits|_ との意図的な違いです。
   後者はあらゆる型に対して定義されており、意図された領域外では無意味な値を暗黙のうちに
   返します (例: ``std::numeric_limits<int>::infinity()`` は ``0`` を返す)。これは
   Kokkos のトレイトが回避するよう設計されているバグの原因です。

------------

補足
----

.. _KnownIssues: ../../../known-issues.html#mathematical-constants-and-numeric-traits

.. |KnownIssues| replace:: known issues

.. important::
   **移植性:** デバイスコードで数値トレイトを参照渡ししたり、そのアドレスを取得したり
   することは、一部のツールチェーンではサポートされていないため、移植性がありません。
   (|KnownIssues|_ を参照)

.. note::
   **特殊化の検出:** 各トレイトはその「有効な型」列に列挙された型に対してのみ特殊化
   されているため、汎用コードは |cpp_reference_numeric_limits|_ のように暗黙のうちに
   無意味な値にフォールバックするのではなく、使用する前に指定された型に対して特殊化が
   存在するかどうかを検出できます。

   数値トレイトが Kokkos に最初に導入されたときに要求された最小の標準である C++14 では、
   この検出はトレイトの ``value`` メンバーに対する式 SFINAE の形をとります。例:

   .. code-block:: cpp

       template <class T>
       constexpr auto has_infinity(T)
               -> decltype(Kokkos::infinity<T>::value, std::true_type{}) {
           return {};
       }

       constexpr std::false_type has_infinity(...) { return {}; }

   以下の例のセクションでは、``has_infinity`` をベースに、
   ``std::numeric_limits<T>::infinity()`` のデバイス互換の代替を実装します。

   C++20 では、``requires`` 節と ``if constexpr`` を組み合わせることで、別途検出関数を
   必要とせずに、より直接的な代替手段が得られます。

------------

例
--

.. code-block:: cpp

    template <class T>
    KOKKOS_FUNCTION constexpr std::enable_if_t<has_infinity(T{}), T>
    legacy_std_numeric_limits_infinity() {
        return Kokkos::infinity<T>::value;
    }

    template <class T>
    KOKKOS_FUNCTION constexpr std::enable_if_t<!has_infinity(T{}), T>
    legacy_std_numeric_limits_infinity() {
        return T();
    }

C++20 の場合:

.. code-block:: cpp

    template <class T>
    KOKKOS_FUNCTION constexpr T legacy_std_numeric_limits_infinity() {
        if constexpr (requires { Kokkos::infinity<T>::value; }) {
            return Kokkos::infinity_v<T>;
        } else {
            return T();
        }
    }

------------

関連項目
--------

.. seealso::
   `Mathematical constants <mathematical-constants.html>`_

   `Common mathematical functions <mathematical-functions.html>`_
