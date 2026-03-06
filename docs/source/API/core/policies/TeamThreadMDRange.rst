``TeamThreadMDRange``
=====================

.. role::cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

ディスクリプション
-----------

TeamThreadMDRange　は、階層的並列処理の中で使用される、`ネストされた実行ポリシーです。


インターフェイス
---------

.. cpp:class:: テンプレート <class Rank, typename TeamHandle> TeamThreadMDRange

   .. rubric:: コンストラクタ

   .. cpp:function:: TeamThreadMDRange(team, extent_1, extent_2, ...);

      チームのスレッド全体でインデックスレンジ ``0`` を ``extent`` に分割します。ここで、 ``extent``　はスレッドされるバックエンド依存のランクです

      :param team: 呼び出しチーム実行コンテキストへの　TeamHandle 

      :param extent_1, extent_2, ...: 各ランクのインデックス範囲長


      * **必要要件**

	* ``TeamHandle`` 「TeamHandle <./TeamHandleConcept.html>'_　をモデル化する型です。

	* ``extent_1, extent_2, ...`` は、ints　です。

	*  ``team``　のすべてのメンバースレッドは同じブランチで操作を呼び出す必要があり、つまり一部のスレッドが一つのブランチでこの関数を呼び出し、``team`` の他のスレッドが別のブランチで呼び出すことは、合法ではありません。

	* ``extent_i`` is such that ``i >= 2 && i <= 8`` は、真です。
	  For example:

	  .. code-block:: cpp

	     TeamThreadMDRange(team, 4);               // OKではありません、 violates i>=2　に違反する

	     TeamThreadMDRange(team, 4,5);             // OK
	     TeamThreadMDRange(team, 4,5,6);           // OK
	     TeamThreadMDRange(team, 4,5,6,2,3,4,5,6); // OK, 範囲の最大値は認められます

制約
------------

 `parallel_reduce <../parallel-dispatch/parallel_reduce.html>`_　において使用される場合には、 還元は、合計に限定されることに注意してください。

例
--------

.. code-block:: cpp

   TeamHandle = TeamPolicy<>::member_type　を使用;

   parallel_for(TeamPolicy<>(N,AUTO),
     KOKKOS_LAMBDA (TeamHandle const& team) {

       int leagueRank = team.league_rank();

       自動　範囲 = TeamThreadMDRange<Rank<4>, TeamHandle>(team, n0, n1, n2, n3);

       parallel_for(range, [=](int i0, int i1, int i2, int i3) {
         A(leagueRank, i0, i1, i2, i3) = B(leagueRank, i1) + C(i1, i2, i3);
       });
       team.team_barrier();

       int teamSum = 0;
       parallel_reduce(range,
         [=](int i0, int i1, int i2, int i3, int& threadSum) {
           threadSum += D(leagueRank, i0, i1, i2, i3);
         }, teamSum
       );
       single(PerTeam(team), [&leagueSum, teamSum]() { leagueSum += teamSum; });
       A_rowSum[leagueRank] = leagueSum;
   });
