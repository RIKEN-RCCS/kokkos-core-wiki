``LastLocScalar``
=================

.. role::cpp(code)
    :language: cpp

:cpp:struct:`LastLocScalar` は、条件を満たす最後の出現の **位置** （インデックス）を、単一の便利な単位として格納するクラステンプレートです。
:cpp:class:`LastLoc` 組み込みリデューサーを使用した :cpp:func:`parallel_reduce` 操作の結果を保持するように設計されています。

正しいテンプレートパラメータが使用されるようにするため、通常はリデューサーの
``::value_type`` メンバー（例： ``LastLoc<Index,Space>::value_type`` ）を使用して
この型を取得することが推奨されます。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使用法
------

.. code-block:: cpp

   LastLocScalar<Index>::value_type result;
   parallel_reduce(N,Functor,LastLocScalar<Index>(result));
   I lastLoc = result.max_loc_true;

インターフェース
----------------

.. cpp:struct::  template<class Index> LastLocScalar

   :tparam Index: 値の位置（インデックス）のデータ型。

   .. rubric:: データメンバー

   .. cpp:var:: Index max_loc_true

      最大値の位置（イテレーションインデックス）