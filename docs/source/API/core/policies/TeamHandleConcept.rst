``TeamHandleConcept``
=====================

.. role:: cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

TeamHandleConcept　は、　``TeamPolicy``　と ``TeamTask``　の ``member_type`` の概念を定義しています。 実際のタイプはポリシーで定義されますが、以下の　API　を満たしています。 特定のクラスは、``TeamPolicy`` および
``TeamTask`` が提供する公開　API　の一部であり、 ``TeamHandleConcept``　で定義された部分のみであることに、注意してください。 
クラスの実際の名称やテンプレートパラメータ、既存のコンストラクタ、概念を超えたメンバー関数などは公開された　Kokkos API　の一部ではないため、変更の対象となります。


ディスクリプション
-----------

.. cpp:class:: TeamHandleConcept


   .. rubric:: 公開ネストエイリアス

   .. cpp:type:: execution_space

     チームに関連付けられた実行空間 <https://kokkos.github.io/kokkos-core-wiki/API/core/execution_spaces.html>`_　を特定します。

   .. cpp:type:: scratch_memory_space

      このチームの実行空間に関連するスクラッチメモリ空間

   .. rubric:: コンストラクタ

   .. cpp:function:: TeamHandleConcept() = default

      デフォルトコンストラクタ。

   .. cpp:function:: TeamHandleConcept( TeamHandleConcept && ) = default

      移動コンストラクタ。

   .. cpp:function:: TeamHandleConcept( TeamHandleConcept const & ) = default

      コピコンストラクタ。

   .. cpp:function:: ~TeamHandleConcept() = default

      デストラクタ。

   .. rubric:: 代入

   .. cpp:function:: TeamHandleConcept & operator = ( TeamHandleConcept && ) = default

      移動代入。

   .. cpp:function:: TeamHandleConcept & operator = ( TeamHandleConcept const & ) = default

      代入演算子。 返し: ``*this``.

   .. rubric:: インデックス照会

   .. cpp:function:: KOKKOS_INLINE_FUNCTION int team_rank() const noexcept ;

      返し:  ``0 <= i < team_size()``　を使って、チーム内の呼び出しスレッドのインデックス 　``i``　

   .. cpp:function:: KOKKOS_INLINE_FUNCTION int team_size() const noexcept ;

      返し: チームに関連付けられたスレッド数。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION int league_rank() const noexcept ;

      返し:  ``0 <= i < league_size()``を使って、リーグ内の呼び出しスレッドのインデックス 　``i``

   .. cpp:function:: KOKKOS_INLINE_FUNCTION int league_size() const noexcept ;

      返し: the number of teams/workitems launched in the kernel.カーネル内で起動したチーム/ワークアイテムの数


   .. rubric:: スクラッチ空間コントロール

   .. cpp:function:: KOKKOS_INLINE_FUNCTION const scratch_memory_space & team_shmem() const ;

       ``team_scratch(0)``　呼び出しに匹敵します。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION const scratch_memory_space & team_scratch(int level) const ;

      この関数はチーム内のすべてのスレッドが共有するスクラッチメモリのハンドルを返し、スクラッチメモリへのアクセスを可能にします。
      本ハンドルは、 ``Kokkos::View``の最初の引数として与えられ、スクラッチメモリとして使用することができます。
      ハンドルは、 ``Kokkos::View`` 割り当てのサイズに応じて、自動的に増加します。

      - ``level``: 要求されたスクラッチメモリのレベルは、 ``0`` または ``1``　のいずれかです。

      - リターン: レベルにより特定されたチームで共有するスクラッチメモリへのスクラッチメモリハンドル。

   .. cpp:function:: KOKKOS_INLINE_FUNCTION const scratch_memory_space & thread_scratch(int level) const ;

      本関数は、呼び出しスレッド固有のスクラッチメモリハンドルを返し、それにより、プライベートなスクラッチメモリへのアクセスが可能になります。 本ハンドルは、 ``Kokkos::View`` の最初の引数として与えられ、スクラッチメモリとして、それを使用することができます。


      - ``level``: 要求されたスクラッチメモリのレベルは、 ``0`` または ``1``　のいずれかです。

      - Returns: レベルにより特定されたチームで共有するスクラッチメモリへのスクラッチメモリハンドル。


   .. rubric:: チーム集合演算子

   以下の関数は、チームの全メンバーがまとめて呼び出さなければなりません。
   これらの呼び出しは語彙的に同一でなければならず、つまりチームの一部が、一方のブランチでコレクティブを呼び、他のメンバーが別のブランチで呼び出すことは、合法ではありません　(例を参照)。


   .. cpp:function:: KOKKOS_INLINE_FUNCTION void team_barrier() const noexcept ;

      チーム全員が、全員が到着するまでバリアで待機します。これもまた、メモリーフェンスを発行します。

   .. cpp:function:: template<typename T> KOKKOS_INLINE_FUNCTION void team_broadcast( T & value , const int source_team_rank ) const noexcept;

      本呼び出しの後、 ``var`` は、チームの全メンバーに対して、``team_rank() == source_team_rank``　であるスレッドからの　``var``　の値を含みます。

      - ``var``: ``T``　の変数で、ソースランクの ``var`` の値によって、上書きされます。

      - ``source_team_rank``: チームのブロードキャストメンバーを特定します。

   .. cpp:function:: template<class Closure, typename T> KOKKOS_INLINE_FUNCTION void team_broadcast( Closure const & f , T & value , const int source_team_rank) const noexcept;

      本呼び出しの後、 ``f`` 適用後に、``var`` は、チームの全メンバーに対して、``team_rank() == source_team_rank``　であるスレッドからの　``var``　の値を含みます。

      - ``f``: ブロードキャスト前に ``var`` に適用された　``void operator() ( T & )`` を伴う関数オブジェクト。

      - ``var``: ''T'' 型の変数で、元のランクの値  ``f(var)``  によって、上書きされます。

      - ``source_team_rank``: チームのブロードキャストメンバーを特定します。

   .. cpp:function:: template< typename ReducerType> KOKKOS_INLINE_FUNCTION void team_reduce( ReducerType const & reducer ) const noexcept;

      Performs a reduction across all members of the team as specified by ``reducer``. ``ReducerType`` must meet the concept of ``Kokkos::Reducer``.

   .. cpp:function:: template< typename T > KOKKOS_INLINE_FUNCTION T team_scan( T const & value , T * const global = 0 ) const noexcept;

      チームメンバーが提供する ``var`` に対して、エクスクルーシブスキャンを行います。  ``t = team_rank()`` および ``VALUES[t]``　を、 the value of from スレッド ``t``　からの　``var`` の値とします。

      - リターン: ``VALUES[0]`` + ``VALUES[1]`` + ``...`` + ``VALUES[t-1]`` または ``t==0``　の0。

      - ``global`` が指定されている場合は、 ``VALUES[0]`` + ``VALUES[1]`` + ``...`` + ``VALUES[team_size()-1]``に設定され、すべてのチームメンバーについて、同じポインタでなければなりません。

