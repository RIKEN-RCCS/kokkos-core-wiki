
``reverse``
===========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲またはランク1の ``View``　内にある要素の順序を逆にします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class InputIterator>
   void reverse(const ExecutionSpace& ex, InputIterator first, InputIterator last);  (1)

   テンプレート <class ExecutionSpace, class InputIterator>
   void reverse(const std::string& label, const ExecutionSpace& ex,                  (2)
                InputIterator first, InputIterator last);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   void reverse(const ExecutionSpace& ex,                                            (3)
                const ::Kokkos::View<DataType, Properties...>& view);

   テンプレート <class ExecutionSpace, class DataType, class... Properties>
   void reverse(const std::string& label, const ExecutionSpace& ex,                  (4)
                const ::Kokkos::View<DataType, Properties...>& view);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class InputIterator>
   KOKKOS_FUNCTION
   void reverse(const TeamHandleType& teamHandle, InputIterator first,               (5)
                InputIterator last);

   テンプレート <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   void reverse(const TeamHandleType& teamHandle,                                    (6)
                const ::Kokkos::View<DataType, Properties...>& view);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1 について、デフォルト文字列は、: "Kokkos::reverse_iterator_api_default"

  - 3 について、デフォルト文字列は、: "Kokkos::reverse_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``first, last``: 逆にする要素の範囲

  - *ランダムアクセスイテレータ*　である必要があり、例えば、 ``Kokkos::Experimental::(c)begin/(c)end``　から返されなければなりません。

  - 有効な範囲、つまり、 ``last >= first``　を表す必要があります。

  - 必ず　`exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``:

  - 必ずランク1であり、``LayoutLeft``　、  ``LayoutRight``　、または ``LayoutStride``　を持たなければなりません。

  - 必ず　``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

戻り値
~~~~~~~~~~~~

無し
