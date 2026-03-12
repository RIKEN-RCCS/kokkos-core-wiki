``Profiling::ScopedRegion``
===========================

.. role:: cpp(code)
   :language: cpp

Defined in header ``<Kokkos_Profiling_ScopedRegion.hpp>``

使用例
-----

.. code-block:: cpp

   Kokkos::Profiling::ScopedRegion region("label");  // (since 4.1)



クラス　``ScopedRegion`` は、RAIIです。　
オブジェクトが作成された際にユーザー定義のプロファイリング領域を　"プッシュし"、スコープが終了する際にその領域を適切に、"ポップする"　ラッパー　
<https://en.cppreference.com/w/cpp/language/raii><https://en.cppreference.com/w/cpp/language/raii>`_ です。これは特に、重要な制御フロー（例：早期リターン）を持つコードのプロファイリングに有用です。 

``ScopedRegion`` クラスのコピーは不可能です。

.. cpp:Function:: ScopedRegion(std::string const& regionName);

   提供されたラベルで、ユーザーが定義した領域を開始します。
   　``Profiling::pushRegion(regionName)``　を呼び出します。

.. cpp:Function:: ~ScopedRegion();

   領域を終了します。
   Calls ``Profiling::popRegion()``　を呼び出します。

例
-------

.. code-block:: cpp

   #include <Kokkos_Profiling_ScopedRegion.hpp>

   void do_work_v1() {
     Kokkos::Profiling::pushRegion("MyApp::do_work");
     // <code>
     if (cond) の場合{
       Kokkos::Profiling::popRegion();  // must remember to pop here as well
       返し;
     }
     // <more code>
     Kokkos::Profiling::popRegion();
   }

   void do_work_v2() {
     Kokkos::Profiling::ScopedRegion region("MyApp::do_work");
     // <code>
     if (cond) を返す場合;
     // <more code>
   }



**以下も参照**

`ProfilingSection <profiling_section.html>`_: Implements a scope-based section ownership wrapper
