パッケージマネージャー
======================

好みのパッケージマネージャーを使って、Kokkos をインストールしてください。

システムパッケージマネージャー
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DNF
---
Kokkos をインストールするには、Fedora Project パッケージマネージャーを使うことができます 
https://packages.fedoraproject.org/pkgs/kokkos/

他のパッケージマネージャー
~~~~~~~~~~~~~~~~~~~~~~~~~~

`Spack <https://spack.io>`_
---------------------------
Kokkos.は HPC向けの、有名なパッケージマネージャーです。  Spack には、 Kokkos のインストールレシピが付属しています。
 
`Kokkos レシピウェブページ <https://packages.spack.io/package.html?name=kokkos>`_ には  、Kokkosの利用可能なバージョンとそのオプションがまとめられています。

ほとんどの場合、Spack Kokkos のバリアントは、Kokkosの `CMake options <./configuration-guide.html>`_. と同じオプションに従っています。
利用可能なバリアントのリストは、以下の実行により、見つけることができます


.. code-block::

    スパック情報 kokkos


Spackを使用する場合、Kokkos のハードウェア自動検出は無効です。 つまり、ユーザーが、常に手動でアーキテクチャを指定しなければならないということです。 しかしながら、CPU の場合、Spack はすでに CPU マイクロアーキテクチャを指定しているため、再度指定する必要はありません。
GPUに関しては、Spack にはそのような仕組みは存在せず、ユーザーは専用のバックエンドキーワードを使って、正しいアーキテクチャを指定する必要があります(次の節参照)。



Spack で Kokkos インストール

++++++++++++++++++++++++++++

デフォルトのオプションを使って、 Spack で Kokkos をインストールするには、以下を実行してください:

.. code-block::

    spack install kokkos


 CUDA バックエンドを有効にした状態で、Kokkos をインストールするには、以下を実行してください:

.. code-block::

    spack install kokkos +cuda cuda_arch=90


`cuda_arch`オプションが、ターゲット GPU アーキテクチャ専用であることに注意してください。  ここでの `cuda_arch` 値 `90` は、NVIDIA Hopper アーキテクチャに対応しています。 Spack ではアーキテクチャを明示的に指定する必要があります (自動検出なし)。


AMD GPU に関しては、従来の Spack のキーワードはKokkosのCMakeでは `hip` ではなく、`rocm` です。HIP バックエンドを有効にした Kokkos をインストールするには、以下を実行してください:

.. code-block::

    spack install kokkos +rocm amdgpu_target=gfx942


 `amdgpu_target` オプションは、対象 GPU アーキテクチャ固有のものです。Spack ではアーキテクチャを明示的に指定する必要があります(自動検出なし)。


Intel GPU に関しては、 SYCL バックエンドを使用して、 以下を実行します:

.. code-block::

    spack spec kokkos +sycl intel_gpu_arch=intel_pvc


`intel_gpu_arch` オプションは、対象のGPU アーキテクチャ専用であることに、注意してください。
Spack ではアーキテクチャを明示的に指定する必要があります(自動検出なし)。


Kokkosモジュールをロードするだけで、インストール済みの Kokkos を使用できます:

.. code-block::

    spack load kokkos


これにより Kokkos 環境がシェルセッションに注入されます。

Spack で自分だけの Kokkos 依存プロジェクトをパッケージ化する方法
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


例えば、プロジェクト `Foo` が  `Kokkos` に依存しているとしましょう。 プロジェクトを Spack でパッケージ化し、 `Kokkos` を依存関係として含めることもできます。

レシピリポジトリの `foo` ディレクトリにある  `package.py` というファイルにレシピを作成する必要があります。
通常通りSpackでパッケージ化できます(例えば,  <https://spack-tutorial.readthedocs.io/en/latest/tutorial_packaging.html>`_ に従うことができます)が、特定のバックエンドでは、それを考慮に入れる必要があり、使用するコンパイラを指定する必要がある場合もあります。

コンパイラは、CUDA の `nvcc_wrapper` のようなラッパーかもしれません。 Kokkosパッケージでは、`kokkos_cxx` 属性としてエクスポートされます。

以下は、Kokkos を依存関係として含む  `package.py` ファイルの例です:

.. code-block:: python

    spack.package からインポート *

    class Foo(CMakePackage):
        #  Spack パッケージの有用なディスクリプション

        depends_on("kokkos")

        def cmake_args(self):
            args = []
            # 適切なコンパイラが使用されていることを保証します
            # それは、 nvcc_wrapper かもしれません。
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))
            return args


より完全な例としては、`Kokkos Spack recipe <https://packages.spack.io/package.html?name=kokkos>`_ の *Required by* セクション内にある既存のレシピを参照するか、以下を実行してください:

.. code-block::

    spack dependents kokkos

