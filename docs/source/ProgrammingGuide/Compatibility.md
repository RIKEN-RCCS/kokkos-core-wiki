# 後方互換性と将来の互換性

十分に賢いユーザーにとっては、、Kokkos に有効に変更を加えることは、破壊的変更となります。本文書の目的は、 何が Kokkos の支援利用に該当し、何が該当しないかについて、および Kokkos の今後の方針を明確にすることです。

改善の自由と後方互換性の間には緊張関係があります。 Kokkosチームが今後改善を進めつつ、高い後方互換性を維持し(ユーザーのフラストレーションや苦痛を回避できる)ルールセットを提示します。 ユーザーを意図的に壊すつもりはありませんが、誤った破損を最小限に抑えつつ、Kokkosチームに良い道筋を提供したいと考えています。  

別途記録がない限り、以下をお願い致します:

*  `namespace Kokkos` への追加を回避
*  `KOKKOS_` で始まるマクロの追加/削除/修正の回避
*  名前が `Kokkos_` で始まるファイルの作成/削除/改変の回避

これにより、Kokkos または ユーザーコード の 将来の変更による、意図しない破損の可能性を最小限に抑えます。 

 Kokkos Team の私的利用ために、以下を保持します:

*  `namespace Kokkos` 内の、任意のネストされた `namespace Impl`  (`Kokkos::Impl`, `Kokkos::Experimental::Impl`)
*  `KOKKOS_IMPL_` で始まる任意のマクロ

これらの情報にはKokkosの実装詳細が含まれています。名称や行動、さらには小さなポイントリリースであっても、予告なしに変更されることがあります。 それらは決して、ユーザーコード内で直接参照されるべきではありません。

## API 互換性

Kokkos のパブリックサポートインターフェースは、以下の通りです:

* トップレベル `namespace Kokkos`
*  `KOKKOS_` から始まるマクロ ( `KOKKOS_IMPL_` で始まるものを除く)

実装の詳細は変わることがありますが、Kokkos チームは、変更については、機能的な挙動の違いがないもの(バグ修正を除く)に制限するか、必要に応じてコンパイル時(推奨)や実行時警告、可能な場合は、適切な非推奨期間を設けての変更となるよう、最善を尽くしています。

 Kokkos の実験的なサポートインターフェースは、以下の中にあります

* `namespace Kokkos::Experimental` 

本名前空間には、まだ本格的に使える準備ができていない、実験的な機能が収められています。 機能が不完全で、リリース間でインターフェースが変わることもあります。 最終的には、それらを最上位のネームスペース Kokkos に移すことを目的としています (適切な非推奨期間があり、両方が名前空間 Kokkos および namespace Kokkos::Experimentalに属しています。)。もし機能 (例えば新しいバックエンド) が必要なら、Kokkos の新しいマイナーリリースでコードを変更する必要があることを承知しながら使うかもしれません (最終的には、 Kokkos のトップレベル名前空間に移行した際にコードも変更しなければならないでしょう)。

## ユーザー定義マクロと互換性

ユーザー定義マクロは、特に問題を抱え、コンパイラが語彙的に認識する内容を変え、言語のスコーピングルールを順守しないことがあります。 これらは、変数名や関数、特に Kokkos や他のライブラリで使われているプライベートなものに、干渉する可能性がありました。
衝突のリスクを最小限に抑えるために、ユーザー定義のマクロは MYPROJECT_(または同様の曖昧さ解消方法)を付け、すべて大文字で表記すべきです(これにより、マクロは通常C++の構文や意味ルールに従わないことをコードリーダーに知らせます)。


衝突のリスクを最小限に抑えるために、ユーザー定義のマクロは、MYPROJECT_ (または同様の曖昧さ解消方法)を付け、すべて大文字で表記すべきです(これにより、マクロは通常 C++ の構文や意味ルールに従わないことをコードリーダーに知らせます)。


## C++ 互換性

 Kokkosチームは、C++ サポートを最小限に抑え、最新の公開 C++ 標準(C++11 から3年ごとに公開)  より、1つ遅らせることを目指しています。 これらのリリースは一般的に重要であると見なされています。 これにより、最小限のサポートコンパイラバージョンが増加し、 Kokkos チームは 新しいライブラリや言語機能を活用でき、古いコンパイラのバグおよび制限に対する回避策も削除できます。 Kokkos はオプションで C++ 標準の後期バージョンをサポートすることもあり、ユーザーがこれらのモードでコンパイルする際に機能を提供します。

