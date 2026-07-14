``ThreadVectorRange``
=====================

ヘッダーファイル: ``Kokkos_Core.hpp``

使用方法

.. code-block:: cpp

   parallel_for(ThreadVectorRange(team,range), [=] (int i) {...});
   parallel_reduce(ThreadVectorRange(team,begin,end), 
     [=] (int i, double& lsum) {...},sum);
   parallel_scan(ThreadVectorRange(team,range), 
     [=] (int i, double& lsum, bool final) {...});

階層的並列処理の中で使われる  `nested execution policy <NestedPolicies.html>`__ です。 グローバルポリシーとは異なり、ネストポリシーのパブリックインターフェースは、チームハンドルを通じて実行空間タイプに暗示的なテンプレート化が可能になるように、関数として実装されています。

概要
-----------

.. code-block:: cpp

   template<class TeamMemberType, class iType>
   /* 実装により定義 */ ThreadVectorRange(TeamMemberType team, iType count);
   template<class TeamMemberType, class iType1, class iType2>
   /* 実装により定義 */ ThreadVectorRange(TeamMemberType team, iType1 begin, iType2 end);


説明
------------------

.. code-block:: cpp

   template<class TeamMemberType, class iType>
   /* 実装により定義 */ ThreadVectorRange(TeamMemberType team, iType count);
   

チームのスレッドとベクトルレーンのインデックス範囲  ``0`` から ``count-1`` まで分割します。
   
*  **引数**:

   * ``team``: 呼び出しチーム実行コンテキストへのハンドルです。

   * ``count``: インデックス範囲長 

*  **戻り値**:

   * 実装定義型。

*  **必要要件**

   * ``TeamMemberType`` は、 `TeamHandle <TeamHandleConcept>`__ をモデル化する型です

   * ``std::is_integral<iType>::value`` は、真です。

   * ``count >= 0`` は、真です;

   * 本関数を、 `TeamVectorRange <TeamVectorRange>`__ ポリシー または ``ThreadVectorRange`` ポリシーを使用してディスパッチされた、並列演算内で呼び出すことはできません。


.. code-block:: cpp

   template<class TeamMemberType, class iType1, class iType2>
   /* 実装により定義 */ ThreadVectorRange(TeamMemberType team, iType1 begin, iType2 end);


呼び出しスレッドのベクトルレーン全体で、インデックスレンジ ``begin`` から  ``end-1`` までを分割します。

*  **引数**

   * ``team``: 呼び出しチーム実行コンテキストへのハンドル

   * ``begin``: インデックス範囲開始。

   * ``end``: インデックス範囲終了。

*  **戻り値**

   * 実装定義型

* **必要要件**:

  * ``TeamMemberType`` は、 `TeamHandle <TeamHandleConcept.html>`__  をモデル化する型です 
  
  * ``std::is_integral<iType1>::value`` は、真です。

  * ``std::is_integral<iType2>::value`` は、真です。

  * ``end >= begin`` は、真です;

  * 本関数を、`TeamVectorRange <TeamVectorRange>`__ ポリシーまたは、 ``ThreadVectorRange`` ポリシーを使用してディスパッチされた並列演算内で呼び出すことはできません。

  
例
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
