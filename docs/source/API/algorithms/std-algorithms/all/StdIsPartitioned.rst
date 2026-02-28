``is_partitioned``
==================

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲内の全要素、またはランク1の ``View`` 内の全要素が
述語　``pred`` を満たす場合、 その　*前に* 述語を満たさない要素が存在すれば、`true`を返します。
範囲または　``ビュー``　が空である場合、 ``真``　を返します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   ブール is_partitioned(const ExecutionSpace& exespace,                              (1)
                       InputIterator first, InputIterator last,
                       PredicateType pred);

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   ブール is_partitioned(const std::string& label, const ExecutionSpace& exespace,    (2)
                       InputIterator first, InputIterator last,
                       PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 is_partitioned(const ExecutionSpace& exespace,
                       const ::Kokkos::View<DataType, Properties...>& view,         (3)
                       PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 is_partitioned(const std::string& label, const ExecutionSpace& exespace,
                       const ::Kokkos::View<DataType, Properties...>& view,         (4)
                       PredicateType pred);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType, class PredicateType>
   KOKKOS_FUNCTION
   ブール is_partitioned(const TeamHandleType& teamHandle, IteratorType first,        (5)
                       IteratorType last, PredicateType pred);

   テンプレート <class TeamHandleType, class PredicateType, class DataType,
             class... Properties>
   KOKKOS_FUNCTION
   ブール is_partitioned(const TeamHandleType& teamHandle,                            (6)
                       const ::Kokkos::View<DataType, Properties...>& view,
                       PredicateType pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス



- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1:デフォルト文字列は、"Kokkos::is_partitioned_iterator_api_default".

  - 3:デフォルト文字列は、"Kokkos::is_partitioned_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索対象となる要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``から返されなければなりません。

  - must represent a valid range, i.e., ``last >= first``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view``:

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``pred``:

  - *unary* predicate returning ``true`` for the required element to replace; ``pred(v)``
    must be valid to be called from the execution space passed, and convertible to bool for every
    argument ``v`` of type (possible const) ``value_type``, where ``value_type``
    is the value type of ``IteratorType`` (for 1,2) or the value type of ``view`` (for 3,4),
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

- ``true``: if range is partitioned according to ``pred`` or if range is empty
- ``false``: otherwise

Example
~~~~~~~

.. code-block:: cpp

   namespace KE = Kokkos::Experimental;

   template<class ValueType>
   struct IsNegative
   {
     KOKKOS_INLINE_FUNCTION
     bool operator()(const ValueType & operand) const {
       constexpr auto zero = static_cast<ValueType>(0);
       return (operand < zero);
     }
   };

   using view_type = Kokkos::View<int*>;
   view_type a("a", 15);
   // fill a somehow

   auto exespace  = Kokkos::DefaultExecutionSpace;
   const auto res = KE::is_partitioned(exespace, KE::cbegin(a), KE::cend(a), IsNegative<int>());
