グラフ
======

使用方法
--------

:cpp:`Kokkos::Graph` は、非同期ワークロードを直接非巡回グラフ(DAG)として組織化した抽象化です。

一度定義されれば、グラフは何度も実行可能です

:cpp:`Kokkos::Graph` は一部のバックエンドに特化しています:

* :cpp:`Cuda`
* :cpp:`HIP`
* :cpp:`SYCL`

これらのバックエンドでは、:cpp:`Kokkos::Graph` の特殊化はネイティブのグラフ API、すなわち、CUDA Graph API、HIP Graph API、およびSYCL(コマンド)グラフAPIに、それぞれマッピングされます。



他のバックエンドについては、 :cpp:`Kokkos::Graph` がデフォルトの実装を提供します。

実行空間インスタンスとグラフの比較
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 :cpp:`Kokkos` の実行空間インスタンス上に提出されたワークロード は、*熱心に* 実行されます。*すなわち*、:cpp:`Kokkos::parallel_` 関数が呼び出されると、デバイス上で即座にワークロードが起動されます。 

対照的に、:cpp:`Kokkos::Graph` 抽象化は、*怠惰* な実行に従い、*すなわち* :cpp:`Kokkos::Graph` に追加されたワークロードは、グラフ全体が準備できて提出される *まで* 実行されません。

常に3段階で
~~~~~~~~~~~~~~~~~~

常、3段階が必要です:

1. 定義
2. インスタンス化
3. 提出

*定義* フェーズは、ワークロードが何をするのか、そして依存関係を記述することから成り立っています。言い換えれば、このフェーズでは、ワークロードの *トポロジカル* グラフが作成されます。

*インスタンス化* フェーズは  位相を *ロックし*、 *つまり*、もはや変更できない状態にします。 この段階では、グラフに欠陥がないかチェックされます。バックエンドは、*実行可能な* グラフを作成します。

最後の段階は、*提出* です。 ワークロードを実行し、その依存関係を観察します。 このフェーズは、複数回実行可能です。

利点
~~~~~~~~~~

多くの利点がありますので、いくつか紹介します:

* ワークロードは、実行前に記述されるため、バックエンドドライバーおよび/またはコンパイラは、最適化の機会を活用できます。 
* ローンチオーバーヘッドが削減され、小規模な作業負荷からなる DAG に有利です。

キャプチャ
~~~~~~~~~~~~

一部の使用例では、 :cpp:`Kokkos::Graph` にノードを追加し、:cpp:`Kokkos` API ではなく、ネイティブコードで表現されるノード、*例えば*、 `cuBLAS` のような外部数学ライブラリを呼び出す必要がある場合があります。

このようなシナリオには、ニューラルネットワークの構築/訓練、共役勾配法の実行など、多くの状況で遭遇します。

キャプチャーを  :cpp:`Kokkos::Graph` にまとめるには、以下のようなスニペットを書き込むことになります:

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

ノードが、 :cpp:`Kokkos::Graph`  に追加されると、ワークロードは、直接デバイスにディスパッチされません。むしろ、バックエンド演算は、後で *キャプチャ* ノードで "再利用"するために、"保存" されます  。

 *キャプチャ* の重要な側面を、一部指摘しておく価値があります:

1. 関数オブジェクトは  :cpp:`Kokkos::Graph` インスタンスによって保存されるため、関数オブジェクトにバインドされたデータはグラフが破壊されるまで必ず存続することが保証されます。 
2. 実行空間インスタンスの `exec` は、キャプチャされたワークロードをデバイスに関連付けます。
3. "*キャプチャ* モード"中では、バックエンド固有の制限が適用される場合があります (例えば、`Cudaプログラミングガイド <https://docs.nvidia.com/cuda/cuda-c-programming-guide/#prohibited-and-unhandled-operations>`_ を参照)。

   .. warning::

      "ストリーム" が複数のスレッドで使用されている場合、あるスレッドでのキャプチャが、他のスレッドに影響を与えることがあります(例えば、Cuda ランタイム API 文書上の :cpp:`cudaThreadExchangeStreamCaptureMode` <https://docs.nvidia.com/cuda/cuda-runtime-api/>`_ で を検索してください)。 

現時点では、*キャプチャ* は以下のバックエンドのみでサポートされています:

.. list-table::

  * - バックエンド
    - リソース
  * - :cpp:`Cuda`
    - `CUDA ストリームキャプチャ <https://docs.nvidia.com/cuda/cuda-c-programming-guide/#creating-a-graph-using-stream-capture>`_
  * - :cpp:`HIP`
    - `HIP ストリームキャプチャ <https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode>`_
  * - :cpp:`SYCL`
    - `SYCL キューレコーディング <https://github.com/intel/llvm/blob/ee5e1ca95c78576c1b6f12b1c2d461ef4b537a9b/sycl/doc/extensions/experimental/sycl_ext_oneapi_graph.asciidoc?plain=1#L167-LL170>`_

.. note::

    :cpp:`SYCL` の文書では、*キャプチャ* ではなく *レコーディング* という用語が使われていますが、実質的には同じ意味です。

例
--------

ダイヤモンド DAG
~~~~~~~~~~~~~~~~

ダイヤモンド様の DAG を考えてみましょう。

.. graphviz::

    digraph diamond {
        A -> B;
        A -> C;
        B -> D;
        C -> D;
    }

以下のスニペットは、この DAG に対して、 :cpp:`Kokkos::Graph` を定義し、インスタンス化し、提出します。

.. code-block:: c++

    auto graph = Kokkos::create_graph([&](auto root) {
        auto node_A = root.then_parallel_for("workload A", ...policy..., ...functor...);

        auto node_B = node_A.then_parallel_for("workload B", ...policy..., ...functor...);
        auto node_C = node_A.then_parallel_for("workload C", ...policy..., ...functor...);

        auto node_D = Kokkos::when_all(node_B, node_C).then_parallel_for("workload D", ...policy..., ...functor...);
    });

    graph.instantiate();

    graph.submit();

`cuBLAS` 呼び出しのキャプチャ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本例は、 `cuBLAS` コールをキャプチャするノードの作成方法を示しています。また、 :cpp:`Kokkos::Graph` (*例* `cuBLAS` ハンドル) の全寿命を通じて、データがどのように保存されているかも示しています。

.. literalinclude:: examples/graph_capture.cpp
   :language: c++
