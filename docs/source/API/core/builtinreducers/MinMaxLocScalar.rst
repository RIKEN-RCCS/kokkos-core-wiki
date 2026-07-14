``MinMaxLocScalar``
===================

.. role:: cpp(code)
    :language: cpp

:cpp:struct:`MinMaxLocScalar` は、最小値・最大値およびそれぞれの保存先を一つの単位として格納するクラステンプレートです。 :cpp:class:`MinMaxLoc` 組み込みリデューサーを使った :cpp:func:`parallel_reduce` 演算の結果を保持するために設計されています。


正しいテンプレートパラメータが使用されていることを確認するために、一般的には、リデューサーの``::value_type`` メンバー (例えば、 ``MinMaxLoc<Scalar,Index,Space>::value_type``) を使って、本タイプを取得することが推奨されています




ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用方法
--------

.. code-block:: cpp

   MinMaxLoc<T,I,S>::value_type result;
   parallel_reduce(N,Functor,MinMaxLoc<T,I,S>(result));
   T minValue = result.min_val;
   T maxValue = result.max_val;
   I minLoc = result.min_loc;
   I maxLoc = result.max_loc;

インターフェイス
----------------

.. cpp:struct::  template<class Scalar, class Index> MinMaxLocScalar

   :tparam Scalar: 縮約された値のデータ型。
   :tparam Index: 値の保存先 （インデックス）のデータ型。

   .. rubric:: データメンバー

   .. cpp:var:: Scalar min_val

      縮約された最小値。

   .. cpp:var:: Scalar max_val

      縮約された最大値。

   .. cpp:var:: Index min_loc

      最小値の保存先（イテレーションインデックス）

   .. cpp:var:: Index max_loc

      最大値の保存先（イテレーションインデックス）
