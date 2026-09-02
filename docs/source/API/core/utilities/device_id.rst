``device_id``
=============

ヘッダー ``<Kokkos_Core.hpp>`` に定義

使い方
------

.. code-block:: cpp

    Kokkos::device_id();

``DefaultExecutionSpace`` が使用するデバイスの id を返します。ホストバックエンドのみが有効な場合は ``-1`` を返します。

インターフェース
----------------

.. cpp:function:: [[nodiscard]] int device_id() noexcept

   :return: ``DefaultExecutionSpace`` が使用するデバイスの id。ホストバックエンドのみが有効な場合は ``-1``。

   .. versionadded:: 4.1

例
--

.. code-block:: cpp

   #include <Kokkos_Core.hpp>
   #include <iostream>

   int main(int argc, char* argv[]) {
       Kokkos::initialize(argc, argv);
       {
         std::cout << "device_id: " << Kokkos::device_id() << '\n';
       }
       Kokkos::finalize();
   }

参照
----
.. seealso::

   :doc:`num_devices`
      Kokkos に利用可能なデバイスの数を返します。

   :doc:`num_threads`
      Kokkos が使用するスレッド数を返します。

   :doc:`print_configuration`
      Kokkos の構成情報を出力ストリームに出力します。

   :doc:`../initialize_finalize/initialize`
     Kokkos 実行環境を初期化します。

   :doc:`../initialize_finalize/InitializationSettings`
     Kokkos を初期化するための設定
