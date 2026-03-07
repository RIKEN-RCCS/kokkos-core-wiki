``ThreadVectorRange``
=====================

ヘッダーファイル: ``Kokkos_Core.hpp``

使用例: 

.. code-block:: cpp

   parallel_for(ThreadVectorRange(team,range), [=] (int i) {...});
   parallel_reduce(ThreadVectorRange(team,begin,end), 
     [=] (int i, double& lsum) {...},sum);
   parallel_scan(ThreadVectorRange(team,range), 
     [=] (int i, double& lsum, bool final) {...});

.階層的並列処理の中で使われる  `nested execution policy <NestedPolicies.html>`__ です。 グローバルポリシーとは異なり、ネストポリシーのパブリックインターフェースは、チームハンドルを通じて実行空間タイプに暗示的なテンプレート化が可能になるように、関数として実装されています。

シノプシス 
--------

.. code-block:: cpp

   template<class TeamMemberType, class iType>
   /* 定義された実装 */ ThreadVectorRange(TeamMemberType team, iType count);
   template<class TeamMemberType, class iType1, class iType2>
   /* 定義された実装 */ ThreadVectorRange(TeamMemberType team, iType1 begin, iType2 end);


ディスクリプション
-----------

.. code-block:: cpp

   template<class TeamMemberType, class iType>
   /* 定義された実装 */ ThreadVectorRange(TeamMemberType team, iType count);
   

チームのスレッドとベクトルレーンのインデックス範囲  ``0`` から ``count-1`` まで分割します。
   
*  **引数**:

   * ``team``: 呼び出しチーム実行コンテキストへのハンドルです。

   * ``count``: インデックス範囲長 

*  **返し**:

   * 実装定義型。

*  **必要要件**

   * ``TeamMemberType`` は、 `TeamHandle <TeamHandleConcept>`__　をモデル化する型です

   * ``std::is_integral<iType>::value`` は、真です。

   * ``count >= 0`` は、真です;

   * 本関数を、 `TeamVectorRange <TeamVectorRange>`__ ポリシー または ``ThreadVectorRange`` ポリシーを使用してディスパッチされた、並列演算内で呼び出すことはできません。


.. code-block:: cpp

   template<class TeamMemberType, class iType1, class iType2>
   /* Implementation defined */ ThreadVectorRange(TeamMemberType team, iType1 begin, iType2 end);


Splits the index range ``begin`` to ``end-1`` over the vector lanes of the calling thread. 

*  **Arguments**

   * ``team``: a handle to the calling team execution context.

   * ``begin``: index range begin. 

   * ``end``: index range end.

*  **Returns**

   * Implementation defined type.

* **Requirements**:

  * ``TeamMemberType`` is a type that models `TeamHandle <TeamHandleConcept.html>`__   
  
  * ``std::is_integral<iType1>::value`` is true.

  * ``std::is_integral<iType2>::value`` is true.

  * ``end >= begin`` is true;

  * This function can not be called inside a parallel operation dispatched using a `TeamVectorRange <TeamVectorRange.html>`__ policy or ``ThreadVectorRange`` policy.

  
Examples
--------

.. code-block:: cpp

    typedef TeamPolicy<>::member_type team_handle;
    parallel_for(TeamPolicy<>(N,AUTO,4), KOKKOS_LAMBDA (const team_handle& team) {
     int n = team.league_rank();
     parallel_for(TeamThreadRange(team,M), [&] (const int i) {
       parallel_for(ThreadVectorRange(team,K), [&] (const int j) {
         A(n,i,j) = B(n,i) + j;
       });
     });
     team.team_barrier();
     int team_sum;
     parallel_reduce(TeamThreadRange(team,M), [&] (const int& i, int& threadsum) {
       int tsum = 0;
       parallel_reduce(ThreadVectorRange(team,K), [&] (const int& j, int& lsum) {
         lsum += A(n,i,j);
       },tsum);
       single(PerThread(team),[&] () {
         threadsum += tsum;
       });
     },team_sum);
       
       lsum += A(n,i);
     },team_sum);
     single(PerTeam(team),[&] () {
       A_rowsum(n) += team_sum;
     });
    });
