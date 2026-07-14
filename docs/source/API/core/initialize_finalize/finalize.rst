``finalize``
============

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

使用方法
--------

.. code-block:: cpp

Kokkos::finalize();

Kokkos 実行環境を終了します。
この関数は、すべての Kokkos 状態をクリーンアップし、関連するリソースを
解放します。
この関数が呼び出されると、 :cpp:func:`is_initialized` または
:cpp:func:`is_finalized` を除き、いかなる Kokkos API 関数
( :cpp:func:`initialize` さえも) を呼び出すことはできません。
ユーザーは、 ``finalize`` が呼び出される前に、すべての Kokkos オブジェクト
(例えば :cpp:class:`View`) が破壊されていることを確認する必要があります。

プログラムは、 :cpp:func:`initialize` を呼び出した後、プログラム終了前に
この関数を呼び出さなければ、不適格となります。

インターフェイス
----------------

.. cpp:function:: void finalize();

:preconditions:
     * :cpp:func:`is_initialized` が ``true`` を返す
     * :cpp:func:`is_finalized` が ``false`` を返す

例
--

.. code-block:: cpp

#include <Kokkos_Core.hpp>

int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        {  // Kokkos::finalize が呼び出される前に、 my_view のデストラクタが確実に呼び出されるようにする範囲
            Kokkos::View<double*> my_view("my_view", 10);
        }  // my_view の範囲がここで終了
        Kokkos::finalize();
    }

.. code-block:: cpp

#include <Kokkos_Core.hpp>
    #include <cstdlib>

int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        std::atexit(Kokkos::finalize); // プログラム終了時に呼び出されるように登録
        Kokkos::View<double*> my_view("my_view", 10);
    } // my_view は Kokkos::finalize の前に適切に破壊される

関連項目
--------

.. seealso::

:doc:`ScopeGuard`
    初期化と終了が正しく処理されることを保証する RAII ベースのアプローチ。
  :doc:`push_finalize_hook`
    finalize() の呼び出し時に呼び出される関数を登録します。
  :doc:`is_initialized_or_finalized`
    Kokkos 実行環境の現在の状態を照会します。
