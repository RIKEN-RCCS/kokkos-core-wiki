Kokkos コーディング規約
=======================

ソースコードのフォーマット
~~~~~~~~~~~~~~~~~~~~~~~~~~

ファイルヘッダー
^^^^^^^^^^^^^^^^
すべてのソースファイルには、ライセンス識別子と著作権表示を含む Kokkos の
`SPDX <https://spdx.dev>`__ ファイルヘッダーを付ける必要があります。

ヘッダーブロックはファイルの最上部に配置しなければなりません:

.. code-block:: cpp

  // SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
  // SPDX-FileCopyrightText: Copyright Contributors to the Kokkos project

  // The rest of the file content follows here.

ヘッダーガード
^^^^^^^^^^^^^^
ヘッダーファイルのガードは、すべて大文字にしたファイル名とパスを反映し、
パス区切り文字と拡張子マーカーの代わりにアンダースコアを使用する必要があります。

この規約の背景にある考え方は、Kokkos リポジトリ全体だけでなく、Kokkos
エコシステム全体、さらには Kokkos ヘッダーをインクルードするユーザー
アプリケーション内にまで及ぶグローバルな一意性を確保することです。これは
次の 2 つの主要なステップによって実現されます:

1.  プロジェクトプレフィックス: すべてのガードを ``PROJECT_NAME_`` で
    始めることで、マクロが外部ライブラリやシステムヘッダーと競合しないように
    します。
2.  パスと名前の導出: 完全なファイルパスと名前 (例:
    ``impl/Kokkos_GarbageCollector.hpp``) を大文字に変換し、パス区切り文字
    (``/``) と拡張子マーカー (``.``) をアンダースコア (``_``) に置き換えます。

例えば、``impl/Kokkos_GarbageCollector.hpp`` のガードは
``KOKKOS_IMPL_GARBAGE_COLLECTOR_HPP`` のようになります。
また、HIP バックエンド固有の実装ファイル
``HIP/Kokkos_HIP_BorrowChecker.hpp`` のガードは
``KOKKOS_HIP_BORROW_CHECKER_HPP`` になります。

