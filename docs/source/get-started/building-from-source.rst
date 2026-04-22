ソースからの構築
====================

Kokkos のソースコード取得
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本セクションでは、Kokkos のソースコードを取得する方法について説明します。 これらのリリースは広範なテストを経ており、一般的に安定性が高いため、多くのユーザーにタグ付きリリースのダウンロードを推奨します。 最新機能が必要な上級者向けにも、開発版が利用可能で、安定性の低いコードにも対応できる場合があります。

リリースアーカイブのダウンロード(推奨)
-------------------------------------------

多くのユーザーに推奨されるアプローチは、GitHub からのリリースアーカイブのダウンロードです。

1.  **最新リリースを探す:**  `Kokkos リリースページ <https://github.com/kokkos/kokkos/releases>`_ にアクセスして最新リリース（または必要な特定のバージョン）を見つけてください。

2.  **アーカイブとチェックサムをダウンロードしてください:** ``kokkos-X.Y.Z.tar.gz`` アーカイブと対応する ``kokkos-X.Y.Z-SHA-256.txt`` チェックサムファイルの両方をダウンロードしてください。 チェックサムを使ってダウンロードしたアーカイブの整合性を確認することが重要です。

3.  **アーカイブの整合性を確認する(重要):**  ダウンロードされたアーカイブの確認には、以下のコマンドを使用してください(バージョン番号を必要に応じて調整してください):


    .. code-block:: sh
    
        export KOKKOS_VERSION=4.5.01  # 実際のバージョンと置き換えます
        export KOKKOS_DOWNLOAD_URL=https://github.com/kokkos/kokkos/releases/download/${KOKKOS_VERSION}
        curl -sLO ${KOKKOS_DOWNLOAD_URL}/kokkos-${KOKKOS_VERSION}.tar.gz
        curl -sLO ${KOKKOS_DOWNLOAD_URL}/kokkos-${KOKKOS_VERSION}-SHA-256.txt
        grep kokkos-${KOKKOS_VERSION}.tar.gz kokkos-${KOKKOS_VERSION}-SHA-256.txt | shasum -c


出力は、 ``kokkos-4.5.01.tar.gz: OK``  (または同様のもの、バージョンによる)であるべきです。 チェックサムが一致しない場合は、 破損や改ざんされている可能性があるため、**ダウンロードしたアーカイブを使用しないでください** 。

4.  **アーカイブを抽出する:**  チェックサムを確認したら、アーカイブを抽出してください:

    .. code-block:: sh

        tar -xzvf kokkos-${KOKKOS_VERSION}.tar.gz

Gitリポジトリのクローニング (開発バージョン用)
-----------------------------------------------------

最新機能が必要な場合、または Kokkos にコントリビュートしたい場合、Git リポジトリをクローンできます

1.  **レポジトリをクローンします:**

    .. code-block:: sh

        git clone https://github.com/kokkos/kokkos.git

    これによりリポジトリは、``kokkos`` というディレクトリにクローンされます。

2.  **リリースタグをチェックアウトします（開発には推奨）:**
    ``develop`` ブランチは概ね安定していますが、現在も活発に開発が進められています。 より予測可能な動作を求めるなら、特定のリリースタグをチェックアウトしてください:


    .. code-block:: sh

        cd kokkos
        git checkout 4.5.01  # 所望のバージョンタグを置き換えます

    利用可能なタグを見るために:

    .. code-block:: sh

        git tag

   あるいは、最先端を保つために(慎重に使用):

    .. code-block:: sh

        git checkout develop


どの方法を使うべきでしょうか?
-----------------------------

* **タグ付きリリース:** 特に開発版を使う理由がない限り、この方法を使ってください。 タグ付きリリースが最も安定していて、十分にテストされています。
* **Git リポジトリ(開発バージョン):** 最新の機能が必要な場合、Kokkos に貢献したい場合、または開発ブランチで修正された特定の問題をデバッグしたい場合に、この方法を使ってください。  開発版は、リリース版よりも安定性が劣る場合がありますので、注意してください。


どの方法を選ぶにしても、必ずダウンロードしたソースコードの整合性を確認してください。  これは重要なセキュリティプラクティスです。


Kokkos の設定と構築
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本節では、Kokkos の設定とビルド方法について説明します。Kokkos ソースコード（または Kokkos を組み込んだプロジェクト）のディレクトリにいることを前提としています。

Kokkos 設定
------------------

Kokkos の設定には以下のコマンドを使用します :

.. code-block:: sh

    cmake -B builddir [<options...>]


``-B builddir`` は、 ``builddir`` というビルドディレクトリを作成します(別の名前を選んでも構いません)。  Kokkos はソース外ビルドを必要とします。   ``[<options...>]``   の部分は設定オプションを指定する部分です。

**一般的な CMake の選択肢**

これらのオプションは、一般的にはあらゆる CMake プロジェクトに役立ちます：

