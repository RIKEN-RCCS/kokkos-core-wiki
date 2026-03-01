``remove_copy``
===============

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

``value`` と等しい要素は除外して、指定された範囲の要素を、``first_to`` から始まる、または ``view_from``　から ``view_dest`` への新しい範囲にコピーします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <
     クラス ExecutionSpace,
     クラス InputIterator, class OutputIterator,
     クラス ValueType>
   OutputIterator remove_copy(const ExecutionSpace& exespace,                   (1)
                              InputIterator first_from,
                              InputIterator last_from,
                              OutputIterator first_to,
                              const ValueType& value);

   テンプレート <
     クラス ExecutionSpace,
     クラス InputIterator, class OutputIterator,
     クラス ValueType>
   OutputIterator remove_copy(const std::string& label,                         (2)
                              const ExecutionSpace& exespace,
                              InputIterator first_from,
                              InputIterator last_from,
                              OutputIterator first_to,
                              const ValueType& value);

   テンプレート <
     クラス ExecutionSpace,
     クラス DataType1, class... Properties1,
     クラス DataType2, class... Properties2,
     クラス ValueType>
   自動 remove_copy(const ExecutionSpace& exespace,                             (3)
                    const Kokkos::View<DataType1, Properties1...>& view_from,
                    const Kokkos::View<DataType2, Properties2...>& view_dest,
                    const ValueType& value);

   テンプレート <
     クラス ExecutionSpace,
     クラス DataType1, class... Properties1,
     クラス DataType2, class... Properties2,
     クラス ValueType>
   自動 remove_copy(const std::string& label,                                   (4)
                    const ExecutionSpace& exespace,
                    const Kokkos::View<DataType1, Properties1...>& view_from,
                    const Kokkos::View<DataType2, Properties2...>& view_dest,
                    const ValueType& value);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <
     クラス TeamHandleType,
     クラス InputIterator, class OutputIterator,
     クラス ValueType>
   KOKKOS_FUNCTION
   OutputIterator remove_copy(const TeamHandleType& teamHandle,                 (5)
                              InputIterator first_from,
                              InputIterator last_from,
                              OutputIterator first_to,
                              const ValueType& value);

   テンプレート <
     クラス TeamHandleType,
     クラス DataType1, class... Properties1,
     クラス DataType2, class... Properties2,
     クラス ValueType>
   KOKKOS_FUNCTION
   自動 remove_copy(const TeamHandleType& teamHandle,                           (6)
                    const Kokkos::View<DataType1, Properties1...>& view_from,
                    const Kokkos::View<DataType2, Properties2...>& view_dest,
                    const ValueType& value);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::remove_copy_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::remove_copy_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first_from, last_from``: コピー元の要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。

  -``last >= first``有効範囲、つまり、 ``last >= first``　を表さなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``first_to``: コピー先への範囲の始め

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``view_from``, ``view_dest``: ソースおよび宛先のビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``value``: 削除する対象値

戻り値
~~~~~~~~~~~~

コピーされた最後の要素の後の要素へのイテレータ。
