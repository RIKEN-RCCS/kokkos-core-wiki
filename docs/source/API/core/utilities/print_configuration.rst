``print_configuration``
=======================

ヘッダー ``<Kokkos_Core.hpp>`` で定義されています。

使用法
------

.. code-block:: cpp

    Kokkos::print_configuration(std::cout);
    Kokkos::print_configuration(output_stream, /*verbose=*/ true);

Kokkos の構成情報を出力ストリームに出力します。
これには、コンパイル時の構成詳細（有効なバックエンド、コンパイラ設定、
バージョン情報、ビルド構成）と、:cpp:func:`initialize` 中に決定される
実行時情報（ホスト並列バックエンドのスレッド数、あるいはデバイス
バックエンドで可視なデバイス数やデバイス ID など）の両方が含まれます。

API リファレンス
----------------

.. cpp:function:: void print_configuration(std::ostream& os, bool verbose = false)

   Kokkos の構成情報を指定された出力ストリームに出力します。

   :param os: 構成情報を書き込む出力ストリーム
   :param verbose: ``true`` の場合、追加の詳細情報を出力します


例
--

.. code-block:: cpp

   #include <Kokkos_Core.hpp>
   #include <iostream>
   
   int main(int argc, char* argv[]) {
       Kokkos::initialize(argc, argv);
       {
       
         // 基本的な構成を標準出力に出力する
         Kokkos::print_configuration(std::cout);

         // 詳細な構成をログファイルに書き込む
         std::ofstream log_file("kokkos_config.log");
         if (log_file.is_open()) {
             Kokkos::print_configuration(log_file, /*verbose=*/ true);
             log_file.close();
         }
       
       }
       Kokkos::finalize();
   }

注記
----

.. warning::
   Kokkos は出力のフォーマットについて何ら保証しません。フォーマットはリリース間で変更される可能性があります。

.. tip::
   明示的な :cpp:func:`print_configuration` 呼び出しを追加して再コンパイルすることなく、
   アプリケーションを実行する前に環境変数 ``KOKKOS_PRINT_CONFIGURATION=1`` を設定することで、
   構成を標準出力に出力できます。

関連項目
--------
.. seealso::

   :doc:`device_id`
      Kokkos が使用するデバイスの id を返します

   :doc:`num_devices`
      Kokkos が利用可能なデバイスの数を返します

   :doc:`num_threads`
      Kokkos が使用するスレッドの数を返します

   :doc:`../initialize_finalize/initialize`
     Kokkos の実行環境を初期化します