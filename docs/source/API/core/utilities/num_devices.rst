``num_devices``
===============

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

使い方
------

.. code-block:: cpp

    Kokkos::num_devices();

システム上で利用可能なデバイスの数を返します。ホストバックエンドのみが有効な場合は ``-1`` を返します。

インターフェース
----------------

.. cpp:function:: [[nodiscard]] int num_devices() noexcept

   :return: Kokkosが利用可能なデバイスの数。ホストバックエンドのみが有効な場合は ``-1`` 。

   .. versionadded:: 4.3

例
--

.. code-block:: cpp

   #include <Kokkos_Core.hpp>
   #include <iostream>

   int main(int argc, char* argv[]) {
     if (Kokkos::num_devices() == 0) {
       std::cerr << "no device available for execution\n";
       return 1;
     }
     Kokkos::initialize(argc, argv);
     // 何かを実行
     Kokkos::finalize();
     return 0;
   }

注意事項
--------

.. note::
   :cpp:func:`num_devices` は、 :cpp:func:`initialize` の前または :cpp:func:`finalize` の後に
   呼び出される可能性のある数少ないランタイム関数の1つです。

以下も参照
----------
.. seealso::

   :doc:`device_id`
      Kokkosが使用するデバイスのidを返します

   :doc:`num_threads`
      Kokkosが使用するスレッドの数を返します

   :doc:`print_configuration`
      Kokkosの構成情報を出力ストリームに出力します

   :doc:`../initialize_finalize/initialize`
     Kokkosの実行環境を初期化します

   :doc:`../initialize_finalize/InitializationSettings`
     Kokkosを初期化するための設定
