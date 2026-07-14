Kokkos コーディング規約
=======================

ソースコードのフォーマット
~~~~~~~~~~~~~~~~~~~~~~~~~~

ファイルヘッダー
^^^^^^^^^^^^^^^^
すべてのソースファイルには、ライセンス識別子と著作権表示を含む Kokkos の
`SPDX <https://spdx.dev>`__ ファイルヘッダーを付ける必要があります。

ヘッダーブロックはファイルの先頭に記述する必要があります。

.. code-block:: cpp

  // SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
  // SPDX-FileCopyrightText: Copyright Contributors to the Kokkos project

  // The rest of the file content follows here.


ヘッダーガード
^^^^^^^^^^^^^^
ヘッダーファイルのガードは、すべて大文字のファイル名とパスを反映し、パス区切り
文字と拡張子マーカーの代わりにアンダースコアを使用する必要があります。

この規約の背後にあるロジックは、Kokkos リポジトリ全体だけでなく、Kokkos
エコシステム全体、および Kokkos ヘッダーをインクルードするユーザーアプリケーション
内にまで及ぶグローバルな一意性を確保することです。これは、次の 2 つの重要な
ステップによって実現されます。

1.  プロジェクトプレフィックス: すべてのガードを ``PROJECT_NAME_`` で開始し、
    マクロが外部ライブラリやシステムヘッダーと競合しないようにします。
2.  パスと名前の導出: 完全なファイルパスと名前（例:
    ``impl/Kokkos_GarbageCollector.hpp``）を大文字に変換し、パス区切り文字
    (``/``) と拡張子マーカー (``.``) をアンダースコア (``_``) に置き換えます。

例えば、``impl/Kokkos_GarbageCollector.hpp`` のガードは
``KOKKOS_IMPL_GARBAGE_COLLECTOR_HPP`` のようになります。
また、HIP バックエンド固有の実装ファイル
``HIP/Kokkos_HIP_BorrowChecker.hpp`` のガードは
``KOKKOS_HIP_BORROW_CHECKER_HPP`` となります。

コメントのフォーマット
^^^^^^^^^^^^^^^^^^^^^^
一般的に、C++ スタイルのコメント（通常のコメントには ``//``、doxygen
ドキュメントコメントには ``///``）を優先してください。

----

これらの規約への準拠を確実にし、CI のノイズを減らすために、Kokkos は
`pre-commit <https://pre-commit.com>`__ を使用してリンティングとフォーマットを
自動化しています。このツールは、ステージングされた変更に対して一連の「フック」を
実行し、C++ (``clang-format``)、CMake (``cmake-format``)、およびメタデータに
関する規約を満たしていることを確認します。

環境のセットアップ
^^^^^^^^^^^^^^^^^^
システムレベルのパッケージとの競合を避けるため、``pre-commit`` は Python
仮想環境内にインストールすることを推奨します。

.. code-block:: bash

   # Create and activate a virtual environment
   python3 -m venv .kokkos-venv
   source .kokkos-venv/bin/activate

   # Install pre-commit
   pip install pre-commit

インストールと自動使用（任意）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``git commit`` を実行するたびにこれらのチェックを自動的に実行させるには、
git フックスクリプトをインストールします。

.. code-block:: bash

   pre-commit install

インストール後、フックが問題を見つけると、自動的に修正を適用してコミットを
「失敗」させます。その後、修正されたファイルを再びステージングして再度コミット
できます。

手動実行と対象を絞ったチェック
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``pre-commit`` を初めて実行すると、フォーマットツールの環境がダウンロードおよび
ビルドされます。この初期セットアップには数分かかることがありますが、以降の実行は
キャッシュされて高速です。

スイート全体を待たずに特定のツールを直接実行したい場合は、そのフック ID で
呼び出すことができます。

* **ステージングされた変更に対してすべてのチェックを実行する:**
  ``pre-commit run``
* **Clang-format のみを実行する（C++ ファイル）:**
  ``pre-commit run clang-format``
* **CMake-format のみを実行する:**
  ``pre-commit run cmake-format``
* **リポジトリ内のすべてのファイルに対して特定のチェックを実行する:**
  ``pre-commit run clang-format --all-files``

これらのフックをローカルで活用することで、あなたのコントリビューションが CI に
到達する前にクリーンな状態であることが保証され、レビュアーはフォーマットの細部
ではなく技術的なロジックに集中できます。

.. note::
   ``git commit --no-verify`` を使用してフックをバイパスすることもできますが、
   これは推奨されません。CI は引き続きこれらのチェックを強制し、規約が満たされて
   いない場合はビルドを失敗させます。

スタイルに関する問題
~~~~~~~~~~~~~~~~~~~~

クラス定義内で関数を定義する際に ``inline`` を使用しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C++ は、クラス本体内で定義されたメンバー関数を暗黙的に inline として扱います。
``inline`` キーワードを追加したり、``KOKKOS_INLINE_FUNCTION`` を使用したりすると、
コンパイラの動作を変えることなく不要な構文上のノイズが追加されます。

悪い例:

.. code-block:: cpp

    class Foo {
    public:
      // Redundant: already implicitly inline
      inline void bar() { /* ... */ }

      // Redundant: KOKKOS_INLINE_FUNCTION expands to 'inline'
      KOKKOS_INLINE_FUNCTION void baz() { /* ... */ }
    };


良い例:

.. code-block:: cpp

  class Foo {
  public:
    // Clean: standard C++ handles inlining
    void bar() { /* ... */ }

    // Correct: Provides __host__ __device__ tags; inlining is implicit
    KOKKOS_FUNCTION void baz() { /* ... */ }
  };