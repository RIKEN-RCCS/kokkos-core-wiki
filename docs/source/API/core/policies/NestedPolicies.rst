``NestedPolicies``
==================

.. ロール:: cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

リスト
----

``Kokkos::PerTeam``
~~~~~~~~~~~~~~~~~~~

``Kokkos::PerThread``
~~~~~~~~~~~~~~~~~~~~~

``Kokkos::TeamThreadRange``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Kokkos::TeamThreadMDRange``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Kokkos::TeamVectorRange``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Kokkos::TeamVectorMDRange``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Kokkos::ThreadVectorRange``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Kokkos::ThreadVectorMDRange``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

汎用テンプレート引数
~~~~~~~~~~~~~~~~~~~~~~~~~~

有効なテンプレートの引数はここ <../Execution-Policies.html#common-arguments-for-all-execution-policies>`_　で説明します。

使用例
~~~~~

.. code-block:: cpp

    parallel_for(TeamThreadRange(チーム,開始,終了), [=] (int i) {});
    parallel_for(ThreadVectorRange(チーム,開始,終了), [=] (int i) {});
    single(PerTeam(team), [=] () {});
    single(PerThread(team), [=] () {});

ネストポリシーは、ネスト並列パターンに使用できます。グローバルポリシーとは異なり、ネストポリシーのパブリックインターフェースは関数として実装されており、チームハンドルを通じて実行空間タイプに、暗示的テンプレート化が可能になります。

シノプシス
~~~~~~~~

.. code-block:: cpp

    Impl::TeamThreadRangeBoundariesStruct TeamThreadRange(TeamMemberType team, IndexType count);
    Impl::TeamThreadRangeBoundariesStruct TeamThreadRange(TeamMemberType team, IndexType begin, IndexType end);
    Impl::ThreadVectorRangeBoundariesStruct ThreadVectorRange(TeamMemberType team, IndexType count);
    Impl::ThreadVectorRangeBoundariesStruct ThreadVectorRange(TeamMemberType team, IndexType begin, IndexType end);
    Impl::ThreadSingleStruct PerTeam(TeamMemberType team);
    Impl::VectorSingleStruct PerThread(TeamMemberType team);

ディスクリプション
~~~~~~~~~~~

.. cpp:function:: Impl::TeamThreadRangeBoundariesStruct TeamThreadRange(TeamMemberType team, IndexType count);

    チームのスレッド上でインデックス範囲 ``0`` から ``count-1`` まで分割します。このコールはチームにとって同期ポイントとなる可能性があり、 ``team_barrier``　の要件を満たす必要があります .
        - ``team``: TeamHandleの要件を満たすオブジェクト
        - ``count``: インデックス範囲長

.. cpp:function:: Impl::TeamThreadRangeBoundariesStruct TeamThreadRange(TeamMemberType team, IndexType begin, IndexType end);

    チームのスレッドでインデックス範囲 ``begin`` から ``end-1`` まで分割  します。このコールはチームの同期ポイントとなる可能性があり、 ``team_barrier``の要件を満たす必要があります。
        - ``team``: TeamHandleの要件を満たすオブジェクト
        - ``begin``: 開始インデックス。
        - ``end``: 終了インデックス。

.. cpp:function:: Impl::ThreadVectorRangeBoundariesStruct ThreadVectorRange(TeamMemberType team, IndexType count);

    呼び出しスレッドのベクトルレーン上でインデックスレンジ　 ``0`` から ``count-1`` まで分割します。この関数をベクトルレベルループ内で呼び出すことは、合法ではありません。
        - ``team``: TeamHandleの要件を満たすオブジェクト
        - ``count``: インデックス範囲長

.. cpp:function:: Impl::ThreadVectorRangeBoundariesStruct ThreadVectorRange(TeamMemberType team, IndexType begin, IndexType end);

    呼び出しスレッドのベクトルレーン上でインデックス範囲 ``begin`` から ``end-1`` まで分割します。この関数をベクトルレベルループ内で呼び出すことは、合法ではありません。
        - ``team``: TeamHandleの要件を満たすオブジェクト
        - ``begin``: 開始インデックス。
        - ``end``: 終了インデックス。

.. cpp:function:: Impl::ThreadSingleStruct PerTeam(TeamMemberType team);

     ``single`` パターンと組み合わせて使用すると、コールチーム内の単一のベクターレーンへの実行が、制限されます。同期イベントではありませんが、このコールはチーム全体が遭遇し、 ``team_barrier``　の呼び出し要件を満たす必要があります。
        - ``team``: TeamHandleの要件を満たすオブジェクト

.. cpp:function:: Impl::VectorSingleStruct PerThread(TeamMemberType team);

     ``single`` パターンと組み合わせて使用すると、呼び出しスレッド内の単一のベクターレーンへの実行が、制限されます。 この関数をベクトルレベルループ内で呼び出すことは合法ではありません。
        - ``team``: object meeting the requirements of TeamHandle

例
~~~~~~~~

.. code-block:: cpp

    型定義 TeamPolicy<>::member_type team_handle;
    parallel_for(TeamPolicy<>(N,AUTO,4), KOKKOS_LAMBDA (const team_handle& team) {
        int n = team.league_rank();
        parallel_for(TeamThreadRange(team,M), [&] (const int& i) {
            int thread_sum;
            parallel_reduce(ThreadVectorRange(team,K), [&] (const int& j, int& lsum) {
                //...
            },thread_sum);
            single(PerThread(team), [&] () {
                A(n,i) += thread_sum;
            });
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
