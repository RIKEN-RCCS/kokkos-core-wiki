``TeamPolicy``
==============

.. role:: cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用方法
--------

.. code-block:: cpp

Kokkos::TeamPolicy<>( league_size, team_size [, vector_length])
    Kokkos::TeamPolicy<ARGS>(league_size, team_size [, vector_length])
    Kokkos::TeamPolicy<>(Space, league_size, team_size [, vector_length])
    Kokkos::TeamPolicy<ARGS>(Space, league_size, team_size [, vector_length])

開始から始まり、開区間で終わる、1次元反復空間の実行ポリシー。

以下も参照: `TeamMember <TeamHandleConcept.html>`_

説明
----

.. cpp:class:: template<class ...Args> TeamPolicy

.. rubric:: テンプレート引数

TeamPolicy の有効なテンプレート引数は `ここ <../Execution-Policies.html#common-arguments-for-all-execution-policies>`_ に説明されています。

.. rubric:: パブリックネスト型定義

.. cpp:type:: execution_space
   .. cpp:type:: schedule_type
   .. cpp:type:: work_tag
   .. cpp:type:: index_type
   .. cpp:type:: iteration_pattern
   .. cpp:type:: launch_bounds
   .. cpp:type:: member_type

.. rubric:: コンストラクタ

.. cpp:function:: TeamPolicy()

デフォルトコンストラクタ非初期化ポリシー。

.. cpp:function:: TeamPolicy(const TeamPolicy&) = default;

コピーコンストラクタ

.. cpp:function:: TeamPolicy(TeamPolicy&&) = default;

移動コンストラクタ

.. cpp:function:: TeamPolicy(index_type league_size, index_type team_size, index_type vector_length=1)

``league_size`` ワークアイテムの起動リクエストで、 ``vector_length`` のベクトル長を使用して、それぞれが ``team_size`` スレッドで、スレッドチームに代入されます。 並列ポリシーを呼び出した際にチームサイズが設定できない場合、そのカーネルの起動がスローされる場合があります。

.. cpp:function:: TeamPolicy(index_type league_size, AUTO_t, index_type vector_length=1)

``league_size`` ワークアイテムの起動リクエストで、 ``vector_length`` のベクトル長を使用して、それぞれが Kokkos が決定したサイズのスレッドチームに代入されます。 チームの規模は、ファンクタの性質を考慮して起動時に遅れて決定することができます。

.. cpp:function:: TeamPolicy(execution_space space, index_type league_size, index_type team_size, index_type vector_length=1)

``league_size`` ワークアイテムの起動リクエストで、 ``vector_length`` のベクトル長を使用して、それぞれが ``team_size`` スレッドのスレッドチームに代入されます。 並列ポリシーを呼び出した際にチームサイズが設定できない場合、そのカーネルの起動がスローされる場合があります。カーネル起動時に提供された実行空間インスタンスを使用します。

.. cpp:function:: TeamPolicy(execution_space space, index_type league_size, AUTO_t, index_type vector_length=1)

``league_size`` ワークアイテムの起動リクエストで、 ``vector_length`` のベクトル長を使用して、それぞれが Kokkos が決定したサイズのスレッドチームに代入されます。チームの規模は、ファンクタの性質を考慮して起動時に遅れて決定することができます。カーネル起動時に提供された実行空間インスタンスを使用します。

.. rubric:: 実行時設定

.. cpp:function:: inline TeamPolicy& set_chunk_size(int chunk);

チャンクサイズを設定します。各物理的なスレッドチームには、連続した ``chunk`` チームが代入されます。デフォルトは 1 です。

Returns:  ``*this`` を参照。

.. cpp:function:: inline TeamPolicy& set_scratch_size(const int& level, const Impl::PerTeamValue& per_team);

.. cpp:function:: inline TeamPolicy& set_scratch_size(const int& level, const Impl::PerThreadValue& per_thread);

.. cpp:function:: inline TeamPolicy& set_scratch_size(const int& level, const Impl::PerTeamValue& per_team, const Impl::PerThreadValue& per_thread);

.. cpp:function:: inline TeamPolicy& set_scratch_size(const int& level, const Impl::PerThreadValue& per_thread, const Impl::PerTeamValue& per_team);

チームごとのスクラッチサイズとスレッドごとのスクラッチサイズを設定します。

- ``level``: ストレージのレベルを設定してください。0 は最も近いキャッシュです。1 は最も近いストレージ(例:高帯域幅メモリ)です。
      - ``per_team``: スクラッチのバイト単位のチームごとのサイズのラッパーです。関数 ``PerTeam(int)`` で返されます。

- ``per_thread``: スレッドごとのスクラッチサイズ(バイト単位)のラッパーです。関数 ``PerThread(int)`` で返されます。

関数を 2回呼び出すことで、レベル 0 と 1 のスクラッチサイズを独立して設定できます。 同じレベルでの後続の呼び出しは、前の値を上書きします。
      返し:  ``*this`` を参照

.. rubric:: 実行時設定の参照制限

.. _parallelFor: ../parallel-dispatch/parallel_for.html

.. |parallelFor| replace:: :cpp:func:`parallel_for`

.. _parallelReduce: ../parallel-dispatch/parallel_reduce.html

.. |parallelReduce| replace:: :cpp:func:`parallel_reduce`

