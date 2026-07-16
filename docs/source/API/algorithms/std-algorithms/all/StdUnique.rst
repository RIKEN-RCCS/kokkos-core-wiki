``unique``
==========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
----

範囲または ``View`` 内の等価な要素からなる連続したグループから、最後の要素を除くすべての要素を除去し、範囲の新しい論理的な終了位置の *後の* 要素へのイテレータを返します。 等価性は ``operator==`` および二項述語  ``pred`` を用いて確認されます。

.. note:: 本動作は、 ``std::unique`` の動作とは異なります。具体的には、 ``std::unique`` は、等価な要素からなる連続したグループごとに、最初の要素を除くすべての要素を除去します。

インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType>
   IteratorType unique(const ExecutionSpace& exespace,                       (1)
                       IteratorType first, IteratorType last);

   template <class ExecutionSpace, class IteratorType>
   IteratorType unique(const std::string& label,                             (2)
                       const ExecutionSpace& exespace,
                       IteratorType first, IteratorType last);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto unique(const ExecutionSpace& exespace,                               (3)
               const Kokkos::View<DataType, Properties...>& view);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto unique(const std::string& label, const ExecutionSpace& exespace,     (4)
               const Kokkos::View<DataType, Properties...>& view);

   template <class ExecutionSpace, class IteratorType, class BinaryPredicate>
   IteratorType unique(const ExecutionSpace& exespace,                       (5)
                       IteratorType first, IteratorType last,
                       BinaryPredicate pred);

   template <class ExecutionSpace, class IteratorType, class BinaryPredicate>
   IteratorType unique(const std::string& label,                             (6)
                       const ExecutionSpace& exespace,
                       IteratorType first, IteratorType last,
                       BinaryPredicate pred);

   template <
     class ExecutionSpace,
     class DataType, class... Properties,
     class BinaryPredicate>
   auto unique(const ExecutionSpace& exespace,                               (7)
               const Kokkos::View<DataType, Properties...>& view,
               BinaryPredicate pred);

   template <
     class ExecutionSpace,
     class DataType, class... Properties,
     class BinaryPredicate>
   auto unique(const std::string& label,                                     (8)
               const ExecutionSpace& exespace,
               const Kokkos::View<DataType, Properties...>& view,
               BinaryPredicate pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   IteratorType unique(const TeamHandleType& teamHandle,                     (9)
                       IteratorType first, IteratorType last);

   template <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   auto unique(const TeamHandleType& teamHandle,                             (10)
               const Kokkos::View<DataType, Properties...>& view);

   template <class TeamHandleType, class IteratorType, class BinaryPredicate>
   KOKKOS_FUNCTION
   IteratorType unique(const TeamHandleType& teamHandle,                     (11)
                       IteratorType first, IteratorType last,
                       BinaryPredicate pred);

   template <
       class TeamHandleType,
       class DataType, class... Properties,
       class BinaryPredicate>
   KOKKOS_FUNCTION
   auto unique(const TeamHandleType& teamHandle,                             (12)
               const Kokkos::View<DataType, Properties...>& view,
               BinaryPredicate pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1, 5: について、デフォルト文字列は、"Kokkos::unique_iterator_api_default".

  - 3, 7: について、デフォルト文字列は、"Kokkos::unique_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索する要素の範囲

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first`` を表す必要があります。

  -  必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``:

  - 必ずランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  -  必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``:

  -   *単項* 述語：置換対象の必須要素に対して， ``真`` を返す述語; ``pred(v)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならず、 型 ``value_type`` すべての引数 ``v`` （constの可能性）について、ブール型に変換可能で、そこでは、 ``value_type`` が、  ``IteratorType`` (1,2,5,6,9,11について) の値型、または  ``view`` (3,4,7,8,10,12について) の値型であり、  ``v`` を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     struct Predicate
     {
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & v) const { return /* ... */; }

       // または、また有効

       KOKKOS_INLINE_FUNCTION
       bool operator()(value_type v) const { return /* ... */; }
     };

戻り値
~~~~~~

範囲の論理上の終わりの *後の* 要素へのイテレータ。
