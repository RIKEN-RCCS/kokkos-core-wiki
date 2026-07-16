.. _kokkos_finalize:

``finalize``
============

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

使用方法

.. code-block:: cpp

    Kokkos::finalize();

Kokkos 実行環境を完了。
この関数は、すべての Kokkos 状態をクリーンアップし、関連するリソースを
解放します。
この関数が呼び出されると、いかなる API 関数
(`Kokkos::initialize <initialize.html>`_ さえも)、
:cpp:func:`Kokkos::is_initialized() <is_initialized()>` または
:cpp:func:`Kokkos::is_finalized() <is_finalized()>` 以外、呼び出すことはできません。
ユーザーは、 ``Kokkos::finalize`` が呼び出される前に、すべての Kokkos オブジェクト (例えば、 ``Kokkos::View``) 
破壊されていることを確認する必要があります。

プログラムは、 `Kokkos::initialize <initialize.html>`_ を呼び出した後、それらがこの関数を呼び出さなければ、不適格となります。

インターフェイス
----------------

.. code-block:: cpp

    Kokkos::finalize();

必要要件
~~~~~~~~
* ``Kokkos::finalize`` は、 Kokkos が MPI コンテクスト内で使用される場合、 ``MPI_Finalize`` の前に呼び出される必要があります。
* ``Kokkos::finalize`` は、ユーザーが初期化した Kokkos オブジェクトが、スコープ外になった後に、呼び出される必要があります。

セマンティクス
~~~~~~~~~~~~~~

* :cpp:func:`Kokkos::is_initialized() <is_initialized()>` は、 ``Kokkos::finalize`` 呼び出し後に falseを返す必要があります。

例
~~

.. code-block:: cpp

    #include <Kokkos_Core.hpp>

    int main(int argc, char* argv[]) {
        Kokkos::initialize(argc, argv);
        {  // Kokkos::finalize が呼び出される前に、 my_view のデストラクタが確実に呼び出されるようにする範囲
            Kokkos::View<double*> my_view("my_view", 10);
        }  // my_view の範囲がここで終了
        Kokkos::finalize();
    }


以下も参照
----------
* `Kokkos::initialize <initialize.html>`_: Kokkos 実行環境を初期化。
* `Kokkos::push_finalize_hook <push_finalize_hook.html>`_: ``Kokkos::finalize()`` 実行の際に呼び出される関数を登録
