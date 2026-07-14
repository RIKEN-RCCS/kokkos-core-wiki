多次元並列性
============

.. _ParallelFor: ../API/core/parallel-dispatch/parallel_for.html
.. |ParallelFor| replace:: ``parallel_for()``

.. _ParallelReduce: ../API/core/parallel-dispatch/parallel_reduce.html
.. |ParallelReduce| replace:: ``parallel_reduce()``

.. _MDRangePolicy: ../API/core/policies/MDRangePolicy.html
.. |MDRangePolicy| replace:: ``MDRangePolicy``

.. _RangePolicy: ../API/core/policies/RangePolicy.html
.. |RangePolicy| replace:: ``RangePolicy``

この章では、複数の次元にわたって並列性を活用する方法について説明します。
問題が複数の並列性の次元を持ち、スクラッチメモリを必要としない場合、
|MDRangePolicy|_ を使用して複数の次元を同時に並列化できます。

``MDRangePolicy`` は密にネストされたループに最適です。密にネストされていないループやスクラッチメモリを必要とするループには、
`TeamPolicy <../API/core/policies/TeamPolicy.html>`_ を使用することをお勧めします。

ユースケース例
--------------

このポリシーは、多次元配列やテンソルデータに対する操作に特に適しています。
典型的な例は、有限要素法などの偏微分方程式（PDE）の数値解法に取り組む際に生じます。この場合、領域の離散化によって ``C`` 個のセル（要素）が生成され、
基底関数は ``P`` 個の点で評価され、そのランクと次元 ``D`` は基底関数の場のランク ``F`` に依存する入力および出力を生成します。

問題の定式化
~~~~~~~~~~~~

**入力**:
  - ``inputData(C,P,D,D)`` - ランク4のView
  - ``inputField(C,F,P,D)`` - ランク4のView

**戻り値**:
  - ``outputField(C,F,P,D)`` - ランク4のView

**計算**:
  ``C,F,P`` の各三つ組について、2つの入力Viewから出力フィールドを計算します:

シリアル実装
~~~~~~~~~~~~

.. code-block:: cpp

  for (int c = 0; c < C; ++c)
  for (int f = 0; f < F; ++f)
  for (int p = 0; p < P; ++p)
  {
    for (int i = 0; i < D; ++i) {
      double tmp(0);

      for (int j = 0; j < D; ++j)
        tmp += inputData(c, p, i, j) * inputField(c, f, p, j);  // compute the product

      outputField(c, f, p, i) = tmp;  // store the result
    }
  }

1次元の並列化 - ``RangePolicy``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上記のシリアルコードを並列化する最も簡単な方法は、シーケンシャルな反復パターンでセルにわたる外側の ``for`` ループを、|RangePolicy|_ を使用した並列forループに変換することです。

.. code-block:: cpp

   Kokkos::parallel_for("for_all_cells",
     Kokkos::RangePolicy<>(0,C),
      KOKKOS_LAMBDA (const int c) {
        for (int f = 0; f < F; ++f)
        for (int p = 0; p < P; ++p)
        {
         for (int i = 0; i < D; ++i) {

           double tmp(0);

           for (int j = 0; j < D; ++j)
             tmp += inputData(c, p, i, j) * inputField(c, f, p, j);

           outputField(c, f, p, i) = tmp;
         }
        }
     });


これは、セルの数が並列化に値するほど十分に大きい場合、つまり並列ディスパッチのオーバーヘッドと計算時間の合計がシリアル実行時間の合計より少ない場合に、うまく機能します。この単純なアプローチだけでも、すでにシリアル版よりパフォーマンスが向上します。

しかし、フィールド ``F`` および点 ``P`` にわたるループには、活用すべき並列性がまだ残っています。これは、メモリレイテンシを隠蔽するために大量の同時作業項目を必要とするデバイスバックエンド（GPU）で特に重要です。

これを達成する1つの方法は、3つの反復範囲を ``C*F*P`` のサイズの単一の範囲に平坦化し、その積に対して ``RangePolicy`` を使用して ``ParallelFor`` を実行することです。しかし、これにはフラットな1次元インデックス（``C*F*P``）とデータ構造が必要とする多次元 ``(C,F,P)`` インデックスとの間をマッピングする抽出ルーチンが必要になります。さらに、パフォーマンスポータブルであるためには、このマッピングはアーキテクチャを意識したものでなければなりません。これは、Kokkosでデータアクセスパターンを確立するために使用される `LayoutLeft <../API/core/view/layoutLeft.html>`_ や `LayoutRight <../API/core/view/layoutRight.html>`_ の概念に似ています。

多次元の並列化 - ``MDRangePolicy``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|MDRangePolicy|_ は、反復範囲の積を手動で計算したり、1次元と3次元の多次元インデックス間をマッピングしたりすることなく、3つの反復範囲すべてにわたって並列化するという目標を達成する自然な方法を提供します。``MDRangePolicy`` は密にネストされたforループでの使用に適しており、``RangePolicy`` を使用した最初の実装で示したように単一の次元で並列化するだけでなく、計算においてさらなる並列性を引き出す手段を提供します。

.. code-block:: cpp

   Kokkos::parallel_for("mdr_for_all_cells",
     Kokkos::MDRangePolicy< Kokkos::Rank<3> > ({0,0,0}, {C,F,P}),
      KOKKOS_LAMBDA (const int c, const int f, const int p) {
       for (int i = 0; i < D; ++i) {

         double tmp(0);

         for (int j = 0; j < D; ++j)
           tmp += inputData(c, p, i, j) * inputField(c, f, p, j);

         outputField(c, f, p, i) = tmp;
       }
     });

MDRangePolicyの使い方
---------------------

