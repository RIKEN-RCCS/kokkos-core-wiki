組み込みリデューサー
====================

 `ReducerConcept <builtinreducers/ReducerConcept.html>`__ は、リデューサーの概念を提供します。

 `parallel_reduce <parallel-dispatch/parallel_reduce.html>`__ と組み合わせて使用されるリデューサーオブジェクト。

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - リデューサー
     - 説明
   * - `BAnd <builtinreducers/BAnd.html>`__
     - バイナリ 'And' 縮約
   * - `BOr <builtinreducers/BOr.html>`__
     - バイナリ 'Or' 縮約
   * - `FirstLoc <builtinreducers/FirstLoc.html>`__
     - 条件を満たす最初のインデックスを提供する縮約
   * - `LAnd <builtinreducers/LAnd.html>`__
     - 論理的 'And' 縮約
   * - `LastLoc <builtinreducers/LastLoc.html>`__
     - 条件を満たす最後のインデックスを提供する縮約
   * - `LOr <builtinreducers/LOr.html>`__
     - 論理的' Or' 縮約
   * - `Max <builtinreducers/Max.html>`__
     - 最大縮約
   * - `MaxFirstLoc <builtinreducers/MaxFirstLoc.html>`__
     - 最大値および関連する最初のインデックスを提供する縮約
   * - `MaxLoc <builtinreducers/MaxLoc.html>`__
     - 最大値および関連インデックスを提供する縮約
   * - `Min <builtinreducers/Min.html>`__
     - 最小縮約
   * - `MinFirstLoc <builtinreducers/MinFirstLoc.html>`__
     - 最小値および関連する最初のインデックスを提供する縮約
   * - `MinLoc <builtinreducers/MinLoc.html>`__
     - 最小値および関連インデックスを提供する縮約
   * - `MinMax <builtinreducers/MinMax.html>`__
     - 最小値および最大値の両方を提供する縮約
   * - `MinMaxFirstLastLoc <builtinreducers/MinMaxFirstLastLoc.html>`__
     - 最小値および最大値の両方並びに関連する最初と最後のインデックスを提供する縮約
   * - `MinMaxLoc <builtinreducers/MinMaxLoc.html>`__
     - 最小値および最大値の両方並びに関連インデックスを提供する縮約
   * - `Prod <builtinreducers/Prod.html>`__
     - 乗法的縮約
   * - `Sum <builtinreducers/Sum.html>`__
     - 和の縮約

:cpp:struct:`reduction_identity` は、様々な縮約演算における中和元（恒等値）を定義します。 特化処理は、組み込みリデューサーがユーザー定義型と連動するために不可欠です。

`縮約スカラー型 <builtinreducers/ReductionScalarTypes.html>`__ は、リデューサーのストレージ用テンプレートクラスです。

.. toctree::
   :hidden:
   :maxdepth: 1

   ./builtinreducers/ReducerConcept
   ./builtinreducers/BAnd
   ./builtinreducers/BOr
   ./builtinreducers/FirstLoc
   ./builtinreducers/LAnd
   ./builtinreducers/LastLoc
   ./builtinreducers/LOr
   ./builtinreducers/Max
   ./builtinreducers/MaxFirstLoc
   ./builtinreducers/MaxLoc
   ./builtinreducers/Min
   ./builtinreducers/MinFirstLoc
   ./builtinreducers/MinLoc
   ./builtinreducers/MinMax
   ./builtinreducers/MinMaxFirstLastLoc
   ./builtinreducers/MinMaxLoc
   ./builtinreducers/Prod
   ./builtinreducers/Sum
   ./builtinreducers/ReductionScalarTypes
   ./builtinreducers/reduction_identity
