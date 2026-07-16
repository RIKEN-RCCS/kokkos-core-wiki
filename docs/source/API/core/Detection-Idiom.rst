検出イディオム
==============

.. role:: cpp(code)
    :language: cpp

.. attention::
   C++20 以前は、Detection Idiom は組み込みの typedef や C++ 式の妥当性を検出するための最良の仕組みでした。 C++20 で追加された言語機能である Concepts は、Detection Idiom よりも優れており、使いやすいため、今後は最初に検討すべきアプローチです。

検出イディオムは、SFINAE に配慮した方法で、あらゆる C++ 式が有効かどうかを認識するために使用されます。

ヘッダーファイル: ``<Kokkos_DetectionIdiom.hpp>``

Kokkos 検出イディオムは、ISO/IEC TS 19568:2017、ライブラリ基礎のための C++ 拡張のバージョン2の検出イディオムに基づいており、
そのドラフトは、`here <https://cplusplus.github.io/fundamentals-ts/v2.html#meta.detect>` に見られます。

元の C++ プロポーザルは、 `here <https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2015/n4436.pdf>` に見られます。

API
---

.. code-block:: cpp

    // VOID_T および DETECTOR は説明用であり、直接使用を目的としていません。

    // SFINAE を効果的に活用する便利なメタ関数
    template<class...>
    using VOID_T = void;

    // 典型的な Op<Args...> をサポートしない型のためのプライマリテンプレート
    template<class Default, class /* AlwaysVoid */, template<class...> class /* Op */, class... /* Args */>
    struct DETECTOR {
        using value_t = std::false_type;
        using type    = Default;
    };

    // 原型の Op<Args...> をサポートする型向けの特殊化
    template<class Default, template<class...> class Op, class... Args>
    struct DETECTOR<Default, VOID_T<Op<Args...>>, Op, Args...> {
        using value_t = std::true_type;
        using type    = Op<Args...>;
    };

.. code-block:: cpp

    namespace Kokkos {

    // 提供されたアーキタイプをサポートしない型について、detected_t が返す型の簡略化。
    struct nonesuch {
        nonesuch(nonesuch&&) = delete;
        ~nonesuch() = delete;
    };

    // is_detected は、Op<Args...> が有効な型である場合に std::true_type の別名です。
    // そうでない場合には、std::false_type についての別名です。

    template <template <class...> class Op, class... Args>
    using is_detected =
        typename DETECTOR<nonesuch, void, Op, Args...>::value_t;

    // detected_t は、Op<Args...> が有効な型である場合に Op<Args...> の別名です。
    //  そうでない場合、 Kokkos::nonesuch の別名です。

    template <template <class...> class Op, class... Args>
    using detected_t = typename DETECTOR<nonesuch, void, Op, Args...>::type;

    // detected_or_t は、Op<Args...> が有効な型である場合に  Op<Args...> の別名です。
    //  そうでない場合、 Default の別名です。

    template <class Default, template <class...> class Op, class... Args>
    using detected_or_t = typename DETECTOR<Default, void, Op, Args...>::type;

    // is_detected_exact は、Op<Args...> が、 Expected と同じ型である場合に std::true_type の別名です。
    //  そうでない場合、std::false_type の別名です。

    template <class Expected, template <class...> class Op, class... Args>
    using is_detected_exact = std::is_same<Expected, detected_t<Op, Args...>>;

    // is_detected_convertible は、Op<Args...> が To へ変換可能な場合に std::true_type の別名となります。
    //  そうでない場合、std::false_type の別名です。

    template <class To, template <class...> class Op, class... Args>
    using is_detected_convertible =
        std::is_convertible<detected_t<Op, Args...>, To>;

    // C++17 またはそれ以降の便利変数

    template <template <class...> class Op, class... Args>
    inline constexpr bool is_detected_v = is_detected<Op, Args...>::value;

    template <class Expected, template <class...> class Op, class... Args>
    inline constexpr bool is_detected_exact_v =
        is_detected_exact<Expected, Op, Args...>::value;

    template <class Expected, template <class...> class Op, class... Args>
    inline constexpr bool is_detected_convertible_v =

    } // Kokkos 名前空間

