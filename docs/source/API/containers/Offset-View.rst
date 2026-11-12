``OffsetView``
==============

ヘッダーファイル: ``Kokkos_OffsetView.hpp``

説明
----

:cpp:class:`OffsetView` は、配列の添字が0以外から始まる場合に使用できます。
その添字は、各ディメンションについて開始インデックス（含む）から終了インデックス（含まない）までの範囲をとります。

.. warning::

  OffsetView は Experimental 名前空間にあります。

インターフェース
----------------

.. cpp:class:: template <class DataType, class... Properties> OffsetView

  :cpp:class:`OffsetView` は、ディメンションごとに任意の値から添字が始まる :cpp:class:`View` です。
  :cpp:class:`View` から派生しており、同じテンプレートパラメータを持ちます。

  .. rubric:: コンストラクタ:

  .. cpp:function:: OffsetView()

    デフォルトコンストラクタは :cpp:class:`View` のプロパティを共有します。
    さらに、begin はゼロに設定されます。

  .. cpp:function:: template <class RT, class... RP> OffsetView(const OffsetView<RT, RP...>& rhs)

    互換性のある :cpp:class:`OffsetView` を用いるコピーコンストラクタです。

    .. seealso:: :ref:`api-view-assignment`

  .. cpp:function:: template <class RT, class... RP> OffsetView(const View<RT, RP...>& aview, const begins_type& begins)

    :cpp:any:`aview` のデータを参照し、ディメンション :cpp:`r` の添字が :cpp:`[begin(r),begin(r) + extent(r))` の範囲をとる :cpp:class:`OffsetView` を構築します。

    :param aview: 参照する :cpp:class:`View`。
    :param begins: 各ディメンションの最初の添字。

  .. cpp:function:: template <class Begins, class Ends> explicit OffsetView(const std::string& name, const Begins& begins, const Ends& ends)

    ディメンション :cpp:`r` の添字が :cpp:`[begin(r),end(r))` の範囲をとる :cpp:class:`OffsetView` を構築します。

    :tparam Begins: :cpp:`std::initializer_list<int64_t>`、:cpp:`Kokkos::Array`、:cpp:`std::array`、または静的エクステントを持つ :cpp:`std::span`。
    :tparam Ends: :cpp:`std::initializer_list<int64_t>`、:cpp:`Kokkos::Array`、:cpp:`std::array`、または静的エクステントを持つ :cpp:`std::span`。

    :param name: :cpp:class:`View` と同じです。
    :param begins: 各ディメンションの最初の添字（含む）。
    :param ends: 各ディメンションの終了添字（含まない）。

    .. rubric:: 要件:

    - :cpp:expr:`begins.size() == rank()` および :cpp:expr:`ends.size() == rank()`。:cpp:`std::initializer_list` の場合は実行時にチェックされます。
    - すべての :cpp:`0 <= r < rank()` について :cpp:expr:`begins[r] <= ends[r]`。これは実行時にチェックされます。

  .. cpp:function:: template <class Begins, class Ends> explicit OffsetView(const ALLOC_PROP& prop, const Begins& begins, const Ends& ends)

    割り当てプロパティ（:cpp:func:`view_alloc` の呼び出しによって作成される）を伴う割り当てコンストラクタです。

    :tparam Begins: :cpp:`std::initializer_list<int64_t>`、:cpp:`Kokkos::Array`、:cpp:`std::array`、または静的エクステントを持つ :cpp:`std::span`。
    :tparam Ends: :cpp:`std::initializer_list<int64_t>`、:cpp:`Kokkos::Array`、:cpp:`std::array`、または静的エクステントを持つ :cpp:`std::span`。

    :param prop: :cpp:class:`View` と同じです。
    :param begins: 各ディメンションの最初の添字（含む）。
    :param ends: 各ディメンションの終了添字（含まない）。

  .. cpp:function:: template <class Begins, class Ends> OffsetView(const pointer_type& ptr, const Begins& begins, const Ends& ends)

    非管理データをラップするコンストラクタです。
    ディメンション :cpp:`r` の添字は :cpp:`[begin(r),end(r))` の範囲をとります。

    :tparam Begins: :cpp:`std::initializer_list<int64_t>`、:cpp:`Kokkos::Array`、:cpp:`std::array`、または静的エクステントを持つ :cpp:`std::span`。
    :tparam Ends: :cpp:`std::initializer_list<int64_t>`、:cpp:`Kokkos::Array`、:cpp:`std::array`、または静的エクステントを持つ :cpp:`std::span`。

    :param ptr: ユーザが提供するメモリ割り当てへのポインタ。
    :param begins: 各ディメンションの最初の添字（含む）。
    :param ends: 各ディメンションの終了添字（含まない）。

    .. rubric:: 要件:

    - :cpp:expr:`begins.size() == rank()` および :cpp:expr:`ends.size() == rank()`。:cpp:`std::initializer_list` の場合は実行時にチェックされます。
    - すべての :cpp:`0 <= r < rank()` について :cpp:expr:`begins[r] <= ends[r]`。これは実行時にチェックされます。

  .. rubric:: パブリックメンバ関数:

  .. cpp:function:: template <class... OtherIndexTypes> constexpr reference_type operator()(OtherIndexTypes... indices) const

    :tparam OtherIndexTypes: :cpp:type:`index_type` に変換可能な型。

    :param indices: 参照を取得する要素の添字。各ディメンションの :cpp:func:`begin` から始まります。
    :return: 指定された添字の要素への参照。

  .. cpp:function:: template <class iType> int64_t begin(const iType dim) const

    :tparam iType: 整数型。

    :param dim: 最初の添字を取得するディメンション。
    :return: ディメンション :cpp:any:`dim` の最初の添字。

  .. cpp:function:: template <class iType> int64_t end(const iType dim) const

    :tparam iType: 整数型。

    :param dim: 終了添字を取得するディメンション。
    :return: :cpp:expr:`begin(dim) + extent(dim)`。すなわち、ディメンション :cpp:any:`dim` の最後の添字より1大きい値。

  .. cpp:function:: view_type view() const

    :return: 対応する :cpp:class:`OffsetView` のプロパティを持つ :cpp:class:`View`。

