``AUTO``、``AUTO_t``
====================

ヘッダー ``<Kokkos_Core.hpp>`` で定義

使い方
------

.. code-block:: cpp

   Kokkos::TeamPolicy<>(league_size, Kokkos::AUTO);
   Kokkos::TeamPolicy<>(league_size, Kokkos::AUTO());


:cpp:var:`AUTO` は :doc:`TeamPolicy` の ``team_size`` 引数の代わりに使用されるタグであり、指定したファンクターと実行空間に対して適切なチームサイズを、起動時に Kokkos が決定できるようにします。

``Kokkos::AUTO`` と ``Kokkos::AUTO()`` の両方の構文がサポートされています。

インターフェース
----------------

.. cpp:struct:: AUTO_t

   Kokkos がチームサイズを自動的に選択するよう要求するために、:doc:`TeamPolicy` の ``team_size`` の代わりに渡されるタグ型。

   .. cpp:function:: KOKKOS_FUNCTION constexpr const AUTO_t& operator()() const;

      ``Kokkos::AUTO()`` 構文を有効にします。

      :returns: ``*this``


.. cpp:var:: inline constexpr AUTO_t AUTO{};

   :doc:`TeamPolicy` に対して自動的なチームサイズの選択を要求するために使用される :cpp:struct:`AUTO_t` の定数インスタンス。


例
--

.. code-block:: cpp

   // N 個のリーグに対して Kokkos にチームサイズを選ばせる
   Kokkos::parallel_for(Kokkos::TeamPolicy<>(N, Kokkos::AUTO),
     KOKKOS_LAMBDA(const Kokkos::TeamPolicy<>::member_type& team) {
       // ...
     });

   // 両方の構文が動作する
   Kokkos::TeamPolicy<> policy1(N, Kokkos::AUTO);
   Kokkos::TeamPolicy<> policy2(N, Kokkos::AUTO());

   // AUTO は明示的なベクトル長と組み合わせることができる
   Kokkos::TeamPolicy<> policy3(N, Kokkos::AUTO, /*vector_length=*/8);


関連項目
--------

.. seealso::

   :doc:`TeamPolicy`
      階層的（スレッドチーム）並列性のための実行ポリシー