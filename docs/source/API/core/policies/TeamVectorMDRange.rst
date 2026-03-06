``TeamVectorMDRange``
=====================

ヘッダーファイル: ``<Kokkos_Core.hpp>``

ディスクリプション
-----------

TeamVectorMDRange は、階層的並列処理の内部で使用される `nested execution policy <./NestedPolicies.html>`_  です。

インターフェイス
---------

.. cpp:class:: テンプレート <class Rank, typename TeamHandle> TeamVectorMDRange

   .. rubric:: コンストラクタ

   .. cpp:function:: TeamVectorMDRange(team, extent_1, extent_2, ...);

      チームのスレッドにインデックス範囲を分け、ベクトルレーン上でインデックスレンジを分割します。
      バックエンドによって決定されるスレッドとベクトル化のランクです。

      :param team: 呼び出しチーム実行コンテキストへのTeamHandle

      :param extent_1, extent_2, ...: 各ランクのインデックス範囲長

      * **必要要件**

	* ``TeamHandle`` は、 `TeamHandle <./TeamHandleConcept.html>`_　をモデル化する型です。

	* ``extent_1, extent_2, ...`` は、 ints　です。

	*  ``team`` のすべてのメンバースレッドは同じブランチで演算を呼び出す必要があり、つまり一部のスレッドが一つのブランチでこの関数を呼び出し、 ``team`` の他のスレッドが  別のブランチで呼び出すことは、合法ではありません。

	* ``extent_i`` は、 ``i >= 2 && i <= 8``　が真であることが条件です。
	  例えば:

	  .. code-block:: cpp

	     TeamVectorMDRange(team, 4);               // NOT OK, violates i>=2

	     TeamVectorMDRange(team, 4,5);             // OK
	     TeamVectorMDRange(team, 4,5,6);           // OK
	     TeamVectorMDRange(team, 4,5,6,2,3,4,5,6); // OK, max num of extents allowed

Restrictions
------------

Note that when used in `parallel_reduce <../parallel-dispatch/parallel_reduce.html>`_, the reduction is limited to a sum.

Examples
--------

.. code-block:: cpp

   using TeamHandle = TeamPolicy<>::member_type;

   parallel_for(TeamPolicy<>(N,AUTO),
     KOKKOS_LAMBDA(TeamHandle const& team) {

       int leagueRank = team.league_rank();

       auto range = TeamVectorMDRange<Rank<4>, TeamType>(team, n0, n1, n2, n3);

       parallel_for(range,
         [=](int i0, int i1, int i2, int i3) {
           A(leagueRank, i0, i1, i2, i3) = B(leagueRank, i1) + C(i1, i2, i3);
       });
       team.team_barrier();

       int teamSum = 0;
       parallel_reduce(range,
           [=](int i0, int i1, int i2, int i3, int& vectorSum) {
             vectorSum += v(leagueRank, i, j, k, l);
           }, teamSum
       );
       single(PerTeam(team), [&leagueSum, teamSum]() { leagueSum += teamSum; });
       A_rowSum[leagueRank] = leagueSum;
     });
