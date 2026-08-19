``ALL``, ``ALL_t``
==================

ヘッダー ``<Kokkos_Core.hpp>`` で定義

使い方
------

.. code-block:: cpp

   Kokkos::subview(v, i, Kokkos::ALL);
   Kokkos::subview(v, i, Kokkos::ALL());


:cpp:var:`ALL` は、次元に沿ったすべての要素を選択するために :cpp:func:`subview` とともに使用されるスライス指定子です。

``Kokkos::ALL`` と ``Kokkos::ALL()`` の両方の構文がサポートされています。

インターフェイス
----------------

.. cpp:struct:: ALL_t
   
   次元内のインデックスの全範囲を示すために :cpp:func:`subview` とともに使用できるスライス指定子型です。

   .. cpp:function:: KOKKOS_FUNCTION constexpr const ALL_t& operator()() const;
   
      ``Kokkos::ALL()`` 構文を有効にします。

      :returns: ``*this``

   .. cpp:function:: KOKKOS_FUNCTION constexpr bool operator==(const ALL_t&) const;
      
      等価比較演算子です。

      :returns: ``true``

      

.. cpp:var:: inline constexpr ALL_t ALL{};
   
   次元内のすべてのインデックスを選択するために使用される :cpp:struct:`ALL_t` の定数インスタンスです。

例
--

.. code-block:: cpp

   Kokkos::View<double**[5]> a("A", N0, N1);

   // 次元 1 と 2 のすべての要素を選択し、次元 0 をインデックス 5 に固定する
   auto s = Kokkos::subview(a, 5, Kokkos::ALL, Kokkos::ALL);
   // 結果: s は次元 (N1, 5) を持つ View<double[5]> 型になる

   // どちらの構文も動作する
   auto s1 = Kokkos::subview(a, 5, Kokkos::ALL,   Kokkos::ALL);
   auto s2 = Kokkos::subview(a, 5, Kokkos::ALL(), Kokkos::ALL());

関連項目
--------

.. seealso::

   :doc:`../view/subview`
      ビューのサブビューを作成する

   :doc:`../stl-compat/pair`
      連続したインデックスの範囲を指定する