``atomic_assign``
=================

.. 警告::
   Kokkos 4.5より、非推奨なので、 代わりに、
   :cpp:func:`atomic_store` をご使用ください。

.. ロール:: cpp(code)
    :language: cpp

 ``<Kokkos_Core.hpp>`` に含まれるヘッダー ``<Kokkos_Atomic.hpp>`` に定義。

使用例
-----

.. code-block:: cpp

    atomic_assign(&obj, desired);

原子レベルで、``obj`` の現在の値を ``desired`` に置換します。

ディスクリプション
-----------

.. cpp:function:: template<class T> void atomic_assign(T* ptr, std::type_identity_t<T> val);

    ``val`` を ``*ptr`` に原子レベルで書き込みます。

   ``{ *ptr = val; }``

   :param ptr: 値が置換対象となるオブジェクトのアドレス
   :param val: 参照されたオブジェクトに格納する値
   :戻り値: (無し)

   .. 非推奨:: 4.5において
     代わりに :cpp:func:`atomic_store` を使用します。
