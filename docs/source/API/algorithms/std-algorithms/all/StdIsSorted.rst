
``is_sorted``
=============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲またはランク1の　``ビュー`` 内の要素が、2つの要素を比較する ``operator<`` またはユーザーが提供した比較演算子を用いて、降順でない順序でソートされているかどうかを確認します。

インターフェイス
---------

.. 警告:: This is currently inside the ``Kokkos::Experimental`` namespace.

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType>
   ブール is_sorted(const ExecutionSpace& exespace,                              (1)
                  IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class IteratorType>
   ブール is_sorted(const std::string& label,                                    (2)
                  const ExecutionSpace& exespace,
                  IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   ブール is_sorted(const ExecutionSpace& exespace,                              (3)
                  const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   ブール is_sorted(const std::string& label, const ExecutionSpace& exespace,    (4)
                  const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   ブール is_sorted(const ExecutionSpace& exespace,                              (5)
                  IteratorType first, IteratorType last,
                  ComparatorType comp);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   ブール is_sorted(const std::string& label, const ExecutionSpace& exespace,    (6)
                  IteratorType first, IteratorType last,
                  ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class... Properties,
             class ComparatorType>
   ブール is_sorted(const ExecutionSpace& exespace,                              (7)
                  const ::Kokkos::View<DataType, Properties...>& view,
                  ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class... Properties,
             class ComparatorType>
   ブール is_sorted(const std::string& label, const ExecutionSpace& exespace,    (8)
                  const ::Kokkos::View<DataType, Properties...>& view,
                  ComparatorType comp);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (9)
                  IteratorType first, IteratorType last);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (10)
                  const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class TeamHandleType, class IteratorType, class ComparatorType>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (11)
                  IteratorType first, IteratorType last,
                  ComparatorType comp);

   テンプレート <class TeamHandleType, class DataType, class... Properties,
             class ComparatorType>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (12)
                  const ::Kokkos::View<DataType, Properties...>& view,
                  ComparatorType comp);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス


- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::is_sorted_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::is_sorted_view_api_default".

  - 5: デフォルト文字列は、 "Kokkos::is_sorted_iterator_api_default".

  - 7: デフォルト文字列は、 "Kokkos::is_sorted_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索対象の要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。

  - 有効範囲、つまり、 ``last >= first``　を表さなければなりません。

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view``:

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``comp``:

  - *binary* functor returning ``true`` if the first argument is *less than* the second argument;
    ``comp(a,b)`` must be valid to be called from the execution space passed,
    and convertible to bool for every pair of arguments ``a,b`` of type ``value_type``,
    where ``value_type`` is the value type of ``IteratorType`` (for 1,2,5,6)
    or the value type of ``view`` (for 3,4,7,8) and must not modify ``a,b``.

  - must conform to:

  .. code-block:: cpp

     struct Comparator
     {
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & a, const value_type & b) const {
         return /* true if a is less than b, based on your logic of "less than" */;
       }
     };

Return Value
~~~~~~~~~~~~

Returns ``true`` if the elements are sorted in descending order.
