``shift_right``
===============

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

説明
------------------

 終りに向けて、 ``n`` 位置により、範囲または ``view`` 内において、要素をシフトします。

インターフェイス
----------------

.. warning:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   template <class ExecutionSpace, class IteratorType>
   IteratorType shift_right(const ExecutionSpace& exespace,                  (1)
                            IteratorType first, IteratorType last,
                            typename IteratorType::difference_type n);

   template <class ExecutionSpace, class IteratorType>
   IteratorType shift_right(const std::string& label,                        (2)
                            const ExecutionSpace& exespace,
                            IteratorType first, IteratorType last,
                            typename IteratorType::difference_type n);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto shift_right(const ExecutionSpace& exespace,                          (3)
                    const Kokkos::View<DataType, Properties...>& view,
                    typename decltype(begin(view))::difference_type n);

   template <class ExecutionSpace, class DataType, class... Properties>
   auto shift_right(const std::string& label,                                (4)
                    const ExecutionSpace& exespace,
                    const Kokkos::View<DataType, Properties...>& view,
                    typename decltype(begin(view))::difference_type n);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   template <class TeamHandleType, class IteratorType>
   KOKKOS_FUNCTION
   IteratorType shift_right(const TeamHandleType& teamHandle,                (5)
                            IteratorType first, IteratorType last,
                            typename IteratorType::difference_type n);

   template <class TeamHandleType, class DataType, class... Properties>
   KOKKOS_FUNCTION
   auto shift_right(const TeamHandleType& teamHandle,                        (6)
                    const Kokkos::View<DataType, Properties...>& view,
                    typename decltype(begin(view))::difference_type n);

パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |ShiftLeft| replace:: ``shift_left``
.. _ShiftLeft: ./StdShiftLeft.html

- ``exespace`` ``teamHandle``, ``first``, ``last``, ``view``:  |ShiftLeft|_ と同様。

- ``label``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1: デフォルト文字列は、 "Kokkos::shift_right_iterator_api_default"

  - 3: デフォルト文字列は、 "Kokkos::shift_right_view_api_default"

  - 注意事項: チームハンドルを受け取るオーバーロードは、内部でラベルを使用しません。


- ``n``: シフトする位置の数

  - 0以上でなければなりません。

戻り値
~~~~~~~~~~~~

結果の範囲の始め。 ``n`` が  ``last - first`` よりも小さい場合には、 ``first + n`` を返します。 そうでなければ ``last`` を返します。

