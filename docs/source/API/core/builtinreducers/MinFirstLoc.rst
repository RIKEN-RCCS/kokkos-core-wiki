``MinFirstLoc``
===============

.. role:: cpp(code)
    :language: cpp

条件を満たす最小値と最初のインデックスを格納する `ReducerConcept <ReducerConcept.html>`_ の具体的な実装です。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使い方
------

.. code-block:: cpp

   MinFirstLoc<T,I,S>::value_type result;
   parallel_reduce(N,Functor,MinFirstLoc<T,I,S>(result));

概要
----

.. code-block:: cpp

   template<class Scalar, class Index, class Space>
   class MinFirstLoc{
     public:
       using reducer = MinFirstLoc;
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
       MinFirstLoc(value_type& value_);

       KOKKOS_INLINE_FUNCTION
       MinFirstLoc(const result_view_type& value_);
   };

インターフェース
----------------

.. cpp:class:: template<class Scalar, class Index, class Space> MinFirstLoc

   .. rubric:: パブリック型

   .. cpp:type:: reducer

      自己型。

   .. cpp:type:: value_type

      リダクションのスカラー型（`ValLocScalar <ValLocScalar.html>`_ の特殊化）

   .. cpp:type:: result_view_type

      リダクション結果を参照する ``Kokkos::View``

   .. rubric:: コンストラクタ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MinFirstLoc(value_type& value_);

      結果の格納場所としてローカル変数を参照するリデューサを構築します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION MinFirstLoc(const result_view_type& value_);

      結果の格納場所として特定のビューを参照するリデューサを構築します。

   .. rubric:: パブリックメンバー関数

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

      ``src`` と ``dest`` のうち最小値と最初のインデックスを ``dest`` に格納します: ``dest = (src.val < dest.val) ? src :dest;``。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

      ``Kokkos::reduction_identity<Scalar>::min()`` メソッドを使用して ``val.val`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` に設定されます。
      ``Kokkos::reduction_identity<Index>::min()`` メソッドを使用して ``val.loc`` を初期化します。デフォルトの実装では ``val=<TYPE>_MAX`` に設定されます。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

      クラスのコンストラクタで指定された結果への参照を返します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;

      クラスのコンストラクタで指定された結果のビューを返します。

追加情報
^^^^^^^^

* ``MinFirstLoc<T,I,S>::result_view_type`` は ``Kokkos::View<T,S,Kokkos::MemoryTraits<Kokkos::Unmanaged>>`` です。S（メモリ空間）は結果が存在する空間と同じでなければならないことに注意してください。

* 要件: ``Scalar`` に ``operator =`` および ``operator <`` が定義されていること。``Kokkos::reduction_identity<Scalar>::min()`` が有効な式であること。

* 要件: ``Index`` に ``operator =`` が定義されていること。``Kokkos::reduction_identity<Index>::min()`` が有効な式であること。

* ``MinFirstLoc`` を ``Scalar`` または ``Index`` のいずれかのカスタム型で使用するには、``Kokkos::reduction_identity<CustomType>`` のテンプレート特殊化を定義する必要があります。詳細は `Built-In Reducers with Custom Scalar Types <../../../ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.html>`_ を参照してください。

例
--

.. code-block:: cpp

  #include <Kokkos_Core.hpp>
  struct Idx3D_t {
    int value[3];
    int& operator[](int i) { return value[i]; }
    const int& operator[](int i) const { return value[i]; }
  };
  template <>
  struct Kokkos::reduction_identity<Idx3D_t> {
    static constexpr Idx3D_t min() { return {0, 0, 0}; }
  };
  int main(int argc, char* argv[]) {
    Kokkos::initialize(argc, argv);
    {
      Kokkos::View<double***> a("A", 5, 5, 5);
      Kokkos::deep_copy(a, 10);
      a(2, 3, 1)        = 5;
      using MinFirstLoc_t    = Kokkos::MinFirstLoc<double, Idx3D_t>;
      using MinFirstLocVal_t = typename MinFirstLoc_t::value_type;
      MinFirstLocVal_t result;
      Kokkos::parallel_reduce(
          Kokkos::MDRangePolicy<Kokkos::Rank<3>>({0, 0, 0}, {5, 5, 5}),
          KOKKOS_LAMBDA(int i, int j, int k, MinFirstLocVal_t& val) {
            if (a(i, j, k) < val.val) {
              val.val    = a(i, j, k);
              val.loc[0] = i;
              val.loc[1] = j;
              val.loc[2] = k;
            }
          },
          MinFirstLoc_t(result));
      printf("%lf %i %i %i\n", result.val, result.loc[0], result.loc[1],
             result.loc[2]);
    }
    Kokkos::finalize();
  }