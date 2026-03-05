``Min``
=======

.. role:: cpp(code)
    :language: cpp

最小値を格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

   T result;
   parallel_reduce(N,Functor,Min<T,S>(result));

シノプシス
--------

.. code-block:: cpp

   template<class Scalar, class Space>
   クラス Min{
     パブリック:
       型定義 Min reducer;
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
       Min(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       Min(const result_view_type& value_);
   };

インターフェイス
---------

.. cpp:class:: template<class Scalar, class Space> Min

   .. rubric:: パブリック型

   .. cpp:type:: リデューサー

      自己型。

   .. cpp:type:: value_type

      還元スカラー型。

   .. cpp:type:: result_view_type

      還元結果を参照する ``Kokkos::View`` 

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION Min(value_type& value_);

       結果の保存先としてローカル変数を参照するリデューサを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION Min(const result_view_type& value_);

      Constructs a reducer which references a specific view as its result location.

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

       ``dest``:  ``dest = (src < dest) ? src :dest;`` に、 ``src`` および ``dest`` の最小値を格納します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

       ``Kokkos::reduction_identity<Scalar>::min()`` メソッドを使って.  ``val`` を初期化します。　デフォルト実装は、 ``val=<TYPE>_MAX``　を設定します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスコンストラクタで提供された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスコンストラクタで提供された結果の保存先のビューを返します。

追加情報
^^^^^^^^^^^^^^^^^^^^^^

* ``Min<T,S>::value_type`` は、 非定数 ``T``

* ``Min<T,S>::result_view_type`` は、 ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>``　です。 Note that the S (memory space) must be the same as the space where the result resides.

* Requires: ``Scalar`` has ``operator =`` and ``operator <`` defined. ``Kokkos::reduction_identity<Scalar>::min()`` is a valid expression.

* In order to use Min with a custom type, a template specialization of ``Kokkos::reduction_identity<CustomType>`` must be defined. See `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ for details
