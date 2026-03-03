``remove_if``
=============

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

削除対象外の要素が範囲の先頭または ``View`` の先頭に配置されるように、範囲または ``View`` 内の要素を移動代入によってシフトすることにより、 ``pred`` が ``true`` を返す要素をすべて削除します。残存する要素の相対的な順序は保持され、コンテナの物理的なサイズは変更されません。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class Iterator, class UnaryPredicate>
   イテレータ remove_if(const ExecutionSpace& exespace,                           (1)
                      Iterator first, Iterator last,
                      UnaryPredicate pred);

   テンプレート <class ExecutionSpace, class Iterator, class UnaryPredicate>
   イテレータ remove_if(const std::string& label,                                 (2)
                      const ExecutionSpace& exespace,
                      Iterator first, Iterator last,
                      UnaryPredicate pred);

   テンプレート <
   　クラス ExecutionSpace,
     クラス DataType, class... Properties,
     クラス UnaryPredicate>
   自動 remove_if(const ExecutionSpace& exespace,                               (3)
                  const Kokkos::View<DataType, Properties...>& view,
                  UnaryPredicate pred);

   テンプレート <
     クラス ExecutionSpace,
     クラス DataType, class... Properties,
     クラス UnaryPredicate>
   自動 remove_if(const std::string& label,                                     (4)
                  const ExecutionSpace& exespace,
                  const Kokkos::View<DataType, Properties...>& view,
                  UnaryPredicate pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class Iterator, class UnaryPredicate>
   KOKKOS_FUNCTION
   イテレータ remove_if(const TeamHandleType& teamHandle,                         (5)
                      Iterator first, Iterator last,
                      UnaryPredicate pred);

   テンプレート <
     クラス TeamHandleType,
     クラス DataType, class... Properties,
     クラス UnaryPredicate>
   KOKKOS_FUNCTION
   自動 remove_if(const TeamHandleType& teamHandle,                             (6)
                  const Kokkos::View<DataType, Properties...>& view,
                  UnaryPredicate pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |remove| replace:: ``remove``
.. _remove: ./StdRemove.html

- ``exespace``, ``first``, ``last``, ``view``:  |remove|_　と同様。

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::remove_if_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::remove_if_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません

- ``pred``:

  - *一項* 述語：置換対象の必須要素に対して「真」を返す述語; ``pred(v)``　は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型　value_type　すべての引数　``v``　（constの可能性）について、bool型に変換可能で、そこでは、``value_type``　が、　``Iterator`` (1,2,5について) の値型、または ``view`` (3,4,6について)　の値型であり、  ``v``　を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     構造体 述語
     {
       KOKKOS_INLINE_FUNCTION
       ブール operator()(const value_type & v) const { return /* ... */; }

       // または、また有効

       KOKKOS_INLINE_FUNCTION
       ブール operator()(value_type v) const { return /* ... */; }
     };

戻り値
~~~~~~~~~~~~

コピーされた最後の要素の *後の* 要素へのイテレータ。
