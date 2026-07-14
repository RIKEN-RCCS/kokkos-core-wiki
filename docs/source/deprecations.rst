非推奨
************

Kokkos 4.x において非推奨
===========================

Kokkos 4.7 において非推奨
---------------------------

* ``KOKKOS_MEMORY_ALIGNMENT[_THRESHOLD]``
   * 置換: 無し
   * 非内部利用を意図したものではありません。

* ``Kokkos::MemoryManaged``
   * 置換: 無し
   * デフォルトのメモリ特性と重複し、不要であり、MemoryManaged で管理対象外ビューを要求する際の混乱を招くので、不要です。

* ``KOKKOS_NONTEMPORAL_PREFETCH_{LOAD,STORE}``
   * 置換: 無し
   * 非内部利用を意図したものではありません。

Kokkos 4.6 において非推奨
---------------------------

* ``StaticCrsGraph`` は、 Kokkos Kernels に移動しました。
   * ``KokkosSparse::StaticCrsGraph``
   * ``KokkosKernels`` が提供した機能性により整合しています。

* ``native_simd`` および ``native_simd_mask`` 型
   * 置換: ``simd`` and ``simd_mask``
   * C++ 標準との整合性。

* Makefile サポート
   * 置換: CMake
   * 使用頻度の低いビルドシステムの保守負担を軽減します

* ``DualView`` における ``d_view`` および ``h_view`` メンバーへ直接アクセス
   * 置換: ``view_host()`` and ``view_device()``
   * DualView において不変条件を実行すること、例えば、参照される2つのビューインスタンス間の一貫性です。

Kokkos 4.5 において非推奨
---------------------------

* タスク割り当てインターフェイス: ``BasicFuture``, ``TaskSingle``, ``TaskPriority``, ``task_spawn``, ``host_spawn``, ``respawn``, ``when_all``, ``wait``
   * 置換: 無し
   * 使用されていません、限定的に実装

* ``HPX::HPX::is_asynchronous(HPX const & = HPX())``
   * 置換: 無し
   * 使用されていません、実行空間の適合性

* ``OpenMP::is_asynchronous(OpenMP const& = OpenMP())``
   * 置換: 無し
   * 使用されていません、実行空間の適合性

* ``atomic_query_version``
   * 置換: 無し
   * 既知の使用例がありません

* :cpp:func:`atomic_assign`
   * 置換: :cpp:func:`atomic_store`
   * 重複した機能

* :cpp:func:`atomic_increment`
   * 置換: :cpp:func:`atomic_inc`
   * 重複した機能

* :cpp:func:`atomic_decrement`
   * 置換: :cpp:func:`atomic_dec`
   * 重複した機能

* :cpp:func:`atomic_compare_exchange_strong`
   * 置換: :cpp:func:`atomic_compare_exchange`
   * 重複した機能

Kokkos 4.4 において非推奨
---------------------------

* ``is_layouttiled``
   * 置換: 無し
   * 使用されていません

* ``layout_iterate_type_selector``
   * 置換: 無し
   * 内部でのみ有用です

* ``Array<T, N, Proxy>``
   * 置換: 無し
   * std::array との整合性

* ``HPX::HPX(instance_mode mode)``
   * 置換: ``explicit HPX(instance_mode mode)``
   * 実行空間インスタンスコンストラクタは、 ``explicit`` であるべきです

* ``HPX::HPX(hpx::execution::experimental::unique_any_sender<> &&sender)``
   * 置換: ``explicit HPX::HPX(hpx::execution::experimental::unique_any_sender<> &&sender)``
   * 実行空間インスタンスコンストラクタは、 ``explicit`` であるべきです

* ``OpenMP::OpenMP(int pool_size)``
   * 置換: ``explicit OpenMP::OpenMP(int pool_size)``
   * 実行空間インスタンスコンストラクタは、 ``explicit`` であるべきです

* ``Serial::Serial(NewInstance)``
   * 置換: ``explicit Serial::Serial(NewInstance)``
   * 実行空間インスタンスコンストラクタは、 ``explicit`` であるべきです

