初期化及び最終処理完了
======================

以下の関数とクラスは、Kokkos 実行環境とリソースのクリーンアップを管理します。

.. list-table::
   :align: left

* - :doc:`initialize_finalize/initialize`
     - Kokkos の内部オブジェクトと、有効化されたすべての Kokkos バックエンドを初期化します。
   * - :doc:`initialize_finalize/finalize`
     - Kokkos 実行環境をシャットダウンし、内部で管理されているリソースを解放します。
   * - :doc:`initialize_finalize/InitializationSettings`
     - ランタイムの動作（スレッド数やデバイス ID など）を制御するノブを表すクラスです。
   * - :doc:`initialize_finalize/ScopeGuard`
     - 初期化と終了処理が正しく扱われることを保証する RAII ベースのアプローチです。
   * - :doc:`initialize_finalize/push_finalize_hook`
     - :cpp:func:`finalize` の呼び出し時に呼び出される関数を登録します。
   * - :doc:`initialize_finalize/is_initialized_or_finalized`
     - Kokkos の初期化ステータスを照会します。

.. toctree::
   :hidden:
   :maxdepth: 1

./initialize_finalize/initialize
   ./initialize_finalize/finalize
   ./initialize_finalize/InitializationSettings
   ./initialize_finalize/ScopeGuard
   ./initialize_finalize/push_finalize_hook
   ./initialize_finalize/is_initialized_or_finalized
