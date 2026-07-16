``Profiling::ScopedRegion``
===========================

.. role:: cpp(code)
   :language: cpp

ヘッダー ``<Kokkos_Profiling_ScopedRegion.hpp>`` に定義

使用方法
--------

.. code-block:: cpp

   Kokkos::Profiling::ScopedRegion region("label");  // (バージョン 4.1以降)



クラス ``ScopedRegion`` は、オブジェクトが作成された際にユーザー定義のプロファイリング領域を "プッシュし"、スコープが終了する際にその領域を適切に "ポップする"、`RAIIスタイル <https://en.cppreference.com/w/cpp/language/raii>`_ のラッパーです。これは特に、重要な制御フロー（例：早期リターン）を持つコードのプロファイリングに有用です。

``ScopedRegion`` クラスのコピーは不可能です。

.. cpp:Function:: ScopedRegion(std::string const& regionName);

   提供されたラベルで、ユーザーが定義した領域を開始します。
    ``Profiling::pushRegion(regionName)`` を呼び出します。

.. cpp:Function:: ~ScopedRegion();

   領域を終了します。
    ``Profiling::popRegion()`` を呼び出します。

例
--

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



**以下も参照**

`ProfilingSection <profiling_section.html>`_: スコープベースのセクション所有権ラッパーを実装
