``initialize``
==============

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

使用法
------

.. code-block:: cpp

Kokkos::initialize(argc, argv);
    Kokkos::initialize(Kokkos::InitializationSettings()
                           .set_disable_warnings(true)
                           .set_num_threads(8)
                           .set_map_device_id_by("random"));
    Kokkos::initialize();

Kokkos の実行環境を初期化します。
この関数は、他の Kokkos API 関数やコンストラクタよりも先に呼び出す必要があります。
:cpp:func:`is_initialized` または :cpp:func:`is_finalized` 等の、
少数の例外もあります。
Kokkos は最大で1回のみ初期化が可能です。その後の呼び出しは誤りです。

この関数には、2つのオーバーロードがあります。
最初の関数は、プログラムが実行される環境からプログラムに渡されるコマンドライン引数に
対応する、 ``main()`` と同じ2つのパラメータを取ります。Kokkos は、
認識するフラグの引数を解析します。Kokkos フラグが検出されるたびに、
それは ``argv`` から削除され、 ``argc`` が1減算されます。
2番目の関数は、引数のプログラムによる制御を可能にする
:cpp:class:`InitializationSettings` クラスオブジェクトを取ります。

インターフェイス
----------------

.. cpp:function:: void initialize(int& argc, char* argv[]);
.. cpp:function:: void initialize(const InitializationSettings& settings = {});

:param argc: 非負の値で、プログラムに渡されたコマンドライン引数の数を表します。

:param argv: ``argc + 1`` 個のポインタの配列の最初の要素へのポインタで、
     その最後のものはヌルであり、その1つ前のものは、もし存在するのであれば、プログラムに渡された引数を表す
     ヌル終端マルチバイト文字列を指します。

:param settings: Kokkos の初期化を制御する設定を含む ``class`` オブジェクト。

:preconditions:
     * :cpp:func:`is_initialized` が ``false`` を返す
     * :cpp:func:`is_finalized` が ``false`` を返す

注意
----
.. important::

Kokkos が MPI コンテクスト内で初期化される際、 ``Kokkos::initialize`` は一般的に
   ``MPI_Init`` の後に呼び出される必要があります。

例
--

例
~~

.. code-block:: cpp

#include <Kokkos_Core.hpp>

int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        {  // Kokkos::finalize が呼び出される前に、my_view のデストラクタが確実に呼び出されるようにする範囲
            Kokkos::View<double*> my_view("my_view", 10);
        }  //  my_view の範囲は、ここで終了
        Kokkos::finalize();
    }

.. seealso::

:doc:`finalize`
    Kokkos の実行環境を終了します。
  :doc:`ScopeGuard`
    初期化と終了処理が正しく扱われることを保証する RAII ベースのアプローチ。
  :doc:`is_initialized_or_finalized`
    Kokkos の実行環境の現在の状態を照会します。
