``FirstLocScalar``
==================

.. role::cpp(code)
    :language: cpp

:cpp:struct:`FirstLocScalar` は、条件を満たす最初の出現の **位置** （インデックス）を単一の便利な単位として格納するクラステンプレートです。
これは、:cpp:class:`FirstLoc` 組み込みリデューサーを使用する :cpp:func:`parallel_reduce` 操作の結果を保持するように設計されています。

正しいテンプレートパラメーターが使用されるようにするため、一般的にはリデューサーの
``::value_type`` メンバー（例: ``FirstLoc<Index,Space>::value_type``）
を使用してこの型を取得することが推奨されます。

ヘッダーファイル: ``<Kokkos_Core.hpp>``

使い方
------

.. code-block:: cpp

   FirstLocScalar<Index>::value_type result;
   parallel_reduce(N,Functor,FirstLocScalar<Index>(result));
   I firstLoc = result.min_loc_true;

インターフェース
----------------

.. cpp:struct::  template<class Index> FirstLocScalar

   :tparam Index: 値の位置（インデックス）のデータ型。

   .. rubric:: データメンバー

   .. cpp:var:: Index min_loc_true

      最小値の位置（反復インデックス）