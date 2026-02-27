
``copy_if``
===========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

ソース範囲またはビューから、述語が ``真`` を返す要素を
別の範囲または ``ビュー``にコピーします。

インターフェイス
---------

.. 警告:: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

  テンプレート <
    クラス ExecutionSpace, class InputIteratorType,
    クラス OutputIteratorType, class UnaryPredicateType>
  OutputIteratorType copy_if(const ExecutionSpace& exespace,                   (1)
                             InputIteratorType first_from,
                             InputIteratorType last_from,
                             OutputIteratorType first_to,
                             UnaryPredicateType pred);

  テンプレート <
    クラス ExecutionSpace, class InputIteratorType,
    クラス OutputIteratorType, class UnaryPredicateType>
  OutputIteratorType copy_if(const std::string& label,
                             const ExecutionSpace& exespace,                   (2)
                             InputIteratorType first_from,
                             InputIteratorType last_from,
                             OutputIteratorType first_to,
                             UnaryPredicateType pred);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス UnaryPredicateType
  >
  自動 copy_if(const ExecutionSpace& exespace,                                 (3)
               const Kokkos::View<DataType1, Properties1...>& view_from,
               const Kokkos::View<DataType2, Properties2...>& view_to,
               UnaryPredicateType pred);

  テンプレート <
    クラス ExecutionSpace,
    クラス DataType1, class... Properties1,
    クラス DataType2, class... Properties2,
    クラス UnaryPredicateType
  >
  自動 copy_if(const std::string& label, const ExecutionSpace& exespace,       (4)
               const Kokkos::View<DataType1, Properties1...>& view_from,
               const Kokkos::View<DataType2, Properties2...>& view_to,
               UnaryPredicateType pred);


チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

  テンプレート <
    クラス TeamHandleType, class InputIteratorType,
    クラス OutputIteratorType, class UnaryPredicateType>
  KOKKOS_FUNCTION
  OutputIteratorType copy_if(const TeamHandleType& teamHandle,                 (5)
                             InputIteratorType first_from,
                             InputIteratorType last_from,
                             OutputIteratorType first_to,
                             UnaryPredicateType pred);

  template <
    class TeamHandleType,
    class DataType1, class... Properties1,
    class DataType2, class... Properties2,
    class UnaryPredicateType>
  KOKKOS_FUNCTION
  auto copy_if(const TeamHandleType& teamHandle,                              (6)
               const Kokkos::View<DataType1, Properties1...>& view_from,
               const Kokkos::View<DataType2, Properties2...>& view_to,
               UnaryPredicateType pred);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |copy| 置換:: ``copy``
.. _copy: ./StdCopy.html

- ``exespace``, ``teamHandle``, ``first_from``, ``last_from``, ``first_to``, ``view_from``, ``view_to``: same as in |copy|_におけるのと同様

- ``ラベル``:

  - 1　について、デフォルト文字列は、: "Kokkos::copy_if_iterator_api_default"

  - 3　について、デフォルト文字列は、: "Kokkos::copy_if_view_api_default"

- ``pred``:コピー対象の必須要素について ``真`` を返す一項述語

  - ``pred(v)``  は、引数として渡された実行空間から呼び出されるためには、有効でなければならない、またはチームハンドルに関連付けられた実行空間でなければならず、そして 型　value_type　の引数　``v``　（constの可能性）のすべてのペアについて、bool型に変換可能で、そこでは、``value_type``が、``InputIteratorType``　の値型、または ``view_from``であり、  ``v``　を変更してはいけません。

  - 以下に一致しなければなりません:

  .. code-block:: cpp

   構造体　述語
   {
      KOKKOS_INLINE_FUNCTION
      ブール operator()(const value_type & v) const { return /* ... */; }

      // または、また有効

      KOKKOS_INLINE_FUNCTION
      ブール operator()(value_type v) const { return /* ... */; }
   };


返し値
~~~~~~~~~~~~

最後の要素がコピーされた *後*　の宛先へのイテレータ。

