``MaxFirstLoc``
===============

.. role:: cpp(code)
    :language: cpp

条件を満たす最大値と最初のインデックスを格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装です。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使い方
------

.. code-block:: cpp

   MaxFirstLoc<T,I,S>::value_type result;
   parallel_reduce(N,Functor,MaxFirstLoc<T,I,S>(result));

概要
----

.. code-block:: cpp

   template<class Scalar, class Index, class Space>
   class MaxFirstLoc{
     public:
       using reducer = MaxFirstLoc;
       using value_type = ValLocScalar<typename std::remove_cv<Scalar>::type,
                               typename std::remove_cv<Index>::type>;
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
       MaxFirstLoc(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       MaxFirstLoc(const result_view_type& value_);
   };

インターフェイス
----------------

.. cpp:class:: template<class Scalar, class Index, class Space> MaxFirstLoc

   .. rubric:: パブリック型

   .. cpp:type:: reducer

      自身の型。

   .. cpp:type:: value_type

      リダクションのスカラー型（`ValLocScalar <ValLocScalar.html>`_ の特殊化）

   .. cpp:type:: result_view_type

      リダクション結果を参照する ``Kokkos::View``

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MaxFirstLoc(value_type& value_);

      結果の格納場所としてローカル変数を参照するリデューサーを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MaxFirstLoc(const result_view_type& value_);

      結果の格納場所として特定のビューを参照するリデューサーを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

      ``src`` と ``dest`` の最大値とその最初のインデックスを ``dest`` に格納します: ``dest = (src.val > dest.val) ? src :dest;``。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

      ``Kokkos::reduction_identity<Scalar>::max()`` メソッドを使用して ``val.val`` を初期化します。デフォルトの実装では ``val=<TYPE>_MIN`` を設定します。
      ``Kokkos::reduction_identity<Index>::min()`` メソッドを使用して ``val.loc`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` を設定します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスのコンストラクタで指定された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスのコンストラクタで指定された結果のビューを返します。

追加情報
^^^^^^^^

* ``MaxFirstLoc<T,I,S>::result_view_type`` は ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>`` です。S（メモリスペース）は、結果が存在するスペースと同じでなければならないことに注意してください。

* 要件: ``Scalar`` に ``operator =`` および ``operator >`` が定義されていること。``Kokkos::reduction_identity<Scalar>::max()`` が有効な式であること。

* 要件: ``Index`` に ``operator =`` が定義されていること。``Kokkos::reduction_identity<Index>::min()`` が有効な式であること。

* ``MaxFirstLoc`` を ``Scalar`` または ``Index`` のいずれかのカスタム型で使用するには、``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。詳細は `カスタムスカラー型を持つ組み込みリデューサー <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。