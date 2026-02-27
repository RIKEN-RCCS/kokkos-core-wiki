
``find``
========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

対象値と等しい範囲またはランク1のビューにおける *first* 要素への反復子を返します。  ``operator==``　を使用して.
等価性が確認されます。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class InputIterator, class T>
   InputIterator find(const ExecutionSpace& exespace,                                   (1)
		      InputIterator first, InputIterator last,
		      const T& value);

   テンプレート <class ExecutionSpace, class InputIterator, class T>
   InputIterator find(const std::string& label, const ExecutionSpace& exespace,         (2)
		      InputIterator first, InputIterator last,
		      const T& value);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
   auto find(const ExecutionSpace& exespace,                                            (3)
	     const Kokkos::View<DataType, Properties...>& view,
	     const T& value);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class T>
   自動 find(const std::string& label, const ExecutionSpace& exespace,                  (4)
	     const Kokkos::View<DataType, Properties...>& view,
	     const T& value);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class InputIterator, class T>
   KOKKOS_FUNCTION
   InputIterator find(const TeamHandleType& teamHandle,                                 (5)
		      InputIterator first, InputIterator last,
		      const T& value);

   テンプレート <class TeamHandleType, class DataType, class... Properties, class T>
   KOKKOS_FUNCTION
   自動 find(const TeamHandleType& teamHandle,                                          (6)
	     const Kokkos::View<DataType, Properties...>& view,
	     const T& value);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で内部の並列カーネルに名付けるために使用

  - 1　について、 デフォルト文字列は、: "Kokkos::find_iterator_api_default"

  - 3　について、 デフォルト文字列は、: "Kokkos::find_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 検索する要素の範囲

  -  例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されるなど、*ランダムアクセスイテレータ*　でなければなりません。 

  - 有効範囲、つまり、 ``last >= first``　を表さなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``: 探索するビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace``　またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

戻り値
~~~~~~~~~~~~

- (1,2,5): 何の要素も見つからない場合、``value``　または ``last`` に等しい最初の要素を指している　``InputIterator`` インスタンス

- (3,4,6):  何の要素も見つからない場合、``value``　または　``Kokkos::Experimental::end(view)``　に等し最初の要素へのイテレータ


例
-------

.. code-block:: cpp

   名前空間 KE = Kokkos::Experimental;
   自動 exespace = Kokkos::DefaultExecutionSpace;
   view_type = Kokkos::View<exespace, int*>　を使用;
   view_type a("a", 15);
   // 何らかの方法で、 "a" を満たす

   自動 exespace = Kokkos::DefaultExecutionSpace;
   自動 it1 = KE::find(exespace, KE::cbegin(a), KE::cend(a), 5);

   // OpenMPが有効化されており、 "a" がホストからアクセス可能であると仮定すれば、以下も可能です。
   自動 it2 = KE::find(Kokkos::OpenMP(), KE::begin(a), KE::end(a), 5);
