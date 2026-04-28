``atomic_store``
================

.. role:: cpp(code)
    :language: cpp

``<Kokkos_Core.hpp>`` に含まれている、ヘッダー ``<Kokkos_Atomic.hpp>`` に定義されています。

使用方法
--------

.. code-block:: cpp

    atomic_store(&obj, desired);

アトミックに、 ``obj`` の現在の値を ``desired`` に置き換えます。

説明
------------------

.. cpp:function:: template<class T> void atomic_store(T* ptr, std::type_identity_t<T> val);

    アトミックに、 ``*ptr`` に ``val`` を書き込みます。

   ``{ *ptr = val; }``

   :param ptr: 置換対象のオブジェクトのアドレス。
   :param val: 参照対象オブジェクトに格納する値。
   :returns: (無し)


以下も参照
----------
* `atomic_load <atomic_load.html>`_: アトミックに、参照対象オブジェクトの値を取得
* `atomic_exchange <atomic_exchange.html>`_: アトミックに、参照対象の値を置き換え、以前保持していた値を取得