例
--

Concepts による式の検出
~~~~~~~~~~~~~~~~~~~~~~~

.. _Concepts: https://eel.is/c++draft/concepts

ある型 ``T`` がコピー代入可能かどうかを検出したいと仮定します。

まず、それを検出するためのコンセプトを記述します:

.. code-block:: cpp

   template<class T>
   concept CopyAssignable = requires(T& lhs, const T& rhs) {
      lhs = rhs;
   };

次に、関数テンプレートを制約します:

.. code-block:: cpp

   template<class U>
       requires(CopyAssignable<U>)
   void DoSomething(U& u) {
    // ...
   }

別の簡潔な構文:

.. code-block:: cpp

   template<CopyAssignable U>
   void DoSomething(U& u) {
    // ...
   }

コピー代入の戻り値の型が ``T&`` であることも確認したい場合、以下を使用します:

.. code-block:: cpp

   #include <concepts>

   template<class T>
   concept CanonicalCopyAssignable = requires(T& lhs, const T& rhs) {
       { lhs = rhs } -> std::same_as<T&>;
   };

.. important::
   Kokkos と C++ 標準ライブラリの両方で、多くのコンセプトがすでに定義されています。 独自に作成するよりも、それらを使用することを推奨します。 標準化されているだけでなく、コーナーケースを網羅する点で厳密です。 標準ライブラリが提供するコンセプトは <https://eel.is/c++draft/concepts> で確認できます（ただし、このリストには C++20 以降に追加されたコンセプトが含まれている場合があります）。

標準ライブラリのコンセプト ``std::assignable_from`` で関数テンプレートを制約する:

.. code-block:: cpp

   #include <concepts>

   template<class U>
       requires std::assignable_from<U&, const U&>
   void DoSomething(U& u) {
    // ...
   }

Detection Idiom による式の検出
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ある型 ``T`` がコピー代入可能かどうかを検出する型特性を記述する必要があると仮定します。 まず、アーキタイプヘルパーエイリアスを記述します:

.. code-block:: cpp

    template<class T>
    using copy_assign_t = decltype(std::declval<T&>() = std::declval<T const&>());

次に、その特性は簡単に次のように表現できます:

.. code-block:: cpp

    template<class T>
    using is_copy_assignable = Kokkos::is_detected<copy_assign_t, T>;

コピー代入の戻り値の型が ``T&`` であることを確認したい場合、以下を使用します:

.. code-block:: cpp

    template<class T>
    using is_canonical_copy_assignable = Kokkos::is_detected_exact<T&, copy_assign_t, T>;

Concepts によるネストされた typedef の検出
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ネストされた ``MyType::difference_type`` が存在する場合にはそれを使用し、そうでない場合には ``std::ptrdiff_t`` を使用したいと仮定します:

まず、``MyType`` がネストされた ``difference_type`` を持つかどうかを検出するためのコンセプトが必要です:

.. code-block:: cpp

   template<class T>
   concept HasDifferenceType = requires {
       typename T::difference_type;
   };

次に、その型を抽出するためのヘルパー構造体を記述します:

.. code-block:: cpp

   template<class In, class U>
   struct Select {
       using type = U;
   };

   template<class In, class U>
       requires HasDifferenceType<In>
   struct Select<In, U> {
       using type = typename In::difference_type;
   };

   template<class In, class U>
   using Select_t = typename Select<In, U>::type;

その後、型を宣言することができます:

.. code-block:: cpp

   using our_difference_type = Select_t<MyType, std::ptrdiff_t>;

Detection Idiom によるネストされた typedef の検出
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ネストされた``MyType::difference_type`` が存在する場合には、それを使用したいと仮定し、そうでない場合には、 ``std::ptrdiff_t`` の使用を所望します:

まず、アーキタイプヘルパーエイリアスを記述します:

.. code-block:: cpp

    template<class T>
    using diff_t = typename T::difference_type;

その後、型を宣言することができます:

.. code-block:: cpp

    using our_difference_type = Kokkos::detected_or_t<std::ptrdiff_t, diff_t, MyType>;
