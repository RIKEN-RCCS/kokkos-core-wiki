
``find_if``
===========

ヘッダー: ``<Kokkos_StdAlgorithms.hpp>``

ディスクリプション
-----------

範囲内の　*最初*　の要素、またはカスタム述語を満たす　``ビュー``　へのイテレータを返します。

インターフェイス
---------

.. :: これは、現在 ``Kokkos::Experimental`` 名前空間内部にあります。

実行空間を受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   InputIterator find_if(const ExecutionSpace& exespace,                                (1)
			 InputIterator first, InputIterator last,
			 PredicateType pred);

   テンプレート <class ExecutionSpace, class InputIterator, class PredicateType>
   InputIterator find_if(const std::string& label, const ExecutionSpace& exespace,      (2)
			 InputIterator first, InputIterator last,
			 PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 find_if(const ExecutionSpace& exespace,
		const Kokkos::View<DataType, Properties...>& view,                      (3)
		PredicateType pred);

   テンプレート <class ExecutionSpace, class DataType, class... Properties, class PredicateType>
   自動 find_if(const std::string& label, const ExecutionSpace& exespace,
		const Kokkos::View<DataType, Properties...>& view,                      (4)
		PredicateType pred);

チームハンドルを受け入れるオーバーロードセット
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.2

.. code-block:: cpp

   テンプレート <class TeamHandleType, class InputIterator, class PredicateType>
   KOKKOS_FUNCTION
   InputIterator find_if(const TeamHandleType& teamHandle,                              (5)
			 InputIterator first, InputIterator last,
			 PredicateType pred);

   テンプレート <class TeamHandleType, class DataType, class... Properties, class PredicateType>
   KOKKOS_FUNCTION
   自動 find_if(const TeamHandleType& teamHandle,
		const Kokkos::View<DataType, Properties...>& view,                      (6)
		PredicateType pred);


パラメータおよび要件
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``exespace``: 実行空間インスタンス

- ``teamHandle``: TeamPolicyを使用する際、並列領域内で指定されたチームハンドルインスタンス

- ``ラベル``: デバッグ目的で内部の並列カーネルに転送された文字列

  - 1　について、デフォルト文字列は、: "Kokkos::find_if_iterator_api_default"

  - 3　について、デフォルト文字列は、 the default string is: "Kokkos::find_if_view_api_default"

  - NOTE: overloads accepting a team handle do not use a label internally

- ``first, last``: range of elements to search in

  - must be *random access iterators*, e.g., returned from ``Kokkos::Experimental::(c)begin/(c)end``

  - must represent a valid range, i.e., ``last >= first``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``view``: view to search in

  - must be rank-1, and have ``LayoutLeft``, ``LayoutRight``, or ``LayoutStride``

  - must be accessible from ``exespace`` or from the execution space associated with the team handle

- ``pred``: unary predicate which returns ``true`` for the required element;

  ``pred(a)`` must be valid to be called from the execution space passed, or
  the execution space associated with the team handle, and convertible to bool for every
  argument ``a`` of type (possible const) ``value_type``, where ``value_type`` is the value
  type of ``InputIterator`` or ``view``, and must not modify ``a``.

  - must conform to:

    .. code-block:: cpp

       struct Predicate
       {
	  KOKKOS_INLINE_FUNCTION
	  bool operator()(const /*type needed */ & operand) const { return /* ... */; }

	  // or, also valid

	  KOKKOS_INLINE_FUNCTION
	  bool operator()(/*type needed */ operand) const { return /* ... */; }
       };

Return Value
~~~~~~~~~~~~

- (1,2,5): ``InputIterator`` instance pointing to the first element
  where the predicate evaluates to true, or ``last`` if no such element is found

- (3,4,6): iterator to the first element where the predicate evaluates to ``true``,
  or ``Kokkos::Experimental::end(view)`` if no such element is found

Example
-------

.. code-block:: cpp

   namespace KE = Kokkos::Experimental;

   template<class ValueType>
   struct EqualsValue
   {
     const ValueType m_value;
     EqualsValFunctor(ValueType value) : m_value(value){}

     KOKKOS_INLINE_FUNCTION
     bool operator()(const ValueType & operand) const {
       return operand == m_value;
     }
   };

   auto exespace = Kokkos::DefaultExecutionSpace;
   using view_type = Kokkos::View<exespace, int*>;
   view_type a("a", 15);
   // fill "a" somehow

   // create predicate
   EqualsValue<int> p(5);

   auto it1 = KE::find_if(exespace, KE::begin(a), KE::end(a), p);

   // assuming OpenMP is enabled, then you can also explicitly call
   auto it2 = KE::find_if(Kokkos::OpenMP(), KE::begin(a), KE::end(a), p);
