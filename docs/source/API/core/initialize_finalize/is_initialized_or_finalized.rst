``is_initialized`` と ``is_finalized``
======================================

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Core.hpp>`` で定義

使用方法
--------

.. code-block:: cpp

  if(Kokkos::is_initialized()) {
    // do work
  }
  if(!Kokkos::is_initialized() && Kokkos::is_finalized()) {
    // may initialize Kokkos
  }

関数 :cpp:func:`is_initialized` と :cpp:func:`is_finalized` は、アプリケーションが
Kokkos 実行環境の現在の状態を照会できるようにします。
Kokkos は厳密な線形ライフサイクルに従うため、これらの関数は初期化や終了処理が
ちょうど一度だけ発生することを保証するためによく使用されます。

インターフェース
----------------

.. cpp:function:: bool is_initialized() noexcept

   :return: Kokkos 実行環境が現在アクティブで使用可能な場合に ``true``。

.. cpp:function:: bool is_finalized() noexcept

   :return: Kokkos 実行環境が :cpp:func:`finalize` によってシャットダウンされた場合に
     ``true``。


補足
----
.. note:: **ライフサイクルステートマシン**

  Kokkos は3つの異なる状態を遷移します。Kokkos が一度終了処理されると、同一プロセスの
  実行内で再初期化 **できない** ことに注意してください。

  .. list-table::
     :widths: 25 20 20 35
     :header-rows: 1

     * - プログラムフェーズ
       - ``is_initialized()``
       - ``is_finalized()``
       - 説明
     * - 初期化前
       - ``false``
       - ``false``
       - Kokkos はまだアクティブではありません。
     * - アクティブ
       - ``true``
       - ``false``
       - ``initialize()`` が呼び出されています。カーネルを起動できます。
     * - 終了処理後
       - ``false``
       - ``true``
       - ``finalize()`` が呼び出されています。Kokkos はもう使用できません。

.. caution::

   **MPI との比較:** MPI に慣れているユーザーは、重要な違いに注意してください。
   MPI では、``MPI_Finalize`` が呼び出された後でも ``MPI_Initialized`` は
   ``true`` を返します。Kokkos では、``is_initialized()`` は終了処理後に
   ``false`` を返します。

   ``Kokkos::initialize()`` が一度でも呼び出されたかを確認するには、次のロジックを
   使用します:

   .. code-block:: cpp

      if (Kokkos::is_initialized() || Kokkos::is_finalized()) { ... }

例
--

.. code-block:: cpp

  #include <Kokkos_Core.hpp>
  #include <cstdio>
  
  int main(int argc, char* argv[]) {
    printf("before initialize: initialized=%d finalized=%d\n",
      Kokkos::is_initialized(), Kokkos::is_finalized());

    Kokkos::initialize();

    printf("kokkos active:     initialized=%d finalized=%d\n",
      Kokkos::is_initialized(), Kokkos::is_finalized());

    Kokkos::finalize();

    printf("after finalize:    initialized=%d finalized=%d\n",
      Kokkos::is_initialized(), Kokkos::is_finalized());
  }


出力:

.. code-block::

    before initialize: initialized=0 finalized=0
    kokkos active:     initialized=1 finalized=0
    after finalize:    initialized=0 finalized=1


参照
----

.. seealso::

  :doc:`initialize`
    Kokkos 実行環境を開始します。
  :doc:`finalize`
    Kokkos 実行環境を終了します。