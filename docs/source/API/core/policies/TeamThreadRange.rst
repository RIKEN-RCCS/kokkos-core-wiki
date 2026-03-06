``TeamThreadRange``
===================

.. role::cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

    parallel_for(TeamThreadRange(team,range), [=] (int i) {...});
    parallel_reduce(TeamThreadRange(team,begin,end), 
        [=] (int i, double& lsum) {...},sum);
    parallel_scan(TeamThreadRange(team,begin,end),
        [=] (lint i, double& lsum, bool final) {...},sum);

TeamThreadRangeは  、階層的並列処理内で使われる、 `nested execution policy <./NestedPolicies.html>`_です。 グローバルポリシーとは異なり、ネストポリシーのパブリックインターフェースは関数として実装されており、チームハンドルを通じて実行空間タイプに、暗示的にテンプレート化することが可能になります。

シノプシス
--------

.. code-block:: cpp
    
    template<class TeamMemberType, class iType>
    /* 定義された実装 */ TeamThreadRange(TeamMemberType team, iType count);
    
    template<class TeamMemberType, class iType1, class iType2>
    /* 定義された実装 */ TeamThreadRange(TeamMemberType team, iType1 begin, iType2 end);

ディスクリプション
-----------

.. code-block:: cpp

    template<class TeamMemberType, class iType>
    /* 定義された実装 */ TeamThreadRange(TeamMemberType team, iType count);

\
    チームのスレッド全体でインデックスレンジ　``0`` から ``count-1`` までを分割します。

    * **引数**  
        - ``team``: 呼び出しチーム実行コンテキストへのハンドル。
        - ``count``: インデックス範囲長

    * **返し**    
        - 実装定義型。

    * **必要要件**   
        - ``TeamMemberType`` は、 `TeamHandle <./TeamHandleConcept.html>`_　をモデル化する型です。
        - ``std::is_integral<iType>::value`` は、真です。
        -  ``team`` のすべてのメンバースレッドは、同じブランチで演算を呼び出す必要があり、つまり一部のスレッドが一つのブランチでこの関数を呼び出し、 ``team`` の他のスレッドが別のブランチで呼び出すことは、合法ではありません。 
        - ``count >= 0`` は、真です;
 
.. code-block:: cpp
    
    template<class TeamMemberType, class iType1, class iType2>
    /* Implementation defined */ TeamThreadRange(TeamMemberType team, iType1 begin, iType2 end);
   
\
    チームのスレッド全体でインデックスレンジ ``begin`` から``end-1`` までを分割します。

    * **引数**   
        - ``team``: 呼び出しチーム実行コンテキストへのハンドル。
        - ``begin``: インデックス範囲開始。
        - ``end``: インデックス範囲終了。

    * **返し**   
        - 実装定義型

    * **必要要件**   
        - ``TeamMemberType`` は、 `TeamHandle <./TeamHandleConcept.html>`_　をモデル化する型です。
        - ``std::is_integral<iType1>::value`` は、真です。
        - ``std::is_integral<iType2>::value`` は、真です。
        -  ``team`` のすべてのメンバースレッドは同じブランチで演算を呼び出す必要があり、つまり一部のスレッドが一つのブランチでこの関数を呼び出し、``team`` の他のスレッドが別のブランチで呼び出すことは、合法ではありません。
        - ``end >= begin`` は、真です;

例
--------

.. code-block:: cpp

    型定義 TeamPolicy<>::member_type team_handle;
    parallel_for(TeamPolicy<>(N,AUTO,4), KOKKOS_LAMBDA (const team_handle& team) {
        int n = team.league_rank();
        parallel_for(TeamThreadRange(team,M), [&] (const int& i) {
            A(n,i) = B(n) + i;
        });
        team.team_barrier();
        int team_sum;
        parallel_reduce(TeamThreadRange(team,M), [&] (const int& i, int& lsum) {
            lsum += A(n,i);
        },team_sum);
        single(PerTeam(team),[&] () {
            A_rowsum(n) += team_sum;
        });
    });