* ``ChunkSize::ChunkSize(int value)``
   * 置換: ``explicit ChunkSize::ChunkSize(int value)``
   * ``ChunkSize`` は、明示的に構築されるべきです

* ``pair<T, void>``
   * 置換: 無し
   * 仕様は文書化されておらず、標準ライブラリに準拠しておらず、テストもされておらず、既知の使用例もありません



Kokkos 4.3 において非推奨
---------------------------

* ``Experimental::swap``
   * 置換: ``kokkos_swap``
   * ADLにより曖昧さを回避

* ``ExecutionSpace::in_parallel``
   * 置換: ``KOKKOS_IF_ON_HOST``/``KOKKOS_IF_ON_DEVICE`` は、部分的に同様の動作を提供します
   * 一貫性を欠いた実装、限定的な利用

* ``Cuda::device_arch()``
   * 置換: 無し
   * 実行空間間での均一性

* ``Cuda::detect_device_count()``
   * 置換: num_devices()
   * 実行空間間での均一性

* ``Cuda::detect_device_arch()``
   * 置換: 無し
   * 実行空間間での均一性

* ``HIP::HIP::detect_device_count()``
   * 置換: ``num_devices()``
   * 実行空間間での均一性

* ``RangePolicy::set(ChunkSize chunksize)``
   * 置換: ``RangePolicy::set_chunk_size(int chunk_size)``
   * ``ChunkSize`` が  ``RangePolicy::set()`` で使用可能な唯一の追加パラメータでした。

* ``InitializationSettings::set_num_devices``, ``InitializationSettings::has_num_devices``, ``InitializationSettings::get_num_devices``
   * 置換: ``num_devices``
   *  `InitializationSettings` の変更により、これらは不要となりました。

* ``InitializationSettings::set_skip_devices``, ``InitializationSettings::has_skip_devices``, ``InitializationSettings::get_skip_devices``
   * 置換: ``KOKKOS_VISIBLE_DEVICES``
   *  `InitializationSettings` の変更により、これらは不要となりました。

Kokkos 4.2 において非推奨
---------------------------

* ``Cuda::Cuda(cudaStream_t stream, bool manage_stream)``
   * 置換: ``Cuda::Cuda(cudaStream_t stream)``
   *  Cuda 実行空間インスタンスの構築には、常に外部管理の ``cudaStream`` オブジェクトを使用すべきです。

* ``HIP::HIP(hipStream_t stream, bool manage_stream)``
    * 置換 ``HIP::HIP(hipStream_t stream)``
    *  HIP 実行空間インスタンスの構築には、常に外部管理の ``hipStream`` オブジェクトを使用すべきです。

* ``vector``
    * 置換: 無し
    * 非標準的な動作であり、Kokkosの概念とは相性が良くありません。

* ``HostSpace::HostSpace(AllocationMechanism)``
    * 置換: ``HostSpace::HostSpace()``
    * ``AllocationMechanism`` は使用されず、 整合性を伴う ``operator new`` は、無条件で使用されています。

*  ``Kokkos::Experimental``
    * 置換: ``Kokkos`` 名前空間内の SIMD 数学関数
    *  ADLの問題、他の数学関数オーバーロードとの一貫性


Kokkos 4.1 において非推奨
---------------------------

*  ``BinSort``, ``BinOp1D``, and ``BinOp3D`` のためのデフォルトコンストラクタ
   * 置換: 無し
   * デフォルトコンストラクタは、無効であり、利用不可能なオブジェクトを作成しました。

* ``View::Rank``
   * 置換: ``View::rank()``
   *  ``View::rank()`` のため、文書化されておらず、冗長です

* ``View::subview<MemoryTraits>(...)``
   * 置換: ``View::subview(...)``
   * 有用ではなく、使用されていません


Kokkos 4.0 において非推奨
---------------------------

* ``CudaUVMSpace::available()``
   * 置換: ``SharedSpace``
   * 移植不可能であり、常に ``true`` を返す

* ``Complex`` ``volatile`` オーバーロード
   * 置換: 無し
   *  ``volatile`` オーバーロードを使用する必要はありません