非メンバ関数
------------

.. cpp:function:: template <class LT, class... LP, class RT, class... RP> bool operator==(const OffsetView<LT, LP...>& lhs, const OffsetView<RT, RP...>& rhs)

  :return: :cpp:`lhs.view() == rhs.view()` かつ :cpp:`lhs.begins() == rhs.begins()` の場合は :cpp:`true`。

.. cpp:function:: template <class LT, class... LP, class RT, class... RP> bool operator!=(const OffsetView<LT, LP...>& lhs, const OffsetView<RT, RP...>& rhs)

  :return: :cpp:expr:`!(lhs == rhs)`

.. cpp:function:: template <class D, class... P, class... Args> auto subview(const OffsetView<D, P...>& src, Args... args)

  :cpp:any:`src` のデータの部分集合を参照する :cpp:class:`OffsetView` を作成します。

  :param src: サブビューを取得する :cpp:class:`OffsetView`。
  :param args: :cpp:any:`src` のディメンションごとに1つのスライス。:cpp:any:`src` の添字で指定します。
    整数の添字、:cpp:`Kokkos::ALL()`、または整数型 :cpp:`T` を用いた :cpp:`Kokkos::pair<T, T>` もしくは :cpp:`std::pair<T, T>` を受け付けます。
  :return: :cpp:class:`OffsetView`。:cpp:`Kokkos::ALL()` でスライスされたディメンションは開始添字を保持し、それ以外のすべてのディメンションの添字は :cpp:`0` から始まります。

  .. seealso:: :doc:`../core/view/subview`

例
--

.. code-block:: cpp

  #include <iostream>
  #include <Kokkos_Core.hpp>
  #include <Kokkos_OffsetView.hpp>

  int main(int argc, char* argv[]) {
    Kokkos::initialize(argc, argv);
    {
      std::cout << std::boolalpha;
      using Kokkos::Experimental::OffsetView;
      OffsetView<int64_t*> ov("ov", {-2}, {3});
      Kokkos::View<int64_t*> v = ov.view();

      Kokkos::parallel_for(
          "WriteIndices", Kokkos::RangePolicy(ov.begin(0), ov.end(0)),
          KOKKOS_LAMBDA(const int64_t i) { ov(i) = i; });

      auto ov_h = Kokkos::create_mirror_view_and_copy(Kokkos::HostSpace(), ov);
      auto v_h  = Kokkos::create_mirror_view_and_copy(Kokkos::HostSpace(), v);
      std::cout << "ov_h(-1) == v_h(1): " << (ov_h(-1) == v_h(1)) << '\n';
      std::cout << "ov_h(-1): " << ov_h(-1) << '\n';
      std::cout << "v_h(1): " << v_h(1) << '\n';
      std::cout << '\n';

      // 部分範囲の開始添字はゼロに設定される
      auto sub   = Kokkos::subview(ov, Kokkos::pair<int64_t, int64_t>{-1, 2});
      auto sub_h = Kokkos::create_mirror_view_and_copy(Kokkos::HostSpace(), sub);
      std::cout << "sub_h(0) == ov_h(-1): " << (sub_h(0) == ov_h(-1)) << '\n';
      std::cout << "sub_h(0): " << sub_h(0) << '\n';
      std::cout << "ov_h(-1): " << ov_h(-1) << '\n';
      std::cout << '\n';

      // 全範囲の開始添字は保持される
      auto sub_all = Kokkos::subview(ov, Kokkos::ALL());
      auto sub_all_h =
          Kokkos::create_mirror_view_and_copy(Kokkos::HostSpace(), sub_all);
      std::cout << "sub_all_h(-2) == ov_h(-2): " << (sub_all_h(-2) == ov_h(-2))
                << '\n';
      std::cout << "sub_all_h(-2) = " << sub_all_h(-2) << '\n';
      std::cout << "ov_h(-2)      = " << ov_h(-2) << '\n';
    }
    Kokkos::finalize();
  }
