``partition_copy``
==================

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

範囲またはランク1の　``ビュー`` から、述語　``pred``　を満たす要素を　``to_first_true`` または　``view_true``　にコピーし、一方で、その他は、 ``to_first_false`` または ``view_false``　にコピーされます。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace,
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

   テンプレート <class ExecutionSpace,
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

   テンプレート <class ExecutionSpace,
             class DataType1, class... Properties1,
             class DataType2, class... Properties2,
             class DataType3, class... Properties3,
             class PredicateType>
   自動 partition_copy(const ExecutionSpace& exespace,                             (3)
                       const ::Kokkos::View<DataType1, Properties1...>& view_from,
                       const ::Kokkos::View<DataType2, Properties2...>& view_dest_true,
                       const ::Kokkos::View<DataType3, Properties3...>& view_dest_false,
                       PredicateType pred);

   テンプレート <class ExecutionSpace,
             class DataType1, class... Properties1,
             class DataType2, class... Properties2,
             class DataType3, class... Properties3,
             class PredicateType>
   自動 partition_copy(const std::string& label,                                   (4)
                       const ExecutionSpace& exespace,
                       const ::Kokkos::View<DataType1, Properties1...>& view_from,
                       const ::Kokkos::View<DataType2, Properties2...>& view_dest_true,
                       const ::Kokkos::View<DataType3, Properties3...>& view_dest_false,
                       PredicateType pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class InputIteratorType,
             class OutputIteratorTrueType, class OutputIteratorFalseType,
             class PredicateType>
   KOKKOS_FUNCTION
   ::Kokkos::pair<OutputIteratorTrueType, OutputIteratorFalseType>
   partition_copy(const TeamHandleType& teamHandle, InputIteratorType from_first,  (5)
               InputIteratorType from_last,
               OutputIteratorTrueType to_first_true,
               OutputIteratorFalseType to_first_false, PredicateType pred);

   テンプレート <class TeamHandleType, class DataType1, class... Properties1,
       class DataType2, class... Properties2, class DataType3,
       class... Properties3, class PredicateType>
   KOKKOS_FUNCTION
   自動 partition_copy(const TeamHandleType& teamHandle,                           (6)
       const ::Kokkos::View<DataType1, Properties1...>& view_from,
       const ::Kokkos::View<DataType2, Properties2...>& view_dest_true,
       const ::Kokkos::View<DataType3, Properties3...>& view_dest_false,
       PredicateType pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicy　使用時に、並列領域内部で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::partition_copy_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::partition_copy_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``from_first, from_last``: コピー元の要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、``Kokkos::Experimental::(c)begin/(c)end``から返されなければなりません。

  - 有効な範囲を表す必要があり、つまり、``last >= first`` でなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``to_first_true``:  ``pred`` を満たす要素をコピーする範囲の始め

  - ``*ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``to_first_false``: ``pred`` を満たさない要素をコピーする範囲の始め

  - *ランダムアクセスイテレータ*　である必要があり、例えば、``Kokkos::Experimental::(c)begin/(c)end``から返されなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view_from``: source view of elements to copy from

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view_dest_true``: destination view to copy the elements that satisfy ``pred`` to
  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view_dest_false``: destination view to copy the elements that do NOT satisfy ``pred`` to

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``pred``:

  - *unary* predicate returning ``true`` for the required element to replace; ``pred(v)``
    must be valid to be called from the execution space passed, and convertible to bool for every
    argument ``v`` of type (possible const) ``value_type``, where ``value_type``
    is the value type of ``InputIteratorType`` (for 1,2) or the value type of ``view_from`` (for 3,4),
    and must not modify ``v``.

  - must conform to:

  .. code-block:: cpp

     struct Predicate
     {
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & v) const { return /* ... */; }

       // or, also valid

       KOKKOS_INLINE_FUNCTION
       bool operator()(value_type v) const { return /* ... */; }
     };

Return Value
~~~~~~~~~~~~

Returns a ``Kokkos::pair`` containing the iterators to the end of two destination ranges (or views)
