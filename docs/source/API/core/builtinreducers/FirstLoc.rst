``FirstLoc``
============

.. role:: cpp(code)
    :language: cpp

条件を満たす最初のインデックスを格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装です。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使い方
------

.. code-block:: cpp

   FirstLoc<I,S>::value_type result;
   parallel_reduce(N,Functor,FirstLoc<I,S>(result));

概要
----

.. code-block:: cpp

   template<class Index, class Space>
   class FirstLoc{
     public:
       using reducer = FirstLoc;
       using value_type = FirstLocScalar<typename std::remove_cv<Index>::type>;
       using result_view_type = Kokkos::View<value_type, Space>;

       KOKKOS_INLINE_FUNCTION
       void join(value_type& dest, const value_type& src) const;

       KOKKOS_INLINE_FUNCTION
       void init(value_type& val) const;

       KOKKOS_INLINE_FUNCTION
       value_type& reference() const;

       KOKKOS_INLINE_FUNCTION
       result_view_type view() const;

       KOKKOS_INLINE_FUNCTION
       FirstLoc(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       FirstLoc(const result_view_type& value_);
   };

インターフェース
----------------

.. cpp:class:: template<class Index, class Space> FirstLoc

   .. rubric:: パブリック型

   .. cpp:type:: reducer

      自身の型です。

   .. cpp:type:: value_type

      リダクションのスカラー型です（ `FirstLocScalar <FirstLocScalar.html>`_ の特殊化）。

   .. cpp:type:: result_view_type

      リダクション結果を参照する ``Kokkos::View`` です。

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION FirstLoc(value_type& value_);

      結果の格納場所としてローカル変数を参照するリデューサーを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION FirstLoc(const result_view_type& value_);

      結果の格納場所として特定のビューを参照するリデューサーを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

      ``src`` と ``dest`` の最初のインデックスの最大値を ``dest`` に格納します: ``dest = (src.min_loc_true < dest.min_loc_true) ? src :dest;`` 。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

      ``Kokkos::reduction_identity<Index>::min()`` メソッドを使用して ``val.min_loc_true`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` に設定します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスコンストラクタで提供された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスコンストラクタで提供された結果のビューを返します。

追加情報
^^^^^^^^

* ``FirstLoc<I,S>::result_view_type`` は ``Kokkos::View<I,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>`` です。S（メモリ空間）は結果が存在する空間と同じでなければならないことに注意してください。

* 必要条件: ``Index`` に ``operator =`` が定義されていること。``Kokkos::reduction_identity<Index>::min()`` が有効な式であること。

* ``FirstLoc`` をカスタム型の ``Index`` で使用するには、``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。詳細については `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。