``MemoryTraits``
================

:cpp:struct:`MemoryTraits` は、 :cpp:class:`View` の最後のテンプレートパラメータです。

使い方
------

.. code-block:: cpp

   using DefaultMT = Kokkos::MemoryTraits<>;
   using UnmanagedMT = Kokkos::MemoryTraits<Kokkos::Unmanaged>;
   using AtomicRandomAccessMT =
       Kokkos::MemoryTraits<Kokkos::Atomic | Kokkos::RandomAccess>;

構造体インターフェイス
----------------------

.. cpp:struct:: template <unsigned N> MemoryTraits

  多次元ビューに提供された場合、 ``MemoryTraits`` は、割り当て処理に関する追加情報を渡すことを許可します。 テンプレート引数は、下記の列挙型値のビット単位の論理和であることが想定されます。

  .. versionchanged:: 4.7
    テンプレートパラメータ ``N`` のデフォルト値として ``0`` が追加されました。

    .. code-block:: cpp

      template <unsigned N = 0>
      struct MemoryTraits;

.. rubric:: ネストされた型

.. cpp:type::  memory_traits

  ``N`` で示されるメモリアクセス特性（複数可）を表すタグタイプ。

.. rubric:: メンバー変数

.. cpp:member::  static constexpr bool is_unmanaged

  管理対象外トレイトが有効かどうかを示すブール値

.. cpp:member::  static constexpr bool is_random_access

  RandomAccessトレイトが有効かどうかを示すブール値。

.. cpp:member::  static constexpr bool is_atomic

  アトミックトレイトが有効かどうかを示すブール値。

.. cpp:member::  static constexpr bool is_restrict

  制約トレイトが有効かどうかを示すブール値。

.. cpp:member::  static constexpr bool is_aligned

  整列トレイトが有効かどうかを示すブール値。

.. _MemoryAccessTraits: ../../../ProgrammingGuide/View.html#memory-access-traits

.. |MemoryAccessTraits| replace:: メモリアクセストレイト

.. _UnmanagedViews: ../../../ProgrammingGuide/View.html#unmanaged-views

.. |UnmanagedViews| replace:: 管理対象外ビュー

非メンバー列挙型
^^^^^^^^^^^^^^^^

以下の列挙値は、メモリアクセス特性指定に使用されます。これらの特性が実際にどのように使用できるかについての詳細については、プログラミングガイドの |MemoryAccessTraits|_ のサブセクションを確認してください。

.. cpp:enum:: MemoryTraitsFlags

この列挙型では、以下の列挙値が定義されています。

.. cpp:enumerator:: Unmanaged

  この特性は、 Kokkos がこのような View に対して参照カウントも自動解放も行わないことを意味します。 この特性は、任意のメモリ空間に割り当てられたメモリに関連付けることができます。例えば、 *非管理ビュー* は、割り当てられたメモリの生ポインタをラップすることで作成でき、同時に実行領域またはメモリ空間を適切に指定することもできます。

.. cpp:enumerator:: RandomAccess

 不規則にアクセスされるビュー（例：非順次アクセス）は、ランダムアクセスとして宣言できます。

.. cpp:enumerator:: Atomic

  このようなビューでは、あらゆる要素へのアクセス（読み取りまたは書き込み）はすべてアトミックです。

.. cpp:enumerator:: Restrict

  本特性は、このビューのメモリが現在のスコープ内の他のデータ構造の別名ではない/重複していないことを示します。

.. cpp:enumerator:: Aligned

  本特性は、この ``View`` におけるメモリ割り当てが、64バイト単位でアラインメントされていることをコンパイラに追加で通知します。

非メンバー型エイリアス
^^^^^^^^^^^^^^^^^^^^^^

以下の型エイリアスも、 ``Kokkos`` 名前空間で利用可能です。

.. cpp:type:: MemoryManaged = MemoryTraits<0>;

  .. deprecated:: 4.7
    
    ``MemoryManaged`` エイリアスは非推奨です。代わりに ``MemoryTraits<>`` を使用してください。以前のバージョンのKokkosでは、明示的な ``0`` テンプレート引数が必要であることに注意してください。

     
.. cpp:type:: MemoryUnmanaged = MemoryTraits<Unmanaged>;
.. cpp:type:: MemoryRandomAccess = MemoryTraits<Unmanaged | RandomAccess>;

  .. versionchanged:: 4.7
    ``MemoryRandomAccess`` は ``MemoryTraits<RandomAccess>`` に変更され、 ``Unmanaged`` を暗黙的に含まなくなりました。

例
^^

.. code-block:: cpp

   Kokkos::View<DayaType,
                LayoutType,
                MemorySpace,
                Kokkos::MemoryTraits<SomeFlag | SomeOtherFlag>> my_view;
