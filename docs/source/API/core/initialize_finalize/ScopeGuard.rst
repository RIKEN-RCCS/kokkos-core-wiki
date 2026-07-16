``ScopeGuard``
==============

.. role:: cpp(code)
   :language: cpp

ヘッダー ``<Kokkos_Core.hpp>`` に定義。

使用方法
--------

.. code-block:: cpp

    Kokkos::ScopeGuard guard(argc, argv);
    Kokkos::ScopeGuard guard(Kokkos::InitializationSettings()
                                .set_map_device_id_by("random")
                                .set_num_threads(1));
    Kokkos::ScopeGuard guard;

``ScopeGuard`` は、 `RAII <https://en.cppreference.com/w/cpp/language/raii>`_ を使用して Kokkos を初期化および最終処理するためのクラスです。
それは、コンストラクタ内で提供された引数とともに :cpp:func:`initialize` を呼び出し、デストラクタ内で :cpp:func:`finalize` を呼び出します。

インタフェース
--------------

.. cpp:class:: ScopeGuard

    そのライフタイムの開始時に :cpp:func:`initialize` を呼び出し、終了時に :cpp:func:`finalize` を呼び出すクラス。

    .. cpp:function:: template <class... Args> ScopeGuard(Args&&... args);

        :param args: :cpp:func:`initialize` に引き渡す引数。

	可能な実装:

	.. code-block:: cpp

	   template <class... Args> ScopeGuard(Args&&... args){
             initialize(std::forward<Args>(args)...);
           }

    .. cpp:function:: ~ScopeGuard();

       可能な実装:

       .. code-block:: cpp

	  ~ScopeGuard() { finalize(); }

    .. cpp:function:: ScopeGuard(ScopeGuard const&) = delete;

       コピーコンストラクタ

    .. cpp:function:: ScopeGuard(ScopeGuard&&) = delete;

       移動コンストラクタ

    .. cpp:function:: ScopeGuard& operator=(ScopeGuard const&) = delete;

       コピー代入演算子

    .. cpp:function:: ScopeGuard& operator=(ScopeGuard&&) = delete;

       移動代入演算子

注意事項
--------

.. caution::

  ``ScopeGuard`` を使用することは、 :cpp:func:`initialize` と :cpp:func:`finalize` を直接呼び出すことと相互に排他的です。
  さらに、プログラムのライフタイム中に作成できる ``ScopeGuard`` オブジェクトは1つだけであり、ほとんどの Kokkos 機能はそのオブジェクトのライフタイム中にのみ使用できます。

  .. code-block:: cpp

     Kokkos::ScopeGuard(argc, argv);  // 一時オブジェクトはただちに破棄され、
     //                ^                 それとともに Kokkos 実行環境が最終処理される
     //                名前付き変数の定義を忘れている
     Kokkos::View<int> v("v");  // エラー Kokkos は最終処理済み

.. note::

  ``ScopeGuard`` は、提供された引数を無条件に :cpp:func:`initialize` に転送します。これは、それらが同じ必須条件を持つことを意味します。バージョン 3.7 まで、 ``ScopeGuard`` は :cpp:func:`is_initialized` が ``false`` を返す場合にのみそのコンストラクタで :cpp:func:`initialize` を呼び出しており、そのコンストラクタで :cpp:func:`initialize` を呼び出した場合にのみそのデストラクタで :cpp:func:`finalize` を呼び出していました。

  古い挙動についてのサポートを停止しました。それが実際に必要であると考えれば、そう考えて構いません:

  .. code-block:: cpp

    auto guard = Kokkos::is_initialized()
                     ? std::make_optional<Kokkos::ScopeGuard>()
                     : std::nullopt;

例
--

.. code-block:: cpp

    int main(int argc, char* argv[]) {
        Kokkos::ScopeGuard guard(argc, argv);
        Kokkos::View<double*> my_view("my_view", 10);
        //  Kokkos::finalize の前に呼び出された my_view デストラクタ
        // 呼び出された ScopeGuard デストラクタが Kokkos::finalize を呼び出します

以下も参照
----------

.. seealso::

  :doc:`initialize`
    Kokkos 実行環境を開始します。
  :doc:`finalize`
    Kokkos 実行環境を終了します。
