``MinMaxFirstLastLoc``
======================

.. role:: cpp(code)
    :language: cpp

最小値と最大値の両方を、対応する最初と最後のインデックスとともに格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装です。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使い方
------

.. code-block:: cpp

   MinMaxFirstLastLoc<T,I,S>::value_type result;
   parallel_reduce(N,Functor,MinMaxFirstLastLoc<T,I,S>(result));

概要
----

.. code-block:: cpp

   template<class Scalar, class Index, class Space>
   class MinMaxFirstLastLoc {
     public:
       using reducer = MinMaxFirstLastLoc;
       using value_type = MinMaxFirstLastLocScalar<typename std::remove_cv<Scalar>::type,
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
       MinMaxFirstLastLoc(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       MinMaxFirstLastLoc(const result_view_type& value_);
   };

インターフェース
----------------

.. cpp:class:: template<class Scalar, class Index, class Space> MinMaxFirstLastLoc

   .. rubric:: パブリック型

   .. cpp:type:: reducer

      自身の型

   .. cpp:type:: value_type

      リダクションのスカラー型（`MinMaxLocScalar <MinMaxLocScalar.html>`_ の特殊化）

   .. cpp:type:: result_view_type

      リダクション結果を参照する ``Kokkos::View``

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MinMaxFirstLastLoc(value_type& value_);

      結果の格納場所としてローカル変数を参照するリデューサーを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MinMaxFirstLastLoc(const result_view_type& value_);

      結果の格納場所として特定のビューを参照するリデューサーを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

      ``src`` と ``dest`` の最小値とその最初の位置を ``dest`` に格納します。
      ``src`` と ``dest`` の最大値とその最後の位置を ``dest`` に格納します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init( value_type& val) const;

      ``Kokkos::reduction_identity<Scalar>::min()`` メソッドを使用して ``val.min_val`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` に設定されます。

      ``Kokkos::reduction_identity<Index>::max()`` メソッドを使用して ``val.max_val`` を初期化します。デフォルトの実装では ``val=<TYPE>_MIN`` に設定されます。

      ``Kokkos::reduction_identity<Scalar>::min()`` メソッドを使用して ``val.min_loc`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` に設定されます。

      ``Kokkos::reduction_identity<Index>::max()`` メソッドを使用して ``val.max_loc`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` に設定されます。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスのコンストラクタで提供された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスのコンストラクタで提供された結果のビューを返します。

追加情報
^^^^^^^^

* ``MinMaxFirstLastLoc<T,I,S>::result_view_type`` は ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>`` です。S（メモリ空間）は結果が存在する空間と同じでなければならないことに注意してください。

* 要件: ``Scalar`` に ``operator =``、``operator <``、``operator >`` が定義されていること。``Kokkos::reduction_identity<Scalar>::min()`` および ``Kokkos::reduction_identity<Scalar>::max()`` が有効な式であること。

* 要件: ``Index`` に ``operator =`` が定義されていること。``Kokkos::reduction_identity<Index>::min()`` が有効な式であること。

* ``MinMaxFirstLastLoc`` を ``Scalar`` または ``Index`` のカスタム型とともに使用するには、``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。詳細は `カスタムスカラー型を用いた組み込みリデューサー <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。