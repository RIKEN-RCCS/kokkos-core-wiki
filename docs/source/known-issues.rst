既知の問題
############

.. role:: cpp(code)
    :language: cpp

``Windows.h`` ヘッダー
=============================

Windows で Kokkos を使用する場合、プログラムやライブラリが `windows.h` を含む場合があります。なぜなら、このヘッダーは、事前に `NOMINMAX` が定義されなければ、`min` と `max` という名前の2つのマクロを定義するため、問題を含みます。プリプロセッサはソースコード内の文字列をマクロで置換するため、解釈不能な結果となり、コンパイルは失敗に終わります。したがって、ヘッダーファイル `Kokkos_Core.hpp` はこれらのマクロに対して保護されており、つまりそれらはヘッダーファイルの先頭では未定義であり、末尾で再定義されるということです。`Kokkos_Core.hpp` 内の定義はマクロに対して保護されていますが、外部のコードは保護されていません。 したがって、定義されるマクロへの対応として、コンパイルラインで、`-DNOMINMAX` または `/DNOMINMAX` を定義する（推奨）ことによる、あるいは `min` または `max` を含む名前に `()` を付けることによるかは、ユーザー次第です。

CUDA
====

- 一部の MPI バージョンまたはレガシー NVIDIA GPU を使用する場合、Kokkos（バージョン4.2から4.4）の `CudaSpace` に対するデフォルトの割り当てメカニズムが問題を引き起こす可能性があります。例えば、MPI は不正なメモリアクセスでクラッシュする可能性があり、Kokkos の初期化では次のようなエラーが報告される場合があります:

  .. code-block::

     terminate called after throwing an instance of 'Kokkos::Experimental::CudaRawMemoryAllocationFailure'

  以下の CMake 引数を追加することで、非同期メモリ割り当てを無効にできます:

  .. code-block::

     -DKokkos_ENABLE_IMPL_CUDA_MALLOC_ASYNC=OFF

