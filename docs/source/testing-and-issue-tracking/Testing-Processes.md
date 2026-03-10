# Kokkos テストプロセスおよび変更プロセス

Kokkos のテストは、以下の3つのカテゴリーに属します::

 - プルリクエストテスト 
 - 夜間テスト
 - 統合テスト(リリーステスト)

## プルリクエストテスト

Kokkos のすべての変更は、Kokkos の開発 github.com ブランチに対するプルリクエストを通じて導入されます。 プルリクエストは、GitHub Actions　のワークフローや外部のテストサーバーでテストされます。

合併するには2つの条件を満たす必要があります:

1) Automatic testing of the pull request must pass.プルリクエストの自動テストは合格しなければなりません。
2) Kokkos　のコア開発者2名が、Kokkos　の開発者標準に適合しているか変更を確認した後、プルリクエストを承認しなければなりません。

プルリクエストテストでテストされた構成は主要な展開システムをカバーし、各種機関のジェンキンスやトラビスによって実行されます。

新しいテスト構成は、Kokkos　チームの開発者会議で提案されます。 新しい構成の導入は、テストリソースの可用性、テストパイプライン全体の期間、主要なコンピューティング施設のソフトウェアスタックに基づいて決定されます。
 
プルリクエストテストでは、リポジトリで指定された　clang-format　スタイルがフォーマットに合っているかの検証も含まれます。

テスト設定はkokkos/jenkins および　`kokkos/.github/workflows/*` ファイルで定義され、公式の主要なソフトウェアスタックサポートを決定します。 テスト済みのコンパイラバージョンもここに掲載しています [here](https://kokkos.github.io/kokkos-core-wiki/requirements.html)。これらのテスト構成は、(ごくわずかに)　)。ハードウェアプラットフォーム(例:　NVIDIA、Intel、および　AMD)、コンパイラ(例:　GCC、Clang、NVC++)、C++標準　(17-23)、Kokkos　のバックエンド　(例:Cuda、OpenMP、HIP)、Kokkos　の設定オプション　(例:Debug、Relocateable Device Code)などのクロス積をカバーしています。

clang　形式のファイルは、 `kokkos/.clang-format`　です。 使用する　clang　形式のバージョンは、`.clang-format`　の設定ファイルのヘッダー内のコメントとして指定されています。

プルリクエストを統合できるのは主要な　Kokkos　の管理者だけで、実施されたレビューが望ましい徹底度を満たしているかどうかを判断する責任があります。

## 夜間テスト

Nightly testing covers a wider range of compilers and configuration of Kokkos
on an extensive list of platforms.

All participating institutions are invited to perform nightly testing.
Test configurations are given in `kokkos/scripts/testings/` in institution specific test configuration files.

Each institution designates a test POC, who will report failures to the entire Kokkos team,
and file github issues with reproduction steps.

## Integration Testing (Release Testing)

In order for a new Kokkos version to be released integration testing is performed.
Integration testing configurations are determined and maintained by the customer projects.

This testing has three components:

### Internal Integration Testing

Kokkos team members will perform integration testing with a select number of customer codes, they are directly involved with.
Currently that includes two code bases:

- Trilinos
- ArborX

Trilinos in particular consists of several million lines of code over multiple packages.
Both codes are tested on the primary hardware platforms, and possibly multiple software stacks (compilers in particular).
They are also tested with a limited set of configurations during nightly testing, allowing the Kokkos team to catch issues early.

### Preferred Customer Testing

Customers funded by the same agencies as Kokkos are explicitly asked to test the release candidate before the actual release, and provide feedback.
This includes currently NNSA and Office of Science DOE users, specifically:

- SNL Empire
- SNL LAMMPS
- SNL Sparta
- SNL Sierra - Aria
- ORNL Cabana
- ANL PETSc

### General Community testing

The release candidate is publicly available as a GitHub branch, and is advertised on the Kokkos Slack channel.
Any user of Kokkos is encouraged to test the release candidate and provide feedback.
The testing phase is at least two weeks.


