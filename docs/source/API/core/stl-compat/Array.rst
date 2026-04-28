``Array``
==============

.. role:: cpp(code)
    :language: cpp

..
  ユーザーがそのコードを含む (パブリックヘッダー) ファイル

``<Kokkos_Core.hpp>`` に含まれる、ヘッダー ``<Kokkos_Array.hpp>`` に定義。

..
  物事が行うこと、そして可能であれば、それがなぜ存在するかについての短い説明についての、高レベルの、人間の言語の概要 (2 - 3 文、最大);

説明
------------------

``Array`` は、連続した集合を所有するコンテナで、固定サイズのオブジェクト列（正確にN個の要素を持つモデル）を格納します。

* これは、 ``std::array<T, N>`` の代替として設計されています。
* このコンテナは所有コンテナです（データはコンテナ自体に埋め込まれています）。
* このコンテナは、この場合 ``N > 0`` であるため、Cスタイル配列 ``T[N]`` を唯一の非静的データメンバーとして保持する構造体と同一の意味論を持つ集合型です；そうでない場合には、それは空のコンテナです。
* Cスタイルの配列とは異なり、自動的に ``T*`` に型変換されることはありません。
* 集合型として、それは、 ``T``: ``Kokkos::Array<int, 3> a = { 1, 2, 3 };`` に変換可能な、最大で ``N`` 個の初期化子による集合初期化で初期化できます。

..
  エンティティの API。

インターフェイス
----------------

.. versionchanged:: 4.4.0

.. cpp:struct:: template <class T, size_t N> Array

  ..
    テンプレートパラメータ (該当する場合)
    特殊化専用に使用される／型推論される／および／またはユーザーに公開すべきでないテンプレートパラメータは省略します。

  .. rubric:: テンプレートパラメータ

  :tparam T: 格納されているエレメント型。
  :tparam N: 格納されているエレメント数。

  .. rubric:: パブリック型

  .. cpp:type:: value_type = T
  .. cpp:type:: pointer = T*
  .. cpp:type:: const_pointer = const T*
  .. cpp:type:: reference = T&
  .. cpp:type:: const_reference = const T&
  .. cpp:type:: size_type = size_t
  .. cpp:type:: difference_type = ptrdiff_t


  .. rubric:: パブリックメンバー関数

  .. cpp:function:: constexpr bool empty() noexcept

    :returns: ``N == 0``
    :since: ``非定数`` 5.0以降

  .. cpp:function:: static constexpr size_type size() noexcept
  .. cpp:function:: constexpr size_type max_size() const noexcept

    :returns: ``N``
    :since: ``非定数`` 5.0以降

  .. cpp:function:: constexpr reference operator[](size_t i)
  .. cpp:function:: constexpr const_reference operator[](size_t i) const

    :returns: 配列の ``i`` 番目の要素への参照。
    :since: 引数が整数型、またはスコープのない列挙型である必要はありません。 (バージョン 5.1以降)

  .. cpp:function:: constexpr pointer data() noexcept
  .. cpp:function:: constexpr const_pointer data() const noexcept

    :returns: 配列の最初の要素へのポインタ。   ``N == 0`` である場合、戻り値は、 特定されておらず、間接参照できません。
    :since: ``非定数`` 5.0以降

  .. cpp:function:: constexpr pointer begin() noexcept
  .. cpp:function:: constexpr const_pointer begin() const noexcept
  .. cpp:function:: constexpr const_pointer cbegin() const  noexcept

    :returns: ``data()``
    :since: 5.0以降

  .. cpp:function:: constexpr pointer end() noexcept
  .. cpp:function:: constexpr const_pointer end() const noexcept
  .. cpp:function:: constexpr const_pointer cend() const noexcept

    :returns: ``data() + size()``。 戻り値は、間接参照できません。  ``N == 0`` である場合、 戻り値は、 ``begin()`` に等しくなります。
    :since: 5.0以降


型推論ガイド
----------------

.. cpp:function:: template<class T, class... U> Array(T, U...) -> Array<T, 1 + sizeof...(U)>

