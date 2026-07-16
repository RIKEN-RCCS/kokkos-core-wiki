はじめに
########

.. toctree::
   :maxdepth: 1
   :hidden:

   get-started/quick-start
   get-started/requirements
   get-started/integrating-kokkos-into-your-cmake-project
   get-started/building-from-source
   get-started/configuration-guide
   get-started/package-managers
   get-started/advanced-configuration-and-build

今すぐ Kokkos を試してみませんか？ `Compiler Explorer <https://godbolt.org/z/svrE563Kn>`_ でご確認ください。

:doc:`クイックスタート <get-started/quick-start>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本ガイドでは、CMake プロジェクトを開始し、Kokkos コードの作成を開始するための最小限の最初の手順を説明します。

:doc:`Kokkos をプロジェクトに統合 <get-started/integrating-kokkos-into-your-cmake-project>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本ガイドでは、Kokkos を使用するためにプロジェクトを設定する方法について詳しく説明します。

:doc:`必要要件 <get-started/requirements>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本ページでは、Kokkos のビルドと使用に必要な様々なコンポーネント（ビルドシステム、ベンダーツールチェーン、コンパイラ、C++ 標準、ターゲットアーキテクチャ（CPU および GPU の両方）など）のサポート対象バージョンについて詳しく説明します。これらのコンポーネントの互換性のある組み合わせを網羅した表も用意しています。

:doc:`ソースからの構築 <get-started/building-from-source>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本ガイドでは、Kokkos ソースコードのダウンロード、ビルドシステムを生成するための構成、ライブラリのコンパイル、システムへのインストールの手順について説明します。

:doc:`設定ガイド <get-started/configuration-guide>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本ページでは、特定のハードウェア設定を対象とするバックエンドの選択、一般およびバックエンド固有の CMake オプション、サードパーティライブラリの使用の制御、サポートされている CPU および GPU アーキテクチャの完全なリストなど、すべての Kokkos 構成オプションに関する包括的なリファレンスを提供します。

:doc:`パッケージマネージャー <get-started/package-managers>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本ページでは、ソースからビルドする代わりに便利な代替手段として、ビルド済みの Kokkos パッケージを提供するパッケージマネージャーを紹介しています。

:doc:`高度な構成とビルド <get-started/advanced-configuration-and-build>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
このページでは、Kokkos で利用可能な構成とビルドに関する高度なトピックを一覧で紹介します。
