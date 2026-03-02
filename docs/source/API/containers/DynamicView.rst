
.. role:: cpp(code)
    :language: cpp

``DynamicView``
===============

ヘッダーファイル: ``<Kokkos_DynamicView.hpp>``


ディスクリプション
-----------

.. cpp:class:: template<typename DataType , typename ... P> DynamicView : public Kokkos::ViewTraits<DataType , P ...>

    ホスト上で動的にサイズ変更可能であり、レイアウトを持たない、参照カウント可能なランク1配列。

    .. rubric:: パブリックメンバー変数

    .. cpp:member:: 静的 constexpr ブール reference_type_is_lvalue_reference

       レファレンス型が、 C++ lvalueレファレンスかどうか。

    .. rubric:: パブリックネスティッド型定義

    .. cpp:type:: Kokkos::ViewTraits< DataType , P ... > 特性

        ``Kokkos::ViewTraits`` 親クラス型。

    .. cpp:type:: array_type

        　``traits::data_type`` および ``traits::device_type``　上にテンプレートされた ``DynamicView`` 型。

    .. cpp:type:: const_type

        　``traits::const_data_type`` および ``traits::device_type``　上にテンプレートされた ``DynamicView`` 型。

    .. cpp:type:: non_const_type

        　``traits::non_const_data_type`` および ``traits::device_type``　上にテンプレートされた ``DynamicView`` 型。

    .. cpp:type:: HostMirror

        ホストアクセス可能メモリ空間に格納された、同一の　``DataType``　および　``LayoutType``　を持つ互換性のあるビュータイプ。

    .. rubric:: パブリックデータハンドル型

    .. cpp:type:: reference_type

        ビューアクセス演算子の戻り値型。

    .. cpp:type:: pointer_type

        スカラー型へのポインタ。

    .. rubric:: コンストラクタ

    .. cpp:function:: DynamicView()

        デフォルトコンストラクタ。割り当ては行われず、参照カウントも発生しません。 すべてのエクステントはゼロであり、そのデータポインタは　NULL　です。

    .. cpp:function:: DynamicView(const DynamicView<RT, RP...>& rhs)

        互換性のある　View　からのコピーコンストラクタ。View　代入ルールに従ってください。

    .. cpp:function:: DynamicView(DynamicView&& rhs)

        移動コンストラクタ。

    .. cpp:function:: DynamicView(const std::string & arg_label, \
			    const unsigned min_chunk_size,  \
			    const unsigned max_extent)

        標準割り当てコンストラクタ。

        :param arg_label: a user-provided label, which is used for profiling and debugging purposes. Names are not required to be unique.
        :param min_chunk_size: a user-provided minimum chunk size needed for memory allocation, will be raised to nearest power-of-two for more efficient memory access operations.
        :param max_extent: a user-provided maximum size, required to allocate a chunk-pointer array.

        The ``resize_serial`` method must be called after construction to reserve the desired amount of memory, bound by ``max_extent``.

    .. rubric:: Public Data Access Functions

    .. cpp:function:: KOKKOS_INLINE_FUNCTION reference_type operator() (const I0 & i0 , const Args & ... args) const

        :return: A value of ``reference_type`` which may or not be referenceable itself. The number of index arguments must be 1 (for non-deprecated code).

    .. rubric:: Data Resizing, Dimensions, Strides


    .. cpp:function:: template< typename IntType > inline void resize_serial(IntType const & n)

       Resizes the DynamicView with sufficient chunks of memory of ``chunk_size`` to store the requested number of elements ``n``.
       This method can only be called outside of parallel regions.
       ``n`` is restricted to be smaller than the ``max_extent`` value passed to the DynamicView constructor.
       This method must be called after the construction of the DynamicView as the constructor
       sets the requested sizes for ``chunk_size`` and ``max_extent``, but does not take input for the actual amount of memory to be used.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION size_t allocation_extent() const noexcept;

        :return: The total size of the product of the number of chunks multiplied by the chunk size. This may be larger than ``size`` as this includes the total size for the total number of complete chunks of memory.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION size_t chunk_size() const noexcept;

        :return: The number of entries a chunk of memory may store, always a power of two.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION size_t size() const noexcept;

        :return: The number of entries available in the allocation based on the number passed to ``resize_serial``. This number is bound by ``allocation_extent``.

    .. cpp:function:: template< typename iType > KOKKOS_INLINE_FUNCTION size_t extent(const iType& dim) const;

        :return: The extent of the specified dimension. ``iType`` must be an integral type, and ``dim`` must be smaller than ``rank``. Returns 1 for rank > 1.

    .. cpp:function:: template< typename iType > KOKKOS_INLINE_FUNCTION int extent_int(const iType& dim) const;

        :return: The extent of the specified dimension as an ``int``. ``iType`` must be an integral type, and ``dim`` must be smaller than ``rank``. Compared to ``extent`` this function can be useful on architectures where ``int`` operations are more efficient than ``size_t``. It also may eliminate the need for type casts in applications that otherwise perform all index operations with ``int``. Returns 1 for rank > 1.

    .. cpp:function:: template< typename iType > KOKKOS_INLINE_FUNCTION void stride(const iType& dim) const;

        :return: The stride of the specified dimension, always returns 0 for ``DynamicView``.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_0() const;

        :return: The stride of dimension 0, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_1() const;

        :return: The stride of dimension 1, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_2() const;

        :return: The stride of dimension 2, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_3() const;

        :return: The stride of dimension 3, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_4() const;

        :return: The stride of dimension 4, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_5() const;

        :return: The stride of dimension 5, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_6() const;

        :return: The stride of dimension 6, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t stride_7() const;

        :return: The stride of dimension 7, always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr size_t span() const;

        :return: Always returns 0 for ``DynamicView`` s.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr pointer_type data() const;

        :return: The pointer to the underlying data allocation.

    .. cpp:function:: KOKKOS_INLINE_FUNCTION constexpr bool span_is_contiguous() const;

        :return: The span is contiguous, always false for ``DynamicView`` s.

    .. rubric:: Other

    .. cpp:function:: KOKKOS_INLINE_FUNCTION int use_count() const;

        :return: The current reference count of the underlying allocation.

    .. cpp:function:: inline const std::string label();

        :return: The label of the ``DynamicView``.

    .. cpp:function:: bool is_allocated() const

        :return: True if the View points to a valid set of allocated memory chunks. Note that this will return false until resize_serial is called with a size greater than 0.


Example
-------

.. code-block:: cpp

   const int chunk_size = 16*1024;
   Kokkos::Experimental::DynamicView<double*> view("v", chunk_size, 10*chunk_size);
   view.resize_serial(3*chunk_size);
   Kokkos::parallel_for("InitializeData", 3*chunk_size, KOKKOS_LAMBDA ( const int i) {
     view(i) = i;
   });
