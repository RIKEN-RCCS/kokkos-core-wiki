``ThreadVectorMDRange``
=======================

.. role::cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

ディスクリプション
-----------

階層的並列処理の中で使われる `nested execution policy <NestedPolicies.html>`_ です。 

インターフェイス
---------

.. cpp:class:: template <class Rank, typename TeamHandle> ThreadVectorMDRange

   .. rubric:: コンストラクタ

   .. cpp:function:: ThreadVectorMDRange(team, extent_1, extent_2, ...);

      呼び出しスレッドのベクトルレーン上で、インデックス範囲 ``0`` から ``extent`` を分割します。
      ここでは、 ``extent`` は、ベクトル化されるバックエンド依存のランクです。

      :param team: 呼び出しチーム実行コンテキストへのTeamHandle

      :param extent_1, extent_2, ...: 各ランクのインデックス範囲長

      * **必要要件**

	* ``TeamHandle`` は、 `TeamHandle <./TeamHandleConcept.html>`_ をモデル化する型です。

	* ``extent_1, extent_2, ...`` は、intsです。

	* ``extent_i`` の条件は、 ``i >= 2 && i <= 8`` が真であることです。
	  例えば:

	  .. code-block:: cpp

	     ThreadVectorMDRange(team, 4);               // OKではありません、 i>=2 に違反します

	     ThreadVectorMDRange(team, 4,5);             // OK
	     ThreadVectorMDRange(team, 4,5,6);           // OK
	     ThreadVectorMDRange(team, 4,5,6,2,3,4,5,6); // OK, 範囲の最大値は認められます


	*  ``TeamVectorRange`` ポリシー、 ``TeamVectorRange`` ポリシー、 ``TeamVectorMDRange`` ポリシー
	  または、 ``ThreadVectorMDRange`` ポリシーを使用して、ディスパッチされた並列演算内で、コンストラクタを呼び出すことは出来ません。

制約
------------

 <../parallel-dispatch/parallel_reduce.html>`_ において使用される場合には、 還元は、合計に限定されることに注意してください。

例
--------

.. code-block:: cpp

   using TeamHandle = TeamPolicy<>::member_type;

   parallel_for(TeamPolicy<>(N, Kokkos::AUTO),
     KOKKOS_LAMBDA(TeamHandle const& team) {
       int leagueRank = team.league_rank();

       auto teamThreadRange = TeamThreadRange(team, n0);
       auto threadVectorMDRange =
           ThreadVectorMDRange<Rank<3>, TeamHandle>(
               team, n1, n2, n3);

       parallel_for(teamThreadRange, [=](int i0) {
         parallel_for(threadVectorMDRange, [=](int i1, int i2, int i3) {
           A(leagueRank, i0, i1, i2, i3) += B(leagueRank, i1) + C(i1, i2, i3);
         });
       });
       team.team_barrier();

       int teamSum = 0;
       parallel_for(teamThreadRange, [=, &teamSum](int const& i0) {
         int threadSum = 0;
         parallel_reduce(threadVectorMDRange,
           [=](int i1, int i2, int i3, int& vectorSum) {
             vectorSum += D(leagueRank, i0, i1, i2, i3);
           }, threadSum
         );

         teamSum += threadSum;
       });
   });