.. cpp:function:: template<class FunctorType> int team_size_max(const FunctorType& f, const ParallelForTag&) const;

.. cpp:function:: template<class FunctorType> int team_size_max(const FunctorType& f, const ParallelReduceTag&) const;

特定のファンクタが与えられた場合、最大チームサイズを参照します。タグは、これが、 |parallelFor|_ か |parallelReduce|_ かを示します。
      注意事項:  これは静的な関数ではありません! 関数は、ベクター長と ``*this`` のスクラッチサイズの設定を考慮します。 戻り値より大きい値を使うと、ディスパッチ失敗になります。 戻り値が正でない場合、有効なチームサイズは見つかりません。 一般的な理由は、スクラッチキャッシュメモリへの要求が過剰であったことです。
      返し:  ``f`` をディスパッチするために、他に同一の ``TeamPolicy`` と組み合わせて使用できることを可能にした``team_size`` の最大値。

.. cpp:function:: template<class FunctorType> int team_size_recommended(const FunctorType& f, const ParallelForTag&) const;

.. cpp:function:: template<class FunctorType> int team_size_recommended(const FunctorType& f, const ParallelReduceTag&) const;

特定のファンクタ ``f`` について推奨されるチームサイズを照会します。タグは、これが |parallelFor|_  か |parallelReduce|_ かを示します。
      注意事項: これは静的な関数ではありません! 関数は、ベクター長と ``*this`` のスクラッチサイズの設定を考慮します。 戻り値が正でない場合、有効なチームサイズは見つかりません。 一般的な理由は、スクラッチキャッシュメモリへの要求が過剰であったことです。
      返し:  ``f`` をディスパッチするために、他に同一の ``TeamPolicy`` と組み合わせて使用できることを可能にした``team_size`` の最大値。

.. cpp:function:: static int vector_length_max();

Returns: ベクトル長の最大有効値。

.. cpp:function:: static int scratch_size_max(int level);

返し: 指定のレベルについて、最大総スクラッチサイズ(バイト単位)。
      注意事項: カーネルがチームレベルの削減やスキャン演算を行う場合、このメモリのすべてが、動的ユーザーリクエストについて、利用可能になるわけではありません。 これらの最大スクラッチサイズの一部は、内部演算に使われています。これらの内部割り当ての実際のサイズは、縮約またはスキャンで使用される値の型によって異なります。

.. rubric:: 照会実行時設定

.. cpp:function:: int team_size() const;

返し: 要求されたチームサイズ。

.. cpp:function:: int league_size() const;

返し: 要求されたリーグサイズ。

.. cpp:function:: int scratch_size(int level, int team_size_ = -1) const;

本関数は、要求されたスクラッチサイズの合計を返します。 ``team_size`` が提供されていない場合は、内部設定から計算用のチームサイズ(すなわち、 ``this->team_size()`` を呼び出した結果)が使われます。 それ以外の場合は、提供されたチームサイズが使用されます。
      返し: 特定されたスクラッチレベルでのチームあたりの総スクラッチサイズ(バイト単位)の値。

.. cpp:function:: int team_scratch_size(int level) const;

返し: 特定されたスクラッチレベルでのチームあたりのスクラッチサイズ(バイト単位)の値。

.. cpp:function:: int thread_scratch_size(int level) const;

返し: 特定されたスクラッチレベルでのスレッドあたりのスクラッチサイズ(バイト単位)の値。

.. cpp:function:: int chunk_size() const;

返し:  ``set_chunk_size()`` 経由で設定された、チャンクサイズ。

例
--

.. code-block:: cpp

TeamPolicy<> policy_1(N,AUTO);
    TeamPolicy<Cuda> policy_2(N,T);
    TeamPolicy<Schedule<Dynamic>, OpenMP> policy_3(N,AUTO,8);
    TeamPolicy<IndexType<int>, Schedule<Dynamic>> policy_4(N,1,4);
    TeamPolicy<OpenMP> policy_5(OpenMP(), N, AUTO);

.. code-block:: cpp

using team_handle = TeamPolicy<>::member_type;
    parallel_for(TeamPolicy<>(N,AUTO), KOKKOS_LAMBDA (const team_handle& team) {

// 各チームが、Aの列を初期化します
        int n = team.league_rank();
        parallel_for(TeamThreadRange(team,M), [&] (const int& i) {
            A(n,i) = B(n) + i;
        });
        team.team_barrier();

// ランク2ビューとして格納されている、行列 A の n 行目の合計を計算
        int team_sum;
        parallel_reduce(TeamThreadRange(team,M), [&] (const int& i, int& lsum) {
            lsum += A(n,i);
        },team_sum);
        
        //  A_rowsum ベクトルの対応する入力における列の合計を格納
        single(PerTeam(team),[&] () {
            A_rowsum(n) = team_sum;
        });
    });

// Compute the sum of the nth row of matrix A, stored as a rank-2 view
        int team_sum;
        parallel_reduce(TeamThreadRange(team,M), [&] (const int& i, int& lsum) {
            lsum += A(n,i);
        },team_sum);
        
        // store the sum of the row in corresponding entry of A_rowsum vector
        single(PerTeam(team),[&] () {
            A_rowsum(n) = team_sum;
        });
    });
