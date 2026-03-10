既知の問題
############

.. ロール:: cpp(code)
    :language: cpp

``Windows.h`` ヘッダー
====================

Windows　で　Kokkos　を使用する場合、プログラムやライブラリが　`windows.h`　を含む場合があります。なぜなら、このヘッダーは、事前に　`NOMINMAX`　が定義されなければ、`min`　と　`max`　という名前の2つのマクロを定義するため、問題を含みます。プリプロセッサはソースコード内の文字列をマクロで置換するため、解釈不能な結果となり、コンパイルは失敗に終わります。したがって、ヘッダーファイル `Kokkos_Core.hpp` はこれらのマクロに対して保護されており、つまりそれらはヘッダーファイルの先頭では未定義であり、末尾で再定義されるということです。`Kokkos_Core.hpp`　内の定義はマクロに対して保護されているが、外部からのコードは保護されていません。 したがって、定義されるマクロへの対応として、コンパイルラインで、`-DNOMINMAX` または `/DNOMINMAX` を定義する（推奨）ことによる、あるいは `min` または `max` を含む名前に `()` を付けることによるかは、ユーザー次第である。

CUDA
====

- 一部の　MPI　バージョンまたはレガシー　NVIDIA GPU　を使用する場合、Kokkos（バージョン4.2から4.4）の　`CudaSpace`　に対するデフォルトの割り当てメカニズムが問題を引き起こす可能性があります。例えば、MPI　は不正なメモリアクセスでクラッシュする可能性があり、Kokkos　の初期化では次のようなエラーが報告される場合があります:

  .. code-block::

    'Kokkos::Experimental::CudaRawMemoryAllocationFailure'　のインスタンスをスローした後、terminate が呼び出されました。

  フィックスとは、以下の CMake 引数を加えることにより、非同期メモリっ割り当てを無効にすることです:

  .. code-block::

     -DKokkos_ENABLE_IMPL_CUDA_MALLOC_ASYNC=OFF

