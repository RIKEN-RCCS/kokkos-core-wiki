``ExecutionPolicy``
===================

.. role::cpp(code)
    :language: cpp

 ``ExecutionPolicy`` の概念は、Kokkos パラレルパターンの実行がどのように行われるかを "どのように" 表現する基本的な抽象化です。このページでは、Kokkos の実行ポリシーの共通機能の使い方について実用的に説明しています。 より正式かつ理論的な説明については、本文書 <../KokkosConcepts.html>`_ を参照してください。

    *免責事項*: C++ における "concept" という用語自体は新しいものではありません。C++でテンプレートを使ったことがある人なら、  知っているかどうかに関わらず概念を使ったことがあるでしょう。  "concept" という言葉自体に混乱しないでください。現在では、この言葉は新しい C++20 言語機能と結びつけられることが多いです。ここでの "概念" とは単に "特定の場所でテンプレートパラメータとなっている型で何が許されるか" という意味です。

``ExecutionPolicy`` とは何ですか?
----------------------------------

 Kokkos における支配的な並列ディスパッチ機構は、プログラミングガイドの他の部分で説明されているように、 ``parallel_pattern`` (例: `Kokkos::parallel_for <../parallel-dispatch/parallel_for.html>`_ または、 `Kokkos::parallel_reduce <../parallel-dispatch/parallel_reduce.html>`_ のようなもの)、 ``ExecutionPolicy``、そして ``Functor`` を含みます。  大まかに言えば:

.. code-block:: cpp
        
    parallel_pattern(
        ExecutionPolicy(),
        Functor()
    );

最も基本的な( "ビギナー" )ケースは、実はショートカットです:

.. code-block:: cpp

    Kokkos::parallel_for(
        42,
        KOKKOS_LAMBDA (int n) { /* ... */ }
    );

上記は、以下の "ショートカット" です

.. code-block:: cpp

    Kokkos::parallel_for(
        Kokkos::RangePolicy<Kokkos::DefaultExecutionSpace>(
            Kokkos::DefaultExecutionSpace(), 0, 42
        ),
        KOKKOS_LAMBDA(int n) { /* ... */ }
    );

本例においては、 ``Kokkos::RangePolicy<Kokkos::DefaultExecutionSpace>`` は、 ``ExecutionPolicy`` 型です。

機能
~~~~~~~~~~~~~

すべての ``ExecutionPolicy`` 型は、 ``index_type`` という名前のネスト型を提供します。
