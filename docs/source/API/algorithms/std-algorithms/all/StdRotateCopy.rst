``rotate_copy``
===============

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

Description
-----------

要素 ``n_first`` または ``view(n_location)`` が新しい範囲の最初の要素となり、``n_first - 1`` が最後の要素となるように、範囲 ``[first_from, last_from)`` の要素を、範囲 ``first_to`` から始まる範囲、または ``view_from`` から ``view_dest`` までの範囲にコピーします。

インターフェイス
----------------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator rotate_copy(const ExecutionSpace& exespace,                   (1)
                              InputIterator first_from,
                              InputIterator n_first,
                              InputIterator last_from,
                              OutputIterator first_to);

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator rotate_copy(const std::string& label,                         (2)
                              const ExecutionSpace& exespace,
                              InputIterator first_from,
                              InputIterator n_first,
                              InputIterator last_from,
                              OutputIterator first_to);

   template <
     class ExecutionSpace,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2>
   auto rotate_copy(const ExecutionSpace& exespace,                             (3)
                    const Kokkos::View<DataType1, Properties1...>& source,
                    std::size_t n_location,
                    const Kokkos::View<DataType2, Properties2...>& dest);

   template <
     class ExecutionSpace,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2>
   auto rotate_copy(const std::string& label,                                   (4)
                    const ExecutionSpace& exespace,
                    const Kokkos::View<DataType1, Properties1...>& source,
                    std::size_t n_location,
                    const Kokkos::View<DataType2, Properties2...>& dest);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class InputIterator, class OutputIterator>
   KOKKOS_FUNCTION
   OutputIterator rotate_copy(const TeamHandleType& teamHandle,                 (5)
                              InputIterator first_from,
                              InputIterator n_first,
                              InputIterator last_from,
                              OutputIterator first_to);

   template <
     class TeamHandleType,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   auto rotate_copy(const TeamHandleType& teamHandle,                           (6)
                    const Kokkos::View<DataType1, Properties1...>& source,
                    std::size_t n_location,
                    const Kokkos::View<DataType2, Properties2...>& dest);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::rotate_copy_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::rotate_copy_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first_from, last_from``: コピー元の要素の範囲

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``first_to``: コピー先の範囲の先頭

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``n_first``: 回転範囲の最初であるべき要素へのイテレータ。

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  -  ``[first_from, n_first)`` および ``[n_first, last_from)`` は、有効な範囲となるようにしなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``source, dest``:

  - 必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``n_location``: 回転の中心となる要素を識別する整数値

戻り値
~~~~~~~~~~~~

コピーした最後の要素の *後の* 要素へのイテレータ。
