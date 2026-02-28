
``move_backward``
=================

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲内の要素、またはランク1の　``ビュー``　から、
``d_last``　で始まる範囲、またはターゲットとなるランク1の ``ビュー``へ、逆順で移動します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType2 move_backward(const ExecutionSpace& ex, IteratorType1 first,          (1)
                               IteratorType1 last, IteratorType2 d_last);

   テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   自動 move_backward(const ExecutionSpace& ex,                                        (2)
                      const ::Kokkos::View<DataType1, Properties1...>& source,
                      ::Kokkos::View<DataType2, Properties2...>& dest);


   テンプレート <class ExecutionSpace, class IteratorType1, class IteratorType2>
   IteratorType2 move_backward(const std::string& label, const ExecutionSpace& ex,     (3)
                               IteratorType1 first, IteratorType1 last,
                               IteratorType2 d_last);

   テンプレート <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   自動 move_backward(const std::string& label, const ExecutionSpace& ex,              (4)
                      const ::Kokkos::View<DataType1, Properties1...>& source,
                      ::Kokkos::View<DataType2, Properties2...>& dest);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType1, class IteratorType2>
   KOKKOS_FUNCTION
   IteratorType2 move_backward(const TeamHandleType& teamHandle, IteratorType1 first,  (5)
                               IteratorType1 last, IteratorType2 d_last);

   テンプレート <class TeamHandleType, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   自動 move_backward(const TeamHandleType& teamHandle,                                (6)
                      const ::Kokkos::View<DataType1, Properties1...>& source,
                      ::Kokkos::View<DataType2, Properties2...>& dest);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: execution space instance

- ``teamHandle``: team handle instance given inside a parallel region when using a TeamPolicy

- ``label``: string forwarded to internal parallel kernels for debugging purposes

  - for 1, the default string is: "Kokkos::move_backward_iterator_api_default"

  - for 3, the default string is: "Kokkos::move_backward_view_api_default"

  - NOTE: overloads accepting a team handle do not use a label internally

- ``first``, ``last``, ``d_last``: range of elements to move from and to in a reverse order

  - must be *random access iterator*

  - must represent a valid range, i.e., ``last >= first``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``source``, ``dest``: views to move from and to in a reverse order

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle


Return Value
~~~~~~~~~~~~

- 1,3,5: an iterator equal to ``d_last - Kokkos::Experimental::distance(first, last)``

- 2,4,6: an iterator equal to
  ``Kokkos::Experimental::end(dest) -
  Kokkos::Experimental:distance(Kokkos::Experimental::begin(source), Kokkos::Experimental::end(source))``
