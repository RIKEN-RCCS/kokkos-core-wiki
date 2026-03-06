``RangePolicy``
===============

.. role::cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

    Kokkos::RangePolicy<...>(開始, 終了)
    Kokkos::RangePolicy<...>(開始, 終了, chunk_size)
    Kokkos::RangePolicy<...>(exec, 開始, 終了)
    Kokkos::RangePolicy<...>(exec, 開始, 終了, chunk_size)

    // CTAD コンストラクタ ( 4.3以降)
    Kokkos::RangePolicy(開始, 終了)
    Kokkos::RangePolicy(開始, 終了, chunk_size)
    Kokkos::RangePolicy(exec, 開始, 終了)
    Kokkos::RangePolicy(exec, 開始, 終了, chunk_size)

RangePolicy は、``begin`` から開始して、開区間で``end`` に行く、1次元反復空間の実行方針を、定義します。

シノプシス
--------

.. code-block:: cpp

    構造体 Kokkos::ChunkSize {
        明示的 ChunkSize(int value_);
    };

    template<class ... Args>
    構造体 Kokkos::RangePolicy {
        execution_policy = RangePolicy　を使用;
        using member_type = PolicyTraits<Args...>::index_type　を使用;

        // PolicyTraits<Args...>　より継承
        execution_space   = PolicyTraits<Args...>::execution_space　を使用;
        schedule_type     = PolicyTraits<Args...>::schedule_type　を使用;
        work_tag          = PolicyTraits<Args...>::work_tag　を使用;
        index_type        = PolicyTraits<Args...>::index_type　を使用;
        iteration_pattern = PolicyTraits<Args...>::iteration_pattern　を使用;
        launch_bounds     = PolicyTraits<Args...>::launch_bounds　を使用;

        // コンストラクタ
        RangePolicy(const RangePolicy&) = default;
        RangePolicy(RangePolicy&&) = default;

        RangePolicy();

        RangePolicy( index_type work_begin
                   , index_type work_end );

        RangePolicy( index_type work_begin
                   , index_type work_end
                   , ChunkSize chunk_size );

        RangePolicy( const execution_space & work_space
                   , index_type work_begin
                   , index_type work_end );

        RangePolicy( const execution_space & work_space
                   , index_type work_begin
                   , index_type work_end
                   , ChunkSize chunk_size );

        // chunk_size を復旧
        index_type chunk_size() const;
        // chunk_size を非連続値に設定します。
        RangePolicy& set_chunk_size(int chunk_size_);

        // コンストラクタに提供された　ExecSpace　インスタンスを返します
        KOKKOS_FUNCTION const execution_space & space() const;
        // Range begin　を返します
        KOKKOS_FUNCTION member_type begin() const;
        // return Range end　を返します
        KOKKOS_FUNCTION member_type end()   const;
    };

パラメータ
----------

汎用テンプレート引数
~~~~~~~~~~~~~~~~~~~~~~~~~~

有効なテンプレート引数は、ここ <../Execution-Policies.html#common-arguments-for-all-execution-policies>`_　で説明します。

パブリッククラスメンバー
--------------------

コンストラクタ
~~~~~~~~~~~~

.. cpp:function:: 明示的 ChunkSize(int value_)

   スケジューリング時に最適なチャンクサイズのヒントを提供します。
   SYCLバックエンドでは、 ``parallel_for`` カーネルで使われるワークグループサイズを、　``RangePolicy``に渡すことで設定できます。

   .. 注意事項::constructorsince Kokkos 4.4以降の ``ChunkSize`` コンストラクタ ``explicit`` 

.. cpp:function:: RangePolicy()

   デフォルトコンストラクタ非初期化ポリシー。

.. cpp:function:: RangePolicy(int64_t begin, int64_t end)

   開始インデックスおよび終了インデックスを提供します。

.. cpp:function:: RangePolicy(int64_t begin, int64_t end, ChunkSize chunk_size)

    ``ChunkSize``　同様に、開始インデックスおよび終了インデックスを提供します。

.. cpp:function:: RangePolicy(const ExecutionSpace& space, int64_t begin, int64_t end)

   開始と終了のインデックスと、実行リソースとして使うための ``ExecutionSpace`` インスタンスを提供します。

.. cpp:function:: RangePolicy(const ExecutionSpace& space, int64_t begin, int64_t end, ChunkSize chunk_size)

    ``ChunkSize``　同様に、 開始と終了のインデックスと、実行リソースとして使うための ``ExecutionSpace`` インスタンスを提供します。

前提条件:
^^^^^^^^^^^^^^

* 開始インデックスは終了インデックスより大きくあってはなりません。
* •	実際のコンストラクターはテンプレート化されており、安全に ``index_type`` に変換されているか確認できます( `#6754 <https://github.com/kokkos/kokkos/pull/6754>`_　参照 )　。

CTAD コンストラクタ (4.3以降):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cpp

   int64_t work_begin = /* ... */; // 同様に変換
   int64_t work_end   = /* ... */; // 同様に変換
   ChunkSize cs       = /* ... */; // 同様に変換
   DefaultExecutionSpace des;      // 同様に変換
   SomeExecutionSpace ses;         // DefaultExecutionSpaceとは異なります

   // RangePolicy<>　に演繹
   RangePolicy rp0;
   RangePolicy rp1(work_begin, work_end);
   RangePolicy rp2(work_begin, work_end, cs);
   RangePolicy rp3(des, work_begin, work_end);
   RangePolicy rp4(des, work_begin, work_end, cs);

   // RangePolicy<SomeExecutionSpace>　に演繹
   RangePolicy rp5(ses, work_begin, work_end);
   RangePolicy rp6(ses, work_begin, work_end, cs);

例
--------

.. code-block:: cpp

    RangePolicy<> policy_1(0, N);
    RangePolicy<Cuda> policy_2(5,N-5);
    RangePolicy<Schedule<Dynamic>, OpenMP> policy_3(n,m);
    RangePolicy<IndexType<int>, Schedule<Dynamic>> policy_4(0, K);
    RangePolicy<> policy_6(-3,N+3, ChunkSize(8));
    RangePolicy<OpenMP> policy_7(OpenMP(), 0, N, ChunkSize(4));

注意事項: 並列パターンに対して単一の整数をポリシーとして提供することは、デフォルトされた　``RangePolicy``　を意味します。 

.. code-block:: cpp

    // 以下の2つの呼び出しは同一です
    parallel_for("Loop", N, ファンクタ);
    parallel_for("Loop", RangePolicy<>(0, N), ファンクタ);
