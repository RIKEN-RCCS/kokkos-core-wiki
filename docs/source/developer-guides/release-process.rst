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