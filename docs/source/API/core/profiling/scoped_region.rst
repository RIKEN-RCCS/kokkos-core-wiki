``Profiling::ScopedRegion``
===========================

.. role:: cpp(code)
   :language: cpp

Defined in header ``<Kokkos_Profiling_ScopedRegion.hpp>``

使用例
-----

.. code-block:: cpp

   Kokkos::Profiling::ScopedRegion region("label");  // (since 4.1)



クラス　``ScopedRegion`` は、`RAIIです。
オブジェクトが作成された際にユーザー定義のプロファイリング領域を　"プッシュし"、スコープが終了する際にその領域を適切に、"ポップする"　ラッパー
<https://en.cppreference.com/w/cpp/language/raii><https://en.cppreference.com/w/cpp/language/raii>`_ です。これは特に、重要な制御フロー（例：早期リターン）を持つコードのプロファイリングに有用です。 

``ScopedRegion`` クラスの is non-copyable.

.. cpp:Function:: ScopedRegion(std::string const& regionName);

   Starts a user-defined region with provided label.
   Calls ``Profiling::pushRegion(regionName)``

.. cpp:Function:: ~ScopedRegion();

   Ends the region.
   Calls ``Profiling::popRegion()``

Example
-------

.. code-block:: cpp

   #include <Kokkos_Profiling_ScopedRegion.hpp>

   void do_work_v1() {
     Kokkos::Profiling::pushRegion("MyApp::do_work");
     // <code>
     if (cond) {
       Kokkos::Profiling::popRegion();  // must remember to pop here as well
       return;
     }
     // <more code>
     Kokkos::Profiling::popRegion();
   }

   void do_work_v2() {
     Kokkos::Profiling::ScopedRegion region("MyApp::do_work");
     // <code>
     if (cond) return;
     // <more code>
   }



**See also**

`ProfilingSection <profiling_section.html>`_: Implements a scope-based section ownership wrapper
