クイックスタート
================

このガイドは、新しい Kokkos ユーザー(特に初心者) のジャンプスタートを目的としたものです。


前提条件
~~~~~~~~~~~~~

このチュートリアルを完了するには、以下の条件が必要です:

* 互換性のあるオペレーティングシステム（例: Linux、macOS、Windows）
* 少なくとも C++20 をサポートする互換性のある C++ コンパイラ
* `CMake <https://cmake.org/>`_ とプロジェクト構築のための互換性のある構築ツール。


  * 互換性のある構築ツールには、 `Make
    <https://www.gnu.org/software/make/>`_, `Ninja <https://ninja-build.org>`_ などがあります - 詳細については、`CMake Generators
    <https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html>`_ を参照してください。

Kokkos 対応プラットフォーム、サポートされたコンパイラおよびソフトウェア開発キット (SDK) のバージョン一覧の詳細については、 :doc:`requirements` を参照してください。


CMake をインストールしていない場合は、`CMake installation guide <https://cmake.org/install>`_ を参照してください。


プロジェクトのセットアップ
~~~~~~~~~~~~~~~~~~~~~~~~~~

CMakeは、``CMakeLists.txt`` というファイルを使って  プロジェクトの構築システムを設定します。 このファイルを使ってプロジェクトを設定し、Kokkos への依存を宣言します。

まず、プロジェクト用のディレクトリを作成します:


.. code-block:: sh

  > mkdir MyProject && cd MyProject

次に、``CMakeLists.txt`` ファイルを作成し、Kokkos への依存を宣言します。 CMake エコシステムでは、依存関係を表現する方法は多岐にわたります； このチュートリアルでは、 `FetchContent CMake module
<https://cmake.org/cmake/help/latest/module/FetchContent.html>`_. を使用します。 そのために、プロジェクトディレクトリ(``MyProject``)に、 以下の内容を含む ``CMakeLists.txt`` というファイルを作成します：

.. code-block:: cmake

  cmake_minimum_required(VERSION 3.22)
  project(MyProject)
  
  include(FetchContent)
  FetchContent_Declare(
    Kokkos
    URL https://github.com/kokkos/kokkos/archive/refs/tags/5.0.0.zip
  )
  FetchContent_MakeAvailable(Kokkos)

上記の設定は、GitHub からダウンロードした Kokkos への依存関係を宣言しています。
``5.0.0`` は、使用する Kokkos バージョンです; 通常は、
`利用可能な最新版 <https://github.com/kokkos/kokkos/releases/latest>`_ の使用を推奨します。

``CMakeLists.txt files`` の作成方法の詳細情報については、 
`CMake Tutorial
<https://cmake.org/cmake/help/latest/guide/tutorial/index.html>`_ を参照してください。


実行ファイルを作成して実行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kokkos を依存関係として宣言すれば、自分のプロジェクト内で、Kokkos のコードを使うことができます。

例えば、  以下の内容で、 ``HelloKokkos.cpp`` を作成します:

.. code-block:: c++

  #include <Kokkos_Core.hpp>

  int main(int argc, char** argv) {
    Kokkos::initialize(argc, argv);
    {
      // 整数の1次元ビューを割り当てます
      Kokkos::View<int*> v("v", 5);
      // ビューを連続的に増加する値v=[0,1,2,3,4] を入力します
      Kokkos::parallel_for("fill", 5, KOKKOS_LAMBDA(int i) { v(i) = i; });
      //  vの要素 r=0+1+2+3+4 の累積和を計算します。
      int r;
      Kokkos::parallel_reduce(
        "accumulate", 5,
        KOKKOS_LAMBDA(int i, int& partial_r) { partial_r += v(i); }, r);
      // 結果を確認してください
      KOKKOS_ASSERT(r == 10);
    }
    Kokkos::printf("Goodbye World\n");
    Kokkos::finalize();
    return 0;
  }

上記のプログラムコードには、Kokkos のメインヘッダーファイルが含まれており、Kokkos の実行環境の初期化および最終処理方法を示しています。

コードをビルドするために、``CMakeLists.txt`` ファイルの末尾に以下の数行を追加します:

.. code-block:: cmake

  add_executable(HelloKokkos HelloKokkos.cpp)
  target_link_libraries(HelloKokkos Kokkos::kokkos)


上記の設定では、構築したい実行ファイル(``HelloKokkos``) を宣言し、それを Kokkos にリンクします

これで Kokkos のプログラムを構築および実行可能です。

まず ``cmake`` を呼び出して、プロジェクトを設定し、ネイティブビルドシステムを生成します:

.. code-block:: sh

  MyProject> cmake -B builddir
  -- The C compiler identification is GNU 13.3.0
  -- The CXX compiler identification is GNU 13.3.0
  ...
  -- Build files have been written to: .../MyProject/builddir

.. note::

   NVIDIA GPU をターゲットにしたい場合は、上記の cmake コマンドに、追加の ``-DKokkos_ENABLE_CUDA=ON`` 引数を渡す必要があります。AMD または Intel GPU については、それぞれ ``-DKokkos_ENABLE_HIP=ON`` または ``-DKokkos_ENABLE_SYCL=ON`` と表記します。 設定時に利用可能なオプションや変数の一覧については、:doc:'configuration-guide' を参照してください。

次に、その構築システムを呼び出して、実際にプロジェクトをコンパイル/リンクします:

.. code-block:: sh

  MyProject> cmake --build builddir
  Scanning dependencies of target ...
  ...
  [100%] Built target HelloKokkos

最後に、新たに構築した ``HelloKokkos`` の使用を試します:

.. code-block:: sh

  MyProject> cd builddir

  MyProject/builddir> HelloKokkos
  Goodbye World

.. note::

   シェルによっては、正しい構文は ``HelloKokkos``、
   ``./HelloKokkos``、または ``.\HelloKokkos`` といった場合もあります。

おめでとうございます! Kokkos を使ってテストバイナリを成功裏に構築し実行することに成功しました！


ヘルプ
~~~~~~~~~~~~

スタートについて、さらにサポートが必要な場合は、 `Kokkos Slack Workspace <https://kokkosteam.slack.com>`_ に参加してください。 サインアップに問題が生じた場合は、 :ref:`参加方法に関するFAQエントリ <join-slack-workspace>` をご覧ください。
