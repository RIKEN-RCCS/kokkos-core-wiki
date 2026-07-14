.. role:: raw-html-m2r(raw)
   :format: html

.. include:: mydefs.rst

Kokkos: プログラミングモデル
=============================

.. admonition:: :medium:`C++ Performance Portability Programming Model`
    :class: important

    :medium:`Kokkos Core は、主要な HPC プラットフォームすべてを対象とした、パフォーマンスポータブルなアプリケーションを記述するための C++ によるプログラミングモデルを実装しています。 その目的のために、コードの並列実行とデータ管理の両方に対する抽象化を提供します。 Kokkos は、N 階層のメモリ階層と複数の種類の実行リソースを備えた複雑なノードアーキテクチャを対象に設計されています。 現在、Kokkos は、CUDA、HIP、SYCL、HPX、OpenMP、C++ スレッドをバックエンドプログラミングモデルとして利用可能であり、その他複数のバックエンドも開発中です。`

`Kokkos エコシステム <https://github.com/kokkos>`_ は以下を含みます:

.. list-table::
   :widths: 30 50 20
   :header-rows: 1
   :align: left

   * - 名前
     - 情報
     -

   * - ``kokkos``
     - (本ライブラリ) プログラミングモデル - 並列実行とメモリ抽象化  
     - `GitHub リンク <https://github.com/kokkos/kokkos>`__

   * - ``kokkos-kernels``
     - スパース、デンス、バッチ処理された数学カーネル
     - `GitHub リンク <https://github.com/kokkos/kokkos-kernels>`__

   * - ``kokkos-tools``
     - プロファイリングおよびデバッグツール
     - `GitHub リンク <https://github.com/kokkos/kokkos-tools>`__

   * - ``pykokkos``
     - Kokkos のパフォーマンスポータブル並列プログラミングへの Python バインディングを提供します。
     - `GitHub リンク <https://github.com/kokkos/pykokkos>`__

   * - ``kokkos-remote-spaces``
     - 複数プロセスにわたる共有メモリのセマンティクス
     - `GitHub リンク <https://github.com/kokkos/kokkos-remote-spaces>`__

   * - ``kokkos-resilience``
     - Kokkos 向けレジリエンスとチェックポイント拡張機能
     - `GitHub リンク <https://github.com/kokkos/kokkos-resilience>`__

C++ 標準ライブラリのための関連作業
-----------------------------------------

関連する取り組みには以下が含まれます:

.. list-table::
   :widths: 20 45 20 15
   :header-rows: 1
   :align: left

   * - 名前
     - 情報
     - 提案
     -

   * - ``mdspan``
     - C++23 を対象とした mdspan の参照実装
     - `P0009 <https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p0009r16.html>`__
     - `GitHub リンク <https://github.com/kokkos/mdspan>`__

   * - ``stdBLAS``
     - stdBLAS の参照実装
     - `P1673 <https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p1673r8.html>`__
     - `GitHub リンク <https://github.com/kokkos/stdBLAS>`__

質問？
----------

Slack (https://kokkosteam.slack.com) でご質問いただくか、`github <https://github.com/kokkos/kokkos/issues>`_ にイシューを作成してください。

ウェブサイトコンテンツ
-----------------------------

.. toctree::
   :maxdepth: 1

   get-started
   programmingguide
   api-references
   tutorials-and-examples
   contributing
   GitHub Repo <https://github.com/kokkos/kokkos>
   known-issues
   faq
   citation
   license
