リリースプロセス
================

（作業中）

リリースブランチの作成とプロジェクトバージョンの更新
----------------------------------------------------
（メンテナー向け）

.. note::
   **バージョン番号付けスキーム**

   開発バージョンでは、そのシリーズ内のどのリリースよりも常に新しいものとして
   比較されるように、パッチ番号として ``.99`` を使用します（例: ``4.2.99`` >
   ``4.2.5``）。これにより、コードは開発バージョンとリリースバージョンを確実に
   区別できます。

機能リリース (X.Y.0)
~~~~~~~~~~~~~~~~~~~~

.. important::
   ステップ1〜7は、``develop`` に他の変更をマージせずに順番に完了する必要が
   あります。これにより、コードベース全体で正確なバージョン追跡が保証されます。

1. Continuous Integration Working Group とともに ``develop`` ブランチが適切な
   状態にあること、すべてのナイトリービルドが成功していること、統合テストに
   未解決の問題がないことを確認します。

2. リリース候補ブランチを作成します:

.. code-block:: console

   git checkout -b release-candidate-X.Y.0

3. ルートの ``CMakeLists.txt`` でバージョン番号を ``X.Y.0`` に更新します:

.. code-block:: cmake

   # CMakeLists.txt の以下の行を編集します:
   set(Kokkos_VERSION_MAJOR X)
   set(Kokkos_VERSION_MINOR Y)
   set(Kokkos_VERSION_PATCH 0)

次に、変更をコミットします:

.. code-block:: console

   git commit -s -m 'Set version number to X.Y.0' CMakeLists.txt

4. リリース候補ブランチをアップストリームリポジトリにプッシュします:

.. code-block:: console

   git push https://github.com/kokkos/kokkos.git release-candidate-X.Y.0

5. ``develop`` を起点として、新しい ``bump_version_number`` ブランチを作成して
   チェックアウトします:

.. code-block:: console

   git checkout -b bump_version_number develop

6. ルートの ``CMakeLists.txt`` でバージョンを ``X.(Y-1).99`` から ``X.Y.99`` に
   更新します:

.. code-block:: cmake

   # CMakeLists.txt の以下の行を編集します:
   set(Kokkos_VERSION_MAJOR X)
   set(Kokkos_VERSION_MINOR Y)
   set(Kokkos_VERSION_PATCH 99)

次に、変更をコミットします:

.. code-block:: console

   git commit -s -m 'Bump version from X.(Y-1).99 to X.Y.99' CMakeLists.txt

7. 自分のフォークにプッシュし、``develop`` ブランチに対してプルリクエストを
   開きます:

.. code-block:: console

   git push <your-fork-remote> bump_version_number

開発ブランチのバージョン整合性を維持するため、**このプルリクエストは他の
機能PRよりも先に、直ちにマージする必要があります**。

8. ``X.(Y+1)`` の changelog 用のトラッカーイシューを開き、リポジトリにピン留め
   します（GitHub の "Pin issue" 機能を使用）。古い ``X.Y`` の changelog イシューの
   ピン留めを解除します。古いイシューをテンプレートとして使用し、すべての
   セクションを保持しつつエントリをクリアします。

9. `#nucleus <https://kokkosteam.slack.com/archives/G5CBLMFLP>`_ チャンネルで
   開発者に、リリースブランチが作成されたこと、およびバージョンバンプPRを
   ``develop`` への次の変更としてマージする必要があることを通知します。

パッチリリース (X.Y.Z)
~~~~~~~~~~~~~~~~~~~~~~

パッチリリースは、既存のリリースシリーズに重大なバグ修正を組み込むために、以前のリリースタグから作成されます。

.. note::
   機能リリースとは異なり、パッチリリースでは ``develop`` ブランチのバージョンを更新する必要はありません。これは、現在の開発シリーズに対してすでに ``.99`` のパッチ番号を使用しているためです。

1. 最新のパッチリリースタグからリリース候補ブランチを作成します:

.. code-block:: console

   git checkout -b release-candidate-X.Y.(Z+1) X.Y.Z

2. ルートの ``CMakeLists.txt`` でバージョン番号を ``X.Y.Z`` から ``X.Y.(Z+1)`` に更新します:

.. code-block:: cmake

   # Edit these lines in CMakeLists.txt:
   set(Kokkos_VERSION_MAJOR X)
   set(Kokkos_VERSION_MINOR Y)
   set(Kokkos_VERSION_PATCH Z+1)

次に、変更をコミットします:

.. code-block:: console

   git commit -s -m 'Bump version from X.Y.Z to X.Y.(Z+1)' CMakeLists.txt

3. リリース候補ブランチをアップストリームリポジトリにプッシュします:

.. code-block:: console

   git push https://github.com/kokkos/kokkos.git release-candidate-X.Y.(Z+1)

