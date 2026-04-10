``MDRangePolicy``
=================

.. ロール:: cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

    Kokkos::MDRangePolicy<..., Rank<N>, ...>(開始, 終了)
    Kokkos::MDRangePolicy<..., Rank<N>, ...>(空間, 開始, 終了)
    Kokkos::MDRangePolicy<..., Rank<N>, ...>(開始, 終了, タイリング)
    Kokkos::MDRangePolicy<..., Rank<N>, ...>(空間, 開始, 終了, タイリング)

 ``MDRangePolicy`` は、 ``開始`` タプルから開区間で ``終わる`` 多次元反復空間の実行ポリシーを定義しています。反復空間はタイルされ、ユーザーはオプションでタイルサイズを設定できます。

インターフェイス
---------

.. code-block:: cpp

    template<class ... Args>
    class Kokkos::MDRangePolicy;

パラメータ
----------

汎用テンプレート引数
~~~~~~~~~~~~~~~~~~~~~~~~~~

 ``MDRangePolicy``の有効なテンプレート引数はここ <../Execution-Policies.html#common-arguments-for-all-execution-policies>`_ に説明されています。


 MDRangePolicy に特有の必要論拠
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

    template<int N,
             Kokkos::Iterate outer = Kokkos::Iterate::Default,
             Kokkos::Iterate inner = Kokkos::Iterate::Default>
    class Kokkos::Rank;

* インデックス空間のランクや、タイルをどの順序で反復するか、またタイル内でどのように反復するかを決定します。 外側と内側は``outer`` および ``inner`` は、``Kokkos::Iterate::Default``、 ``Kokkos::Iterate::Left``、または``Kokkos::Iterate::Right`` である可能性があります。


パブリッククラスメンバー
--------------------

コンストラクタ
~~~~~~~~~~~~

.. cpp:function:: MDRangePolicy()

    * デフォルトのコンストラクタの初期化されていないポリシー。

.. cpp:function:: MDRangePolicy(const Kokkos::Array<int64_t,rank>& begin, const Kokkos::Array<int64_t,rank>& end)

    * 開始および終了のインデックスを提供します。

.. cpp:function:: MDRangePolicy(const Kokkos::Array<int64_t,rank>& begin, const Kokkos::Array<int64_t,rank>& end,  const Kokkos::Array<int64_t,rank>& tiling)

    * タイル次元同様に、開始と終了のインデックスを提供します。

.. cpp:function:: template<class OT, class IT, class TT> MDRangePolicy(const std::initializer_list<OT>& begin, const std::initializer_list<IT>& end)

    * 開始および終了のインデックスを提供します。 リストの長さは、ポリシーのランクに一致しなければなりません。

.. cpp:function:: template<class OT, class IT, class TT> MDRangePolicy(const std::initializer_list<OT>& begin, const std::initializer_list<IT>& end,  std::initializer_list<TT>& tiling)

    * タイル次元同様に、開始と終了のインデックスを提供します。 リストの長さは、ポリシーのランクに一致しなければなりません。

CTAD コンストラクタ ( 4.3以降)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cpp

   DefaultExecutionSpace des;
   SomeExecutionSpace ses; // DefaultExecutionSpace とは異なります

   // MDRangePolicy<Rank<3>> に演繹します
   MDRangePolicy pl0({0, 0, 0}, {4, 5, 10}};
   MDRangePolicy pl1({0, 0, 0}, {4, 5, 10}, {3, 3, 3}};

   // MDRangePolicy<SomeExecutionSpace, Rank<3>> に演繹します
   MDRangePolicy pl4(ses, {0, 0, 0}, {4, 5, 10}};
   MDRangePolicy pl5(ses, {0, 0, 0}, {4, 5, 10}, {3, 3, 3}};

   int cbegin[3];
   int cend[3];
   int64_t ctiling[3];

   // MDRangePolicy<Rank<3>> に演繹します
   MDRangePolicy pc0(cbegin, cend);
   MDRangePolicy pc1(cbegin, cend, ctiling);
   MDRangePolicy pc2(des, cbegin, cend);
   MDRangePolicy pc3(des, cbegin, cend, ctiling);

   // MDRangePolicy<SomeExecutionSpace, Rank<3>> に演繹します
   MDRangePolicy pc4(ses, cbegin, cend);
   MDRangePolicy pc5(ses, cbegin, cend, ctiling);

   Array<int, 2> abegin;
   Array<int, 2> aend;
   Array<int, 2> atiling;

   // MDRangePolicy<Rank<2>> に演繹します
   MDRangePolicy pa0(abegin, aend);
   MDRangePolicy pa1(abegin, aend, atiling);
   MDRangePolicy pa2(des, abegin, aend);
   MDRangePolicy pa3(des, abegin, aend, atiling);

   // MDRangePolicy<SomeExecutionSpace, Rank<2>> に演繹します
   MDRangePolicy pa4(ses, abegin, aend);
   MDRangePolicy pa5(ses, abegin, aend, atiling);

メンバー関数
^^^^^^^^^^^^^^^^
.. cpp:function:: tile_type tile_size_recommended() const

    * ``Kokkos::Array<array_index_type, rank>`` 型を返します。これは、 ``MDRangePolicy`` が内部でデフォルトで使うランクごとのタイルサイズを含みます。デフォルトのタイルサイズは静的で、指定されたバックエンドに基づいて設定されています。

    .. 注意事項:: ``tile_size_recommended()`` は、 Kokkos 4.5以降利用可能です。

.. cpp:function:: int max_total_tile_size() const

    * すべてのタイルサイズの積の上限を表す値を返します。

    .. 注意事項:: ``max_total_tile_size()`` は、 Kokkos 4.5以降利用可能です。

注意事項
^^^^^

* すべてのランクで、開始インデックスが一致する終了インデックスより大きくあってはいけません。
* 開始と終了の配列ランクは一致しなければなりません。
* タイル配列のランクは、開始/終了配列のランクより、小さくなければなりません。

例
--------

.. code-block:: cpp

    MDRangePolicy<Rank<3>> policy_1({0,0,0},{N0,N1,N2});
    MDRangePolicy<Cuda,Rank<3,Iterate::Right,Iterate::Left>> policy_2({5,5,5},{N0-5,N1-5,N2-5},{T0,T1,T2});
