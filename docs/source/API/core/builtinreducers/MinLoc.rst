``MinLoc``
==========

.. ロール:: cpp(code)
    :language: cpp

インデックスを伴って最小値を格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

   MinLoc<T,I,S>::value_type result;
   parallel_reduce(N,Functor,MinLoc<T,I,S>(result));

シノプシス
--------

.. code-block:: cpp

   template<class Scalar, class Index, class Space>
   クラス MinLoc{
     パブリック:
       型定義 MinLoc リデューサー;
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
       MinLoc(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       MinLoc(const result_view_type& value_);
   };

インターフェイス
---------

.. cpp:class:: template<class Scalar, class Index, class Space> MinLoc

   .. rubric:: パブリック型

   .. cpp:type:: リデューサー

      自己型。

   .. cpp:type:: value_type

      The reduction scalar type ( `ValLocScalar <ValLocScalar.html>`_　の特殊化))

   .. cpp:type:: result_view_type

      還元結果を参照する ``Kokkos::View`` 

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MinLoc(value_type& value_);

      結果の保存先としてローカル変数を参照するリデューサを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MinLoc(const result_view_type& value_);

      特定のビューを結果の保存先として参照するリデューサーを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

      ``dest``:  ``dest = (src.val < dest.val) ? src :dest;``に、 ``src`` および ``dest`` のインデックスを持つ最小値を格納します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

      Initialize using the ``Kokkos::reduction_identity<Scalar>::min()`` メソッドを使って、 ``val.val`` を初期化します。　デフォルト実装は、The default implementation sets ``val=<TYPE>_MAX``　を設定します。
      Initialize using the ``Kokkos::reduction_identity<Index>::min()``  メソッドを使って、 ``val.loc`` を初期化します。　デフォルト実装は、 ``val=<TYPE>_MAX``　を設定します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスコンストラクタで提供された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      特定のビューを結果の保存先として参照するリデューサーを構築します。

追加情報
^^^^^^^^^^^^^^^^^^^^^^

* ``MinLoc<T,I,S>::value_type`` は、 非定数 ``T`` および 非定数 ``I``　上の ValLocScalar の特殊化です。

* ``MinLoc<T,I,S>::result_view_type`` は ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>``　です。 S(メモリ空間)は結果が存在する空間と同じでなければならないことに、注意してください。

* 必要条件: ``Scalar`` には、 ``operator =`` および　``operator <`` が定義されます。 ``Kokkos::reduction_identity<Scalar>::min()``  は有効な式です。

* 必要条件: ``Index`` は、定義された ``operator =`` を持ちます。 ``Kokkos::reduction_identity<Index>::min()`` は有効な式です。

*  ``Scalar`` または ``Index``のいずれかのカスタム型で  MinLoc を使用するために、``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。 詳細については、 `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。

例
-------

.. code-block:: cpp

  #include <Kokkos_Core.hpp>
  構造体 Idx3D_t {
    int value[3];
    int& operator[](int i) { return value[i]; }
    const int& operator[](int i) const { return value[i]; }
  };
  テンプレート <>
  構造体 Kokkos::reduction_identity<Idx3D_t> {
    静的 constexpr Idx3D_t min() { return {0, 0, 0}; }
  };
  int main(int argc, char* argv[]) {
    Kokkos::initialize(argc, argv);
    {
      Kokkos::View<double***> a("A", 5, 5, 5);
      Kokkos::deep_copy(a, 10);
      a(2, 3, 1)        = 5;
      MinLoc_t    = Kokkos::MinLoc<double, Idx3D_t>　を使用;
      MinLocVal_t = typename MinLoc_t::value_type　を使用;
      MinLocVal_t result;
      Kokkos::parallel_reduce(
          Kokkos::MDRangePolicy<Kokkos::Rank<3>>({0, 0, 0}, {5, 5, 5}),
          KOKKOS_LAMBDA(int i, int j, int k, MinLocVal_t& val) {
            if (a(i, j, k) < val.val) {
              val.val    = a(i, j, k);
              val.loc[0] = i;
              val.loc[1] = j;
              val.loc[2] = k;
            }
          },
          MinLoc_t(result));
      printf("%lf %i %i %i\n", result.val, result.loc[0], result.loc[1],
             result.loc[2]);
    }
    Kokkos::finalize();
  }