例
--------

.. code-block:: cpp

    型定義 TeamPolicy<...> policy_type;
    parallel_for(policy_type(N,TEAM_SIZE).set_scratch_size(PerTeam(0,4096)),
                KOKKOS_LAMBDA (const typename policy_type::member_type& team_handle) {
        int ts = team_handle.team_size(); // returns TEAM_SIZE
        int tid = team_handle.team_rank(); // returns a number between 0 and TEAM_SIZE
        int ls = team_handle.league_size(); // returns N
        int lid = team_handle.league_rank(); // returns a number between 0 and N

        int value = tid * 5;
        team_handle.team_broadcast(value, 3);
        // あらゆるスレッド上で、value==15 
        value += tid;
        team_handle.team_broadcast([&] (int & var) { var*=2 }, value, 2);
        // value==34 on every thread
        int global;
        int scan = team_handle.team_scan(tid+1, &global);
        // あらゆるスレッド上で、scan == tid*(tid+1)/2 
        // あらゆるスレッド上で、global == ts*(ts-1)/2 
        //  team_handle.team_scratch(0) がポインタに減衰するため、本ビューは、管理対象外特性を必要としません。
        // しかし、ここでは明確にするために追加しています。渡されたポインタが、管理対象外ビューを作成するビュー構造体の引き金となります。
        Kokkos::View<int*, policy_type::execution_space::scratch_memory_space, Kokkos::MemoryTraits<Kokkos::Unmanaged>>
        a(team_handle.team_scratch(0), 1024);

    });
