``ReducerConcept``
==================

.. ロール:: cpp(code)
    :language: cpp

リデューサーの概念とは、並列還元実行パターンにおいて、 "還元" が"どのように"実行されるかを定義する抽象化です。"何"　の抽象化はテンプレート引数として指定され、`parallel_reduce <../parallel-dispatch/parallel_reduce.html>`_ 演算において、還元対象となる　"何"　に対応します。本ページでは、仮定の　'リデューサー'　クラス定義を用いたリデューサーに求められる定義と機能について説明します。 組み込みリデューサーの簡単な説明も含まれます。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

    T result;
    parallel_reduce(N,Functor,ReducerConcept<T>(result));


シノプシス
--------

.. code-block:: cpp

    クラス リデューサー {
        パブリック:
            //概念に必要
            型定義 リデューサー リデューサー;
            型定義 ... value_type;
            型定義 Kokkos::View<value_type, ... > result_view_type;

            KOKKOS_INLINE_FUNCTION
            void join(value_type& dest, const value_type& src) const;

            KOKKOS_INLINE_FUNCTION
            value_type& reference() const;

            KOKKOS_INLINE_FUNCTION
            result_view_type view() const;

            //オプション
            KOKKOS_INLINE_FUNCTION
            void init(value_type& val) const;

            KOKKOS_INLINE_FUNCTION
            void final(value_type& val) const;

            // Kokkosの組み込みリデューサーの一部
            KOKKOS_INLINE_FUNCTION
            Reducer(value_type& value_);

            KOKKOS_INLINE_FUNCTION
            Reducer(const result_view_type& value_);
    };

パブリッククラス関数
--------------------

型定義
~~~~~~~~

* ``リデューサー``: 自己型。
* ``value_type``: 還元スカラー型。
* ``result_view_type``: 還元結果を配置すべき場所を参照する ``Kokkos::View`` 。 スカラーまたは複素データ型（クラスまたは構造体）の管理対象外ビューとして使用できます。 管理対象外ビューは、参照されるスカラー（または複素データ型）が存在する場所と同じメモリ空間を指定する必要があります。

コンストラクタ
~~~~~~~~~~~~

コンストラクタは、概念の一部ではありません。カスタムリデューサーは、複雑なカスタムコンストラクタを持つことができます。  Kokkos　における組み込みリデューサーは、以下の2つのコンストラクタを持ちます :

.. cpp:function:: KOKKOS_INLINE_FUNCTION Reducer(value_type& value_);

    * 結果の保存先としてローカル変数を参照するリデューサを構築します。

.. cpp:function:: KOKKOS_INLINE_FUNCTION Reducer(const result_view_type& value_);

    * 特定のビューを結果の保存先として参照するリデューサーを構築します。

関数
~~~~~~~~~

.. cpp:function:: KOKKOS_INLINE_FUNCTION void join(value_type& dest, const value_type& src) const;

    * Combine  into ``dest``　に ``src``　を組み合わせます。　例えば、 ``Add`` は、　``dest+=src;``　を実行します。

.. cpp:function:: KOKKOS_INLINE_FUNCTION void init(value_type& val) const;

    * 適切な初期値を使って、 ``val``　を初期化するオプションのコールバックです。　例えば、 'Add' は、　``val = 0;``を代入しますが、 Prod は、``val = 1;``　を代入します。
      デフォルトコンストラクタの呼び出しへのデフォルト。

.. cpp:function:: KOKKOS_INLINE_FUNCTION void final(value_type& val) const;

    * 結果　``val``　を修正するオプションのコールバック。 Defaults to a no-op.

.. cpp:function:: KOKKOS_INLINE_FUNCTION value_type& reference() const;

    * 参照を結果の保存先に戻します。

.. cpp:function:: KOKKOS_INLINE_FUNCTION result_view_type view() const;
Returns a view of the result place.結果の保存先のビューを返します。

要件
~~~~~~~~~~~~

リデューサーは、使用される値型、つまりにに関して可換モノイドを定義すると仮定されます。

.. code-block:: cpp

    value_type op(const value_type& val1, const value_type& val2) {
      value_type result = val1;
      reducer.join(result, val2);
      return result;
    }

上記は、可換法則および結合法則を満たし、``reducer.init(el)`` を呼び出すことにより設定可能な、単位元と可換であり、関連付けられています。

組み込みリデューサー
~~~~~~~~~~~~~~~~~

Kokkos　は、C++　の組み込み型および``Kokkos::complex``に対して自動的に動作する、複数の組み込みリデューサーを提供しております。 組み込みリデューサーをカスタム型で使用するために、   ``Kokkos::reduction_identity<CustomType>``　のテンプレート特殊化を定義する必要があります。いかに簡単な例を示し、詳細については、 `Custom Reductions <../../../ProgrammingGuide/Custom-Reductions.html>`_　において閲覧可能です。

* `Kokkos::BAnd <BAnd.html>`_
* `Kokkos::BOr <BOr.html>`_
* `Kokkos::LAnd <LAnd.html>`_
* `Kokkos::LOr <LOr.html>`_
* `Kokkos::Max <Max.html>`_
* `Kokkos::MaxLoc <MaxLoc.html>`_
* `Kokkos::Min <Min.html>`_
* `Kokkos::MinLoc <MinLoc.html>`_
* `Kokkos::MinMax <MinMax.html>`_
* `Kokkos::MinMaxLoc <MinMaxLoc.html>`_
* `Kokkos::Prod <Prod.html>`_
* `Kokkos::Sum <Sum.html>`_

例
--------

.. code-block:: cpp

    #include<Kokkos_Core.hpp>

    int main(int argc, char* argv[]) {

        long N = argc>1 ? atoi(argv[1]):100;
        long result;
        Kokkos::parallel_reduce("ReduceSum: ", N, KOKKOS_LAMBDA (const int i, long& lval) {
            lval += i;
        }, Sum<long>(result));

        printf("Result: %l Expected: %l\n",result,N*(N-1)/2);
    }
