``ParallelScanTag``
===================

.. role::cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_ExecPolicy.hpp>``

.. _parallelScan: ../parallel-dispatch/parallel_scan.html

.. |parallelScan| replace:: :cpp:func:`parallel_scan`

チーム規模の要求対象となるファンクターを示すための、チーム規模計算機能で使用されるタグは、 |parallelScan|_ に使用されています。

使用例
-----

.. code-block:: cpp

    using PolicyType = Kokkos::TeamPolicy<>; 
    PolicyType policy;
    int recommended_team_size = policy.team_size_recommended(
        Functor, Kokkos::ParallelScanTag());

シノプシス
--------

.. code-block:: cpp

    struct ParallelScanTag{};

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
