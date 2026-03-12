``Profiling::ProfilingSection``
===============================

.. role:: cpp(code)
   :language: cpp

ヘッダー ``<Kokkos_Profiling_ProfileSection.hpp>``　に定義。

使用例
-----

.. code-block:: cpp

   Kokkos::Profiling::ProfilingSection section("label");
   section.start();
   // <code>
   section.stop();
    


クラス ``ProfilingSection`` は、ユーザー定義のプロファイリングセクションを管理するための便利な
`RAIIスタイル <https://en.cppreference.com/w/cpp/language/raii>`_ メカニズムを提供する、セクション　ID　ラッパーです。


　``ProfilingSection``　オブジェクトが作成されると、ユーザーが提供した文字列を用いてプロファイリングセクションが作成され、そのオブジェクトはセクションIDを保持します。

制御が　``ProfilingSection``　オブジェクトが作成されたスコープを離れた場合、``ProfilingSection``　は、破棄され、基盤となるセクションは適切に破棄されます。

 ``ProfilingSection`` クラスのコピーは不可能です。


.. cpp:Function:: ProfilingSection(std::string const& sectionName);

   ユーザーに提供されたラベルを使って、セクションを構築します。
    ``Profiling::createProfileSection(sectionName, &sectionID);``　を呼び出します。

.. cpp:Function:: ~ProfilingSection();

   セクションを削除します。
   Calls ``Profiling.destroyProfileSection(sectionID);``　を呼び出します。

.. cpp:Function:: void start();

   セクションを開始します。
   Calls ``Profiling::startSection(sectionID);``　を呼び出します。


.. cpp:Function:: void stop();

   セクションを終了します。
   Calls ``Profiling::stopSection(sectionID);``　を呼び出します。


**以下も参照**

`ScopedRegion <scoped_region.html>`_: スコープベースの領域所有権ラッパーを実装
