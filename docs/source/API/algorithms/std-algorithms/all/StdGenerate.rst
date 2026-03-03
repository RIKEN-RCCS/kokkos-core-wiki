
``generate``
============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

ファンクタ ``g`` によって生成された値を、範囲 ``[first, last)``　内の各要素（オーバーロード 1,2,5）または ``ビュー``　内の各要素（オーバーロード 3,4,6）に割り当てます。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

  テンプレート <class ExecutionSpace, class IteratorType, class GeneratorType>
  void generate(const ExecutionSpace& exespace,                                (1)
                IteratorType first, IteratorType last,
                GeneratorType g);

  テンプレート <class ExecutionSpace, class IteratorType, class GeneratorType>
  void generate(const std::string& label, const ExecutionSpace& exespace,      (2)
                IteratorType first, IteratorType last,
                GeneratorType g);

  テンプレート <class ExecutionSpace, class DataType, class... Properties, class GeneratorType>
  void generate(const ExecutionSpace& exespace,                                (3)
                const Kokkos::View<DataType, Properties...>& view,
                GeneratorType g);

  テンプレート <class ExecutionSpace, class DataType, class... Properties, class GeneratorType>
  void generate(const std::string& label, const ExecutionSpace& exespace,      (4)
                const Kokkos::View<DataType, Properties...>& view,
                GeneratorType g);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

  テンプレート <class TeamHandleType, class IteratorType, class GeneratorType>
  KOKKOS_FUNCTION
  void generate(const TeamHandleType& teamHandle,                              (5)
                IteratorType first, IteratorType last,
                GeneratorType g);

  テンプレート <class TeamHandleType, class DataType, class... Properties, class GeneratorType>
  KOKKOS_FUNCTION
  void generate(const TeamHandleType& teamHandle,                              (6)
                const Kokkos::View<DataType, Properties...>& view,
                GeneratorType g);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で実装カーネルに名付けるために使用

  - 1　について、デフォルト文字列は、 : "Kokkos::generate_iterator_api_default"

  - 3　について、デフォルト文字列は、 : "Kokkos::generate_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 変更するための要素数

　- *ランダムアクセスイテレータ*　でなければなりません。

  - 有効な範囲、つまり、 ``last >= first``　を表す必要があります。　（デバッグモードで確認済み）

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``: 変更するためのビュー

  - 必ずランク-1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``g``:

  - 以下の形式のファンクタであり、ここで　``return_type`` は　``value_type``に代入可能である必要があり、 ``value_type`` としては、 ``IteratorType`` または ``view``　の値の型を使用します。:

  .. code-block:: cpp

     構造体 Generate
     {
	 KOKKOS_INLINE_FUNCTION
	 return_type operator()() const{ return /* ... */; }
     };


戻り値
~~~~~~~~~~~~

無し