4. 承認された変更のチェリーピックに進みます (次のセクションを参照)。

リリース候補への変更のチェリーピック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**一般的なワークフロー**

変更は、次のような例外的な理由がない限り、develop-first ワークフローに従う必要があります:

- develop が大幅に分岐しており、チェリーピックが実用的でない
- develop が一時的に壊れている、またはテスト不可能な状態にある
- develop での後続の修正により、バグがリリースブランチにのみ存在する
- develop に互換性のない変更が含まれており、根本的に異なる修正が必要である

1. **まず develop にマージする:** すべての変更は、バックポートの検討対象となる前に、``develop`` ブランチに統合されテストされている必要があります。

2. **承認を得る:** develop にマージされたら、バックポートする前に、メンテナーから、週次の開発者会議を通じて、または `#nucleus <https://kokkosteam.slack.com/archives/G5CBLMFLP>`_ チャンネルで承認を得てください。

3. **チェリーピック PR を開く:** リリース候補ブランチをターゲットとするプルリクエストを、以下の内容で作成します:

   - **タイトル形式:** ``[X.Y.Z] Original Well-Crafted Subject Line``
   - **説明の冒頭:** "Cherry-picking the changes from PR #1234 into the X.Y.(Z+1) release candidate branch"

.. tip::
   変更がリリースに不適切と判断された場合の不要な作業を避けるため、開発者はバックポート PR を開く**前に**承認を求めることが推奨されます (必須ではありません)。

**機能リリース候補 (X.Y.0) のスコープガイドライン**

新しい機能リリースのリリース候補フェーズでは、パッチは以下に限定されるべきです:

- テスト中に発見された**バグ修正**
- パフォーマンスに大きく影響する**重要な最適化の改善**
- ブランチ作成前に開始されていた**機能の完成**

.. warning::
   **リリース日が近づくにつれて**、パッチはますます保守的になり、以下に限定されるべきです:

   - コア機能に影響する重大なバグ
   - 以前のリリースからのリグレッション
   - サポートされているプラットフォームでのビルドシステムの失敗

**パッチリリース (X.Y.Z、Z > 0) のスコープガイドライン**

バグ修正リリースのパッチには、より厳格な要件があります:

- **バグ修正のみ** (推奨)
- **非常に安全かつ重要なパフォーマンス改善** (強力な正当化が必要)
- X.Y.0 リリースとの**完全な API 互換性を維持する必要がある**

.. important::
   パッチリリースは、すでに X.Y.0 リリースをデプロイしたユーザーに安定性を提供するために存在します。いかなる種類の破壊的変更も許容されません。

最終タスク
----------
（メンテナー向け）

**自動化されたステップ**

1. リリースにタグを付けてプッシュします:

.. code-block:: console

    git tag --sign X.Y.Z
    git push https://github.com/kokkos/kokkos.git X.Y.Z

``release`` ワークフローは、``X.Y.Z`` の Git タグに対してダウンロード可能な
ソースコードアーカイブ（``.zip`` および ``.tar.gz``）を自動的に生成し、
対応する SHA-256 チェックサムを計算し、``kokkos-X.Y.Z-SHA-256.txt`` ファイルを
作成して、リリースページにアップロードします。
また、ソース配布物とサマリーファイルへのリンクをまとめたテーブルを含む
リリースノートのドラフトを作成します。

**手動検証ステップ**

2. チェックサムを検証します:

GitHub CI Action が実行されたら、生成されたアーティファクトの整合性を
ダウンロードして検証します:

.. code-block:: console

  sha256sum -c kokkos-X.Y.Z-SHA-256.txt

3. チェックサムファイルに署名します:

.. code-block:: console

  gpg --detach-sig --armor kokkos-X.Y.Z-SHA-256.txt

**リリースの公開**

4. GitHub のリリースページに移動します
(https://github.com/kokkos/kokkos/releases/latest):

- "Edit" ボタンをクリックします
- リリース日を ``YYYY-MM-DD`` に調整します
- リリースノートに、GPG 署名鍵の情報を追加します（例:
  ``Digitally signed with [Key short ID](link-to-public-key)``）
- ``kokkos-X.Y.Z-SHA-256.txt.asc`` 署名ファイルをアップロードします
- "Update release" をクリックします

すべてが問題ないか再確認してください。おめでとうございます、リリースが
出荷されました！

.. note::
   CI/CD Action は ``X.Y.Z`` リリースを GitHub 上で "Latest" リリースとして
   公開します。これが古いバージョンのパッチリリースである場合（例: 5.0.0 が
   すでにリリースされた後に 4.7.3 をリリースする場合）、どのリリースを
   "Latest" としてマークするかを手動で変更する必要がある場合があります。