コメントのフォーマット
^^^^^^^^^^^^^^^^^^^^^^
一般的には、C++ スタイルのコメント (通常のコメントには ``//``、doxygen
ドキュメントコメントには ``///``) を優先してください。

----

これらの規約への準拠を確実にし、CI のノイズを減らすために、Kokkos は
`pre-commit <https://pre-commit.com>`__ を利用してリンティングとフォーマットを
自動化しています。このツールは、ステージングされた変更に対して一連の
「フック」を実行し、C++ (``clang-format``)、CMake (``cmake-format``)、および
メタデータに関する規約を満たしていることを確認します。

環境のセットアップ
^^^^^^^^^^^^^^^^^^
システムレベルのパッケージとの競合を避けるため、Python 仮想環境内に
``pre-commit`` をインストールすることをお勧めします:

.. code-block:: bash

   # Create and activate a virtual environment
   python3 -m venv .kokkos-venv
   source .kokkos-venv/bin/activate

   # Install pre-commit
   pip install pre-commit

インストールと自動実行 (オプション)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``git commit`` を実行するたびにこれらのチェックを自動的に実行するには、git
フックスクリプトをインストールします:

.. code-block:: bash

   pre-commit install

インストールされると、フックが問題を検出した場合、自動的に修正を適用して
コミットを「失敗」させます。その後、修正されたファイルを再ステージングして
再度コミットできます。

手動実行と対象を絞ったチェック
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``pre-commit`` を初めて実行すると、フォーマットツールの環境をダウンロードして
ビルドします。この初回のセットアップには数分かかることがありますが、以降の
実行はキャッシュされて高速になります。

スイート全体を待たずに特定のツールを直接実行したい場合は、フック ID を指定して
呼び出すことができます:

* **ステージングされた変更に対してすべてのチェックを実行:**
  ``pre-commit run``
* **Clang-format のみ実行 (C++ ファイル):**
  ``pre-commit run clang-format``
* **CMake-format のみ実行:**
  ``pre-commit run cmake-format``
* **リポジトリ内のすべてのファイルに対して特定のチェックを実行:**
  ``pre-commit run clang-format --all-files``

これらのフックをローカルで活用することで、コントリビューションが CI に到達する
前にクリーンな状態になり、レビュアーがフォーマットの細かい点ではなく技術的な
ロジックに集中できるようになります。

.. note::
   ``git commit --no-verify`` を使用してフックをバイパスすることもできますが、
   これは推奨されません。CI は引き続きこれらのチェックを強制し、規約を
   満たしていない場合はビルドを失敗させます。

スタイルに関する問題
~~~~~~~~~~~~~~~~~~~~

クラス定義内で関数を定義する際に ``inline`` を使用しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C++ では、クラス本体内で定義されたメンバー関数は暗黙的に inline として
扱われます。``inline`` キーワードを追加したり ``KOKKOS_INLINE_FUNCTION`` を
使用したりすると、コンパイラの動作を変えることなく、不要な構文上のノイズが
追加されるだけです。

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

指定子と修飾子の配置に一貫性を持たせる
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``const West`` スタイル（指定子/修飾子を左側に置く）と ``East const`` スタイル（指定子/修飾子を右側に置く）のどちらも許容されます。どちらか一方を強制することはありません。同じコードブロック内で2つのスタイルを混在させないことのみをお願いしています。

1つだけ例外があります。``constexpr West`` は常に使用していただくようお願いします。

さらに、複数の修飾子が存在する場合、それらは同じ側に配置する必要があります。それらを分割しないでください（例: ``const int volatile``）。

悪い例:

.. code-block:: cpp

    // Mixing left and right alignment in the same block
    const int i  = 42;
    auto const f = 3.14f;

    // constexpr on the right
    int constexpr c = 3;

    // Qualifiers split on both sides
    const int volatile d = 4;

良い例:

.. code-block:: cpp

    // Consistent left alignment within the block
    const int i  = 42;
    const auto f = 3.14f;

    // Or consistent right alignment within the block
    int const i  = 42;
    auto const f = 3.14f;

    // constexpr always on the left
    constexpr int c = 3;

    // Qualifiers grouped on the same side
    const volatile int d = 4;
    // or
    int const volatile d = 4;

    // A const pointer to a const, using either style
    const int* const p   = &i;
    float const* const q = &f;

シンボル命名スタイルの規約
^^^^^^^^^^^^^^^^^^^^^^^^^^
以下の規約は、Kokkos Core で最も一般的に使用されているパターンに基づいています。
これらはガイドラインであり、常に一貫して守られてきたわけではありません。

* **クラスとコンセプト**: ``UpperCamelCase`` を使用します（例: ``View``、
  ``Device``、``ExecutionSpace``、``GraphNodeImpl``）。
* **テンプレートパラメータ**: 型パラメータには意味のある ``UpperCamelCase``
  の名前を使用します（例: ``ExecutionSpace``、``MemorySpace``、``DataType``、
  ``FunctorType``）。可変長パックは通常、``Properties`` や ``Args`` のような
  説明的な複数形の名前を使用します。短い名前（``T``、``P`` など）は主に
  ローカルまたは内部のコンテキストで使用されます。
* **マクロ**: アンダースコアを伴うすべて大文字で、``KOKKOS_`` プレフィックスを
  使用します。内部専用のマクロには ``KOKKOS_IMPL_`` を使用します。
* **関数（メンバ関数を含む）**: ``lower_snake_case`` の名前を使用します
  （例: ``parallel_for``、``create_mirror_view_and_copy``、
  ``impl_static_fence``、``print_configuration``）。実装上の理由で
  ``private`` にできない非公開のメンバ関数には ``impl_`` プレフィックスを
  使用します。
* **クラスのデータメンバ**: ``m_`` + ``lower_snake_case`` を使用します（例:
  ``m_space_instance``、``m_thread_team_data``、``m_queue``）。
* **名前空間**: パブリック API には ``Kokkos`` を使用し、内部または実験的な
  シンボルのスコープには ``Kokkos::Impl`` と ``Kokkos::Experimental`` を
  使用します。
* **型エイリアスと特性エイリアス**: 有用な場合は ``_type`` サフィックスを
  伴う ``lower_snake_case`` を一般的に使用します（例: ``execution_space``、
  ``value_type``、``device_type``）。