* ``pair`` ``volatile`` オーバーロード
   * 置換: 無し
   *  ``volatile`` オーバーロードを使用する必要はありません

* ``ScratchMemorySpace::align(const IntType& size)``
   * 置換: 無し
   * 使用されておらず、有用ではありません


Kokkos-3.x において非推奨
===========================



Kokkos-3.7 において非推奨である型エイリアス
-------------------------------------------
``ActiveExecutionMemorySpace``, ``host_execution_space``, ``host_memory_space``, ``host_mirror_space``, ``is_array_layout``, ``is_execution_policy``, ``is_execution_space``, ``is_memory_space``, ``is_memory_traits``, ``is_space``, ``Iterate``, ``MDRangePolicy``, ``Rank``, ``SpaceAccessibility``


Kokkos-3.7 において非推奨であるマクロ
--------------------------------------

``KOKKOS_RESTRICT_EXECUTION_TO_(DATA_SPACE)``, ``HIP_SAFE_CALL(call)``


Kokkos-3.7 において非推奨である自由関数
----------------------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 名前
     - 場所

   * - .. code-block:: cpp

          std::vector<OpenMP> OpenMP::partition(...)

     - OpenMP

   * - .. code-block:: cpp

          OpenMP OpenMP::create_instance(...)

     - OpenMP

   * - .. code-block:: cpp

          void OpenMP::partition_master(F const& f,
                                        int num_partitions,
                                        int partition_size)

     - OpenMP (Kokkos_OpenMP_Instance.hpp)

   * - .. code-block:: cpp

          void Experimental::HIPSpace::access_error()

     - ``namespace Kokkos`` (Kokkos_HIP_Space.cpp)

   * - .. code-block:: cpp

          void Experimental::HIPSpace::access_error(const void* const)

     - ``namespace Kokkos`` (Kokkos_HIP_Space.cpp)

   * - ..  code-block:: cpp

           inline void hip_internal_safe_call_deprecated

     - ``namespace Kokkos::Impl`` (Kokkos_HIP_Error.hpp)


Kokkos-3.7 において非推奨
------------------------------------------

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - メソッド名
     - クラス

   * - ``static void OpenMP::partition_master()``
     - ``class OpenMP`` (Kokkos_OpenMP.hpp)

   * - ``static void OpenMPInternal::validate_partition()``
     - ``class OpenMPInternal`` (Kokkos_OpenMP_Instance.hpp)

   * - ``std::string ProfilingSection::getName()``
     - ``class ProfilingSection`` (Kokkos_Profiling_ProfileSection.hpp)

   * - ``uint32_t ProfilingSection::getSectionID()``
     - ``class ProfilingSection`` (Kokkos_Profiling_ProfileSection.hpp)

   * - ``int TeamPolicyInternal::vector_length() const``
     - ``class TeamPolicyInternal`` (Kokkos_HIP_Parallel_Team.hpp, Kokkos_SYCL_Parallel_Team.hpp)

   * - ``inline int TeamPolicyInternal::vector_length() const``
     - ``class TeamPolicyInternal`` (Kokkos_OpenMPTarget_Exec.hpp, Kokkos_Cuda_Parallel_Team.hpp)

   * - ``static void CudaSpace::access_error();``
     - ``class CudaSpace`` (Kokkos_CudaSpace.hpp), ``class HIPSpace`` (Kokkos_HIP_Space.hpp)

   * - ``static void CudaSpace::access_error(const void* const);``
     - ``class CudaSpace`` (Kokkos_CudaSpace.hpp), ``class HIPSpace`` (Kokkos_HIP_Space.hpp)

   * - ``static int CudaUVMSpace::number_of_allocations();``
     - ``class CudaUVMSpace`` (Kokkos_CudaSpace.hpp)

   * - ``HPX::partition(...), HPX::partition_master()``
     - ``class HPX`` (Kokkos_HPX.hpp)


Kokkos-3.7 において非推奨であるクラス
-------------------------------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * -

   * - ``class MasterLock<OpenMP>``

   * - ``class KOKKOS_ATTRIBUTE_NODISCARD ScopeGuard``


