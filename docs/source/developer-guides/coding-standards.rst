Kokkos コーディング規約
=======================

ソースコードのフォーマット
~~~~~~~~~~~~~~~~~~~~~~~~~~

ファイルヘッダー
^^^^^^^^^^^^^^^^
すべてのソースファイルには、ライセンス識別子と著作権表示を含む Kokkos の
`SPDX <https://spdx.dev>`__ ファイルヘッダーを付ける必要があります。

ヘッダーブロックはファイルの一番先頭に配置しなければなりません:

.. code-block:: cpp

  // SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
  // SPDX-FileCopyrightText: Copyright Contributors to the Kokkos project

  // The rest of the file content follows here.


ヘッダーガード
^^^^^^^^^^^^^^
ヘッダーファイルのガードは、すべて大文字にしたファイル名とパスを反映し、
パス区切りと拡張子マーカーの代わりにアンダースコアを使用する必要があります。

この規約の背後にある論理は、Kokkos リポジトリ全体にとどまらず、Kokkos
エコシステム全体、さらには Kokkos ヘッダーをインクルードするユーザーアプリケーション
内にまで広がるグローバルな一意性を確保することです。これは 2 つの重要なステップで
達成されます:

1.  プロジェクトプレフィックス: すべてのガードを ``PROJECT_NAME_`` で始めることで、
    マクロが外部ライブラリやシステムヘッダーと衝突しないようにします。
2.  パスと名前の導出: 完全なファイルパスと名前（例:
    ``impl/Kokkos_GarbageCollector.hpp``）を大文字に変換し、パス区切り
    （``/``）と拡張子マーカー（``.``）をアンダースコア（``_``）に置き換えます。

例えば、``impl/Kokkos_GarbageCollector.hpp`` のガードは
``KOKKOS_IMPL_GARBAGE_COLLECTOR_HPP`` のようになります。
また、HIP バックエンド固有の実装ファイル
``HIP/Kokkos_HIP_BorrowChecker.hpp`` のガードは
``KOKKOS_HIP_BORROW_CHECKER_HPP`` となります。

コメントのフォーマット
^^^^^^^^^^^^^^^^^^^^^^
一般的には、C++ スタイルのコメント（通常のコメントには ``//``、doxygen
ドキュメントコメントには ``///``）を使用することを推奨します。

----

これらの標準への準拠を確実にし、CI のノイズを減らすために、Kokkos は
`pre-commit <https://pre-commit.com>`__ を利用してリンティングとフォーマットを
自動化しています。このツールは、ステージングされた変更に対して一連の「フック」を
実行し、C++（``clang-format``）、CMake（``cmake-format``）、およびメタデータの
標準を満たしていることを確認します。

環境のセットアップ
^^^^^^^^^^^^^^^^^^
システムレベルのパッケージとの衝突を避けるために、Python 仮想環境内に
``pre-commit`` をインストールすることを推奨します:

.. code-block:: bash

   # Create and activate a virtual environment
   python3 -m venv .kokkos-venv
   source .kokkos-venv/bin/activate

   # Install pre-commit
   pip install pre-commit

インストールと自動使用（オプション）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``git commit`` を実行するたびにこれらのチェックを自動的に実行させるには、
git フックスクリプトをインストールします:

.. code-block:: bash

   pre-commit install

インストールされると、フックが問題を見つけた場合、自動的に修正を適用して
コミットを「失敗」させます。その後、修正されたファイルを再ステージングして、
再度コミットできます。

手動実行と対象を絞ったチェック
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``pre-commit`` を初めて実行すると、フォーマットツールの環境をダウンロードして
ビルドします。この初回セットアップには数分かかることがありますが、以降の実行は
キャッシュされて高速になります。

スイート全体を待たずに特定のツールを直接実行したい場合は、フック ID で
呼び出すことができます:

* **ステージングされた変更に対してすべてのチェックを実行:**
  ``pre-commit run``
* **Clang-format のみを実行（C++ ファイル）:**
  ``pre-commit run clang-format``
* **CMake-format のみを実行:**
  ``pre-commit run cmake-format``
* **リポジトリ内のすべてのファイルに対して特定のチェックを実行:**
  ``pre-commit run clang-format --all-files``

これらのフックをローカルで活用することで、あなたの貢献が CI に到達する前に
クリーンであることが保証され、レビュアーはフォーマットの細かい点ではなく
技術的なロジックに集中できます。

.. note::
   ``git commit --no-verify`` を使用してフックをバイパスすることもできますが、
   これは推奨されません。CI は引き続きこれらのチェックを強制し、標準が
   満たされていない場合はビルドを失敗させます。

スタイルの問題
~~~~~~~~~~~~~~

クラス定義内で関数を定義するときに ``inline`` を使用しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C++ は、クラス本体内で定義されたメンバー関数を暗黙的に inline として扱います。
``inline`` キーワードを追加したり、``KOKKOS_INLINE_FUNCTION`` を使用したりすると、
コンパイラの動作を変えることなく不要な構文的ノイズが追加されます。

避けるべき例:

.. code-block:: cpp

    class Foo {
    public:
      // Redundant: already implicitly inline
      inline void bar() { /* ... */ }

      // Redundant: KOKKOS_INLINE_FUNCTION expands to 'inline'
      KOKKOS_INLINE_FUNCTION void baz() { /* ... */ }
    };


推奨される例:

.. code-block:: cpp

  class Foo {
  public:
    // Clean: standard C++ handles inlining
    void bar() { /* ... */ }

    // Correct: Provides __host__ __device__ tags; inlining is implicit
    KOKKOS_FUNCTION void baz() { /* ... */ }
  };