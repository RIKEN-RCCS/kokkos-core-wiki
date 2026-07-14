Kokkos をプロジェクトに統合
===========================

このドキュメントは、Kokkos ライブラリを CMake プロジェクトに統合する方法を説明しています。

Kokkosは、 ``Kokkos::kokkos`` というターゲットを提供しており、必要なディレクトリ、リンクライブラリ、コンパイラオプション、その他の使用要件を自動的に処理することでプロセスを簡素化します。

以下はそれぞれ利点を持ついくつかの統合方法です：

1. 外部 Kokkos (ほとんどのユーザーに推奨)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

推奨アプローチは、Kokkosを外部依存関係として利用することです。 これにより管理や更新がより容易になります。  CMake の `find_package() <https://cmake.org/cmake/help/latest/command/find_package.html>`_ コマンドを使って、既存の Kokkos インストールを特定しリンクしてください:

.. code-block:: cmake

find_package(Kokkos 4.2 REQUIRED CONFIG) # Kokkos バージョン 4.2 以降を検索
  # ...
  target_link_libraries(MyTarget PRIVATE Kokkos::kokkos)

* ``find_package(Kokkos ...)`` は、Kokkos の構築およびインストール時に生成される ``KokkosConfig.cmake`` ファイルを検索します。このファイルには、Kokkos にリンクするために必要な情報が含まれています。
* ``4.2`` 引数は、最低限必要な Kokkos バージョンを指定します。これは任意ですが、互換性を確保するために推奨されています。なお、これによってプロジェクトは、次のメジャーリリース（例えば ``5.0``）を含む、より新しいバージョンをすべて受け入れるように設定される点に注意してください。

* Kokkos ``4.x`` に厳密にとどまる必要がある場合（``5.0`` での破壊的変更を避けるため）は、代わりにバージョン範囲を指定する必要があります。

.. code-block:: cmake

# Kokkos 4.2 以降を検索するが、5.0 より前で停止する
      find_package(Kokkos 4.2...<5.0 REQUIRED CONFIG)

* ``Kokkos::kokkos`` は、必要なビルドフラグをすべて提供する名前空間付きのインポートターゲットです。
* ``CONFIG`` キーワードは、CMake に設定ファイルを使うように指示します。

Kokkos は別途インストールし、CMake で``Kokkos_ROOT`` 変数を使ってその場所を指すこともできます。

.. code-block:: sh

MyProject> cmake -DKokkos_ROOT=/path/to/kokkos/install/dir -B builddir

2.  ``add_subdirectory()`` 経由の組み込み Kokkos および Git サブモジュール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本方法は、Kokkos のソースコードを直接プロジェクトに組み込む方法です。 Kokkos バージョンを非常に厳密に管理したい場合や、Kokkos を別途インストールできない場合に便利です。

1.  `Git submodule <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_ として、Kokkos を追加します

.. code-block:: sh

MyProject> git submodule add -b 4.5.01 https://github.com/kokkos/kokkos.git tpls/kokkos
  MyProject> git commit -m 'サブモジュールとして Kokkos v4.5.1 を追加'

``tpls/kokkos/`` は、完全な Kokkos ソースツリーを含む必要があります。

2. CMakeLists.txt 内で、 ``add_subdirectory()`` を使用します:

.. code-block:: cmake

add_subdirectory(tpls/kokkos)
  # ...
  target_link_libraries(MyTarget PRIVATE Kokkos::kokkos)

3.  ``FetchContent`` 経由での組み込み Kokkos 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
`FetchContent <https://cmake.org/cmake/help/latest/module/FetchContent.html>`_ は、
CMake の設定段階で、Kokkos をダウンロードし依存関係として含めるプロセスを簡素化します。

.. code-block:: cmake

include(FetchContent)
  FetchContent_Declare(
      Kokkos
      URL      https://github.com/kokkos/kokkos/releases/download/4.5.01/kokkos-4.5.01.tar.gz
      URL_HASH SHA256=52d003ffbbe05f30c89966e4009c017efb1662b02b2b73190670d3418719564c
  )
  FetchContent_MakeAvailable(Kokkos)
  # ...
  target_link_libraries(MyTarget PRIVATE Kokkos::kokkos)

