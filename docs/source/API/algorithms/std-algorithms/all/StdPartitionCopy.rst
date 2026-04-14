``partition_copy``
==================

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
------------------

範囲またはランク1の ``ビュー`` から、述語 ``pred`` を満たす要素を ``to_first_true`` または ``view_true`` にコピーし、一方で、その他は、 ``to_first_false`` または ``view_false`` にコピーされます。

インターフェイス
----------------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace,
             class InputIteratorType,
             class OutputIteratorTrueType,
             class OutputIteratorFalseType,
             class PredicateType>
   ::Kokkos::pair<OutputIteratorTrueType, OutputIteratorFalseType>
   partition_copy(const ExecutionSpace& exespace,                                  (1)
                  InputIteratorType from_first,
                  InputIteratorType from_last,
                  OutputIteratorTrueType to_first_true,
                  OutputIteratorFalseType to_first_false,
                  PredicateType pred);

   template <class ExecutionSpace,
             class InputIteratorType,
             class OutputIteratorTrueType,
             class OutputIteratorFalseType,
             class PredicateType>
   ::Kokkos::pair<OutputIteratorTrueType, OutputIteratorFalseType>
   partition_copy(const std::string& label,                                        (2)
                  const ExecutionSpace& exespace,
                  InputIteratorType from_first,
                  InputIteratorType from_last,
                  OutputIteratorTrueType to_first_true,
                  OutputIteratorFalseType to_first_false,
                  PredicateType pred);

   template <class ExecutionSpace,
             class DataType1, class... Properties1,
             class DataType2, class... Properties2,
             class DataType3, class... Properties3,
             class PredicateType>
   auto partition_copy(const ExecutionSpace& exespace,                             (3)
                       const ::Kokkos::View<DataType1, Properties1...>& view_from,
                       const ::Kokkos::View<DataType2, Properties2...>& view_dest_true,
                       const ::Kokkos::View<DataType3, Properties3...>& view_dest_false,
                       PredicateType pred);

   template <class ExecutionSpace,
             class DataType1, class... Properties1,
             class DataType2, class... Properties2,
             class DataType3, class... Properties3,
             class PredicateType>
   auto partition_copy(const std::string& label,                                   (4)
                       const ExecutionSpace& exespace,
                       const ::Kokkos::View<DataType1, Properties1...>& view_from,
                       const ::Kokkos::View<DataType2, Properties2...>& view_dest_true,
                       const ::Kokkos::View<DataType3, Properties3...>& view_dest_false,
                       PredicateType pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class InputIteratorType,
             class OutputIteratorTrueType, class OutputIteratorFalseType,
             class PredicateType>
   KOKKOS_FUNCTION
   ::Kokkos::pair<OutputIteratorTrueType, OutputIteratorFalseType>
   partition_copy(const TeamHandleType& teamHandle, InputIteratorType from_first,  (5)
               InputIteratorType from_last,
               OutputIteratorTrueType to_first_true,
               OutputIteratorFalseType to_first_false, PredicateType pred);

   template <class TeamHandleType, class DataType1, class... Properties1,
       class DataType2, class... Properties2, class DataType3,
       class... Properties3, class PredicateType>
   KOKKOS_FUNCTION
   auto partition_copy(const TeamHandleType& teamHandle,                           (6)
       const ::Kokkos::View<DataType1, Properties1...>& view_from,
       const ::Kokkos::View<DataType2, Properties2...>& view_dest_true,
       const ::Kokkos::View<DataType3, Properties3...>& view_dest_false,
       PredicateType pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicy 使用時に、並列領域内部で指定されたチームハンドルインスタンス

- ``label`` : デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::partition_copy_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::partition_copy_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``from_first, from_last``: コピー元の要素の範囲

  -  *ランダムアクセスイテレータ* である必要があり、例えば、``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、``last >= first`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``to_first_true``:  ``pred`` を満たす要素をコピーする範囲の始め

  -  *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``to_first_false``: ``pred`` を満たさない要素をコピーする範囲の始め

  - *ランダムアクセスイテレータ* である必要があり、例えば、``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view_from``: コピー元の要素のソースビュー

  - 必ず ランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``view_dest_true``: ``pred`` を満たす要素をコピーするデスティネーションビュー

  - 必ず ランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。


  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``view_dest_false``: ``pred`` を満たさない要素をコピーするデスティネーションビュー

  - ``必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``pred``:

  - 置換するために必要な要素について、 ``真`` を返す *一項* 述語;  ``pred(v)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型 value_type のすべての引数 ``v`` （constの可能性）について、ブール型に変換可能で、そこでは、``value_type`` が、 ``InputIteratorType``  (1,2について) の値型、または ``ビュー`` (3,4について) の値型であり、  ``v`` を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     struct Predicate
     {
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & v) const { return /* ... */; }

       // または、また有効

       KOKKOS_INLINE_FUNCTION
       bool operator()(value_type v) const { return /* ... */; }
     };

戻り値
~~~~~~~~~~~~

イテレータを含む ``Kokkos::pair`` を、2つのデスティネーション範囲（またはビュー）の最後に返します。
