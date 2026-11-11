バックエンド
============

``KOKKOS_ENABLE_<BACKEND>`` マクロは、構成時に対応するバックエンドが
``-DKokkos_ENABLE_<BACKEND>=ON`` で有効化されている場合に定義されます。
このページでは、それらのマクロをバックエンド固有のメモリスペースおよびオプションとともに一覧します。

.. note::

   アプリケーションコードでこれらのマクロが必要になることはほとんどありません。``Kokkos::Cuda`` や ``Kokkos::OpenMP`` のような具体的な実行スペースを指定する代わりに、``Kokkos::DefaultExecutionSpace`` および ``Kokkos::DefaultHostExecutionSpace`` を使用してください。
   同様に、バックエンド固有のメモリスペースよりも ``Kokkos::DefaultExecutionSpace::memory_space`` および ``Kokkos::HostSpace`` を優先してください。これにより、コードがバックエンド間で移植可能に保たれます。

   これらのマクロの正当な用途は、:ref:`以下に示す <macros_backends_interoperability>` ように、基盤となるプログラミングモデルとの相互運用です。

実行スペースとメモリスペース
----------------------------

これらのマクロの存在をテストしてください。例: ``#ifdef KOKKOS_ENABLE_SERIAL``。バックエンドを組み合わせる際の制約については、構成ガイドの :ref:`keywords_backends` を参照してください。デバイスバックエンドは独自のメモリスペースも提供しますが、これらはバックエンドが有効化されている場合にのみ存在します。

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 30 25 45

   * - マクロ
     - 実行スペース
     - バックエンド固有のメモリスペース
   * - ``KOKKOS_ENABLE_SERIAL``
     - :cpp:class:`Serial`
     -
   * - ``KOKKOS_ENABLE_OPENMP``
     - :cpp:class:`OpenMP`
     -
   * - ``KOKKOS_ENABLE_THREADS``
     - :cpp:class:`Threads`
     -
   * - ``KOKKOS_ENABLE_CUDA``
     - :cpp:class:`Cuda`
     - :cpp:class:`CudaSpace`, :cpp:class:`CudaUVMSpace`, :cpp:class:`CudaHostPinnedSpace`
   * - ``KOKKOS_ENABLE_HIP``
     - :cpp:class:`HIP`
     - :cpp:class:`HIPSpace`, :cpp:class:`HIPManagedSpace`, :cpp:class:`HIPHostPinnedSpace`
   * - ``KOKKOS_ENABLE_HPX``
     - :cpp:class:`HPX`
     -
   * - ``KOKKOS_ENABLE_SYCL``
     - :cpp:class:`SYCL`
     - :cpp:class:`SYCLDeviceUSMSpace`, :cpp:class:`SYCLSharedUSMSpace`, :cpp:class:`SYCLHostUSMSpace`
   * - ``KOKKOS_ENABLE_OPENACC``
     - :cpp:class:`OpenACC`
     -

詳細については :doc:`../execution_spaces` および :doc:`../memory_spaces` を参照してください。

.. _macros_backends_interoperability:

バックエンドプログラミングモデルとの相互運用
--------------------------------------------

バックエンドマクロでコードをガードすることで、Kokkos のリソースをネイティブライブラリやカーネルに渡すことができます。例えば CUDA ストリームは次のように渡せます:

.. code-block:: c++

   #include <Kokkos_Core.hpp>

   void do_work() {
   #ifdef KOKKOS_ENABLE_CUDA
     Kokkos::Cuda space;
     cudaStream_t stream = space.cuda_stream();
     // CUDA ライブラリや手書きの CUDA カーネルにストリームを渡す
   #endif
   }

バックエンド固有のオプション
----------------------------

これらは同じ命名規則に従っており、構成ガイドの :ref:`keywords_enable_backend_specific_options` にある対応する CMake オプションとともに文書化されています。

.. list-table::
   :header-rows: 1
   :align: left
   :widths: 45 55

   * - マクロ
     - 説明
   * - ``KOKKOS_ENABLE_CUDA_CONSTEXPR``
     - CUDA バックエンドで緩和された constexpr 関数が有効化されます。
   * - ``KOKKOS_ENABLE_CUDA_RELOCATABLE_DEVICE_CODE``
     - CUDA バックエンドで再配置可能デバイスコード (RDC) が有効化されます。
   * - ``KOKKOS_ENABLE_HIP_RELOCATABLE_DEVICE_CODE``
     - HIP バックエンドで再配置可能デバイスコード (RDC) が有効化されます。
   * - ``KOKKOS_ENABLE_SYCL_RELOCATABLE_DEVICE_CODE``
     - SYCL バックエンドで再配置可能デバイスコード (RDC) が有効化されます。