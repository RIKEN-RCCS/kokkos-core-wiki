ビット操作
================

.. role:: cpp(code)
    :language: cpp

.. role:: strike
    :class: strike

.. _KokkosBitManipulation: https://github.com/kokkos/kokkos/blob/4.1.00/core/src/Kokkos_BitManipulation.hpp

.. |KokkosBitManipulation| replace:: ``<Kokkos_BitManipulation.hpp>``

.. _StandardLibraryHeaderBit: https://en.cppreference.com/w/cpp/header/bit

.. |StandardLibraryHeaderBit| replace:: ``<bit>``

``<Kokkos_Core.hpp>`` に含まれる ヘッダー  |KokkosBitManipulation|_ に定義。

標準ライブラリヘッダー |StandardLibraryHeaderBit|_ から関数テンプレートを提供します( C++20 以降)。

Kokkos 4.1ビット演算関数テンプレートは、Kokkos 4.1以降、Kokkos:: 名前空間で定義されています。

.. _bit_cast: https://en.cppreference.com/w/cpp/numeric/bit_cast

.. |bit_cast| replace:: ``bit_cast``

.. _byteswap: https://en.cppreference.com/w/cpp/numeric/byteswap

.. |byteswap| replace:: ``byteswap``

.. _has_single_bit: https://en.cppreference.com/w/cpp/numeric/has_single_bit

.. |has_single_bit| replace:: ``has_single_bit``

.. _bit_ceil: https://en.cppreference.com/w/cpp/numeric/bit_ceil

.. |bit_ceil| replace:: ``bit_ceil``

.. _bit_floor: https://en.cppreference.com/w/cpp/numeric/bit_floor

.. |bit_floor| replace:: ``bit_floor``

.. _bit_width: https://en.cppreference.com/w/cpp/numeric/bit_width

.. |bit_width| replace:: ``bit_width``

.. _rotl: https://en.cppreference.com/w/cpp/numeric/rotl

.. |rotl| replace:: ``rotl``

.. _rotr: https://en.cppreference.com/w/cpp/numeric/rotr

.. |rotr| replace:: ``rotr``

.. _countl_zero: https://en.cppreference.com/w/cpp/numeric/countl_zero

.. |countl_zero| replace:: ``countl_zero``

.. _countl_one: https://en.cppreference.com/w/cpp/numeric/countl_one

.. |countl_one| replace:: ``countl_one``

.. _countr_zero: https://en.cppreference.com/w/cpp/numeric/countr_zero

.. |countr_zero| replace:: ``countr_zero``

.. _countr_one: https://en.cppreference.com/w/cpp/numeric/countr_one

.. |countr_one| replace:: ``countr_one``

.. _popcount: https://en.cppreference.com/w/cpp/numeric/popcount

.. |popcount| replace:: ``popcount``

================== ============================================================
|bit_cast|_        あるタイプのオブジェクト表現を別のタイプのものとして再解釈します (下記の注参照)
|byteswap|_        与えられた整数値のバイトを反転します 
|has_single_bit|_  数が2の整数乗であるかどうかを検証します 
|bit_ceil|_        与えられた値より小さい2の最小積分べき乗を求めます
|bit_floor|_       与えられた値より大きくない2の最大の積分冪を求めます
|bit_width|_       与えられた値を表現するために必要な最小ビット数を見つけます
|rotl|_            ビットごとに左回転した結果を計算します
|rotr|_            ビットごとに右回転した結果を計算します
|countl_zero|_     最上位ビットから連続した0ビットの数を数えます
|countl_one|_      最上位ビットから連続した1ビットの数を数えます
|countr_zero|_     連続した0ビットの数を、下位ビットから数えます
|countr_one|_      下位ビットから連続した1ビットの数を数えます
|popcount|_        符号なし整数の1ビット数を数えます
================== ============================================================

----

注意事項
--------

* 上記のテンプレート関数すべてに対して、 ``Kokkos::Experimental::namespace`` に ``*_builtin`` で終わる非 ``constexpr`` 対応関数が提供されており、定数式には現れないコンパイラの内在要素を補っています。
* C++ 標準ライブラリの対応するものとは異なり、 ``Kokkos::bit_cast`` は定数式 (``constexpr`` 関数ではありません) では使用できません。ライブラリ機能として実装できず、コンパイラの魔法を必要としますが、利用はできません。
