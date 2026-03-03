
``none_of``
===========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲またはランク1の ``ビュー``　内の要素が、ターゲットの単項述語を満たさない場合に、 ``真`` を返します。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class IteratorType, class Predicate>
   ブール none_of(const ExecutionSpace& exespace,                              (1)
		IteratorType first, IteratorType last,
		Predicate predicate);

   テンプレート <class ExecutionSpace, class IteratorType, class Predicate>
   ブール none_of(const std::string& label, const ExecutionSpace& exespace,    (2)
		IteratorType first, IteratorType last,
		Predicate predicate);

   テンプレート <class ExecutionSpace, class DataType, class... Properties,      (3)
	     class Predicate>
   ブール none_of(const ExecutionSpace& exespace,
		const ::Kokkos::View<DataType, Properties...>& v,
		Predicate predicate);

   テンプレート <class ExecutionSpace, class DataType, class... Properties,
	     class Predicate>
    none_of(const std::string& label, const ExecutionSpace& exespace,    (4)
		const ::Kokkos::View<DataType, Properties...>& v,
		Predicate predicate);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class IteratorType, class Predicate>
   KOKKOS_FUNCTION
   ブール none_of(const TeamHandleType& teamHandle,                            (5)
		IteratorType first, IteratorType last,
		Predicate predicate);

   テンプレート <class TeamHandleType, class DataType, class... Properties,
	     class Predicate>
   KOKKOS_FUNCTION
   ブール none_of(const TeamHandleType& teamHandle,                           (6)
		const ::Kokkos::View<DataType, Properties...>& v,
		Predicate predicate);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::none_of_iterator_api_default".

  - 3: デフォルト文字列は、 "Kokkos::none_of_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索対象の要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first``　を表す必要があります。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``ビュー``:

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``: ``pred(v)`` が、引数として渡された実行空間、またはチームハンドルに関連付けられた実行空間から呼び出されるために、有効でなければならず、型 ``value_type``　のあらゆる引数 ``v``についてブール型に変換可能である *一項* ファンクタであり、ここで ``value_type`` は、``IteratorType`` または ``view``の値型であり、 ``v``を変更してはなりません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     構造体 CustomPredicate{
       KOKKOS_INLINE_FUNCTION
       bool operator()(const value_type & v) const;
     };

戻り値
~~~~~~~~~~~~

範囲またはビュー内の要素が単項述語を満たさない場合、
あるいは範囲または　``ビュー`` が空の場合、 ``真``  を返します。それ以外の場合は  ``偽``　を返します。
