``shift_left``
==============

ヘッダーファイル: ``Kokkos_StdAlgorithms.hpp``

ディスクリプション
-----------

 *始め*　に向けて、``n``　位置により、範囲または ``view``　内において、要素をシフトします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType>
   IteratorType shift_left(const ExecutionSpace& exespace,                 (1)
                           IteratorType first, IteratorType last,
                           typename IteratorType::difference_type n);

   テンプレート <class ExecutionSpace, class IteratorType>
   IteratorType shift_left(const std::string& label,                       (2)
                           const ExecutionSpace& exespace,
                           IteratorType first, IteratorType last,
                           typename IteratorType::difference_type n);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 shift_left(const ExecutionSpace& exespace,                         (3)
                  const Kokkos::View<DataType, Properties...>& view,
                  typename decltype(begin(view))::difference_type n);

   templateテンプレート <class ExecutionSpace, class DataType, class... Properties>
   自動 shift_left(const std::string& label,                               (4)
                   const ExecutionSpace& exespace,
                   const Kokkos::View<DataType, Properties...>& view,
                  typename decltype(begin(view))::difference_type n);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   IteratorType shift_left(const TeamHandleType& teamHandle,               (5)
                           IteratorType first, IteratorType last,
                           typename IteratorType::difference_type n);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   自動 shift_left(const TeamHandleType& teamHandle,                       (6)
                   const Kokkos::View<DataType, Properties...>& view,
                   typename decltype(begin(view))::difference_type n);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::shift_left_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::shift_left_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 変更対象の要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first``　を表す必要があります。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``: 変更対象のビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``n``: シフトする位置の数

  - 0以上でなければなりません。

戻り値
~~~~~~~~~~~~

結果の範囲の終わり。 ``n`` が ``last - first``よりも小さい場合には、 ``first + (last - first - n)``　を返します。 そうでなければ、``first``　を返します。
