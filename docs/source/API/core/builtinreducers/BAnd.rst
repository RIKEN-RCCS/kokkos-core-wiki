``BAnd``
========

.. role:: cpp(code)
    :language: cpp

ビット単位の ``AND`` 演算を実行する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用方法
--------

.. code-block:: cpp

    T result;
    parallel_reduce(N, Functor, BAnd<T, S>(result));

概要
----

.. code-block:: cpp

    template<class Scalar, class Space>
    class BAnd {
      public:
        using reducer = BAnd<Scalar, Space>;
        using value_type = typename std::remove_cv<Scalar>::type;

        KOKKOS_INLINE_FUNCTION
        void join(value_type& dest, const value_type& src) const {
          dest = dest & src;
        }

        KOKKOS_INLINE_FUNCTION
        void init(value_type& val) const {
          val = Kokkos::reduction_identity<value_type>::band();
        }

        // ReducerConcept を満たすためのその他のメンバー
    };

インターフェイス
----------------

`ReducerConcept <ReducerConcept.html>`_ のすべてのパブリック型、コンストラクター、メソッドが利用可能です。以下の型とメソッドは、このリデューサーによってオーバーライドされます。

.. cpp:class:: template<class Scalar, class Space> BAnd

   .. rubric:: パブリック型

   .. cpp:type:: reducer

      自己型

   .. cpp:type:: value_type

      ``Scalar`` テンプレートパラメーターから、その潜在的な ``const`` および/または ``volatile`` 修飾子を取り除いたものです。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

       ``src`` と ``dest`` のビット単位の ``and`` を ``dest`` に格納します: ``dest = src & dest``。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

       ``Kokkos::reduction_identity<value_type>::band()`` メソッドを使用して、 ``val`` を初期化します。デフォルト実装は、 ``val=~(0x0)`` を設定します。

追加情報
~~~~~~~~

* 要件: ``value_type`` に ``operator =`` および ``operator &`` が定義されていること。 ``Kokkos::reduction_identity<value_type>::band()`` が有効な式であること。

* カスタム型で ``BAnd`` を使用するには、 ``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。詳細については、 `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。
