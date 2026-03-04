``Max``
=======

.. :: cpp(code)
    :language: cpp

最大値を格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

   T result;
   parallel_reduce(N,Functor,Max<T,S>(result));

シノプシス
--------

.. code-block:: cpp

   template<class Scalar, class Space>
   クラス Max{
     パブリック:
       型定義 Max リデューサー;
       型定義 型名 std::remove_cv<Scalar>::type value_type;
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
       Max(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       Max(const result_view_type& value_);
   };

インターフェイス
---------

.. cpp:class:: template<class Scalar, class Space> Max

   .. rubric:: パブリック型

   .. cpp:type:: リデューサー

      自己型。

   .. cpp:type:: value_type

      還元スカラー型。

   .. cpp:type:: result_view_type

    　還元結果を参照する ``Kokkos::View``

   .. rubric:: コンストラク

   .. cpp:function:: KOKKOS_INLINE_FUNCTION Max(value_type& value_);

      結果の保存先としてローカル変数を参照するリデューサを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION Max(const result_view_type& value_);

      特定のビューを結果の保存先として参照するリデューサーを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

       ``src``　および　``dest`` の最大値を　``dest``: ``dest = ( src > dest ) ? src :dest;``にビット単位で格納します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

       ``Kokkos::reduction_identity<Scalar>::max()``  メソッドを使用して、``val``　を初期化します。 デフォルト実装は、　``val=<TYPE>_MIN``　を設定します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスコンストラクタで提供された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスコンストラクタで提供された結果の保存先のビューを返します。

Additional Information
^^^^^^^^^^^^^^^^^^^^^^

*  ``LOr<T,S>::value_type`` は、 非定数 ``T``　です。

* ``Max<T,S>::result_view_type`` は、 ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>``　です。 S(メモリ空間)は結果が存在する空間と同じでなければならないことに、注意してください。

* 必要要件:  ``Scalar`` は、 定義した ``operator =`` and ``operator >`` を持ちます。``Kokkos::reduction_identity<Scalar>::max()``  は、有効な式です。

* Max をカスタム型で使用するには、 ``Kokkos::reduction_identity<CustomType>`` のテンプレート仕様を定義する必要があります。 詳細については、 `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。