名前空間アップデート
----------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - 以前
     - 現在使用すべきもの

   * - ``Kokkos::Experimental::aMathFunction``
     - ``Kokkos::aMathFunction``

   * - ``Kokkos::Experimental::clamp``
     - ``Kokkos::clamp``

   * - ``Kokkos::Experimental::max;``
     - ``Kokkos::max``

   * - ``Kokkos::Experimental::min``
     - ``Kokkos::min``

   * - ``Kokkos::Experimental::minmax``
     - ``Kokkos::minmax``


他の非推奨
------------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - 以前
     - 置換対象

   * - ``Kokkos::is_reducer_type``
     - ``Kokkos::is_reducer``

   * - 生ポインタを使った配列縮約
     - 戻し引数として ``Kokkos::View`` を使用します

   * -  ``index_list_type`` を選択する ``OffsetView`` コンストラクタ
     - ``Kokkos::pair`` (CPU および GPU)

   * - パラメータ ``bool always_use_kokkos_sort`` を選択する ``Kokkos::sort`` のオーバーロード
     - 必要であれば、 ``Kokkos::BinSort`` を使用するか、または、ブール値パラメータを伴わない ``Kokkos::sort`` を呼びます

   * - 空ではない WorkTag が使用される場合には、非推奨警告を発します
     - 空の WorkTag クラスを使用します

   * - ``InitArguments`` 構造体
     - 問い合わせ可能な属性を持つ ``InitializationSettings()`` クラスオブジェクト 

   * - ``finalize_all()``
     - ``finalize()``

   * -  ``volatile`` キーワードにより修飾された引数を伴う ``join()`` を呼び出す ``parallel_reduce`` 事例について、警告します
     -  ``volatile`` オーバーロードを削除します


   * - 第一引数として、 ``WithOutInitializing`` を選択する ``create_mirror_view`` 
     - ``create_mirror_view(Kokkos::Impl::WithoutInitializing_t wi, Kokkos::View<T, P...> const& v)``

   * - ``#define KOKKOS_THREAD_LOCAL`` マクロ
     - ``thread_local``

   * - ``class MasterLock``
     - クラスを削除します

   * - ``Kokkos::Impl::is_view``
     - ``Kokkos::is_view``

   * - ``inline void cuda_internal_safe_call_deprecated()``
     - ``#define CUDA_SAFE_CALL(call)``

   * - 後続引数として、ラベルを選択する ``parallel_*`` オーバーロード
     - ``Kokkos::parallel_*("KokkosViewLabel", ポリシー, f);``


Kokkos-3.7 におけるパブリックヘッダー
-------------------------------------

Kokkos-3.7 より、 以下の項目が、 *パブリック* ヘッダーです:

コア
~~~~~~~~~~~~
``Kokkos_Core.hpp``, ``Kokkos_Macros.hpp``, ``Kokkos_Atomic.hpp``, ``Kokkos_DetectionIdiom.hpp``, ``Kokkos_MathematicalConstants.hpp``, ``Kokkos_MathematicalFunctions.hpp``, ``Kokkos_NumericTraits.hpp``, ``Kokkos_Array.hpp``, ``Kokkos_Complex.hpp``, ``Kokkos_Pair.hpp``, ``Kokkos_Half.hpp``, ``Kokkos_Timer.hpp``

アルゴリズム
~~~~~~~~~~~~~~~~~~
``Kokkos_StdAlgorithms.hpp``, ``Kokkos_Random.hpp``, ``Kokkos_Sort.hpp``

コンテナ
~~~~~~~~~~~~~~~~~~
``Kokkos_Bit.hpp``, ``Kokkos_DualView.hpp``, ``Kokkos_DynRankView.hpp``, ``Kokkos_ErrorReporter.hpp``, ``Kokkos_Functional.hpp``, ``Kokkos_OffsetView.hpp``, ``Kokkos_ScatterView.hpp``, ``Kokkos_StaticCrsGraph.hpp``, ``Kokkos_UnorderedMap.hpp``, ``Kokkos_Vector.hpp``
