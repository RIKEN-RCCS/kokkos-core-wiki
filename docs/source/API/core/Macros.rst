マクロ
======

``<Kokkos_Macros.hpp>``\ （これは ``<Kokkos_Core.hpp>`` がインクルードします）をインクルードすると、2種類のマクロにアクセスできます。

常に定義されるマクロ
--------------------

これらのマクロは、すべての Kokkos ビルドで定義されます。これらは、アプリケーションコード内で直接使用し、関数をマークしたり、ホストまたはデバイスのコードを選択したり、Kokkos のバージョンを確認したりすることを目的としています。

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 30 70

   * - ページ
     - 内容
   * - :doc:`関数アノテーション <macros-special/host_device_macros>`
     - ``KOKKOS_FUNCTION``、``KOKKOS_LAMBDA`` など、ホストやデバイスから呼び出すことができる関数をマークします。
   * - :doc:`条件付きホスト/デバイスコード <macros-special/if_on_host_or_device>`
     - ``KOKKOS_IF_ON_HOST`` および ``KOKKOS_IF_ON_DEVICE`` は、ホスト向けにコンパイルされるかデバイス向けにコンパイルされるかに応じてコードを選択します。
   * - :doc:`バージョン <macros/version>`
     - ``KOKKOS_VERSION`` と比較ヘルパーで、使用中の Kokkos のバージョンを確認します。

設定マクロ
----------

これらのマクロを使用すると、Kokkos がどのように設定されたか、例えばどのバックエンドが有効化されているかを確認できます。上記のマクロとは異なり、これらは対応するオプションが有効化されている場合にのみ定義されるため、``#ifdef`` または ``#if defined(...)`` でテストしてください。

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 30 70

   * - ページ
     - 内容
   * - :doc:`一般設定 <macros/general>`
     - デバッグ、非推奨、チューニング、C++標準、サードパーティライブラリ。
   * - :doc:`バックエンド <macros/backends>`
     - どの実行空間が有効化されているか、およびバックエンド固有のオプション。
   * - :doc:`アーキテクチャ <macros/architectures>`
     - ``KOKKOS_ARCH_*``: Kokkos が設定されたハードウェア。アプリケーションコードはこれらに依存すべきではありません。

.. _macros_configuration_relationship:

CMake 設定オプションとの関係
----------------------------

``KOKKOS_ENABLE_*`` および ``KOKKOS_ARCH_*`` マクロは、ほとんどの場合、:doc:`設定ガイド <../../get-started/configuration-guide>` に記載されている CMake オプションに対応しています。名前は単純なルールに従います:

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 40 40

   * - CMake オプション
     - マクロ
   * - ``Kokkos_ENABLE_<NAME>=ON``
     - ``KOKKOS_ENABLE_<NAME>`` が定義される
   * - ``Kokkos_ARCH_<NAME>=ON``
     - ``KOKKOS_ARCH_<NAME>`` が定義される
   * - ``CMAKE_CXX_STANDARD=<N>``
     - ``KOKKOS_ENABLE_CXX<N>`` が定義される

これらのマクロは、定義されているかどうかのいずれかです: 値ではなく、``#if defined(...)``、``#ifdef`` または ``#ifndef`` でテストしてください。``OFF`` のオプションはマクロを未定義のままにします。命名ルールの例外や、CMake に対応するものがないマクロは、各ページで明記されています。

.. code-block:: c++

   #include <Kokkos_Core.hpp>

   #ifdef KOKKOS_ENABLE_CUDA
   // Kokkos は -DKokkos_ENABLE_CUDA=ON で設定されました
   #endif

.. toctree::
   :hidden:
   :maxdepth: 1

   macros-special/host_device_macros
   macros-special/if_on_host_or_device
   macros/version
   macros/general
   macros/backends
   macros/architectures
