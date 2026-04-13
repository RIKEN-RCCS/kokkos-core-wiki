
``reverse_copy``
================

ヘッダーファイル: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
------------------

範囲またはランク1の ``View`` から要素をコピーし、
逆順で ``d_first`` で始まる範囲、または対象ランク1の ``View`` に書き込みます。

インターフェイス
----------------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator reverse_copy(const ExecutionSpace& exespace, InputIterator first,      (1)
                               InputIterator last, OutputIterator d_first);

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator reverse_copy(const std::string& label, const ExecutionSpace& exespace, (2)
                               InputIterator first, InputIterator last,
                               OutputIterator d_first);

   template <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   auto reverse_copy(const ExecutionSpace& exespace,                                     (3)
                     const ::Kokkos::View<DataType1, Properties1...>& source,
                     ::Kokkos::View<DataType2, Properties2...>& dest);

   template <class ExecutionSpace, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   auto reverse_copy(const std::string& label, const ExecutionSpace& exespace,           (4)
                     const ::Kokkos::View<DataType1, Properties1...>& source,
                     ::Kokkos::View<DataType2, Properties2...>& dest);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class InputIterator, class OutputIterator>
   KOKKOS_FUNCTION
   OutputIterator reverse_copy(const TeamHandleType& teamHandle, InputIterator first,    (5)
                               InputIterator last, OutputIterator d_first);

   template <class TeamHandleType, class DataType1, class... Properties1,
             class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   auto reverse_copy(const TeamHandleType& teamHandle,                                   (6)
                     const ::Kokkos::View<DataType1, Properties1...>& source,
                     ::Kokkos::View<DataType2, Properties2...>& dest);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1 について、デフォルト文字列は、: "Kokkos::reverse_copy_iterator_api_default"

  - 3 について、デフォルト文字列は、: "Kokkos::reverse_copy_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first``, ``last``, ``d_first``: 逆順での、コピー元およびコピー先の要素の範囲

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``source``, ``dest``: 逆順での、コピー元およびコピー先のビュー

  - 必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。


  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

戻り値
~~~~~~~~~~~~

- 1,2,5:  ``d_first + Kokkos::Experimental::distance(first, last)`` に等しいイテレータ。

- 3,4,6:  ``Kokkos::Experimental::begin(dest) +
  Kokkos::Experimental:distance(Kokkos::Experimental::cbegin(source), Kokkos::Experimental::cend(source))`` に等しいイテレータ。
 