このポリシーを無効化することが、特に　UCX　のような低レベル層において、一部の　MPI　実装を機能させるのに役立つ理由は何かについての技術的に説明すると、それは部分的には、`cudaMallocAsync` が、 `cudaMemPool_t,`を使用しており、デフォルトのメモリプールは調整なしではプロセス間通信（IPC）をサポートしないことに起因しています。 (https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-2/#interprocess_communication_support)。ユーザーは、IPC　を適切にサポートするためにデフォルトのメモリプールを設定する必要があります (https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-2/#library_composability)。

  そのため、バージョン4.5からは、Kokkosのデフォルト動作では、予防上 `cudaMallocAsync.`を無効にします。

- CUDA 11.0 から 11.2 は、 glibc 2.34 の librt スタブと互換性がありません。そのイシューは、CMakeパッケージが　librt　とのリンクをどのように処理するかに関連しています。詳細については、イシュー　`#7512　をご覧ください。
<https://github.com/kokkos/kokkos/issues/7512>`_.

- Microsoft Visual Studio　と　Cuda　バックエンドを有効化した状態で、Kokkos　を利用するアプリケーションを構築するには、CMake　言語機能の使用が必要です。 以下を参照してください
:ref:`keywords_enable_backend_specific_options`.

HIP
===

- When using `HIPManagedSpace`, the memory migrates between the CPU and the GPU if:
   - the hardware supports it
   - the kernel was compiled to support page migration
   - the environment variable `HSA_XNACK` is set to 1

   See `here <https://docs.olcf.ornl.gov/systems/frontier_user_guide.html#enabling-gpu-page-migration>`_ for more explanation.

- Compatibility issue between HIP and gcc 8. You may encounter the following error:

  .. code-block::

     error: reference to __host__ function 'operator new' in __host__ __device__ function

  gcc 7, 9, and later do not have this issue.

SYCL
====

- Several of the Kokkos algorithm functions use third-party libraries like oneDPL.
  When using these, Kokkos doesn't control the kernel launch and thus the user has to make sure that all arguments
  that are forwarded to the TPL satisfy the sycl::is_device_copyable trait to avoid compiler errors. This holds true in particular
  for comparators used with Kokkos::sort in Kokkos versions prior to 4.7 and oneDPL versions prior to 2022.8.0.
  The best advice to give is to make sure the respective parameters are trivially-copyable, e.g., by using raw pointers instead of Kokkos::Views.
  If that's not possible and the oneDPL version is at least 2022.8.0, specializing sycl::is_device_copyable provides another workaround.

  .. code-block:: cpp

     MyComparator my_comparator;
     Kokkos::sort(exec, values, my_comparator);

  would give errors similar to

  .. code-block:: console

     /usr/bin/compiler/../../include/sycl/types.hpp:2572:17: error: static assertion failed due to requirement 'is_device_copyable_v<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1816:20)> || detail::IsDeprecatedDeviceCopyable<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1816:20), void>::value': The specified type is not device copyable
      2572 |   static_assert(is_device_copyable_v<FieldT> ||
           |                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      2573 |                     detail::IsDeprecatedDeviceCopyable<FieldT>::value,
           |                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      /usr/bin/compiler/../../include/sycl/types.hpp:2605:7: note: in instantiation of template class 'sycl::detail::CheckFieldsAreDeviceCopyable<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83), 4>' requested here
      2605 |     : CheckFieldsAreDeviceCopyable<FuncT, __builtin_num_fields(FuncT)>,
           |       ^
     /usr/bin/compiler/../../include/sycl/types.hpp:2613:7: note: in instantiation of template class 'sycl::detail::CheckDeviceCopyable<(lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>' requested here
      2613 |     : CheckDeviceCopyable<KernelType> {};
           |       ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:1652:5: note: in instantiation of template class 'sycl::detail::CheckDeviceCopyable<sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>>' requested here
      1652 |     detail::CheckDeviceCopyable<KernelType>();
           |     ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:1694:5: note: in instantiation of function template specialization 'sycl::handler::unpack<sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::ext::oneapi::experimental::properties<std::tuple<>>, false, (lambda at /usr/bin/compiler/../../include/sycl/handler.hpp:1697:21)>' requested here
      1694 |     unpack<KernelName, KernelType, PropertiesT,
           |     ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:1293:7: note: in instantiation of function template specialization 'sycl::handler::kernel_parallel_for_wrapper<sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::item<1, true>, sycl::detail::RoundedRangeKernel<sycl::item<1, true>, 1, (lambda at /usr/include/oneapi/dpl/pstl/hetero/dpcpp/parallel_backend_sycl.h:1578:83)>, sycl::ext::oneapi::experimental::properties<std::tuple<>>>' requested here
      1293 |       kernel_parallel_for_wrapper<KName, TransformedArgType, decltype(Wrapper),
           |       ^
     /usr/bin/compiler/../../include/sycl/handler.hpp:2332:5: note: (skipping 7 contexts in backtrace; use -ftemplate-backtrace-limit=0 to see all)
      2332 |     parallel_for_lambda_impl<KernelName, KernelType, 1, PropertiesT>(
           |     ^
     [...]

  this is fixed by

  .. code-block:: cpp

    struct sycl::is_device_copyable<MyComparator>
      : std::true_type {};


Mathematical functions
======================

- Compatibility issue with using-directives and mathematical functions:

.. code-block:: cpp

    #include <Kokkos_Core.hpp>
    
    using namespace Kokkos;  // avoid using-directives

    KOKKOS_FUNCTION void do_math() {
      auto sqrt5 = sqrt(5);  // error: ambiguous ::sqrt or Kokkos::sqrt?
    }


.. _Compatibility: ./ProgrammingGuide/Compatibility.html

.. |Compatibility| replace:: Kokkos compatibility guidelines

The using-directive ``using namespace Kokkos;`` is highly discouraged (see
|Compatibility|_) and will cause compilation errors in presence of unqualified
calls to mathematical functions.  Instead, prefer explicit qualification
``Kokkos::sqrt`` or an using-declaration ``using Kokkos::sqrt;`` at local
scope.

Mathematical constants
======================

- Avoid taking the address of mathematical constants in device code.  It is not supported by some toolchains, hence not portable.

.. code-block:: cpp

    #include <Kokkos_Core.hpp>

    KOKKOS_FUNCTION void do_math() {
      // complex constructor takes scalar arguments by reference!
      Kokkos::complex z1(Kokkos::numbers::pi);
      // error: identifier "Kokkos::numbers::pi" is undefined in device code

      // 1*pi is a temporary
      Kokkos::complex z2(1 * Kokkos::numbers::pi);  // OK

      // copy into a local variable
      auto pi = Kokkos::numbers::pi;
      Kokkos::complex z3(pi);  // OK
    }
