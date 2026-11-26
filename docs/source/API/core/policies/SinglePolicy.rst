``SinglePolicy``
================

.. _single: ../parallel-dispatch/single.html

.. |single| replace:: ``Kokkos::single``


ヘッダー ``<Kokkos_ExecPolicy.hpp>``:sup:`Kokkos 5.3 以降`\ で定義されており、これは ``<Kokkos_Core.hpp>``\ からインクルードされます。

使い方
------

.. code-block:: cpp

    Kokkos::SinglePolicy<...>()
    Kokkos::SinglePolicy<...>(exec_space)

    // CTAD Constructor
    Kokkos::SinglePolicy()

``SinglePolicy`` は、ファンクターまたはラムダを正確に1回だけ実行する実行ポリシーを定義します。
これは、1回だけ実行して出力を返す可能性があるパターン |single|_ \ とのみ併用できます。

概要
----

.. code-block:: cpp

    template <typename... Properties>
    struct Kokkos::SinglePolicy {
        using traits = Kokkos::Impl::PolicyTraits<Properties...>;
        using execution_policy = Kokkos::SinglePolicy<Properties...>;
        using execution_space  = typename traits::execution_space;

        // Inherited from PolicyTraits<Args...>
        using execution_space = PolicyTraits<Args...>::execution_space;

        // Constructors
        SinglePolicy(const SinglePolicy&) = default;

        SinglePolicy();

        SinglePolicy(const execution_space& exec_space);

        // return ExecSpace instance provided to the constructor
        inline const execution_space & space() const;
    };

パラメーター
------------

一般的なテンプレート引数
~~~~~~~~~~~~~~~~~~~~~~~~

``SinglePolicy`` の有効なテンプレート引数は `こちら <../Execution-Policies.html#common-arguments-for-all-execution-policies>`_\ で説明されています。

唯一の例外は、``LaunchBounds`` 引数が ``SinglePolicy`` と互換性がないことです。


パブリッククラスメンバー
------------------------

コンストラクター
~~~~~~~~~~~~~~~~

.. cpp:function:: SinglePolicy()

   デフォルトコンストラクター。デフォルトの実行空間を使用します。

.. cpp:function:: SinglePolicy(const ExecutionSpace& exec_space)

    ``ExecutionSpace`` インスタンスを受け取るコンストラクター。

例
--


ファンクターを引数なしで1回実行します。ファンクターは、どの `operator()` が呼び出されるかを選択するために WorkTag とともに呼び出すこともできます。

.. code-block:: cpp

    struct Functor {
      Kokkos::View<double> v;
      KOKKOS_FUNCTION void operator()() const { v() *= 3; }
      KOKKOS_FUNCTION void operator()(const TimesTwoTag) const { v() *= 2; }
    };

    Kokkos::View<double> v("v");
    Functor f{v};

    // Default execution space
    Kokkos::single("label", Kokkos::SinglePolicy(), f);

    // With an ExecutionSpace instance
    Kokkos::DefaultExecutionSpace exec_space;
    Kokkos::single("label", Kokkos::SinglePolicy(exec_space), f);

    // With both a WorkTag and an ExecutionSpace
    Kokkos::single("label",
        Kokkos::SinglePolicy<TimesTwoTag, Kokkos::DefaultExecutionSpace>(), f);