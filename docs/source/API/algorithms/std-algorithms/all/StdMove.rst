
``move``
========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
------------------

範囲内の要素、またはランク1の ``ビュー`` から、
``d_first`` で始まる範囲、またはターゲットとなるランク1の ``ビュー`` へ移動します。

インターフェイス
----------------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator move(const ExecutionSpace& ex, InputIterator first,          (1)
                       InputIterator last, OutputIterator d_first);

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator move(const std::string& label, const ExecutionSpace& ex,     (2)
                       InputIterator first, InputIterator last,
                       OutputIterator d_first);

   template <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   auto move(const ExecutionSpace& ex,                                         (3)
             const ::Kokkos::View<DataType1, Properties1...>& source,
             ::Kokkos::View<DataType2, Properties2...>& dest);

   template <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
    move(const std::string& label, const ExecutionSpace& ex,               (4)
             const ::Kokkos::View<DataType1, Properties1...>& source,
             ::Kokkos::View<DataType2, Properties2...>& dest);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class InputIterator, class OutputIterator>
   KOKKOS_FUNCTION
   OutputIterator move(const TeamHandleType& teamHandle, InputIterator first,  (5)
                       InputIterator last, OutputIterator d_first);

   template <class TeamHandleType, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   auto move(const TeamHandleType& teamHandle,                                 (6)
             const ::Kokkos::View<DataType1, Properties1...>& source,
             ::Kokkos::View<DataType2, Properties2...>& dest);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1 について、デフォルト文字列は、 : "Kokkos::move_iterator_api_default"

  - 3 について、デフォルト文字列は、 : "Kokkos::move_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first``, ``last``, ``d_first``: 移動元および移動先の要素の範囲

  - *ランダムアクセスイテレータ* でなければなりません

  - 有効な範囲、つまり、 ``last >= first`` を表す必要があります。

  - 必ず `exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``source``, ``dest``: 移動元および移動先へのビュー

  - 必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず `exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


戻り値
~~~~~~~~~~~~

- 1,2,5: ``d_first + Kokkos::Experimental::distance(first, last)`` に等しいイテレータ。

- 3,4,6: ``Kokkos::Experimental::begin(dest) +
  Kokkos::Experimental:distance(Kokkos::Experimental::begin(source), Kokkos::Experimental::end(source))`` に等しいイテレータ。
