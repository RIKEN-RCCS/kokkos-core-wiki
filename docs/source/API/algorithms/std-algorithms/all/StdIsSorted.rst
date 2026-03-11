
``is_sorted``
=============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲またはランク1の　``ビュー`` 内の要素が、2つの要素を比較する ``operator<`` またはユーザーが提供した比較演算子を用いて、降順でない順序でソートされているかどうかを確認します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType>
   ブール is_sorted(const ExecutionSpace& exespace,                              (1)
                  IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class IteratorType>
   ブール is_sorted(const std::string& label,                                    (2)
                  const ExecutionSpace& exespace,
                  IteratorType first, IteratorType last);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   ブール is_sorted(const ExecutionSpace& exespace,                              (3)
                  const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   ブール is_sorted(const std::string& label, const ExecutionSpace& exespace,    (4)
                  const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   ブール is_sorted(const ExecutionSpace& exespace,                              (5)
                  IteratorType first, IteratorType last,
                  ComparatorType comp);

   テンプレート <class ExecutionSpace, class IteratorType, class ComparatorType>
   ブール is_sorted(const std::string& label, const ExecutionSpace& exespace,    (6)
                  IteratorType first, IteratorType last,
                  ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class... Properties,
             class ComparatorType>
   ブール is_sorted(const ExecutionSpace& exespace,                              (7)
                  const ::Kokkos::View<DataType, Properties...>& view,
                  ComparatorType comp);

   テンプレート <class ExecutionSpace, class DataType, class... Properties,
             class ComparatorType>
   ブール is_sorted(const std::string& label, const ExecutionSpace& exespace,    (8)
                  const ::Kokkos::View<DataType, Properties...>& view,
                  ComparatorType comp);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (9)
                  IteratorType first, IteratorType last);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (10)
                  const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class TeamHandleType, class IteratorType, class ComparatorType>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (11)
                  IteratorType first, IteratorType last,
                  ComparatorType comp);

   テンプレート <class TeamHandleType, class DataType, class... Properties,
             class ComparatorType>
   KOKKOS_FUNCTION
   ブール is_sorted(const TeamHandleType& teamHandle,                            (12)
                  const ::Kokkos::View<DataType, Properties...>& view,
                  ComparatorType comp);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス


- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::is_sorted_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::is_sorted_view_api_default".

  - 5: デフォルト文字列は、 "Kokkos::is_sorted_iterator_api_default".

  - 7: デフォルト文字列は、 "Kokkos::is_sorted_view_api_default".

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索対象の要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。

  - 有効範囲、つまり、 ``last >= first``　を表す必要があります。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``ビュー``:

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``comp``:

  - *二項*　ファンクタで、第1の引数が、2番目の引数　*より小さい*　場合に、``真``を返します;
    ``comp(a,b)``　は、 渡された実行空間から呼び出されるためには有効である必要があり、そして、 型　``value_type``　の引数　``a,b``　のすべてのペアについて、ブール型に変換可能で、そこでは、``value_type``　が 　``IteratorType`` (1,2,5,6について)　の値型、または ``ビュー`` (3,4,7,8について)　の値型であり、 ``a,b``　を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     構造体 コンパレータ
     {
       KOKKOS_INLINE_FUNCTION
       ブール operator()(const value_type & a, const value_type & b) const {
         return /* true if a is less than b, based on your logic of "less than" */;
       }
     };

戻り値
~~~~~~~~~~~~

要素が降順でソートされる場合に、 ``真``　を返します。
