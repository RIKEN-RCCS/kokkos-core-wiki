
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

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ````: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1　について、デフォルト文字列は、: "Kokkos::move_backward_iterator_api_default"

  - 3　について、デフォルト文字列は、: "Kokkos::move_backward_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first``, ``last``, ``d_last``: 逆順での移動元および移動先の要素の範囲

  - *ランダムアクセスイテレータ*　でなければなりません

  - 有効な範囲を表す必要があり、つまり、 ``last >= first``　でなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``source``, ``dest``: 逆順での移動元および移動先へのビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります


戻り値
~~~~~~~~~~~~

- 1,3,5: ``d_last - Kokkos::Experimental::distance(first, last)``　に等しいイテレータ。

- 2,4,6: ``Kokkos::Experimental::end(dest) -
  Kokkos::Experimental:distance(Kokkos::Experimental::begin(source), Kokkos::Experimental::end(source))``　に等しいイテレータ。
