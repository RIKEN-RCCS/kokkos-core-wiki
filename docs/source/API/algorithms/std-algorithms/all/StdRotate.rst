``rotate``
==========

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

要素　``n_first``　または　``view(n_location)``　を新しい範囲の最初の要素とし、``n_first - 1``　が最後の要素となるように、範囲または　``view``　内の要素を入れ替えます。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType>
   IteratorType rotate(const ExecutionSpace& exespace,                            (1)
                       IteratorType first,
                       IteratorType n_first,
                       IteratorType last);

   template <class ExecutionSpace, class IteratorType>
   IteratorType rotate(const std::string& label, const ExecutionSpace& exespace,  (2)
                       IteratorType first,
                       IteratorType n_first,
                       IteratorType last);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto rotate(const ExecutionSpace& exespace,                                    (3)
               const Kokkos::View<DataType, Properties...>& view,
               std::size_t n_location);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto rotate(const std::string& label, const ExecutionSpace& exespace,          (4)
               const Kokkos::View<DataType, Properties...>& view,
               std::size_t n_location);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   IteratorType rotate(const TeamHandleType& teamHandle,                          (5)
                       IteratorType first,
                       IteratorType n_first,
                       IteratorType last);

   template <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   auto rotate(const TeamHandleType& teamHandle,                                  (6)
               const Kokkos::View<DataType, Properties...>& view,
               std::size_t n_location);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::rotate_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::rotate_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 変更対象の要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - 有効な範囲を表す必要があり、つまり、 ``last >= first``　でなければなりません。

  - 必ず　``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``n_first``: 回転された範囲の最初の要素となるべき要素へのイテレータ

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - ``[first, n_first)``　および　``[n_first, last)``　が有効な範囲となるようにする必要があります。

  - 必ず　``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``:

  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``n_location``: 回転の中心となる要素を特定する整数値

戻り値
~~~~~~~~~~~~

- 1, 2, 5:  ``first + (last - n_first)``　として計算されたイテレータを返します。

- 3, 4, 6:  ``Kokkos::begin(view) + (Kokkos::end(view) - n_location)``　を返します。