非メンバー関数
--------------------

..
  これらは密接に関連している場合にのみ、ここに記載されるべきです。例えば、 フレンド演算子。しかしながら、
  view_alloc のようなものは、 ビューのためにはここに存在すべきではありません。

.. cpp:function:: template<class T, size_t N> constexpr bool operator==(const Array<T, N>& l, const Array<T, N>& r) noexcept

   :returns:  ``l`` および ``r`` の ∀ 要素がすべて等しい場合に限り、 ``true``

.. cpp:function:: template<class T, size_t N> constexpr bool operator!=(const Array<T, N>& l, const Array<T, N>& r) noexcept

   :returns: ``!(l == r)``

.. cpp:function:: template<class T, size_t N> constexpr kokkos_swap(Array<T, N>& l, Array<T, N>& r) noexcept(N == 0 || is_nothrow_swappable_V<T>)

   :returns: ``T`` が交換可能、または  ``N == 0`` の場合、  `l` および `r` の中のそれぞれの要素は、 ``kokkos_swap`` を通じて交換されます。

.. cpp:function:: template<class T, size_t N> constexpr Array<remove_cv_t<T>, N> to_array(T (&a)[N])
.. cpp:function:: template<class T, size_t N> constexpr Array<remove_cv_t<T>, N> to_array(T (&&a)[N])

   :returns: ``a`` からコピー/移動した要素を含む ``Array``

.. cpp:function:: template<size_t I, class T, size_t N> constexpr T& get(Array<T, N>& a) noexcept
.. cpp:function:: template<size_t I, class T, size_t N> constexpr const T& get(const Array<T, N>& a) noexcept

   :returns: （タプルプロトコル／構造化バインディングのサポート）についての ``a[I]``

.. cpp:function:: template<size_t I, class T, size_t N> constexpr T&& get(Array<T, N>&& a) noexcept
.. cpp:function:: template<size_t I, class T, size_t N> constexpr const T&& get(const Array<T, N>&& a) noexcept

   :returns: （タプルプロトコル／構造化バインディングのサポート）についての  ``std::move(a[I])``

.. cpp:function:: template<class T, size_t N> constexpr T* begin(Array<T, N>& a) noexcept
.. cpp:function:: template<class T, size_t N> constexpr const T* begin(const Array<T, N>& a) noexcept

   :returns: ``a.data()``

.. cpp:function:: template<class T, size_t N> constexpr T* end(Array<T, N>& a) noexcept
.. cpp:function:: template<class T, size_t N> constexpr const T* end(const Array<T, N>& a) noexcept

   :returns: ``a.data() + a.size()``

非推奨インターフェイス
----------------------
.. deprecated:: 4.4.00

.. cpp:struct:: template<class T = void, size_t N = KOKKOS_INVALID_INDEX, class Proxy = void> Array

* 一次テンプレートは、型 ``T`` の要素 ``N`` 個からなる完全な連続集合を保持するコンテナでした。
* 本コンテナは、移動セマンティクスをサポートしていませんでした。

.. cpp:struct:: template<class T, class Proxy> Array<T, 0, Proxy>

* 本コンテナは、空のコンテナでした。

.. cpp:struct:: template<class T> Array<T, KOKKOS_INVALID_INDEX, Array<>::contiguous>

* 本コンテナは、非所有コンテナです。
* 本コンテナのサイズは、構築時に決定されました。
* 本コンテナは、任意の ``Array<T, N , Proxy>`` から割り当てられる可能性があります。
* 代入により、このコンテナーのサイズは変更されませんでした。
* 本コンテナは、移動セマンティクスをサポートしていませんでした。

.. cpp:struct:: template<class T> Array<T, KOKKOS_INVALID_INDEX, Array<>::strided>

* 本コンテナは、非所有コンテナです。
* 本コンテナのサイズおよびストライドは、構築時に決定されました。
* 本コンテナは、任意の ``Array<T, N , Proxy>`` から割り当てられる可能性があります。
* 代入により、このコンテナーのサイズは変更されませんでした。
* 本コンテナは、移動セマンティクスをサポートしていませんでした。