* ダウンロードされたアーカイブの整合性を検証するために、 ``URL_HASH`` を強く推奨します。 Kokkos リリースの SHA256 チェックサムは、
  `Kokkos リリースページ <https://github.com/kokkos/kokkos/releases>`_ 上 の ``kokkos-X.Y.Z-SHA-256.txt`` ファイル内で、確認できます。

4. 外部および組み込み両型の Kokkos のサポート
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

このアプローチにより、プロジェクトは外部の Kokkos インストールまたは組み込みバージョンのいずれかを使用でき、異なるビルド環境に柔軟性を提供します。

.. code-block:: cmake

find_package(Kokkos CONFIG) # Kokkos の外部での発見を試みます
  if(Kokkos_FOUND)
      message(STATUS "Found Kokkos: ${Kokkos_DIR} (version \"${Kokkos_VERSION}\")")
  else()
      message(STATUS "Kokkos は外部で確認できません。 FetchContent 経由でフェッチします。")
      include(FetchContent)
      FetchContent_Declare(
          Kokkos
          URL https://github.com/kokkos/kokkos/archive/refs/tags/4.4.01.tar.gz
      )
      FetchContent_MakeAvailable(Kokkos)
  endif()
  # ...
  target_link_libraries(MyTarget PRIVATE Kokkos::kokkos)

Kokkos 統合をコントロール:

* `CMAKE_DISABLE_FIND_PACKAGE_Kokkos <https://cmake.org/cmake/help/latest/variable/CMAKE_DISABLE_FIND_PACKAGE_PackageName.html>`_:
  外部でのインストールが見つかった場合でも、組み込み  Kokkos の使用を強制するために、本変数を ``TRUE`` に設定します。
* `CMAKE_REQUIRE_FIND_PACKAGE_Kokkos <https://cmake.org/cmake/help/latest/variable/CMAKE_REQUIRE_FIND_PACKAGE_PackageName.html>`_:
  外部の Kokkosインストールを要求するために、本変数を ``TRUE`` に設定します。Kokkos が見つからない場合には、構築は失敗します。
* ``Kokkos_ROOT``: CMake が``find_package()`` を使う際に、Kokkos  を検索すべきディレクトリを指定するために、本変数を使用します。

例えば:

.. code-block:: sh

cmake -DCMAKE_REQUIRE_FIND_PACKAGE_Kokkos=ON -DKokkos_ROOT=/path/to/kokkos/install/dir

または

.. code-block:: sh

cmake -DCMAKE_DISABLE_FIND_PACKAGE_Kokkos=ON

.. note::
   CMake バージョン 3.24 以降では、``FetchContent`` を ``find_package()`` と統合する標準的な方法が導入されました。
   上記の例のように、ソースからのダウンロードおよびビルドにフォールバックする前に、まず `find_package()` を介して Kokkos を検索しようとする場合は、次のより簡潔な構文を使用できます。

.. code-block:: cmake

FetchContent_Declare(
          Kokkos
          URL https://github.com/kokkos/kokkos/archive/refs/tags/4.4.01.tar.gz
          FIND_PACKAGE_ARGS 4.2 CONFIG 
      )
      FetchContent_MakeAvailable(Kokkos)

`FIND_PACKAGE_ARGS <https://cmake.org/cmake/help/latest/module/FetchContent.html#integrating-with-find-package>`_ キーワードは、CMake に対して、``FetchContent`` を介してダウンロードする前に、まず指定された引数で ``find_package()`` を呼び出すように指示します。
   常に取得された ``Kokkos`` を使用するには、`OVERRIDE_FIND_PACKAGE <https://cmake.org/cmake/help/latest/module/FetchContent.html#integrating-with-find-package>`_ オプションを追加します。

.. code-block:: cmake

FetchContent_Declare(
          Kokkos
          URL https://github.com/kokkos/kokkos/archive/refs/tags/4.4.01.tar.gz
          OVERRIDE_FIND_PACKAGE
      )
      # 以下は自動的に FetchContent_MakeAvailable() に転送されます
      find_package(Kokkos 4.4 CONFIG)

このオプションは、CMake に対して、取得された ``Kokkos`` を使用し、後続のすべての ``find_package(Kokkos)`` 呼び出しをバイパスするように指示します。
   これはまた、``find_package(Kokkos)`` 呼び出しのバージョン要件が無視されることを意味します。
