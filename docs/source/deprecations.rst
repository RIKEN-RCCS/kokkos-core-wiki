非推奨
******

Kokkos 5.x において非推奨
=========================

Kokkos 5.0 において非推奨
-------------------------

* ``View::stride_N()``
   * 置換: ``View::stride(N)``
   * ``std::mdspan`` との整合

* ``KOKKOS_ATTRIBUTE_NODISCARD``
   * 置換: なし
   * 内部以外での使用は意図されていません。

* ``{Owning,Observing}RawPtr``
   * 置換: なし
   * 内部以外での使用は意図されていません。

* ネストされた OpenMP が有効になっていない状態でのネストされた OpenMP 並列の使用
   * 置換: なし
   * 非推奨コードなしでコンパイルされた際に、バグのあるコードパスの使用を回避します。

* OpenMP 並列領域内での ``OpenMP`` インスタンスの生成
   * 置換: なし
   * パーティションのスレッド数が 0 のときに ``partition_space`` が中断するのを回避します。

* ``Random_XorShift{64,1024}_Pool::init``
   * 置換: なし
   * 内部以外での使用は意図されていません。

* ``[const_]where_expression``
   * 置換: なし
   * std::simd インターフェイスと整合しません。

* ``View::HostMirror``
   * 置換: ``View::host_mirror_type``
   * 命名スタイルの一貫性

* ``{DynRankView,OffsetView,View}::scalar_array_type``
   * 置換: ``{DynRankView,OffsetView,View}::data_type``
   * Kokkos 5 以前の ``View`` 実装での ``{DynRankView, OffsetView, View}`` の特定の外部部分特殊化にのみ関連します。ほとんどの場合 ``data_type`` と等しくなります。

* ``{DynRankView,OffsetView,View}::const_scalar_array_type``
   * 置換: ``{DynRankView,OffsetView,View}::const_data_type``
   * Kokkos 5 以前の ``View`` 実装での ``{DynRankView, OffsetView, View}`` の特定の外部部分特殊化にのみ関連します。ほとんどの場合 ``const_data_type`` と等しくなります。

* ``{DynRankView,OffsetView,View}::non_const_scalar_array_type``
   * 置換: ``{DynRankView,OffsetView,View}::non_const_data_type``
   * Kokkos 5 以前の ``View`` 実装での ``{DynRankView, OffsetView, View}`` の特定の外部部分特殊化にのみ関連します。ほとんどの場合 ``non_const_data_type`` と等しくなります。

* ``{DynRankView,OffsetView,View}::array_type``
   * 置換: ``{DynRankView,OffsetView,View}::type``
   * ``array`` は ``View`` に対する非常に古い呼称です。

* ``DynamicView::array_type``
   * 置換: ``DynamicView::uniform_type``
   * ``View`` との一貫性

* ``ErrorReporter::getCapacity``
   * 置換: ``ErrorReporter::capacity``
   * 命名スタイルの一貫性

* ``ErrorReporter::getNumReports``
   * 置換: ``ErrorReporter::num_reports``
   * 命名スタイルの一貫性

* ``ErrorReporter::getNumReportAttempts``
   * 置換: ``ErrorReporter::num_report_attempts``
   * 命名スタイルの一貫性

* ``ErrorReporter::getReports``
   * 置換: ``ErrorReporter::get_reports``
   * 命名スタイルの一貫性

Kokkos 4.x において非推奨
=========================

Kokkos 4.7 において非推奨
-------------------------

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
-------------------------

* ``StaticCrsGraph`` は Kokkos Kernels に移動しました。
   * 置換: ``KokkosSparse::StaticCrsGraph``
   * ``KokkosKernels`` が提供する機能性により整合しています。

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
-------------------------

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
-------------------------

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
-------------------------

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

* ``HIP::detect_device_count()``
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
-------------------------

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
-------------------------

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
-------------------------

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

* 静的な ``ExecutionSpace::concurrency()``
   * 置換: 非静的な ``ExecutionSpace::concurrency()`` メンバー関数
   * 並行性は実行空間インスタンスのプロパティであり、その型のプロパティではありません。