|MDRangePolicy|_ は多次元反復空間の実行ポリシーを定義し、Kokkosの |ParallelFor|_ パターンと |ParallelReduce|_ パターンの両方で使用できます。反復空間は「begin」インデックスのタプルと「end」インデックスのタプルによって定義され、これらは |MDRangePolicy|_ コンストラクタの引数として提供されます。

次元数 (``Kokkos::Rank``)
~~~~~~~~~~~~~~~~~~~~~~~~~

|MDRangePolicy|_ は |RangePolicy|_ と同じテンプレートパラメータを受け付けますが、追加の型 - :cpp:class:`Kokkos::Rank` パラメータも必要とします。ここで ``R`` はランク、つまりネストされたforループの数であり、コンパイル時に提供する必要があります。

インデックス引数
~~~~~~~~~~~~~~~~

このポリシーは2つの引数を必要とします:

1. 「begin」インデックスの初期化子リスト、または :cpp:struct:`Kokkos::Array`
2. 「end」インデックスの初期化子リスト、または :cpp:struct:`Kokkos::Array`

.. code-block:: cpp

  // Using initializer lists
  Kokkos::MDRangePolicy<Kokkos::Rank<3>> mdrange_policy({0, 0, 0}, {C, F, P});
  
  // Using Kokkos::Array
  Kokkos::Array<int64_t, 3> begin{0, 0, 0};
  Kokkos::Array<int64_t, 3> end{C, F, P};
  Kokkos::MDRangePolicy<Kokkos::Rank<3>> mdrange_policy(begin, end);

ラムダ（またはファンクタの ``operator()``）は、ポリシーのランクごとに1つの整数引数を取る必要があります。

.. code-block:: cpp

  // With rank 3, the lambda requires 3 arguments
  KOKKOS_LAMBDA(const int c, const int f, const int p) {
    // body of the lambda
  }

  // Agnostic rank functor example
  struct AddFunctor {
    // ...
    template<std::integral... Args>
    KOKKOS_INLINE_FUNCTION
    void operator()(Args... args) const {
      view_c(args...) = view_a(args...) + view_b(args...);
    }
  };


.. _MDRangePolicy-Iteration-order:

反復順序の指定 (``Kokkos::Iterate``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最良のパフォーマンスを得るために、|MDRangePolicy|_ の反復順序をデータのメモリレイアウトに合わせて指定したい場合があります。
反復順序は :cpp:class:`Kokkos::Rank` テンプレートパラメータで指定します。これは :cpp:enum:`Kokkos::Iterate` 型の ``outer`` と ``inner`` という2つのオプションのテンプレートパラメータを受け付けます。

.. code-block:: cpp

  // One mandatory template parameter is the rank of the iteration space
  Kokkos::Rank<3>;
  // Optionally, you can specify the iteration order
  Kokkos::Rank<3, Kokkos::Iterate::Default, Kokkos::Iterate::Default>;
  
  // Then use it inside the MDRangePolicy template parameters
  Kokkos::MDRangePolicy<Kokkos::Rank<3, Kokkos::Iterate::Left, Kokkos::Iterate::Right>>;

デフォルトでは、反復順序はデフォルトの実行空間に依存します。

デフォルトでは、反復順序とデータレイアウトは一致するはずです。
例えば、Kokkosを ``CUDA`` で構成した場合、デフォルトの反復順序は ``Kokkos::Iterate::Left`` で、デフォルトのデータレイアウトは ``LayoutLeft`` です。
Kokkosを ``OpenMP`` で構成した場合、デフォルトの反復順序は ``Kokkos::Iterate::Right`` で、デフォルトのデータレイアウトは ``LayoutRight`` です。

.. note:: ホストバックエンドで最良のキャッシュパフォーマンスを得るため、およびデバイスバックエンドで結合メモリアクセスを確保するために、反復パターンをデータレイアウトに合わせてください。

タイリング戦略
~~~~~~~~~~~~~~

内部的には、|MDRangePolicy|_ は多次元反復空間に対してタイリングを使用します。カスタマイズのために、オプションの3番目の引数 - タイル次元サイズの初期化子リスト - をポリシーに渡すことができます。この引数は、単純なデフォルトサイズは問題に依存し自動的に決定するのが難しいため、パフォーマンスチューニングの際に重要になることがあります。

.. code-block:: cpp

  // Tiling dimensions can be specified with an initializer list as the third argument to the MDRangePolicy constructor
  Kokkos::MDRangePolicy<Kokkos::Rank<3>> mdrange_policy({0, 0, 0}, {C, F, P}, {16, 4, 4});

タイルサイズを調整することは、``MDRangePolicy`` を使用する際にパフォーマンスを最適化する一般的な方法です。
最適なタイルサイズは、実行されるカーネル、アクセスされるデータ、および実行されるハードウェアに依存します。
デフォルトのタイルサイズはメンバー関数 :cpp:func:`tile_size_recommended` で照会できます。

* **デバイスバックエンド** (``CUDA``、``HIP``、``SYCL``): タイルサイズは、作業グループごとの作業項目の数を決定するために使用されます。
  そのサイズは基盤となるハードウェアによって制限されます。合計タイルサイズの上限は :cpp:func:`max_total_tile_size` で照会できます。

* **ホストバックエンド** (``Serial``、``OpenMP``、``Threads``): タイルサイズに制限はありません。

参考文献
--------

この例が基づいているユースケースは、Trilinosの `Intrepid2 <https://trilinos.github.io/docs/intrepid2/index.html>`_ パッケージから来ています。さらなる例については、Trilinosの次のファイル内のコードをチェックしてください: ``Trilinos/packages/intrepid2/src/Shared/Intrepid2_ArrayToolsDef*.hpp``。