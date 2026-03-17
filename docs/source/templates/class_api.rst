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
        エンティティを相互参照できます。

      The :cpp:func:`frobrnicator` free function.

  .. rubric:: Constructorsコンストラクタ:

  .. cpp:function:: CoolerView(CoolerView&& rhs)

    それが、移動/コピー/デフォルト　コンストラクタかどうか。それが何であるかを記述します。

  ..
    デストラクタでリソースを解放するRAIIクラス等、APIの一部として何か有用な処理を行う場合にのみ、デストラクタを含めてください。メンバの処理や破棄を行うだけのクラスについては、そのメンバを記録する必要はありません。

  .. rubric:: デストラクタ:

  .. cpp:function:: ~CoolerView()

    破棄された場合、何らかの特別な演算を実行します。

  .. rubric:: パブリックメンバー関数:

  .. cpp:function:: template<class U> foo(U x)

    関数の簡単なディスクリプション。

    :tparam U:  U　のディスクリプション

    :param:  x　のディスクリプション

    ..
      Describe any API changes between versions.

    .. versionchanged:: 3.7.1

      バージョン間で変更された事柄What changed between versions: 例えば、2つのパラメータの代わりに、fooスタイル演算については、1つのパラメータのみを選択します。

  ..
   非推奨の表記には、C++　の構文を使用してください（Kokkosの非推奨マクロは使用しないでください）。Sphinx　がこれを認識します。将来的には、HTML生成後に追加の解析を行い、より好ましい状態で表示する可能性があります。

  .. cpp:type:: [[deprecated("in version 4.0.1")]] foobar

    フットバー機能を表示します。

    .. 非推奨:: 4.0.1

      代わりに、 :cpp:type:`foobat` を使用します。

  .. cpp:type:: foobat

   フットバーのより好ましいバージョン

    .. versionadded:: 4.0.1


非メンバー関数
--------------------

..
  これらは、例えば、フレンド関数等、緊密に関連している場合にのみ、ここに示される必要があります。 しかしながら、view_alloc 等は、ここに、ビューを目的としてここに示すべきではありません。

.. cpp:function:: template<class ViewSrc> bool operator==(CoolerView, ViewSrc);

  :tparam ViewDst: その他

  :return:  :cpp:expr:`0<=r<rank`　について、:cpp:type:`View::value_type`, :cpp:type:`View::array_layout`, :cpp:type:`View::memory_space`, :cpp:func:`View::rank`, :cpp:func:`View::data()` and :cpp:expr:`View::extent(r)`が、　一致すれば、真

.. cpp:function:: void frobrnicator(CoolerView &v) noexcept

  :param: v the :cpp:class:　意味不明化のための`CoolerView` 

  CoolerView　を意味不明化

例
--------

..
  上記の個々の関数についても、例を挙げておくと役立つかもしれません。

  文章による説明（　"使用例"　等）よりも、実際に動作するコンパイル可能な例を優先いたします。

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
