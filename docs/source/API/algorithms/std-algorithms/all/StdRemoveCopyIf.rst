``remove_copy_if``
==================

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

``pred``　が  ``真``　を返す要素は除外して、範囲から、``first_to`` から始まる新たな範囲、または ``view_from``　から ``view_dest`` への新しい範囲にコピーします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <
     クラス ExecutionSpace,
     クラス InputIterator, class OutputIterator,
     クラス UnaryPredicate>
   OutputIterator remove_copy_if(const ExecutionSpace& exespace,                   (1)
                                 InputIterator first_from,
                                 InputIterator last_from,
                                 OutputIterator first_to,
                                 const UnaryPredicate& pred);

   テンプレート <
     クラス ExecutionSpace,
     クラス InputIterator, class OutputIterator,
     クラス UnaryPredicate>
   OutputIterator remove_copy_if(const std::string& label,                         (2)
                                 const ExecutionSpace& exespace,
                                 InputIterator first_from,
                                 InputIterator last_from,
                                 OutputIterator first_to,
                                 const UnaryPredicate& pred);

   テンプレート <
     クラス ExecutionSpace,
     クラス DataType1, class... Properties1,
     クラス DataType2, class... Properties2,
     クラス UnaryPredicate>
   自動 remove_copy_if(const ExecutionSpace& exespace,                             (3)
                     const Kokkos::View<DataType1, Properties1...>& view_from,
                     const Kokkos::View<DataType2, Properties2...>& view_dest,
                     const UnaryPredicate& pred);

   テンプレート <
     クラス ExecutionSpace,
     クラス DataType1, class... Properties1,
     クラス DataType2, class... Properties2,
     クラス UnaryPredicate>
   自動 remove_copy_if(const std::string& label,                                   (4)
                       const ExecutionSpace& exespace,
                       const Kokkos::View<DataType1, Properties1...>& view_from,
                       const Kokkos::View<DataType2, Properties2...>& view_dest,
                       const UnaryPredicate& pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <
     クラス TeamHandleType,
     クラス InputIterator, class OutputIterator,
     クラス UnaryPredicate>
   KOKKOS_FUNCTION
   OutputIterator remove_copy_if(const TeamHandleType& teamHandle,                 (5)
                                 InputIterator first_from,
                                 InputIterator last_from,
                                 OutputIterator first_to,
                                 const UnaryPredicate& pred);

   テンプレート <
     クラス TeamHandleType,
     クラス DataType1, class... Properties1,
     クラス DataType2, class... Properties2,
     クラス UnaryPredicate>
   KOKKOS_FUNCTION
   自動 remove_copy_if(const TeamHandleType& teamHandle,                           (6)
                       const Kokkos::View<DataType1, Properties1...>& view_from,
                       const Kokkos::View<DataType2, Properties2...>& view_dest,
                       const UnaryPredicate& pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |RemoveCopy| replace:: ``remove_copy``
.. _RemoveCopy: ./StdRemoveCopy.html

- ``exespace``, ``teamHandle``, ``first_from, last_from``, ``first_to``, ``view_from``, ``view_dest``: |RemoveCopy|_　と同様。

- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::remove_copy_if_iterator_api_default"。

  - 3: デフォルト文字列は、 "Kokkos::remove_copy_if_view_api_default"。

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``pred``:

  - *一項* 述語：置換対象の必須要素に対して「真」を返す述語; ``pred(v)``　は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型　value_type　すべての引数　``v``　（constの可能性）について、bool型に変換可能で、そこでは、``value_type``　が、``InputIteratorType``　 (1,2,5について) の値型、または ``view`` (3,4,6について)　の値型であり、  ``v``　を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     構造体 述語
     {
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & v) const { return /* ... */; }

       // または、また有効

       KOKKOS_INLINE_FUNCTION
       ブール operator()(value_type v) const { return /* ... */; }
     };

戻り値
~~~~~~~~~~~~

コピーされた最後の要素の後の要素へのイテレータ。