このポリシーを無効化することが、特に UCX のような低レベル層において、一部の MPI 実装を機能させるのに役立つ理由は何かについての技術的に説明すると、それは部分的には、 `cudaMallocAsync` が、 `cudaMemPool_t` を使用しており、デフォルトのメモリプールは調整なしではプロセス間通信（IPC）をサポートしないことに起因しています。 (https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-2/#interprocess_communication_support)。ユーザーは、IPC を適切にサポートするためにデフォルトのメモリプールを設定する必要があります (https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-2/#library_composability)。

  そのため、バージョン4.5からは、Kokkosのデフォルト動作では、予防上 `cudaMallocAsync` を無効にします。

- CUDA 11.0 から 11.2 は、 glibc 2.34 の librt スタブと互換性がありません。そのイシューは、CMakeパッケージが librt とのリンクをどのように処理するかに関連しています。詳細については、イシュー `#7512 <https://github.com/kokkos/kokkos/issues/7512>`_ をご覧ください。

- Microsoft Visual Studio と Cuda バックエンドを有効化した状態で、Kokkos を利用するアプリケーションを構築するには、CMake 言語機能の使用が必要です。 :ref:`keywords_enable_backend_specific_options` を参照してください。

HIP
===

-  `HIPManagedSpace` を使用する場合、以下の条件下では、 メモリは CPU と GPU の間を移動します:
   - ハードウェアがそれをサポートする場合
   - カーネルが、ページ移行をサポートするようにコンパイルされた場合
   - 環境変数 `HSA_XNACK` が 1 に設定されている場合。

   より詳細な説明については、 `here <https://docs.olcf.ornl.gov/systems/frontier_user_guide.html#enabling-gpu-page-migration>`_ を参照してください。

- HIP および gcc 8間の互換性の問題。 以下のエラーに遭遇する可能性があります:

  .. code-block::

     error: reference to __host__ function 'operator new' in __host__ __device__ function

  gcc 7, 9, 以降では、この問題は発生していません。

SYCL
====

- Kokkosアルゴリズムのいくつかの関数は、oneDPL のようなサードパーティによるライブラリを使用しています。これらを使用する場合、Kokkos はカーネル起動を制御しませんので、ユーザーは、コンパイラエラーを回避するために、TPLに渡されるすべての引数が sycl::is_device_copyable トレイトを満たしていることを確認する必要があります。これは特に、Kokkos 4.7以前のバージョンおよび oneDPL 2022.8.0 以前のバージョンで、 Kokkos::sort と共に使用される比較関数に当てはまります。例えば、Kokkos::Viewsの代わりに生のポインタを使用するなど、各パラメータが単純にコピー可能であることを確認することを、最も推奨します。それが不可能な場合で、oneDPLのバージョンが少なくとも、2022.8.0 であるならば、sycl::is_device_copyable を特化させることで、別の回避策を提供できます。

  .. code-block:: cpp

     MyComparator my_comparator;
     Kokkos::sort(exec, values, my_comparator);

  以下と同様のエラーを発生させます

  .. code-block:: console

     /usr/bin/compiler/../../include/sycl/types.hpp:2572:17: error: static assertion failed due to requirement 'is_device_copyable_v<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1816:20)> || detail::IsDeprecatedDeviceCopyable<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1816:20), void>::value': 特定の型は、コピー可能なデバイスではありません
      2572 |   static_assert(is_device_copyable_v<FieldT> ||
           |                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      2573 |                     detail::IsDeprecatedDeviceCopyable<FieldT>::value,
           |                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      /usr/bin/compiler/../../include/sycl/types.hpp:2605:7: note: テンプレートクラスのインスタンス化において 'sycl::detail::CheckFieldsAreDeviceCopyable<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83), 4>' ここでリクエスト
      2605 |     : CheckFieldsAreDeviceCopyable<FuncT, __builtin_num_fields(FuncT)>,
           |       ^
     /usr/bin/compiler/../../include/sycl/types.hpp:2613:7: note: テンプレートクラスのインスタンス化において 'sycl::detail::CheckDeviceCopyable<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>' ここでリクエスト
      2613 |     : CheckDeviceCopyable<KernelType> {};
           |       ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:1652:5: note: テンプレートクラスのインスタンス化において 'sycl::detail::CheckDeviceCopyable<sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>>' ここでリクエスト
      1652 |     detail::CheckDeviceCopyable<KernelType>();
           |     ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:1694:5: note: 関数テンプレート特殊化のインスタンス化において 'sycl::handler::unpack<sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::ext::oneapi::experimental::properties<std::tuple<>>, false, (lambda at /usr/bin/compiler/../../include/sycl/handler.hpp:1697:21)>' ここでリクエスト
      1694 |     unpack<KernelName, KernelType, PropertiesT,
           |     ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:1293:7: note: 関数テンプレート特殊化のインスタンス化において 'sycl::handler::kernel_parallel_for_wrapper<sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::item<1, true>, sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::ext::oneapi::experimental::properties<std::tuple<>>>' ここでリクエスト
      1293 |       kernel_parallel_for_wrapper<KName, TransformedArgType, decltype(Wrapper),
           |       ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:2332:5: note: (バックトレースの中にある7コンテクストをスキップ;すべてを参照するには、-ftemplate-backtrace-limit=0 を使ってください)
      2332 |     parallel_for_lambda_impl<KernelName, KernelType, 1, PropertiesT>(
           |     ^
     [...]

  以下で修正できます

  .. code-block:: cpp

    struct sycl::is_device_copyable<MyComparator>
      : std::true_type {};


数学関数
======================

-  using ディレクティブと数学関数の互換性問題:

.. code-block:: cpp

    #include <Kokkos_Core.hpp>
    
    using namespace Kokkos;  // using ディレクティブを回避

    KOKKOS_FUNCTION void do_math() {
      auto sqrt5 = sqrt(5);  // error: ambiguous ::sqrt or Kokkos::sqrt?
    }


.. _Compatibility: ./ProgrammingGuide/Compatibility.html

.. |Compatibility| replace:: Kokkos compatibility guidelines

using ディレクティブ   ``using namespace Kokkos;`` の使用は、大いに避けるべきです(
|Compatibility|_ 参照) 。 数学関数への修飾子なしの呼び出しが存在する場合、コンパイルエラーが発生するからです。代わりに、  ローカルスコープでは、明示的な修飾子 ``Kokkos::sqrt`` または、using宣言 ``using Kokkos::sqrt;`` を選択してください。

数学定数
======================

- デバイスコード内での数学定数のアドレス取得は避けてください。 一部のツールチェーンではサポートされていないため、移植性がありません。

.. code-block:: cpp

    #include <Kokkos_Core.hpp>

    KOKKOS_FUNCTION void do_math() {
      // 複合コンストラクタは、スカラー引数を参照渡しで受け取ります！
      Kokkos::complex z1(Kokkos::numbers::pi);
      // エラー: 識別子 "Kokkos::numbers::pi" は、 デバイスコード内で未定義です

      // 1*pi は、 一時的なものです
      Kokkos::complex z2(1 * Kokkos::numbers::pi);  // OK

      // ローカル変数にコピー
      auto pi = Kokkos::numbers::pi;
      Kokkos::complex z3(pi);  // OK
    }
