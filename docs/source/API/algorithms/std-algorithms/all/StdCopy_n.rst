``copy_n``
==========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

ソース範囲またはランク1の ``ビュー`` から最初の ``n`` 個の要素を、別の範囲またはランク1の ``ビュー``にコピーします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

  テンプレート <
    クラス ExecutionSpace, class InputIteratorType,
    クラス SizeType, class OutputIteratorType>
  OutputIteratorType copy_n(const ExecutionSpace& exespace,                    (1)
                            InputIteratorType first_from,
                            SizeType n,
                            OutputIteratorType first_to);

  テンプレート <
    クラス ExecutionSpace, class InputIteratorType,
    クラス SizeType, class OutputIteratorType>
  OutputIteratorType copy_n(const std::string & label,
                            const ExecutionSpace& exespace,                    (2)
                            InputIteratorType first_from,
                            SizeType n,
                            OutputIteratorType first_to);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス SizeType,
    クラス DataType2, class... Properties2>
  自動 copy_n(const ExecutionSpace& exespace,                                  (3)
              const Kokkos::View<DataType1, Properties1...>& view_from,
              SizeType n,
              const Kokkos::View<DataType2, Properties2...>& view_to);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス SizeType,
    クラス DataType2, class... Properties2>
  自動 copy_n(const std::string& label, const ExecutionSpace& exespace,        (4)
              const Kokkos::View<DataType1, Properties1...>& view_from,
              SizeType n,
              const Kokkos::View<DataType2, Properties2...>& view_to);

チームハンドルを受け入れるオーバーロード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

  テンプレート <
    クラス TeamHandleType, class InputIteratorType,
    クラス SizeType, class OutputIteratorType>
  KOKKOS_FUNCTION
  OutputIteratorType copy_n(const TeamHandleType& teamHandle,                 (5)
                            InputIteratorType first_from,
                            SizeType n,
			    OutputIteratorType first_to);

  テンプレート <
    クラス TeamHandleType,
    クラス DataType1, class... Properties1, class SizeType,
    クラス DataType2, class... Properties2>
  KOKKOS_FUNCTION
  自動 copy_n(const TeamHandleType& teamHandle,                               (6)
              const ::Kokkos::View<DataType1, Properties1...>& view_from,
	      SizeType n,
              ::Kokkos::View<DataType2, Properties2...>& view_to);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |コピー| 置換:: ``コピー``
.. _コピー: ./StdCopy.html


- ``exespace``, ``teamHandle``, ``first_from``, ``first_to``, ``view_from``, ``view_to``: same as in |copy|_

- ``label``: used to name the implementation kernels for debugging purposes

  - for 1, the default string is: "Kokkos::copy_n_if_iterator_api_default"

  - for 3, the default string is: "Kokkos::copy_n_if_view_api_default"

  - NOTE: overloads accepting a team handle do not use a label internally

- ``n``: number of elements to copy (must be non-negative)


Return Value
~~~~~~~~~~~~

If ``n>0``, returns an iterator to the destination element *after* the last element copied.

Otherwise, returns ``first_to`` (for 1,2,5) or ``Kokkos::begin(view_to)`` (for 3,4,6).
