``shift_left``
==============

ヘッダーファイル: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

 *始め*　に向けて、``n``　位置により、範囲または ``view``　内において、要素をシフトします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType>
   IteratorType shift_left(const ExecutionSpace& exespace,                 (1)
                           IteratorType first, IteratorType last,
                           typename IteratorType::difference_type n);

   テンプレート <class ExecutionSpace, class IteratorType>
   IteratorType shift_left(const std::string& label,                       (2)
                           const ExecutionSpace& exespace,
                           IteratorType first, IteratorType last,
                           typename IteratorType::difference_type n);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 shift_left(const ExecutionSpace& exespace,                         (3)
                  const Kokkos::View<DataType, Properties...>& view,
                  typename decltype(begin(view))::difference_type n);

   templateテンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 shift_left(const std::string& label,                               (4)
                   const ExecutionSpace& exespace,
                   const Kokkos::View<DataType, Properties...>& view,
                  typename decltype(begin(view))::difference_type n);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   IteratorType shift_left(const TeamHandleType& teamHandle,               (5)
                           IteratorType first, IteratorType last,
                           typename IteratorType::difference_type n);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   自動 shift_left(const TeamHandleType& teamHandle,                       (6)
                   const Kokkos::View<DataType, Properties...>& view,
                   typename decltype(begin(view))::difference_type n);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: execution space instance

- ``teamHandle``: team handle instance given inside a parallel region when using a TeamPolicy

- ``label``: string forwarded to internal parallel kernels for debugging purposes

  - 1: The default string is "Kokkos::shift_left_iterator_api_default".

  - 3: The default string is "Kokkos::shift_left_view_api_default".

  - NOTE: overloads accepting a team handle do not use a label internally

- ``first, last``: range of elements to shift

  - must be *random access iterators*, e.g., returned from ``Kokkos::Experimental::(c)begin/(c)end``

  - must represent a valid range, i.e., ``last >= first``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view``: view to modify

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``n``: the number of positions to shift

  - must be non-negative

Return Value
~~~~~~~~~~~~

The end of the resulting range. If ``n`` is less than ``last - first``, returns ``first + (last - first - n)``. Otherwise, returns ``first``.
