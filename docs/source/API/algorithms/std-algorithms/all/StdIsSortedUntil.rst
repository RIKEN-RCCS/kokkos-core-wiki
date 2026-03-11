``is_sorted_until``
===================

ヘッダー: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

``first`` または ``Kokkos::Experimental::begin(view)`` から始まる範囲の中で、要素が降順でない順序でソートされている最大の範囲を見つけます。 要素間の比較は、``operator<`` または二項ファンクタ ``comp`` 経由で行われます。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType>
   IteratorType is_sorted_until(const ExecutionSpace& exespace,                     (1)
                                IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class IteratorType>
   IteratorType is_sorted_until(const std::string& label,                           (2)
                                const ExecutionSpace& exespace,
                                IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   IteratorType is_sorted_until(const ExecutionSpace& exespace,                     (3)
                                IteratorType first, IteratorType last,
                                ComparatorType comp);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   IteratorType is_sorted_until(const std::string& label,                           (4)
                                const ExecutionSpace& exespace,
                                IteratorType first, IteratorType last,
                                ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 is_sorted_until(const ExecutionSpace& exespace,                             (5)
                        const Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 is_sorted_until(const std::string& label,                                   (6)
                        const ExecutionSpace& exespace,
                        const Kokkos::View<DataType, Properties...>& view);

   テンプレート <
      クラス ExecutionSpace,
      クラス DataType, class... Properties, class ComparatorType>
   自動 is_sorted_until(const ExecutionSpace& exespace,                             (7)
                        const Kokkos::View<DataType, Properties...>& view,
                        ComparatorType comp);

   テンプレート <
      クラス ExecutionSpace,
      クラス DataType, class... Properties, class ComparatorType>
   自動 is_sorted_until(const std::string& label, const ExecutionSpace& exespace,   (8)
                        const Kokkos::View<DataType, Properties...>& view,
                        ComparatorType comp);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   IteratorType is_sorted_until(const TeamHandleType& teamHandle,                   (9)
                                IteratorType first, IteratorType last);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   自動 is_sorted_until(const TeamHandleType& teamHandle,                           (10)
                        const Kokkos::View<DataType, Properties...>& view);

   テンプレート <class TeamHandleType, class IteratorType, class ComparatorType>
   KOKKOS_FUNCTION
   IteratorType is_sorted_until(const TeamHandleType& teamHandle,                   (11)
                                IteratorType first, IteratorType last,
                                ComparatorType comp);

   テンプレート <
      クラス TeamHandleType,
      クラス DataType, class... Properties, class ComparatorType>
   KOKKOS_FUNCTION
   自動 is_sorted_until(const TeamHandleType& teamHandle,                           (12)
                        const Kokkos::View<DataType, Properties...>& view,
                        ComparatorType comp);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |IsSorted| 置換:: ``is_sorted``
.. _IsSorted: ./StdIsSorted.html

- ``exespace``, ``teamHandle``, ``first``, ``last``, ``view``, ``comp``:  |IsSorted|_　と同様。

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - ``exespace``　からアクセス可能でなければなりません。

  - 1 & 3: デフォルト文字列は、 "Kokkos::is_sorted_until_iterator_api_default"

  - 5 & 7: デフォルト文字列は、 "Kokkos::is_sorted_until_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。


戻り値
~~~~~~~~~~~~

- 範囲 ``[first, it)`` がソートされる最後のイテレータ 　``it``　およびかつ以下の条件が真である場合: ``std::is_same_v<decltype(it), IteratorType>``　、または範囲　``[Kokkos::Experimental::begin(view), it)``　がソートされている場合。 この2番目の事例については、以下の通りに``it``　が計算されることに注意してください。　``Kokkos::Experimental::begin(view) + increment``　：ここで、``increment`` は、アルゴリズム内に認められます。
