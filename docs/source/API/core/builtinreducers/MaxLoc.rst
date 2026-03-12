``MaxLoc``
==========

.. role:: cpp(code)
    :language: cpp

最大値を格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

   MaxLoc<T,I,S>::value_type result;
   parallel_reduce(N,Functor,MaxLoc<T,I,S>(result));

シノプシス
--------

.. code-block:: cpp

   template<class Scalar, class Index, class Space>
   クラス MaxLoc{
     パブリック:
       型定義 MaxLoc リデューサー;
       型定義 ValLocScalar<typename std::remove_cv<Scalar>::type,
                               typename std::remove_cv<Index>::type > value_type;
       型定義 Kokkos::View<value_type, Space> result_view_type;

       KOKKOS_INLINE_FUNCTION
       void join(value_type& dest, const value_type& src) const;

       KOKKOS_INLINE_FUNCTION
       void init(value_type& val) const;

       KOKKOS_INLINE_FUNCTION
       value_type& reference() const;

       KOKKOS_INLINE_FUNCTION
       result_view_type view() const;

       KOKKOS_INLINE_FUNCTION
       MaxLoc(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       MaxLoc(const result_view_type& value_);
   };

インターフェイス
---------

.. cpp:class:: template<class Scalar, class Index, class Space> MaxLoc

   .. rubric:: パブリック型

   .. cpp:type:: リデューサー

      自己型。

   .. cpp:type:: value_type

      還元スカラー型 ( `ValLocScalar <ValLocScalar.html>`_　の特殊化)

   .. cpp:type:: result_view_type

      還元結果を参照する ``Kokkos::View`` 

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MaxLoc(value_type& value_);

      結果の保存先としてローカル変数を参照するリデューサを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MaxLoc(const result_view_type& value_);

      特定のビューを結果の保存先として参照するリデューサーを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

       ``dest``: ``dest = (src.val > dest.val) ? src :dest;``　に、 ``src`` および ``dest`` のインデックスを持つ最大値を格納します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

       ``Kokkos::reduction_identity<Scalar>::max()`` メソッドを使って、 ``val.val`` を初期化します。 デフォルト実装は、 ``val=<TYPE>_MIN``　を設定します。
       ``Kokkos::reduction_identity<Index>::min()``  メソッドを使って、 ``val.loc`` を初期化します。 デフォルト実装は、  ``val=<TYPE>_MAX`` を設定します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスコンストラクタで提供された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスコンストラクタで提供された結果の保存先のビューを返します。

追加情報
^^^^^^^^^^^^^^^^^^^^^^

* ``MaxLoc<T,I,S>::value_type`` は  非定数 ``T`` および 非定数 ``I``　上の ValLocScalar の特殊化です。

* ``MaxLoc<T,I,S>::result_view_type`` は、 ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>``　です。  S(メモリ空間)は結果が存在する空間と同じでなければならないことに、注意してください。

* 必要条件:  ``Scalar`` には、 定義した ``operator =`` および  ``operator >``  が定義されます。 ``Kokkos::reduction_identity<Scalar>::max()`` は、有効な式です。

* 必要条件: ``Index`` は、定義した ``operator =`` を持ちます。 ``Kokkos::reduction_identity<Index>::min()``  は、有効な式です。

* MaxLoc を ``Scalar`` または ``Index``　いずれかのカスタム型で使用するために、 ``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。 詳細については、`Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください
