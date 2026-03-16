``TeamVectorRange``
===================

.. role::cpp(code)
   :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

   parallel_for(TeamVectorRange(team,range), [=] (int i) {...});
   parallel_reduce(TeamVectorRange(team,begin,end),
       [=] (int i, double& lsum) {...},sum);

階層的並列処理の中で使われる `nested execution policy <NestedPolicies.html>`_ です。 グローバルポリシーとは異なり、ネストポリシーのパブリックインターフェースは、チームハンドルを通じて実行空間タイプに暗示的なテンプレート化が可能になるように、関数として実装されています。

シノプシス
--------

.. code-block:: cpp

   template<class TeamMemberType, class iType>
   /* implementation defined */ TeamVectorRange(TeamMemberType team, iType count);
   template<class TeamMemberType, class iType1, class iType2>
   /* implementation defined */ TeamVectorRange(TeamMemberType team, iType1 begin, iType2 end);

ディスクリプション
-----------

.. code-block:: cpp

   template<class TeamMemberType, class iType>
   /* Implementation defined */ TeamVectorRange(TeamMemberType team, iType count);

チームのスレッドとベクトルレーンのインデックス範囲 ``0``  から ``count-1`` まで分割します。

* **引数**
    - ``team``: 呼び出しチーム実行コンテキストへのハンドルです。
    - ``count``: インデックス範囲長。

* **リターン**
    - 実装定義型。

* **必要要件**
    - ``TeamMemberType`` は、 `TeamHandle <TeamHandleConcept.html>`_　をモデル化する型です。
    - ``std::is_integral<iType>::value`` は、真です。
    - ``team`` のすべてのメンバースレッドは同じブランチで演算を呼び出す必要があり、つまり一部のスレッドが一つのブランチでこの関数を呼び出し、 ``team`` の他のスレッドが別のブランチで呼び出すことは、合法ではありません。
    - ``count >= 0`` は、真です;

.. code-block:: cpp

   template<class TeamMemberType, class iType1, class iType2>
   /* implementation defined */ TeamVectorRange(TeamMemberType team, iType1 begin, iType2 end);

チームのスレッドとベクトルレーンのインデックス範囲 ``begin`` から　``end-1`` まで分割します。

* **引数**
    - ``team``: 呼び出しチーム実行コンテキストへのハンドル
    - ``begin``: インデックス範囲開始。
    - ``end``: インデックス範囲終了。

* **返し**
    - 実装定義型。

* **必要要件**
    - ``TeamMemberType`` は、 `TeamHandle <TeamHandleConcept.html>`_　をモデル化する型です。
    - ``std::is_integral<iType1>::value`` は、真です。
    - ``std::is_integral<iType2>::value`` は、真です。
    - ``team`` のすべてのメンバースレッドは同じブランチで演算を呼び出す必要があり、つまり一部のスレッドが一つのブランチでこの関数を呼び出し、 ``team`` の他のスレッドが別のブランチで呼び出すことは、合法ではありません。
    - ``end >= begin`` は、真です;

例
--------

.. code-block:: cpp

   typedef TeamPolicy<>::member_type team_handle;
   parallel_for(TeamPolicy<>(N,AUTO,4), KOKKOS_LAMBDA (const team_handle& team) {
       int n = team.league_rank();
       parallel_for(TeamVectorRange(team,M), [&] (const int& i) {
           A(n,i) = B(n) + i;
       });
       team.team_barrier();
       int team_sum;
       parallel_reduce(TeamVectorRange(team,M), [&] (const int& i, int& lsum) {
           lsum += A(n,i);
       },team_sum);
       single(PerTeam(team),[&] () {
           A_rowsum(n) += team_sum;
       });
   });
