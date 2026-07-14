``MinMaxScalar``
================

.. role:: cpp(code)
    :language: cpp

:cpp:struct:`MinMaxScalar` は、最小値と最大値を単一の便利な単位として格納するクラステンプレートです。主に :cpp:class:`MinMax` 組み込みリデューサーを使った :cpp:func:`parallel_reduce` 演算の結果を保持するために設計されています。


正しいテンプレートパラメータが使用されていることを確認するために、一般的には、リデューサーの``::value_type`` メンバー (例えば、 ``MinMax<Scalar,Space>::value_type`` ) を使って、本タイプを取得することが推奨されています。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用方法
--------

.. code-block:: cpp

   MinMax<T,S>::value_type result;
   parallel_reduce(N,Functor,MinMax<T,S>(result));
   T minValue = result.min_val;
   T maxValue = result.max_val;

インターフェイス
----------------

.. cpp:struct::  template<class Scalar> MinMaxScalar

   :tparam Scalar: 縮約された値のデータ型 (例えば、 ``double``、 ``int``).

   .. rubric:: データメンバー

   .. cpp:var:: Scalar min_val

      縮約された最小値。

   .. cpp:var:: Scalar max_val

      縮約された最大値。
