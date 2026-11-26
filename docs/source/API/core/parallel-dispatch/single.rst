``single``
==========

.. _SinglePolicy: ../policies/SinglePolicy.html

.. |SinglePolicy| replace:: ``SinglePolicy``


ヘッダー ``<impl/Kokkos_Single.hpp>``:sup:`since Kokkos 5.3` で定義されており、``<Kokkos_Core.hpp>`` からインクルードされます

使い方
------

.. code-block:: cpp

    Kokkos::single(name, policy, functor);
    Kokkos::single(name, policy, functor, output);
    Kokkos::single(policy, functor);
    Kokkos::single(policy, functor, output);
    Kokkos::single(functor);
    Kokkos::single(name, functor);

ポリシーで定義された実行空間上で、ファンクターを正確に1回だけ実行します

インターフェース
----------------

.. code-block:: cpp

    template <class ExecPolicy, class FunctorType> 
    Kokkos::single(const std::string& name, 
                   const ExecPolicy& policy, 
                   const FunctorType& functor);

.. code-block:: cpp

    template <class ExecPolicy, class FunctorType, class ReturnType> 
    Kokkos::single(const ExecPolicy& policy, 
                   const FunctorType& functor, 
                   ReturnType& ret);

.. code-block:: cpp

    template <class ExecPolicy, class FunctorType> 
    Kokkos::single(const ExecPolicy& policy, const FunctorType& functor);

.. code-block:: cpp

    template <class FunctorType> 
    Kokkos::single(const std::string& name, const FunctorType& functor);

.. code-block:: cpp

    template <class FunctorType> 
    Kokkos::single(const FunctorType& functor);


パラメータ:
~~~~~~~~~~~

* ``name``: Kokkos Profiling Hooks を介してプロファイリングやデバッグのツールで使用される、ユーザー提供の文字列です。

* ``ExecPolicy``: 実行特性を定義します。有効なポリシーは以下の通りです:

  - :cpp:func:`SinglePolicy` は実行空間内の単一スレッドに実行を制限します。
  - :cpp:func:`PerTeam` は呼び出し元チーム内の単一のベクターレーンに実行を制限します。
  - :cpp:func:`PerThread` は呼び出し元スレッド内の単一のベクターレーンに実行を制限します。

  ``policy`` 引数が指定されない場合、``policy`` は :cpp:func:`SinglePolicy` となります

*  ``FunctorType``: 実行される操作を定義するファンクターです。ファンクターは C++ のクラス/構造体またはラムダを使用して定義できます。

* ``ret``: 出力変数への参照です。ファンクターの ``operator()`` はこの値への参照を受け取ります。

要件
~~~~
* ``policy`` は ``LaunchBounds`` 属性なしで定義する必要があります。

* ``single`` が戻り値なしで呼び出される場合、``FunctorType`` にはシグネチャ ``operator() () const`` のメンバー関数が必要です。実行ポリシーの ``work_tag`` が ``void`` でない場合は ``operator() (typename ExecPolicy::work_tag) const`` が必要です。

* ``single`` が戻り値ありで呼び出される場合、``FunctorType`` にはシグネチャ ``operator() (ReturnType&) const`` のメンバー関数が必要です。実行ポリシーの ``work_tag`` が ``void`` でない場合は ``operator() (typename ExecPolicy::work_tag, ReturnType&) const`` が必要です。

セマンティクス
--------------

* ファンクターの呼び出し演算子は、並列化なしで正確に1回呼び出されます。

* この呼び出しは非同期である可能性があります。カーネルが完了したことを保証するには、開発者はカーネルが実行される実行空間上で fence を呼び出す必要があります。

例
--

階層的並列化における ``Kokkos::single`` の使用

.. code-block:: cpp

  #include<Kokkos_Core.hpp>

  int main(int argc, char* argv[]) {
    Kokkos::ScopeGuard guard(argc,argv);

    using team_policy = Kokkos::TeamPolicy<Kokkos::DefaultExecutionSpace>;
    using team_handle = team_policy::member_type;
    Kokkos::View<int> counter("Counter");
    Kokkos::parallel_for(team_policy(100, Kokkos::AUTO()),
      KOKKOS_LAMBDA(const team_handle& team) {
        int val;
        Kokkos::single(Kokkos::PerTeam(team), [&](int& tmp) {
          tmp = Kokkos::atomic_inc(&counter());
        }, val);
        if(val >= 100) Kokkos::abort("Too many atomics");
    });

    return 0;
  }


``Kokkos::single`` を使用してファンクターを1回実行し、スカラー出力を生成する

.. warning::
   OpenACC バックエンドは現在、``single`` での値の返却をサポートしていません

.. code-block:: cpp

  #include<Kokkos_Core.hpp>

  int main(int argc, char* argv[]) {
    Kokkos::ScopeGuard guard(argc,argv);

    float value;
    Kokkos::single("label", Kokkos::SinglePolicy(),
      KOKKOS_LAMBDA(float& val) {
        val = 1.0;
    }, value);

    return 0;
  }


``Kokkos::single`` を使用して複数の出力を生成するには、カスタム戻り値型を使用する必要があります

.. warning::
   OpenACC バックエンドは現在、``single`` での値の返却をサポートしていません

.. code-block:: cpp

  #include<Kokkos_Core.hpp>

  struct CustomReturn {
    int val1;
    int val2;
  };

  int main(int argc, char* argv[]) {
    Kokkos::ScopeGuard guard(argc,argv);

    CustomReturn ret;

    Kokkos::single("label", Kokkos::SinglePolicy(),
        KOKKOS_LAMBDA(CustomReturn& r) {
          r.val1 = 1;
          r.val2 = 2;
        }, ret);

    return 0;
  }