``is_partitioned``
==================

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲内の全要素、またはランク1の ``View`` 内の全要素が
述語　``pred`` を満たす場合、 その　*前に* 述語を満たさない要素が存在すれば、`true`を返します。
範囲または　``ビュー``　が空である場合、 ``真``　を返します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   ブール is_partitioned(const ExecutionSpace& exespace,                              (1)
                       InputIterator first, InputIterator last,
                       PredicateType pred);

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   ブール is_partitioned(const std::string& label, const ExecutionSpace& exespace,    (2)
                       InputIterator first, InputIterator last,
                       PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 is_partitioned(const ExecutionSpace& exespace,
                       const ::Kokkos::View<DataType, Properties...>& view,         (3)
                       PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 is_partitioned(const std::string& label, const ExecutionSpace& exespace,
                       const ::Kokkos::View<DataType, Properties...>& view,         (4)
                       PredicateType pred);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType, class PredicateType>
   KOKKOS_FUNCTION
   ブール is_partitioned(const TeamHandleType& teamHandle, IteratorType first,        (5)
                       IteratorType last, PredicateType pred);

   テンプレート <class TeamHandleType, class PredicateType, class DataType,
             class... Properties>
   KOKKOS_FUNCTION
   ブール is_partitioned(const TeamHandleType& teamHandle,                            (6)
                       const ::Kokkos::View<DataType, Properties...>& view,
                       PredicateType pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス


- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1:デフォルト文字列は、"Kokkos::is_partitioned_iterator_api_default".

  - 3:デフォルト文字列は、"Kokkos::is_partitioned_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索対象となる要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first``　を表す必要があります。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


- ``view``:

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``:

  - *一項* 述語：置換対象の必須要素に対して「真」を返す述語; ``pred(v)``　は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型　value_type　の引数　``v``　（constの可能性）のすべてのペアについて、bool型に変換可能で、そこでは、``value_type``　が、``InputIteratorType``　 (1,2について) の値型、または ``ビュー`` (3,4について)　の値型であり、  ``v``　を変更してはいけません。


  - 以下に一致しなければなりません:

  .. code-block:: cpp

     構造体 述語
     {
       KOKKOS_INLINE_FUNCTION
       ブール operator()(const value_type & v) const { return /* ... */; }

       // または、また有効

       KOKKOS_INLINE_FUNCTION
       ブール operator()(value_type v) const { return /* ... */; }
     };

戻り値
~~~~~~~~~~~~

- ``真``: 範囲が``pred``に従って分割されている場合、または範囲が空の場合
- ``偽``: その他の場合

例
~~~~~~~

.. code-block:: cpp

   名前空間 KE = Kokkos::Experimental;

   テンプル<class ValueType>
   構造体 IsNegative
   {
     KOKKOS_INLINE_FUNCTION
     ブール operator()(const ValueType & operand) const {
       constexpr auto zero = static_cast<ValueType>(0);
       返し (operand < zero);
     }
   };

   view_type = Kokkos::View<int*>　を使用;
   view_type a("a", 15);
   // 何らかの方法で　a を満たす

   自動 exespace  = Kokkos::DefaultExecutionSpace;
   const 自動 res = KE::is_partitioned(exespace, KE::cbegin(a), KE::cend(a), IsNegative<int>());
