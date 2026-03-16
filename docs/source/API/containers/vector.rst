
.. ロール:: cpp(code)
    :language: cpp

``vector`` [非推奨]
=======================

ヘッダーファイル: ``<Kokkos_Vector.hpp>`` ( Kokkos 4.3において非推奨)

Kokkos Vector　は意味的に　std::vector　に似ていますが、異なるメモリ空間を持つデバイスで作業する際のメモリ割り当てやコピーの問題を克服するよう設計されています。  ``Kokkos::Vector`` は、std::vector と同じインターフェースを実装したランク1の　DualView　です。 これにより、std::vector　に大きく依存するプログラムでも、ホスト以外の実行空間内からプログラムデータへアクセス可能です。 多くの　std::vector　互換関数はホスト専用であるため、カーネルの複雑さによってアクセスが制限される場合があります。 以下はクラスの概要であり、各メソッドの説明にはホスト、デバイス、または両方でサポートされているかどうかが明記されています

使用例
-----

.. code-block:: cpp

    Kokkos::vector<Scalar, Device> v(n,1);  // (バージョン 4.3以降非推奨)
    v.push_back(2);
    v.resize(n+3)
    v.[n+1] = 3;
    v.[n+2] = 4;

ディスクリプション
-----------

.. cpp:class:: template<class Scalar, class Arg1Type = void> vector :  public DualView<Scalar*, LayoutLeft, Arg1Type>

   .. rubric:: パブリック型定義

   .. cpp:type:: Scalar value_type;

      スカラー値型。

   .. cpp:type:: Scalar* pointer;

      スカラーポインタ型。

   .. cpp:type:: const Scalar* const_pointer;

      定数スカラー参照型。

   .. cpp:type:: Scalar& reference;

      スカラー参照型。

   .. cpp:type:: const Scalar& const_reference;

      定数スカラー参照型。

   .. cpp:type:: スカラー* イテレータ;

      イテレータ型

   .. cpp:type:: const Scalar* const_iterator;

      定数イテレータ型

   .. rubric:: Accessors

   .. cpp:function:: KOKKOS_INLINE_FUNCTION reference operator()(int i) const;

      アクセサー

      .. 警告:: ホストのみ

   .. cpp:function:: KOKKOS_INLINE_FUNCTION reference operator[](int i) const;

      アクセサー

      .. 警告:: ホストのみ

   .. rubric:: コンストラクタ

   .. cpp:function:: vector();

      空のベクトルを構築します。

   .. cpp:function:: vector(int n, Scalar val = Scalar());

      サイズ n + 10% のベクトルを構築し、 ``val``　に値を初期化します。

   .. rubric:: Other Public Methods

   .. cpp:function:: void resize(size_t n);

      サイズ n + 10%　にベクトルのサイズを変更します。

   .. cpp:function:: void resize(size_t n, const Scalar& val);

      サイズ n + 10%　にベクトルのサイズを変更し、値を ``val``　に設定します。

   .. cpp:function:: void assign(size_t n, const Scalar& val);

      値を ``val`` に設定し、ホストとデバイス間で自動的に同期します。

   .. cpp:function:: void reserve(size_t n);

      サイズ変更と同様です（互換性のため）。

   .. cpp:function:: void push_back(Scalar val);

      ベクトルをsize() + 1　にサイズ変更し、最後の値を  val に設定します。

      .. 警告:: ホストのみ、 デバイスを自動的に同期

   .. cpp:function:: void pop_back();

      size()を　1　削減します。

   .. cpp:function:: void clear();

      Set size() を　0　に設定します。

   .. cpp:function:: size_type size() const;

      ベクトル内の要素数を返します。

   .. cpp:function:: size_type max_size() const;

      可能な限り最大の要素数を返します。

   .. cpp:function:: size_type span() const;

      ベクターが使用したメモリを返します。

   .. cpp:function:: bool empty() const;

　　　ベクトルが空である場合には、真を返します。

   .. cpp:function:: pointer data() const;

      基盤となる配列に、ポインタを返します。

      .. 警告:: ホストのみ

   .. cpp:function:: iterator begin() const;

      先頭から始まるイテレータを返します。

      .. 警告:: ホストのみ

   .. cpp:function:: iterator end() const;

      最後の要素を超えたイテレータを返します。

      .. 警告:: ホストのみ

   .. cpp:function:: reference front();

      リストの先頭への参照を返します。

      .. 警告:: ホストのみ

   .. cpp:function:: reference back();

      リスト内の最後のエレメントに参照を返します。

      .. 警告:: ホストのみ

   .. cpp:function:: const_reference front() const;

      リストの先頭への定数参照を返します。

      .. 警告:: ホストのみ

   .. cpp:function:: const_reference back() const;

      リスト内の最後のエレメントに定数参照を返します。

      .. 警告:: ホストのみ

   .. cpp:function:: size_t lower_bound(const size_t& start, const size_t& theEnd, const Scalar& comp_val) const;

      範囲 start-theEnd 内で val < comp_val を満たす最大値のインデックスを返します。

      .. 警告:: ホストのみ

   .. cpp:function:: bool is_sorted();

      リストがソートされている場合、真を返します。

   .. cpp:function:: iterator find(Scalar val) const;

       ``val``　に一致する要素を指すイテレータを返します。

   .. cpp:function:: void device_to_host();

      デバイスからホストへデータをコピーします。

   .. cpp:function:: void host_to_device() const;

      ホストからデバイスにデータをコピーします。

   .. cpp:function:: void on_host();

      ホスト側の観点からデュアルビューのデータを更新/同期します。

   .. cpp:function:: void on_device();

      デバイス側の観点からデュアルビューのデータを更新/同期します。

   .. cpp:function:: void set_overallocation(float extra);

      ベクトルの末尾に利用可能なデータバッファを設定します。

   .. cpp:function:: constexpr bool is_allocated() const;

      内部ビュー（ホストとデバイス）が割り当てられている場合（NULLでないポインタの場合）、真を返します。
