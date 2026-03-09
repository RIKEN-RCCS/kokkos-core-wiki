..
  見出しの表記については、以下の規則を使用してください：

    # 各部に対して、オーバーラインを使用　（章の集まり）

    * 各部に対して、オーバーラインを使用

    = 節用

    - 小節用

    ^ 小々節用

    " パラグラフ用

..
  クラス / メソッド / コンテナ名)
  呼び出し可能なフリー関数について、命名規則を保持、 `view_alloc()`

``CoolerView``
==============

.. role:: cpp(code)
    :language: cpp

..
  ユーザーがそのコードに含める (パブリックヘッダー) ファイル 

ヘッダーファイル: ``Kokkos_Core.hpp``

..
  そのものが何を行うのかについて、高レベルで、人間が理解しやすい言葉で簡潔にまとめた概要、そして可能であれば、それが存在する理由についての簡潔な説明　（最高で2，3文）；

ディスクリプション
-----------

..
  エンティティの　API　。

インターフェイス
---------

..
  エンティティの宣言または署名。

.. cpp:class:: template <class DataType, class... Traits> CoolerView

  ..
    テンプレートパラメータ (該当すれば)
     特殊化/演鐸/のためにだけ使用され、 および/または ユーザーに暴露されるべきではない、テンプレートパラメータを省略してください。

  :tparam Foo: Foo テンプレートパラメータのディスクリプション

  ..
    パラメータ (該当すれば)

  :param bar: バーパラメータのディスクリプション

  .. rubric:: パブリック型:

  .. cpp:type:: data_type

    型についての何らかの興味深いディスクリプションおよびその使用方法。

  .. rubric:: 静的パブリックメンバー変数:

  .. cpp:member:: int some_var = 5;

    some_var　のディスクリプション

    ..
      関連情報を持つ場合

    .. seealso::

      ..
        We can cross-reference entities

      The :cpp:func:`frobrnicator` free function.

  .. rubric:: Constructors:

  .. cpp:function:: CoolerView(CoolerView&& rhs)

    Whether it's a move/copy/default constructor. Describe what it does.

  ..
    Only include the destructor if it does something interesting as part of the API, such as RAII classes that release a resource on their destructor. Classes that merely
    clean up or destroy their members don't need this member documented.

  .. rubric:: Destructor:

  .. cpp:function:: ~CoolerView()

    Performs some special operation when destroyed.

  .. rubric:: Public Member Functions:

  .. cpp:function:: template<class U> foo(U x)

    Brief description of the function.

    :tparam U: Description of U

    :param: description of x

    ..
      Describe any API changes between versions.

    .. versionchanged:: 3.7.1

      What changed between versions: e.g. Only takes one parameter for foo-style operations instead of two.

  ..
    Use the C++ syntax for deprecation (don't use the Kokkos deprecated macro) as Sphinx will recognize it. We may in the future
    add extra parsing after the html is generated to render this more nicely.

  .. cpp:type:: [[deprecated("in version 4.0.1")]] foobar

    Represents the foobar capability.

    .. deprecated:: 4.0.1

      Use :cpp:type:`foobat` instead.

  .. cpp:type:: foobat

    A better version of foobar.

    .. versionadded:: 4.0.1


Non-Member Functions
--------------------

..
  These should only be listed here if they are closely related. E.g. friend operators. However,
  something like view_alloc shouldn't be here for view

.. cpp:function:: template<class ViewSrc> bool operator==(CoolerView, ViewSrc);

  :tparam ViewDst: the other

  :return: true if :cpp:type:`View::value_type`, :cpp:type:`View::array_layout`, :cpp:type:`View::memory_space`, :cpp:func:`View::rank`, :cpp:func:`View::data()` and :cpp:expr:`View::extent(r)`, for :cpp:expr:`0<=r<rank`, match.

.. cpp:function:: void frobrnicator(CoolerView &v) noexcept

  :param: v the :cpp:class:`CoolerView` to frobnicate

  Frobnicates a CoolerView.

Examples
--------

..
  It may be useful to also have examples for individual functions above.

  Prefer working and compilable examples to prose descriptions (such as "Usage").

.. code-block:: cpp

  #include <Kokkos_Core.hpp>
  #include <cstdio>

  int main(int argc, char* argv[]) {
     Kokkos::initialize(argc,argv);

     int N0 = atoi(argv[1]);
     int N1 = atoi(argv[2]);

     Kokkos::View<double*> a("A",N0);
     Kokkos::View<double*> b("B",N1);

     Kokkos::parallel_for("InitA", N0, KOKKOS_LAMBDA (const int& i) {
       a(i) = i;
     });

     Kokkos::parallel_for("InitB", N1, KOKKOS_LAMBDA (const int& i) {
       b(i) = i;
     });

     Kokkos::View<double**,Kokkos::LayoutLeft> c("C",N0,N1);
     {
       Kokkos::View<const double*> const_a(a);
       Kokkos::View<const double*> const_b(b);
       Kokkos::parallel_for("SetC", Kokkos::MDRangePolicy<Kokkos::Rank<2,Kokkos::Iterate::Left>>({0,0},{N0,N1}),
         KOKKOS_LAMBDA (const int& i0, const int& i1) {
         c(i0,i1) = a(i0) * b(i1);
       });
     }

     Kokkos::finalize();
  }
