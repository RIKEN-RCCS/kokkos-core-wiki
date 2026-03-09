パッケージマネージャー
================

好みのパッケージマネージャーを使って、Kokkos　をインストールしてください。

システムパッケージマネージャー
~~~~~~~~~~~~~~~~~~~~~~~

DNF
---

 Kokkos　をインストールするには、Fedora Project　パッケージマネージャーを使うことができます 
https://packages.fedoraproject.org/pkgs/kokkos/

他のパッケージマネージャー
~~~~~~~~~~~~~~~~~~~~~~

`Spack <https://spack.io>`_
---------------------------

 Kokkos.は　HPC向けの、有名なパッケージマネージャーです。  Spack　には、　Kokkos　のインストールレシピが付属しています。

 `Kokkos レシピウェブページ <https://packages.spack.io/package.html?name=kokkos>`_ には  、Kokkosの利用可能なバージョンとそのオプションがまとめられています。

ほとんどの場合、Spack Kokkos　のバリアントは、Kokkosの　`CMake options <./configuration-guide.html>`_. と同じオプションに従っています。
利用可能なバリアントのリストは、以下の実行により、見つけることができます


.. code-block::

    スパック情報 kokkos


Spackを使用する場合、Kokkos のハードウェア自動検出は無効です。 つまり、ユーザーが、常に手動でアーキテクチャを指定しなければならないということです。 しかしながら、CPU　の場合、Spack　はすでに　CPU　マイクロアーキテクチャを指定しているため、再度指定する必要はありません。
GPUに関しては、Spack　にはそのような仕組みは存在せず、ユーザーは専用のバックエンドキーワードを使って、正しいアーキテクチャを指定する必要があります(次の節参照)。



Spack　で　Kokkos　インストール

++++++++++++++++++++++++++++

デフォルトのオプションを使って、　Spack　で　Kokkos　をインストールするには、以下を実行してください:

.. code-block::

    spack インストール kokkos


 CUDA バックエンドを有効にした状態で、Kokkos　をインストールするには、以下を実行してください:

.. code-block::

    spack インストール kokkos +cuda cuda_arch=90


`cuda_arch`オプションが、ターゲット　GPU　アーキテクチャ専用であることに注意してください。  ここでの `cuda_arch` 値　`90` は、NVIDIA Hopper　アーキテクチャに対応しています。 Spack　ではアーキテクチャを明示的に指定する必要があります　(自動検出なし)。


AMD GPU　に関しては、従来の　Spack　のキーワードはKokkosのCMakeでは　`hip` ではなく、`rocm` です。HIP　バックエンドを有効にした　Kokkos　をインストールするには、以下を実行してください:

.. code-block::

    spack インストール kokkos +rocm amdgpu_target=gfx942


 `amdgpu_target`　オプションは、対象　GPU　アーキテクチャ固有のものです。
Spack　ではアーキテクチャを明示的に指定する必要があります(自動検出なし)。



Intel GPU　に関しては、 SYCL バックエンドを使用して、 以下を実行します:

.. code-block::

    spack spec kokkos +sycl intel_gpu_arch=intel_pvc


 `intel_gpu_arch` オプションは、対象のGPU　アーキテクチャ専用であることに、注意してください。
Spack　ではアーキテクチャを明示的に指定する必要があります(自動検出なし)。


To use the installed Kokkos, you can simply load the Kokkos module:

.. code-block::

    spack load kokkos


This will inject the Kokkos environment into your shell session.

Packaging your own Kokkos dependent project with Spack
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Let's say you have a project `Foo` that depends on `Kokkos`. You can package your project with Spack and include `Kokkos` as a dependency.

You have to create a recipe that is contained in a file named `package.py` in the `foo` directory of your recipe repository.
You can package as usual with Spack (for example, you can follow the `packaging tutorial <https://spack-tutorial.readthedocs.io/en/latest/tutorial_packaging.html>`_),
but you have to take into account that for certain backends, you might need to specify the compiler to use.

The compiler might be a wrapper, like `nvcc_wrapper` for CUDA. It is exported by the Kokkos package as the `kokkos_cxx` attribute.

Here is an example of a `package.py` file that includes Kokkos as a dependency:

.. code-block:: python

    from spack.package import *

    class Foo(CMakePackage):
        # Usual description of a Spack package

        depends_on("kokkos")

        def cmake_args(self):
            args = []
            # Ensure that the proper compiler is used
            # It might be nvcc_wrapper
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))
            return args


For more complete examples, you can look at already existing recipes in the *Required by* section of
`Kokkos Spack recipe <https://packages.spack.io/package.html?name=kokkos>`_ or by running:

.. code-block::

    spack dependents kokkos

