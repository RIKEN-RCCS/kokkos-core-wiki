一般設定
========

このページのマクロは、Kokkos がどのように構成されたかを示します。それぞれのマクロは、対応する
:doc:`CMake オプション <../../../get-started/configuration-guide>`
が有効になっているときに定義されます（:ref:`macros_configuration_relationship`\ を参照）。

デバッグ
--------

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 50 50

   * - マクロ
     - 説明
   * - ``KOKKOS_ENABLE_DEBUG``
     - 追加のデバッグ機能が有効化されます。
   * - ``KOKKOS_ENABLE_DEBUG_BOUNDS_CHECK``
     - 追加の境界チェックが有効化されます。

Kokkos はこれらのチェックを自身で適用するため、主に情報提供を目的としています。
対応するオプションについては、構成ガイドの :ref:`debugging` を参照してください。

非推奨コード
------------

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 50 50

   * - マクロ
     - 説明
   * - ``KOKKOS_ENABLE_DEPRECATED_CODE_<N>``
     - メジャーリリース ``<N>`` で非推奨になった機能が引き続き利用可能です。
   * - ``KOKKOS_ENABLE_DEPRECATION_WARNINGS``
     - 非推奨機能が非推奨警告を生成します。

``KOKKOS_ENABLE_DEPRECATED_CODE_<N>`` は、複数の Kokkos バージョンでビルドする必要があるコードに役立ちます:

.. code-block:: c++

   #include <Kokkos_Core.hpp>

   #ifdef KOKKOS_ENABLE_DEPRECATED_CODE_4
   // Kokkos 4.x deprecated features are still available
   #endif

チューニングとパフォーマンス
----------------------------

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 50 50

   * - マクロ
     - 説明
   * - ``KOKKOS_ENABLE_TUNING``
     - チューニングツール用のバインディングが利用可能です（`#2422 <https://github.com/kokkos/kokkos/pull/2422>`_\ を参照）。
   * - ``KOKKOS_ENABLE_AGGRESSIVE_VECTORIZATION``
     - Kokkos 内部ループの積極的なベクトル化のため、特定の依存関係の仮定が無視されます。
   * - ``KOKKOS_ENABLE_COMPLEX_ALIGN``
     - 複素数型がアラインメントされます。このマクロには文書化された CMake オプションはありません。

C++ 標準
--------

Kokkos がコンパイルされた C++ 標準に一致する、ちょうど 1 つのマクロが定義されます。
アプリケーションは Kokkos と同じ標準（および同じコンパイラ）でコンパイルすべきであるため、
ほとんどのコードではこれらのマクロをテストする必要はありません。

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 30 50 30

   * - マクロ
     - 説明
     - 備考
   * - ``KOKKOS_ENABLE_CXX17``
     - Kokkos は C++17 言語標準でコンパイルされました。
     - Kokkos 5.0 で削除
   * - ``KOKKOS_ENABLE_CXX20``
     - Kokkos は C++20 言語標準でコンパイルされました。
     -
   * - ``KOKKOS_ENABLE_CXX23``
     - Kokkos は C++23 言語標準でコンパイルされました。
     -
   * - ``KOKKOS_ENABLE_CXX26``
     - Kokkos は C++26 言語標準でコンパイルされました。
     -

サードパーティライブラリ
------------------------

これらのマクロは、Kokkos がどのサードパーティライブラリでコンパイルされたかについての情報を提供します。
これらは、構成ガイドの :ref:`keywords_tpls` にリストされている ``Kokkos_ENABLE_<TPL>`` オプションに対応します。

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 30 70

   * - マクロ
     - 説明
   * - ``KOKKOS_ENABLE_HWLOC``
     - NUMA とアーキテクチャ情報のために `libhwloc <https://www.open-mpi.org/projects/hwloc/>`_ が有効化されます。
   * - ``KOKKOS_ENABLE_LIBDL``
     - Kokkos が動的リンカ（libdl）にリンクします。
   * - ``KOKKOS_ENABLE_LIBQUADMATH``
     - Kokkos が `GCC Quad-Precision Math Library API <https://gcc.gnu.org/onlinedocs/libquadmath/>`_ にリンクします。
   * - ``KOKKOS_ENABLE_ONEDPL``
     - SYCL バックエンドを使用する際に、Kokkos が `oneDPL ライブラリ <https://github.com/oneapi-src/oneDPL>`_ にリンクします。
       この TPL を有効にすると、それを使用する Kokkos アルゴリズム（例: ``sort``）のパフォーマンスに影響を与える可能性があります。
   * - ``KOKKOS_ENABLE_ROCTHRUST``
     - HIP バックエンドを使用する際に、Kokkos が `rocThrust ライブラリ <https://github.com/ROCm/rocThrust>`_ にリンクします。
       この TPL を有効にすると、それを使用する Kokkos アルゴリズム（例: ``sort``）のパフォーマンスに影響を与える可能性があります。