``Kokkos::num_devices``
=======================

.. role:: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_Core.hpp>``　に定義。

.. code-block:: cpp

    [[nodiscard]] int num_devices() noexcept;  // ( 4.3以降)

ホストバックエンドのみが有効な場合は、システム上で利用可能なデバイスの数、または　``-1``を返します。

Notes注意事項
-----

``Kokkos::num_devices()`` may be used to determine the number of devices that
are available to Kokkos for execution.
It is one of the few runtime functions that may be called before
``Kokkos::initialize()`` or after ``Kokkos::finalize()``.

Example
-------

.. code-block:: cpp

   #include <Kokkos_Core.hpp>
   #include <iostream>

   int main(int argc, char* argv[]) {
     if (Kokkos::num_devices() == 0) {
       std::cerr << "no device available for execution\n";
       return 1;
     }
     Kokkos::initialize(argc, argv);
     // do stuff
     Kokkos::finalize();
     return 0;
   }


----

**See also**

.. _device_id : device_id.html

.. |device_id| replace:: ``device_id``

.. _num_threads : num_threads.html

.. |num_threads| replace:: ``num_threads``

.. _initialize: ../initialize_finalize/initialize.html

.. |initialize| replace:: ``initialize``

.. _InitializationSettings: ../initialize_finalize/InitializationSettings.html

.. |InitializationSettings| replace:: ``InitializationSettings``

|device_id|_: returns the id of the device used by Kokkos

|num_threads|_: returns the number of threads used by Kokkos

|initialize|_: initializes the Kokkos execution environment

|InitializationSettings|_: settings for initializing Kokkos
