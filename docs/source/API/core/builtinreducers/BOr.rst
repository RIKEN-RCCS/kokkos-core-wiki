``BOr``
=======

.. role:: cpp(code)
    :language: cpp

ビット単位の ``OR`` 演算を行う `ReducerConcept <ReducerConcept.html>`_ の具体的な実装。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用方法
--------

.. code-block:: cpp

T result;
   parallel_reduce(N, Functor, BOr<T, S>(result));

概要
----

.. code-block:: cpp

template<class Scalar, class Space>
   class BOr {
     public:
       using reducer = BOr<Scalar, Space>;
       using value_type = typename std::remove_cv<Scalar>::type;

KOKKOS_INLINE_FUNCTION
       void join(value_type& dest, const value_type& src) const {
         dest = dest | src;
       }

KOKKOS_INLINE_FUNCTION
       void init(value_type& val) const {
         val = Kokkos::reduction_identity<value_type>::bor();
       }

// ReducerConcept を満たすためのその他のメンバー
   };

インターフェイス
----------------

`ReducerConcept <ReducerConcept.html>`_ のすべてのパブリック型、コンストラクター、メソッドが利用可能です。次の型とメソッドは、このリデューサーによってオーバーライドされます。

.. cpp:class:: template<class Scalar, class Space> BOr

.. rubric:: パブリック型

.. cpp:type:: reducer

自己型

.. cpp:type:: value_type

``Scalar`` テンプレートパラメーターから、潜在的な ``const`` および/または ``volatile`` 修飾子を除去した型。

.. rubric:: パブリックメンバー関数

.. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

``src`` と ``dest`` の論理 ``or`` を ``dest`` に格納します: ``dest = src | dest``。

.. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

``Kokkos::reduction_identity<value_type>::bor()`` メソッドを使用して、 ``val`` を初期化します。デフォルト実装は、 ``val=0x0`` を設定します。

追加情報
^^^^^^^^

* 要件: ``value_type`` に ``operator =`` および ``operator |`` が定義されていること。``Kokkos::reduction_identity<value_type>::bor()`` が有効な式であること。

* ``BOr`` をカスタム型で使用するには、 ``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。詳細については、 `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。
