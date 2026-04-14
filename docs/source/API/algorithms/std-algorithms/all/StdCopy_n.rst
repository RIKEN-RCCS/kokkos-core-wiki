``copy_n``
==========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
------------------

ソース範囲またはランク1の ``ビュー`` から最初の ``n`` 個の要素を、別の範囲またはランク1の ``ビュー`` にコピーします。

インターフェイス
----------------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

  template <
    class ExecutionSpace, class InputIteratorType,
    class SizeType, class OutputIteratorType>
  OutputIteratorType copy_n(const ExecutionSpace& exespace,                    (1)
                            InputIteratorType first_from,
                            SizeType n,
                            OutputIteratorType first_to);

  template <
    class ExecutionSpace, class InputIteratorType,
    class SizeType, class OutputIteratorType>
  OutputIteratorType copy_n(const std::string & label,
                            const ExecutionSpace& exespace,                    (2)
                            InputIteratorType first_from,
                            SizeType n,
                            OutputIteratorType first_to);

  template <
    class ExecutionSpace,
    class DataType1, class... Properties1,
    class SizeType,
    class DataType2, class... Properties2>
  auto copy_n(const ExecutionSpace& exespace,                                  (3)
              const Kokkos::View<DataType1, Properties1...>& view_from,
              SizeType n,
              const Kokkos::View<DataType2, Properties2...>& view_to);

  template <
    class ExecutionSpace,
    class DataType1, class... Properties1,
    class SizeType,
    class DataType2, class... Properties2>
  auto copy_n(const std::string& label, const ExecutionSpace& exespace,        (4)
              const Kokkos::View<DataType1, Properties1...>& view_from,
              SizeType n,
              const Kokkos::View<DataType2, Properties2...>& view_to);

チームハンドルを受け入れるオーバーロード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

  template <
    class TeamHandleType, class InputIteratorType,
    class SizeType, class OutputIteratorType>
  KOKKOS_FUNCTION
  OutputIteratorType copy_n(const TeamHandleType& teamHandle,                 (5)
                            InputIteratorType first_from,
                            SizeType n,
			    OutputIteratorType first_to);

  template <
    class TeamHandleType,
    class DataType1, class... Properties1, class SizeType,
    class DataType2, class... Properties2>
  KOKKOS_FUNCTION
  auto copy_n(const TeamHandleType& teamHandle,                               (6)
              const ::Kokkos::View<DataType1, Properties1...>& view_from,
	      SizeType n,
              ::Kokkos::View<DataType2, Properties2...>& view_to);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |copy| replace:: ``コピー``
.. _copy: ./StdCopy.html


- ``exespace``, ``teamHandle``, ``first_from``, ``first_to``, ``view_from``, ``view_to``: same as in |copy|_ と同様。

- ``label``: デバッグ目的で実装カーネルに名付けるために使用

  - 1 について、 デフォルト文字列は、: "Kokkos::copy_n_if_iterator_api_default"

  - 3 について、 デフォルト文字列は、: "Kokkos::copy_n_if_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``n``:  コピーする要素数 (0以上でなければならない)


戻り値
~~~~~~~~~~~~

 ``n>0`` の場合、 最後の要素がコピーされた *後* 宛先要素に、イテレータを返します。

そうでない場合には、 ``first_to`` (1,2,5について) または、 ``Kokkos::begin(view_to)`` (3,4,6について) を返します。