## ABI 互換性

Kokkos ユーザーが、新しいリリースまたは Kokkos の構築に対してコードを再コンパイルすることが予想されています。 本レベルでの ABI (アプリケーションバイナリインターフェース) 保証はありません。

例外として、Kokkos Tools がありますが、既にコンパイルされた古いバージョンのツールにおいて、新しい Kokkos と機能するように、細心の注意を払っています。

## 非推奨
時として、KokkosTeam が Kokkos コードベースの全体的な改善のために、削除を行う必要があります。 その際、KokkosTeam は非推奨化警告および移行/進化の道筋 (理想的には廃止版と新バージョンの両方が適切な期間共存) を通じての、改善インターフェースの改善および機能への移行に向けて、最善を尽くしています。

## ヘッダー

Kokkos_ で始まるヘッダーファイルの作成/削除/変更は避けてください。プロジェクトの他の部分についても、同じです。ビルドシステムの構成によっては、例えば、誤ったファイルが含まれてしまい、多くのデバッグ時間が無駄になる場合もあります。


以下は公開ヘッダーです:

    // Core API
    Kokkos_Core.hpp

    Kokkos_Abort.hpp                     // Kokkos 4.2以降
    Kokkos_Array.hpp
    Kokkos_Assert.hpp                    // Kokkos 4.2以降
    Kokkos_Atomic.hpp
    Kokkos_BitManipulation.hpp           // Kokkos 4.1以降
    Kokkos_Clamp.hpp                     // Kokkos 4.3以降
    Kokkos_Complex.hpp
    Kokkos_DetectionIdiom.hpp
    Kokkos_Macros.hpp
    Kokkos_MathematicalConstants.hpp
    Kokkos_MathematicalFunctions.hpp
    Kokkos_MinMax.hpp                    // Kokkos 4.3以降
    Kokkos_Pair.hpp
    Kokkos_Printf.hpp                    // Kokkos 4.2以降
    Kokkos_Profiling_ProfileSection.hpp
    Kokkos_Profiling_ScopedRegion.hpp
    Kokkos_Swap.hpp                      // since Kokkos 4.3
    Kokkos_Timer.hpp

    // Containers API
    Kokkos_Bitset.hpp
    Kokkos_DualView.hpp
    Kokkos_DynamicView.hpp
    Kokkos_DynRankView.hpp
    Kokkos_OffsetView.hpp
    Kokkos_ScatterView.hpp
    Kokkos_UnorderedMap.hpp

    // Algorithms API
    Kokkos_NestedSort.hpp
    Kokkos_Random.hpp
    Kokkos_Sort.cppm
    Kokkos_Sort.hpp
    Kokkos_StdAlgorithms.hpp


 ヘッダーが公開されていない場合は、直接 #include を行わないでください。今も効果があるわけでも、将来効果が続くことも保証されていません。これにはサブディレクトリ内のヘッダーも含まれます。

### その他の権利はKokkosチームが留保

* `namespace Kokkos` に新しい名前およびエンティティを追加することは、Kokkos には以下が含まれますが、これらに限定されません::
  * 関数 (これには新しいメンバー関数や既存関数のオーバーロードが含まれます) 
  * 列挙
  * 名前空間
  * エイリアス (`using`, `typedef`, etc.)
  * クラス (`struct`/`class`/`union`)
  * 概念
  * 変数
* 関数やテンプレートに新しいデフォルト引数を追加
* 関数のリターンタイプを互換性のある方法で変更します(例えば、任意のものにvoidを出すなど)。
* 既存のインターフェースを、型のインスタンス化や関数呼び出し専用に使う場合、後方互換性のある方法で変更を加えます。 実装の詳細 (型のプライマリネーム、関数呼び出し可能な実装の詳細) は依存できない場合があります。

### その他の将来の準備

*  `namespace Kokkos` 内の関数や変数のアドレスは避けてください
*  `using namespace` 宣言 (`using namespace Kokkos;`, `using namespace Kokkos::Experimental;`) を避けてください

