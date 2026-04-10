
``copy_backward``
=================

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲 ``[first_from, last_from)`` の要素を逆順で、
``last_to`` で *終了する* もう一つの範囲、またはソースビュー ``view_from`` から宛先ビュー ``view_to`` へコピーします。 相対的な順序は保たれています。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

  template <class ExecutionSpace, class InputIteratorType, class OutputIteratorType>
  OutputIteratorType copy_backward(const ExecutionSpace& exespace,                (1)
                                   InputIteratorType first_from,
                                   InputIteratorType last_from,
                                   OutputIteratorType last_to);

  template <class ExecutionSpace, class InputIteratorType, class OutputIteratorType>
  OutputIteratorType copy_backward(const std::string& label,
                                   const ExecutionSpace& exespace,                (2)
                                   InputIteratorType first_from,
                                   InputIteratorType last_from,
                                   OutputIteratorType last_to);

  template <
    class ExecutionSpace,
    class DataType1, class... Properties1,
    class DataType2, class... Properties2
  >
  auto copy_backward(const ExecutionSpace& exespace,                              (3)
                     const Kokkos::View<DataType1, Properties1...>& view_from,
                     const Kokkos::View<DataType2, Properties2...>& view_to);

  template <
    class ExecutionSpace,
    class DataType1, class... Properties1,
    class DataType2, class... Properties2
  >
  auto copy_backward(const std::string& label, const ExecutionSpace& exespace,    (4)
                     const Kokkos::View<DataType1, Properties1...>& view_from,
                     const Kokkos::View<DataType2, Properties2...>& view_to);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

  template <class TeamHandleType, class InputIteratorType, class OutputIteratorType>
  KOKKOS_FUNCTION
  OutputIteratorType copy_backward(const TeamHandleType& teamHandle,             (5)
                                   InputIteratorType first_from,
                                   InputIteratorType last_from,
			           OutputIteratorType last_to);

  template <
    class TeamHandleType,
    class DataType1, class... Properties1,
    class DataType2, class... Properties2>
  KOKKOS_FUNCTION
  auto copy_backward(const TeamHandleType& teamHandle,                           (6)
                     const ::Kokkos::View<DataType1, Properties1...>& view_from,
                     ::Kokkos::View<DataType2, Properties2...>& view_to);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``:  TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で実装カーネルに名付けるために使用

  - 1 について、 デフォルト文字列は、 : "Kokkos::copy_backward_iterator_api_default"

  - 3 について、 デフォルト文字列は、: "Kokkos::copy_backward_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first_from, last_from``: コピー元の要素範囲

  - *ランダムアクセスイテレータ* でなければなりません。

  - 有効な範囲、つまり、``last_from >= first_from``を表す必要があります。（デバッグモードで確認済み）

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``last_to``: コビー先への範囲の最後の要素を過ぎたイテレータ

  - *ランダムアクセスイテレータ* でなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``view_from``, ``view_to`` : 要素のコピー元およびコピー先である、ソースおよび宛先

  - 必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

返し値
~~~~~~~~~~~~

コピーされた最後の要素へのイテレータ
