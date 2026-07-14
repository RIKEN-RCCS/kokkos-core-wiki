``unique_copy``
===============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
------------------

連続する同一要素が存在しないように、範囲または ``source`` ビューから要素をコピーし、 ``first_to`` で始まる範囲または ``dest`` ビューに配置します。それは、目的の場所または目的のビューにコピーされた最後の要素の *後の* 要素へのイテレータを返します。等価性は、 ``operator==`` または二項述語 ``pred`` を使用して、確認されます。

インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator unique_copy(const ExecutionSpace& exespace,                 (1)
                              InputIterator first_from, InputIterator last_from,
                              OutputIterator first_to);

   template <class ExecutionSpace, class InputIterator, class OutputIterator>
   OutputIterator unique_copy(const std::string& label,                       (2)
                              const ExecutionSpace& exespace,
                              InputIterator first_from, InputIterator last_from,
                              OutputIterator first_to);

   template <
     class ExecutionSpace,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2>
   auto unique_copy(const ExecutionSpace& exespace,                           (3)
                    const Kokkos::View<DataType1, Properties1...>& source,
                    const Kokkos::View<DataType2, Properties2...>& dest);

   template <
     class ExecutionSpace,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2>
   auto unique_copy(const std::string& label,                                 (4)
                    const ExecutionSpace& exespace,
                    const Kokkos::View<DataType1, Properties1...>& source,
                    const Kokkos::View<DataType2, Properties2...>& dest);

   template <
     class ExecutionSpace,
     class InputIterator, class OutputIterator,
     class BinaryPredicate>
   OutputIterator unique_copy(const ExecutionSpace& exespace,                 (5)
                              InputIterator first_from, InputIterator last_from,
                              OutputIterator first_to,
                              BinaryPredicate pred);

   template <
     class ExecutionSpace,
     class InputIterator, class OutputIterator,
     class BinaryPredicate>
   OutputIterator unique_copy(const std::string& label,                       (6)
                              const ExecutionSpace& exespace,
                              InputIterator first_from, InputIterator last_from,
                              OutputIterator first_to,
                              BinaryPredicate pred);

   template <
     class ExecutionSpace,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2,
     class BinaryPredicate>
   auto unique_copy(const ExecutionSpace& exespace,                           (7)
                    const Kokkos::View<DataType1, Properties1...>& source,
                    const Kokkos::View<DataType2, Properties2...>& dest,
                    BinaryPredicate pred);

   template <
     class ExecutionSpace,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2,
     class BinaryPredicate>
   auto unique_copy(const std::string& label,                                 (8)
                    const ExecutionSpace& exespace,
                    const Kokkos::View<DataType1, Properties1...>& source,
                    const Kokkos::View<DataType2, Properties2...>& dest,
                    BinaryPredicate pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class InputIterator, class OutputIterator>
   KOKKOS_FUNCTION
   OutputIterator unique_copy(const TeamHandleType& teamHandle,               (9)
                              InputIterator first_from, InputIterator last_from,
                              OutputIterator first_to);

   template <
     class TeamHandleType,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2>
   KOKKOS_FUNCTION
   auto unique_copy(const TeamHandleType& teamHandle,                         (10)
                    const Kokkos::View<DataType1, Properties1...>& source,
                    const Kokkos::View<DataType2, Properties2...>& dest);

   template <
     class TeamHandleType,
     class InputIterator, class OutputIterator,
     class BinaryPredicate>
   KOKKOS_FUNCTION
   OutputIterator unique_copy(const TeamHandleType& teamHandle,               (11)
                              InputIterator first_from, InputIterator last_from,
                              OutputIterator first_to,
                              BinaryPredicate pred);

   template <
     class TeamHandleType,
     class DataType1, class... Properties1,
     class DataType2, class... Properties2,
     class BinaryPredicate>
   KOKKOS_FUNCTION
   auto unique_copy(const TeamHandleType& teamHandle,                         (12)
                    const Kokkos::View<DataType1, Properties1...>& source,
                    const Kokkos::View<DataType2, Properties2...>& dest,
                    BinaryPredicate pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1, 5: について、デフォルト文字列は、 "Kokkos::unique_copy_iterator_api_default".

  - 3, 7: について、デフォルト文字列は、 "Kokkos::unique_copy_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first_from, last_from``, ``first_to``:  ソース範囲 ``{first,last}_from``
  および宛先範囲 ``first_to`` へのイテレータ

  - *ランダムアクセスイテレータ* である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end`` から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first`` を表す必要があります。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``source``, ``dest``:

  - 必ずランク1であり、 ``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``:

  -  *単項* 述語：置換対象の必須要素に対して、 ``真`` を返す述語; ``pred(v)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならず、 型 ``value_type`` すべての引数 ``v`` （constの可能性）について、ブール型に変換可能で、そこでは、 ``value_type`` が、  ``InputIterator`` (1,2,5,6,9,11について) の値型、または  ``view`` (3,4,7,8,10,12について) の値型であり、  ``v`` を変更してはいけません。

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
~~~~~~~~~~~~

宛先範囲またはビュー内にコピーされる最後の要素の *後の* 要素へのイテレータ。
