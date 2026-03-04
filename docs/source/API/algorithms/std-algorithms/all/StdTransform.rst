
``transform``
=============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

- オーバーロード (1,2,9): 指定された *一項* 演算子を範囲 ``[first_from, last_from)`` 内の全要素に適用し、結果を ``first_to`` から始まる範囲に格納します。

- オーバーロード (3,4,10): 指定された *一項* 演算を ``source`` ビュー内の全要素に適用し、結果を ``dest`` ビューに格納します。

- オーバーロード (5,6,11): 指定された　*二項* 演算を、範囲 ``[first_from1, last_from1)`` および ``[first_from2, last_from2]`` から取得した要素のペアに対して適用し、結果を ``first_to`` から始まる範囲に格納します。

- オーバーロード (7,8,12): 指定された　*二項* 演算を、ビュー ``source1, source2`` から取得した要素のペアに対して適用し、結果を ``dest`` ビューに格納します。


インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

  テンプレート <
    クラス ExecutionSpace, class InputIterator,
    クラス OutputIterator, class UnaryOperation>
  OutputIterator transform(const ExecutionSpace& exespace,                        (1)
                           InputIterator first_from, InputIterator last_from,
                           OutputIterator first_to,
                           UnaryOperation unary_op);

  テンプレート <
    クラス ExecutionSpace, class InputIterator,
    クラス OutputIterator, class UnaryOperation>
  OutputIterator transform(const std::string& label,                              (2)
                           const ExecutionSpace& exespace,
                           InputIterator first_from, InputIterator last_from,
                           OutputIterator first_to,
                           UnaryOperation unary_op);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス UnaryOperation
  >
  自動 transform(const ExecutionSpace& exespace,                                  (3)
                 const Kokkos::View<DataType1, Properties1...>& source,
                 Kokkos::View<DataType2, Properties2...>& dest,
                 UnaryOperation unary_op);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス UnaryOperation
  >
  自動 transform(const std::string& label, const ExecutionSpace& exespace,        (4)
                 const Kokkos::View<DataType1, Properties1...>& source,
                 Kokkos::View<DataType2, Properties2...>& dest,
                 UnaryOperation unary_op);

  テンプレート <
    クラス ExecutionSpace,
    クラス InputIterator1, class InputIterator2, class OutputIterator,
    クラス BinaryOperation
  >
  OutputIterator transform(const ExecutionSpace& exespace,                        (5)
                           InputIterator1 first_from1, InputIterator1 last_from1,
                           InputIterator2 first_from2, OutputIterator first_to,
                           BinaryOperation binary_op);

  テンプレート <
    クラス ExecutionSpace,
    クラス InputIterator1, class InputIterator2, class OutputIterator,
    クラス BinaryOperation
  >
  OutputIterator transform(const std::string& label,                              (6)
                           const ExecutionSpace& exespace,
                           InputIterator1 first_from1, InputIterator1 last_from1,
                           InputIterator2 first_from2, OutputIterator first_to,
                           BinaryOperation binary_op);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス DataType3, class... Properties3,
    クラス BinaryOperation
  >
  自動 transform(const ExecutionSpace& exespace,                                  (7)
                 const Kokkos::View<DataType1, Properties1...>& source1,
                 const Kokkos::View<DataType2, Properties2...>& source2,
                 Kokkos::View<DataType3, Properties3...>& dest,
                 BinaryOperation binary_op);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス DataType3, class... Properties3,
    クラス BinaryOperation
  >
  自動 transform(const std::string& label, const ExecutionSpace& exespace,        (8)
                 const Kokkos::View<DataType1, Properties1...>& source1,
                 const Kokkos::View<DataType2, Properties2...>& source2,
                 Kokkos::View<DataType3, Properties3...>& dest,
                 BinaryOperation binary_op);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

  テンプレート <
    クラス TeamHandleType, class InputIterator,
    クラス OutputIterator, class UnaryOperation>
  KOKKOS_FUNCTION
  OutputIterator transform(const TeamHandleType& teamHandle,                      (9)
                           InputIterator first_from,
                           InputIterator last_from,
			   OutputIterator first_to,
                           UnaryOperation unary_op);

  テンプレート <
    class TeamHandleType,
    class DataType1, class... Properties1,
    class DataType2, class... Properties2,
    class UnaryOperation>
  KOKKOS_FUNCTION
  自動 transform(const TeamHandleType& teamHandle,                               (10)
                 const ::Kokkos::View<DataType1, Properties1...>& source,
                 ::Kokkos::View<DataType2, Properties2...>& dest,
		 UnaryOperation unary_op);

  テンプレート <
    クラス TeamHandleType, class InputIterator1,
    クラス InputIterator2, class OutputIterator,
    クラス BinaryOperation>
  KOKKOS_FUNCTION
  OutputIterator transform(const TeamHandleType& teamHandle,                     (11)
                           InputIterator1 first_from1,
			   InputIterator1 last_from1,
                           InputIterator2 first_from2,
			   OutputIterator first_to,
                           BinaryOperation binary_op);

  テンプレート <
    クラス TeamHandleType,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス DataType3, class... Properties3,
    クラス BinaryOperation>
  KOKKOS_FUNCTION
  自動 transform(const TeamHandleType& teamHandle,                               (12)
                 const ::Kokkos::View<DataType1, Properties1...>& source1,
                 const ::Kokkos::View<DataType2, Properties2...>& source2,
                 ::Kokkos::View<DataType3, Properties3...>& dest,
                 BinaryOperation binary_op);

メータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で実装カーネルに名付けるために使用。

  - 1,3,5,7　について、デフォルト文字列は、: "Kokkos::transform_iterator_api_default"

  - 2,4,6,8, について、デフォルト文字列は、: "Kokkos::transform_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first_from, last_from, first_from1, first_from2``: 変換対象の要素の範囲

  - 　*ランダムアクセスイテレータ*　でなければなりません。

  -  有効な範囲、つまり、 ``first_from >= last_from``, ``first_from1 >= last_from2``　を表す必要があります。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``first_to``: 書き込み先の範囲の先頭

  - 　*ランダムアクセスイテレータ*　でなければなりません。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``source, source1, source2, dest``: ソースおよび宛先のビュー

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。


戻り値
~~~~~~~~~~~~

変換された最後の *後の* 要素へのイテレータ