.. cpp:struct:: template<> Array<void, KOKKOS_INVALID_INDEX, void>

   .. rubric:: パブリック型

   .. cpp:type:: contiguous
   .. cpp:type:: strided

* 本仕様は、埋め込みタグの種類を定義した型: ``contiguous`` および ``strided`` 。

例
________

.. code-block:: cpp

 #include "Kokkos_Core.hpp"
 #include <algorithm>
 #include <iostream>
 #include <iterator>
 #include <memory>
 #include <string>
 #include <string_view>
 #include <type_traits>
 #include <utility>

 // string_view's の constexpr 配列を作成
 constexpr auto w1n = Kokkos::to_array<std::string_view>(
     {"Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer"});
 static_assert(
     std::is_same_v<decltype(w1n), const Kokkos::Array<std::string_view, 6>>);
 static_assert(w1n.size() == 6 and w1n[5] == "Jennifer");

 extern int Main(int /* argc */, char const *const /* argv */[]);
 int Main(int /* argc */, char const *const /* argv */[]) {
   Kokkos::ScopeGuard _;

   // 構築には集合体の初期化が使用されます
   [[maybe_unused]] Kokkos::Array<int, 3> a1{
       {1, 2, 3}}; // C++11では、ダブルブレースが必要で
                   // C++14 およびそれ以降においてもまだ、認められています

   Kokkos::Array<int, 3> a2 = {1, 2, 3}; //  = の後に決して必要のないダブルブレース

   // 出力は、 3 2 1
   std::reverse_copy(std::data(a2), end(a2),
                     std::ostream_iterator<int>(std::cout, " "));
   std::cout << '\n';

   // ループの範囲指定をサポートしています
   // 出力は、 E Ǝ
   Kokkos::Array<std::string, 2> a3{"E", "\u018E"};
   for (const auto &s : a3)
     std::cout << s << ' ';
   std::cout << '\n';

   // 配列作成のための型推論ガイド
   [[maybe_unused]] Kokkos::Array a4{3.0, 1.0, 4.0}; // Kokkos::Array<double, 3>

   // 特定されていない要素のビヘイビアは、組み込み配列と同様
   [[maybe_unused]] Kokkos::Array<int, 2> a5; // init のリストはなく, a5[0] および a5[1] の
                                              // デフォルトは、初期化されています。
   [[maybe_unused]] Kokkos::Array<int, 2>
       a6{}; // init のリストで、両方の要素が、初期化された値で、
             //  a6[0] = a6[1] = 0
   [[maybe_unused]] Kokkos::Array<int, 2> a7{
       1}; // init のリストで、 非特定要素は、初期化された値で、
           //  a7[0] = 1, a7[1] = 0

   // 文字列リテラルをコピー
   auto t1 = Kokkos::to_array("foo");
   static_assert(t1.size() == 4);

   // 要素の型および長さ両方を型推論
   auto t2 = Kokkos::to_array({0, 2, 1, 3});
   static_assert(std::is_same_v<decltype(t2), Kokkos::Array<int, 4>>);

   // 特定された要素の型を使って、長さを型推論
   // 暗示的変換が発生
   auto t3 = Kokkos::to_array<long>({0, 1, 3});
   static_assert(std::is_same_v<decltype(t3), Kokkos::Array<long, 3>>);

   auto t4 = Kokkos::to_array<std::pair<int, float>>(
       {{3, 0.0f}, {4, 0.1f}, {4, 0.1e23f}});
   static_assert(t4.size() == 3);

   // コピー不可能な Kokkos::Array を作成
   auto t5 = Kokkos::to_array({std::make_unique<int>(3)});
   static_assert(t5.size() == 1);

   // エラー: 多次元配列のコピーは、サポート対象外
   // char s[2][6] = {"nice", "thing"};
   // auto t6 = Kokkos::to_array(s);

   return 0;
 }