* ``-DCMAKE_CXX_COMPILER=<compiler>``: C++ コンパイラへの完全なパスを指定します。例えば、AMD GPU には ``hipcc``、Intel GPU には ``icpx``、CPU には ``g++`` または ``clang++`` を使いましょう。

  例: ``-DCMAKE_CXX_COMPILER=/path/to/hipcc``

* ``-DCMAKE_CXX_STANDARD=<standard>``: C++ 標準を設定します  。デフォルトは、``20`` です。

  例: ``-DCMAKE_CXX_STANDARD=23``

* ``-DCMAKE_BUILD_TYPE=<type>``: 最適化レベルとデバッグ情報を制御します。一般的な選択肢は、 ``Debug`` 、 ``Release`` 、 ``RelWithDebInfo`` (デフォルト)、 および ``MinSizeRel`` です。

  例: ``-DCMAKE_BUILD_TYPE=Release``

* ``-DCMAKE_INSTALL_PREFIX=<prefix>``: ディスク上のディレクトリを指定します。
  Kokkos が設置される予定です。


  例: ``-DCMAKE_INSTALL_PREFIX=/path/to/install/dir``

** Kokkos 固有の重要なオプション:**


* ``-DKokkos_ENABLE_<BACKEND>=ON``: 現在オープンソース化されている実験的バックエンド等、ターゲットデバイス向けの特定のバックエンドを有効にします。完全なリストについては :ref:`keywords_backends` を参照してください。

  一般的なバックエンド:

  * ``OPENMP`` または ``THREADS``:  CPUs 上でマルチスレッド処理
  
  * ``CUDA``: NVIDIA GPUs
  
  * ``HIP``: AMD GPUs

  * ``SYCL``: Intel GPUs
    
  例: ``-DKokkos_ENABLE_CUDA=ON``
  Windows  上でCUDAとMSVCを使ったビルドでは、 ``-DKokkos_ENABLE_COMPILE_AS_CMAKE_LANGUAGE=ON`` が必要であることに注意してください。



  実験的なバックエンドと :ref:`keywords_enable_backend_specific_options` を含めます。


* ``-DKokkos_ARCH_<ARCHITECTURE>=ON``: コード生成のためのターゲットアーキテクチャを指定します。一部のバックエンドはアーキテクチャを自動検出できますが、明示的に指定するのが最適である場合が多いです。
  完全なリストについては、 :ref:`keywords_arch` を参照してください。
  例えば:

  * ``AMD_GFX90A``: AMD MI210X (Frontier)

  * ``INTEL_PVC``: Intel Data Center Max 1550 (Aurora)

  * ``AMPERE80``: NVIDIA A100 (Perlmutter)

  例: ``-DKokkos_ARCH_AMPERE80=ON``

* ``-DKokkos_ENABLE_DEPRECATED_CODE_4=ON``: 非推奨とマークされた、すべてのコードを有効化します。これを、 ``OFF`` に設定すると、非推奨のシンボルが削除されます。
  
* ``-DKokkos_ENABLE_DEPRECATION_WARNINGS=ON``: 非推奨警告を有効にします。
  今後のリリースでサプライズを避けるために、これを強く推奨します。理由がない限り、これを無効にしないでください。


**構成例**

.. code-block:: sh

    cmake -B builddir \
        -DCMAKE_CXX_COMPILER=g++ \
        -DCMAKE_BUILD_TYPE=Release \
        -DKokkos_ENABLE_OPENMP=ON \
        -DKokkos_ARCH_NATIVE=ON \
        -DKokkos_ENABLE_DEPRECATED_CODE_4=OFF


Kokkos 構築
---------------

設定後、以下のコマンドで Kokkos をビルドします:

.. code-block:: sh

    cmake --build builddir

これにより Kokkos をコンパイルします。複数コアを使うには、``-j<N>`` を追加することで、高速にコンパイルできます（``<N>`` をコア数に置換します）。

例: ``cmake --build builddir -j8``


Kokkos インストール
--------------------

Kokkos のインストール (ヘッダーファイルおよびライブラリ) のために、以下を使用してください:

.. code-block:: sh

    cmake --install builddir [--prefix <prefix>]

``--prefix <prefix>`` オプションはインストールディレクトリを指定します。 省略すると、Kokkos はデフォルトの場所、多くの場合 ``/usr/local`` (**非推奨**) にインストールされます。

オプション: Kokkos 構築テスト
-----------------------------------

Kokkos の構築を確認し、すべてが期待通りに動作しているか確認するには、内部テストスイートを設定し、実行できます。

これを行うには、``-DKokkos_ENABLE_TESTS=ON`` を設定および構築し、以下でテストを実行します：

.. code-block:: sh

    ctest --test-dir builddir --output-on-failure


上級:ビルドディレクトリに対する設定
-------------------------------------------------

(エキスパート専用)プロジェクトは、インストールツリーを使うのと同様に、ツリー外ビルド内の ``<builddir>/cmake_packages/`` ディレクトリに直接プロジェクトを設定することができます。  これは開発目的において、有用です。
