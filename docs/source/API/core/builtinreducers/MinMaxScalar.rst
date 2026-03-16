``MinMaxScalar``
================

.. role::cpp(code)
    :language: cpp

:cpp:struct:`MinMaxScalar` は、
単一の便利な単位として、最小値および最大値は、クラステンプレートです。主に、:cpp:class:`MinMax` builtin リデューサーを使って :cpp:func:`parallel_reduce` 演算の結果保持を目的として設計されています。


正しいテンプレートパラメータが使用されていることを確認するために、一般的には、リデューサーの``::value_type`` メンバー　(例えば、 ``MinMax<Scalar,Space>::value_type``　)　を使って、本タイプを取得することが推奨されています。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用例
-----

.. code-block:: cpp

   MinMax<T,S>::value_type result;
   parallel_reduce(N,Functor,MinMax<T,S>(result));
   T minValue = result.min_val;
   T maxValue = result.max_val;

インターフェイス
---------

.. cpp:struct::  template<class Scalar> MinMaxScalar

   :tparam Scalar: 還元された値のデータ型 (例えば、 ``double``、 ``int``).

   .. rubric:: データメンバー

   .. cpp:var:: Scalar min_val

      還元された最小値。

   .. cpp:var:: Scalar max_val

      還元された最大値。
