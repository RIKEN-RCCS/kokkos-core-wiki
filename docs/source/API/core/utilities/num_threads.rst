``num_threads``
===============

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

使い方
------

.. code-block:: cpp

    Kokkos::num_threads();

``DefaultHostExecutionSpace`` が使用する同時実行スレッドの数を返します。

インターフェース
----------------

.. cpp:function:: [[nodiscard]] int num_threads() noexcept

   :return: ``DefaultHostExecutionSpace`` が使用する同時実行スレッドの数。

   .. versionadded:: 4.1

例
--

.. code-block:: cpp

   #include <Kokkos_Core.hpp>
   #include <iostream>

   int main(int argc, char* argv[]) {
       Kokkos::initialize(argc, argv);
       {
         std::cout << "num_threads: " << Kokkos::num_threads() << '\n';
       }
       Kokkos::finalize();
   }

以下も参照
----------
.. seealso::

   :doc:`device_id`
      Kokkos が使用するデバイスの id を返します。

   :doc:`num_devices`
      Kokkos が利用可能なデバイス数を返します。

   :doc:`print_configuration`
      Kokkos の構成情報を出力ストリームに表示します。

   :doc:`../initialize_finalize/initialize`
     Kokkos 実行環境を初期化します。

   :doc:`../initialize_finalize/InitializationSettings`
     Kokkos 初期化の設定
