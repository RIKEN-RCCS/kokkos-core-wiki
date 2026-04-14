``ErrorReporter``
=================

.. :: cpp(code)
    :language: cpp

ヘッダー ``<Kokkos_ErrorReporter.hpp>`` において定義。

``ErrorReporter`` は、スレッドセーフな方法でエラーレポートを収集できるクラスです。
レポートの型はユーザー定義であり、定義された容量までしかエラーを保存しません。

インターフェイス
----------------

.. cpp:class:: template<class ReportType, class DeviceType> ErrorReporter

   スレッドセーフな方法でエラーレポートを収集するクラス。

   :tparam ReportType: 報告されたエラーデータの型。 :cpp:struct:`View` について有効な要素型でなければなりません。

   :tparam DeviceType:  ``ErrorReporter`` のデバイス型。 デフォルトは、 ``DefaultExecutionSpace::device_type`` です。

   |

   .. rubric:: *Public* typedefs

   .. cpp:type:: report_type

      :cpp:any:`ReportType` これは、保存されたエラーデータの型であり、ユーザーが定義可能です。


   .. cpp:type:: device_type

      :cpp:any:`DeviceType` どの実行空間レポートを追加できるかを定義するデバイス型です。

   .. cpp:type:: execution_space

      :cpp:type:`device_type::execution_space`


   .. rubric:: *Public* constructors

   .. cpp:function:: ErrorReporter(const std::string& label, int size)

      特定の大きさおよび規模を持つ新たな ErrorReporter インスタンスを構築します。
   
   .. cpp:function:: ErrorReporter(int size)

      特定の大きさおよび規模を持つ新たな ErrorReporter インスタンスを構築します。 

   .. rubric:: メンバー関数

   .. cpp:function:: int capacity() const

      :returns: インスタンスが保存可能なエラーの最大数。
   
   .. cpp:function:: int num_reports() const

      :returns: 記録されたエラー数。

   .. cpp:function:: int num_report_attempts() const

      :returns: 2つの ``std::vector`` で、1つは報告者の ID を、もう1つは報告内容自体を格納します。 ベクトルのサイズは :cpp:any:`num_reports()` に等しいです。

   .. cpp:function:: std::pair<std::vector<int>, std::vector<report_type>> get_reports() const

      :returns: レポーターの id を含む2つの ``std::vector``  およびレポートそれ自体。 ベクトルサイズは、 :cpp:any:`num_reports()` に等しいです。

   .. cpp:function:: bool full() const

      :returns: 試行されたレポートの数が :cpp:any:`capacity()` に等しいか、それを超える場合にのみ、`` 真`` 。

   .. cpp:function:: void clear() const

      エラーリポーターをリセットします。:cpp:any:`num_reports()` は、この演算の後、0 であり、新たなエラーの記録が可能です。

   .. cpp:function:: void resize(const size_t size)

      インスタンスの容量を ``size`` に変更します。 既存のエラーレポートが失われる可能性があります。

   .. cpp:function:: bool add_report(int reporter_id, report_type report) const
      
     エラーの記録を試行します。 スペースがある場合、``report`` が保存され、試行は成功します。

      :returns: エラー記録の試行が成功した場合にのみ、`` 真`` 。


例
-------

.. code-block:: cpp
  
   #include <Kokkos_Core.hpp>
   #include <Kokkos_ErrorReporter.hpp>
   #include <Kokkos_Random.hpp>

   // ErrorReporter は、デバッグ目的で一定数のエラーを
   // 特定のポイントまで記録するために使用できます。
   // ErrorReporter の主な利点は、スレッドセーフであること、および
   // 実行環境のアーキテクチャの並行性に依存する
   // ストレージを必要としないことです。

   // この小さな例では、粒子を位置に基づいて
   // ボックスに分類することを想定しておりますが、しかし、いずれかの粒子がボックスの外にある場合、
   // それを報告します。
   int main(int argc, char* argv[]) {
     Kokkos::initialize(argc, argv);
     {
       Kokkos::View<double*> positions("Pos", 10000);
       Kokkos::View<int*> box_id("box_id");

       // -5から105の範囲でランダムな位置を生成しましょう。
       Kokkos::Random_XorShift64_Pool<> rand_pool(103201);
       Kokkos::fill_random(positions, rand_pool, -5., 105.);

       // 10件のレポートを保存できるエラーリポーターを作成します。
       // 単に位置を報告しますが
       // ユーザー定義型である可能性があります。
       Kokkos::Experimental::ErrorReporter<double> errors("MyErrors", 10);

       // 0-50 および 50-100 の範囲に該当するポジションの数を数えます。
       int num_lower_box = 0;
       int num_upper_box = 0;
       Kokkos::parallel_reduce(
           "ErrorReporter Example", positions.extent(0),
           KOKKOS_LAMBDA(int i, int& count_lower, int& count_upper) {
             double pos = positions(i);
	     // まず範囲外の位置を確認します。
	     if (pos < 0. || pos > 100.) {
               // add_report は、IDおよびペイロードを選択します。
               // いくつのレポートがすでに提出されたかを確認する必要がないことに
               // 注意してください。
               errors.add_report(i, pos);
             } else if (pos < 50.)
               count_lower++;
             else
               count_upper++;
           },
           num_lower_box, num_upper_box);

       // 結果をレポートしましょう
       printf(
           "%i パーティクルのうち、%i は、下のボックスに属し、 %i はのボックスに属します "
           "box\n",
           positions.extent_int(0), num_lower_box, num_upper_box);

       // エラーをリポートしましょう
       printf(
           "有効なドメイン (0 - 100)の外に、%i パーティクルがありました。 ここに、 "
           "最初の %i:\n があります",
           errors.num_report_attempts(), errors.num_reports());

       // レポーターIDおよびレポートを獲得するための、構築されたバインディングの使用。
       自動 [reporter_ids, reports] = errors.get_reports();
       for (int e = 0; e < errors.num_reports(); e++)
         printf("%i %lf\n", reporter_ids[e], reports[e]);
     }
     Kokkos::finalize();
   }
