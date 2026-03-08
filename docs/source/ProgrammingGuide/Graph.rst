グラフ
======

使用例
-----

:cpp:`Kokkos::Graph` は、非同期ワークロードを直接非巡回グラフ(DAG)として組織化した抽象化です。

一度定義されれば、グラフは何度も実行可能です

:cpp:`Kokkos::Graph` は一部のバックエンドに特化しています:

* :cpp:`Cuda`
* :cpp:`HIP`
* :cpp:`SYCL`

これらのバックエンドでは、:cpp:'Kokkos::Graph'　の特殊化はネイティブのグラフ　API、すなわち、CUDA Graph API、HIP Graph API、およびSYCL(コマンド)グラフAPIに、それぞれマッピングされます。



他のバックエンドについては、:cpp:'Kokkos::Graph'　がデフォルトの実装を提供します。

実行空間インスタンスとグラフの比較
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Workloads submitted onexecution space instances execute *eagerly*, *i.e.*,
once the :cpp:`Kokkos::parallel_` function is called, the workload is immediately launched on the device. :cpp:`Kokkos` の実行空間インスタンス上に提出されたワークロード は、*熱心に*　実行されます。*すなわち*、:cpp:'Kokkos::p arallel_'　関数が呼び出されると、デバイス上で即座にワークロードが起動されます。 

対照的に、:cpp:'Kokkos::Graph' 抽象化は、*怠惰*　な実行に従い、*すなわち*　　:cpp:`Kokkos::Graph`　に追加されたワークロードは、グラフ全体が準備できて提出される　*まで*　実行されません。

常に3段階で
~~~~~~~~~~~~~~~~~~

Typically, 3 phases are needed:

1. definition
2. instantiation
3. submission

The *definition* phase consists in describing the workloads: what they do, as well as their dependencies.
In other words, this phase creates a *topological* graph of workloads.

The *instantiation* phase **locks** the topology, *i.e.*, it cannot be changed anymore.
During this phase, the graph will be checked for flaws.
The backend creates an *executable* graph.

The last phase is *submission*. It will execute the workloads, observing their dependencies.
This phase can be run multiple times.

Advantages
~~~~~~~~~~

There are many advantages. Here are a few:

* Since the workloads are described ahead of execution,
  the backend driver and/or compiler can leverage optimization opportunities.
* Launch overhead is reduced, benefitting DAGs consisting of small workloads.

Capture
~~~~~~~

Some use cases might require adding nodes to a :cpp:`Kokkos::Graph`
with workloads that aren't expressed in terms of :cpp:`Kokkos` API
but rather in native code, *e.g.*, calling external math libraries like `cuBLAS`.

Such a scenario can be encountered in many situations like building and training a neural network,
running a conjugate gradient method, and so on.

Capturing into a :cpp:`Kokkos::Graph` boils down to writing the following snippet:

.. code:: c++

    struct MyCudaCapture {
        ViewType data;

        void operator()(const Kokkos::Cuda& exec) const { ... }
    };

    ...

    auto my_captured_node = predecessor.cuda_capture(
        exec,
        MyCudaCapture{.data = my_data}
    );

When the node is added to the :cpp:`Kokkos::Graph`, the workloads are not directly dispatched to the device.
Rather, the backend operations are "saved" for later "reuse" in the *capture* node.

Some important aspects of *capture* are worth pointing out:

1. The function object will be stored by the :cpp:`Kokkos::Graph` instance,
   thereby ensuring that any data bound to the function object is guaranteed to
   stay alive until the graph is destroyed.
2. The execution space instance `exec` associates the captured workloads to a device.
3. While in "*capture* mode", backend-specific restrictions may apply (see `the Cuda programming guide <https://docs.nvidia.com/cuda/cuda-c-programming-guide/#prohibited-and-unhandled-operations>`_
   for instance).

   .. warning::

      When a "stream" is used by multiple threads, capturing on one thread may affect other threads
      (search for :cpp:`cudaThreadExchangeStreamCaptureMode` on `Cuda runtime API documentation <https://docs.nvidia.com/cuda/cuda-runtime-api/>`_ for instance).

For now, *capture* is only supported for the following backends:

.. list-table::

  * - Backend
    - Resources
  * - :cpp:`Cuda`
    - `CUDA stream capture <https://docs.nvidia.com/cuda/cuda-c-programming-guide/#creating-a-graph-using-stream-capture>`_
  * - :cpp:`HIP`
    - `HIP stream capture <https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode>`_
  * - :cpp:`SYCL`
    - `SYCL queue recording <https://github.com/intel/llvm/blob/ee5e1ca95c78576c1b6f12b1c2d461ef4b537a9b/sycl/doc/extensions/experimental/sycl_ext_oneapi_graph.asciidoc?plain=1#L167-LL170>`_

.. note::

    The :cpp:`SYCL` documentation will use the term *recording* instead of *capture*, but it is essentially the same thing.

Examples
--------

Diamond DAG
~~~~~~~~~~~

Consider a diamond-like DAG.

.. graphviz::

    digraph diamond {
        A -> B;
        A -> C;
        B -> D;
        C -> D;
    }

The following snippet defines, instantiates and submits a :cpp:`Kokkos::Graph`
for this DAG.

.. code-block:: c++

    auto graph = Kokkos::create_graph([&](auto root) {
        auto node_A = root.then_parallel_for("workload A", ...policy..., ...functor...);

        auto node_B = node_A.then_parallel_for("workload B", ...policy..., ...functor...);
        auto node_C = node_A.then_parallel_for("workload C", ...policy..., ...functor...);

        auto node_D = Kokkos::when_all(node_B, node_C).then_parallel_for("workload D", ...policy..., ...functor...);
    });

    graph.instantiate();

    graph.submit();

Capture of a `cuBLAS` call
~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a node that captures a `cuBLAS` call.
It also demonstrates how data is kept alive during
the whole lifetime of the :cpp:`Kokkos::Graph` (*e.g.* the `cuBLAS` handle).

.. literalinclude:: examples/graph_capture.cpp
   :language: c++
