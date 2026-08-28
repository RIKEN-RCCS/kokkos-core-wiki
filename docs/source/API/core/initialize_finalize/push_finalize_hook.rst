``push_finalize_hook``
======================

.. role:: cpp(code)
    :language: cpp

ヘッダー  ``<Kokkos_Core.hpp>`` に定義。

使用方法
--------

.. code-block:: cpp

    Kokkos::push_finalize_hook(func);

Kokkos 実行環境が完了した場合に、呼び出されるべき、呼び出し可能なオブジェクト ``func`` を
登録。

``push_finalize_hook()`` 経由で登録された関数は、
取得したリソースを解放し、すべてのバックエンドの最終処理を完了する前に、
:cpp:func:`finalize` に入る際、逆順（後入れ先出し）で呼び出されます。

関数が例外をスローして終了した場合、 ``std::terminate`` が呼び出されます。

インターフェイス
----------------

.. cpp:function:: void push_finalize_hook(std::function<void()> func);

   :cpp:func:`finalize` 入力の際に
   呼び出されるべき関数オブジェクト ``func`` を登録。

補足
----
.. note::

   :cpp:func:`push_finalize_hook` は、:cpp:func:`initialize` の前を含め、
   プログラムの任意の時点で呼び出すことができます。:cpp:func:`initialize`
   の前に登録されたフックは保持され、初期化後に登録されたフックと同様に
   :cpp:func:`finalize` の際に呼び出されます。フックは登録の逆順で実行されるため、
   :cpp:func:`initialize` の前に登録されたフックは\ *最後*\ に実行されるものの一つになります。

   逆に、:cpp:func:`finalize` はプログラムごとに一度しか呼び出せないため、
   :cpp:func:`finalize` の実行後に登録されたフックは決して呼び出されません。

例
--

.. code-block:: cpp

    #include <Kokkos_Core.hpp>
    #include <iostream>

    void my_hook() {
      std::cout << "Cruel world!\n";
    }

    int main(int argc, char* argv[]) {
        // Kokkos::initialize() の前にフックを登録するのは合法
        Kokkos::push_finalize_hook(my_hook);
        Kokkos::initialize(argc, argv);
        Kokkos::push_finalize_hook([]{ std::cout << "Goodbye\n"; });
        std::cout << "Calling Kokkos::finalize() ...\n";
        Kokkos::finalize();
        // 決して呼び出されない: finalize() は既に実行済みであり、一度しか呼び出せないため、
        // このフックは決して呼び出されない（そうでなければ std::terminate を呼び出すことになる）。
        Kokkos::push_finalize_hook([]{ throw 42; });
    }

出力:

.. code-block::

    Calling Kokkos::finalize() ...
    Goodbye
    Cruel world!

以下も参照
----------

.. seealso::

  :doc:`finalize`
    Kokkos 実行環境を終了する
