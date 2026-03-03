
``find_if_not``
===============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

Descriptionディスクリプション
-----------

範囲内の　*最初*　の要素、またはカスタム述語を満たす　``ビュー``　へのイテレータを返します。

インターフェイス
---------

.. :: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   InputIterator find_if_not(const ExecutionSpace& exespace,                            (1)
		             InputIterator first, InputIterator last,
			     PredicateType pred);

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   InputIterator find_if_not(const std::string& label, const ExecutionSpace& exespace,  (2)
			     InputIterator first, InputIterator last,
			     PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 find_if_not(const ExecutionSpace& exespace,                                     (3)
		    const Kokkos::View<DataType, Properties...>& view,
		    PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 find_if_not(const std::string& label, const ExecutionSpace& exespace,           (4)
		    const Kokkos::View<DataType, Properties...>& view,
		    PredicateType pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class InputIterator, class PredicateType>
   KOKKOS_FUNCTION
   InputIterator find_if_not(const TeamHandleType& teamHandle,                          (5)
		             InputIterator first, InputIterator last,
			     PredicateType pred);

   テンプレート <class TeamHandleType, class DataType, class... Properties, class PredicateType>
   KOKKOS_FUNCTION
   自動 find_if_not(const TeamHandleType& teamHandle,                                   (6)
		    const Kokkos::View<DataType, Properties...>& view,
		    PredicateType pred);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1　について、デフォルト文字列は、: "Kokkos::find_if_not_iterator_api_default"

  - 3　について、デフォルト文字列は、: "Kokkos::find_if_not_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索する要素の範囲

  - 例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。

  - 有効範囲、つまり、 ``last >= first``　を表さなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``: 探索対象のビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``pred``: 必要な要素について ``真`` を返す一項述語;

  ``pred(a)`` は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型 (可能性のあるconst)　value_type　の引数　``a``　のすべてのペアについて、ブール型に変換可能で、そこでは、``value_type``　が、``IteratorType``　の値型、または ``view``　であり、  ``a``　を変更してはいけません。

  - 以下に一致しなければなりません:

    .. code-block:: cpp

       構造体　述語
       {
	  KOKKOS_INLINE_FUNCTION
	  ブール operator()(const /*type needed */ & operand) const { return /* ... */; }

	  // または、また有効

	  KOKKOS_INLINE_FUNCTION
	  bool operator()(/*type needed */ operand) const { return /* ... */; }
       };


戻り値
~~~~~~~~~~~~

- (1,2,5): そのような要素が見つからない場合、述語が真を評価する最初の要素を指している ``InputIterator`` インスタンス、または ``last``

- (3,4,6): そのような要素が見つからない場合、述語が　``真``　を評価する最初の要素へのイテレータ、または ``Kokkos::Experimental::end(view)`` 
