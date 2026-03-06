``ParallelReduceTag``
=====================

.. role::cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_ExecPolicy.hpp>``

.. _parallelReduce: ../parallel-dispatch/parallel_reduce.html

.. |parallelReduce| replace:: :cpp:func:`parallel_reduce`

チーム規模の要求対象となるファンクターを示すための、チーム規模計算機能で使用されるタグは、 |parallelReduce|_　に使用されています。

使用例
-----

.. code-block:: cpp

    PolicyType = Kokkos::TeamPolicy<>　を使用; 
    PolicyType policy;
    int recommended_team_size = policy.team_size_recommended(
        Functor, Kokkos::ParallelReduceTag());

シノプシス
--------

.. code-block:: cpp

    構造体 ParallelReduceTag{};

パブリックメンバー関数
--------------------

無し

型定義
~~~~~~~~

無し

コンストラクタ
~~~~~~~~~~~~

デフォルト

関数
~~~~~~~~~

無し
