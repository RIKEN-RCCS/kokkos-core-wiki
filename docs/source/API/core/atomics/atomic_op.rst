``atomic_[op]``
===============

.. role:: cpp(code)
    :language: cpp

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用方法
--------

.. code-block:: cpp

    atomic_[op](ptr_to_value,update_value);

``ptr_to_value`` と ``update_value`` で与えられたアドレスの ``value`` を、関連する演算に従って、アトミックに更新します。


説明
----

.. cpp:function:: template<class T> void atomic_add(T* const ptr_to_value, const T value);

    ``*ptr_to_value += value`` をアトミックに実行します。

   * ``ptr_to_value``: 更新対象の値のアドレス

   * ``value``: 追加する値。

.. cpp:function:: template<class T> void atomic_and(T* const ptr_to_value, const T value);

    ``*ptr_to_value &= value`` をアトミックに実行します。

   * ``ptr_to_value``: 更新対象の値のアドレス

   * ``value``: 元の値を組み合わせるための値。

.. cpp:function:: template<class T> void atomic_dec(T* ptr_to_value);

    ``(*ptr_to_value)--`` をアトミックに実行、または  ``atomic_fetch_sub(ptr_to_value, T(-1))`` を呼び出します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

.. cpp:function:: template<class T> void atomic_decrement(T* const ptr_to_value);

    ``(*ptr_to_value)--`` アトミックに実行、または  ``atomic_fetch_sub(ptr_to_value, T(-1))`` を呼び出します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

   .. deprecated:: 4.5
       :cpp:func:`atomic_dec` を使ってください。

.. cpp:function:: template<class T> void atomic_inc(T* ptr_to_value);

    ``(*ptr_to_value)++`` をアトミックに実行、または ``atomic_fetch_add(ptr_to_value, T(1))`` を呼び出します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

.. cpp:function:: template<class T> void atomic_increment(T* const ptr_to_value);

    ``(*ptr_to_value)++`` をアトミックに実行、または、 ``atomic_fetch_add(ptr_to_value, T(1))`` を呼び出します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

   .. deprecated:: 4.5
       :cpp:func:`atomic_dec` を使ってください。

.. cpp:function:: template<class T> void atomic_max(T* const ptr_to_value, const T value);

    ``if (value > *ptr_to_value) *ptr_to_value = value`` をアトミックに実行します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

   * ``value``: 最大値を取るべき値。

.. cpp:function:: template<class T> void atomic_min(T* const ptr_to_value, const T value);

    ``if (value < *ptr_to_value) *ptr_to_value = value`` をアトミックに実行します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

   * ``value``: 最小値を取るべき値。

.. cpp:function:: template<class T> void atomic_or(T* const ptr_to_value, const T value);

    ``*ptr_to_value |= value`` をアトミックに実行します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

   * ``value``: 元の値を組み合わせるための値。

.. cpp:function:: template<class T> void atomic_sub(T* const ptr_to_value, const T value);

    ``*ptr_to_value -= value`` をアトミックに実行します。

   * ``ptr_to_value``: 更新対象の値のアドレス。

   * ``value``: 差し引かれる値。
