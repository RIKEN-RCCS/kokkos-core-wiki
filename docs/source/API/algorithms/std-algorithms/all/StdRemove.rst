``remove``
==========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
------------------

削除されない要素が、範囲の先頭、または ``View`` の先頭に配置されるという条件で、指定された範囲または ``View`` 内の要素を、移動代入によってシフトし、 ``value`` と等しい要素をすべて削除します。 相対的な順序は保持され、コンテナの物理的なサイズは変更されません。

インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class Iterator, class ValueType>
   Iterator remove(const ExecutionSpace& exespace,                       (1)
                   Iterator first, Iterator last,
                   const ValueType& value);

   template <class ExecutionSpace, class Iterator, class ValueType>
   Iterator remove(const std::string& label,                             (2)
                   const ExecutionSpace& exespace,
                   Iterator first, Iterator last,
                   const ValueType& value);

   template <
     class ExecutionSpace,
     class DataType, class... Properties,
     class ValueType>
   auto remove(const ExecutionSpace& exespace,                           (3)
               const Kokkos::View<DataType, Properties...>& view,
               const ValueType& value);

   template <
     class ExecutionSpace,
     class DataType, class... Properties,
     class ValueType>
   auto remove(const std::string& label,                                 (4)
               const ExecutionSpace& exespace,
               const Kokkos::View<DataType, Properties...>& view,
               const ValueType& value);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class Iterator, class ValueType>
   KOKKOS_FUNCTION
   Iterator remove(const TeamHandleType& teamHandle,                     (5)
                   Iterator first, Iterator last,
                   const ValueType& value);

   template <
     class TeamHandleType,
     class DataType, class... Properties,
     class ValueType>
   KOKKOS_FUNCTION
   auto remove(const TeamHandleType& teamHandle,                         (6)
               const Kokkos::View<DataType, Properties...>& view,
               const ValueType& value);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::remove_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::remove_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 変更対象の要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されるなど、*ランダムアクセスイテレータ* でなければなりません。

  - 有効な範囲、つまり、 ``last >= first`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``value``: 削除の対象値

- ``view``: 変更対象の要素のビュー

  - 必ずランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

戻り値
~~~~~~~~~~~~

新たな論理上の終了 *後* の要素へのイテレータ。
