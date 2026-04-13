
``generate_n``
==============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

ファンクタ ``g`` によって生成された値を、``count`` イテレータの範囲、またはランク 1 の ``View`` の最初の ``count`` の要素それぞれを割り当てます。

インターフェイス
---------

.. warning: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。


実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType, class Size, class Generator>
   IteratorType generate_n(const ExecutionSpace& exespace,                           (1)
                           IteratorType first, Size count,
                           Generator g);

   template <class ExecutionSpace, class IteratorType, class Size, class Generator>
   IteratorType generate_n(const std::string& label, const ExecutionSpace& exespace, (2)
                           IteratorType first, Size count,
                           Generator g);

   template <class ExecutionSpace, class DataType, class... Properties, class Size,
             class Generator>
   auto generate_n(const ExecutionSpace& exespace,                                   (3)
                   const ::Kokkos::View<DataType, Properties...>& view, Size count,
                   Generator g);

   template <class ExecutionSpace, class DataType, class... Properties, class Size,
             class Generator>
   auto generate_n(const std::string& label, const ExecutionSpace& ex,               (4)
                   const ::Kokkos::View<DataType, Properties...>& view, Size count,
                   Generator g);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType, class Size, class Generator>
   KOKKOS_FUNCTION
   IteratorType generate_n(const TeamHandleType& teamHandle,                         (5)
                           IteratorType first, Size count,
                           Generator g);

   template <class TeamHandleType, class DataType, class... Properties, class Size,
             class Generator>
   KOKKOS_FUNCTION
   auto generate_n(const TeamHandleType& teamHandle,                                 (6)
                   const ::Kokkos::View<DataType, Properties...>& view, Size count,
                   Generator g);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``label``: デバッグ目的で内部並列カーネルに転送される文字列

  - 1 について、デフォルト文字列は、: "Kokkos::generate_n_iterator_api_default"

  - 3 について、デフォルト文字列は、: "Kokkos::generate_n_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。

- ``count``: 割り当てる要素数 （0 以上でなければなりません）

- ``first``: 範囲の始めを定義するイテレータ

  - *ランダムアクセスイテレータ* でなければなりません。

  - ``[first, first+count)`` は、有効な範囲を表さなければなりません

  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``view``:

  - 必ずランク1であり、``LayoutLeft`` 、  ``LayoutRight`` 、または ``LayoutStride`` を持たなければなりません。


  - 必ず ``exespace`` またはチームハンドルに関連付けられた実行空間からアクセス可能である必要があります。

- ``g``: すべての要素上で呼び出される関数オブジェクト

  - 以下の形式のファンクタであり、, ここで、 (1,2,5 について) または、 ``view`` (3,4,6 について) の ``IteratorType`` の値型である、 ``value_type`` を使って、 ``return_type`` は、``value_type`` に割り当て可能でなければなりません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

     struct Generate
     {
        KOKKOS_INLINE_FUNCTION
        return_type operator()() const{ return /* ... */; }
     };

戻り値
~~~~~~~~~~~~

- 1,2,5:  ``first + count`` に等しいイテレータ

- 3,4,6:  ``Kokkos::Experimental::begin(view) + count`` に等しいイテレータ
