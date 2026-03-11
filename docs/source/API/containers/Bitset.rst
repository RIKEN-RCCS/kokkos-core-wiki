
.. ロール:: cpp(code)
   :language: cpp

``ビットセット``
==========

ヘッダーファイル: ``<Kokkos_Bitset.hpp>``

クラスインターフェース
---------------

.. cpp:class:: テンプレート <typename Device> ビットセット

  :cpp:`Kokkos::Bitset` は、固定サイズ（実行時）の　N　ビットシーケンスへのスレッドセーフビューを表します。


  :tparam デバイス: ビットを物理的に収容するデバイス。

  .. rubric:: 静的定数

  .. cpp:member:: 静的 constexpr  BIT_SCAN_REVERSE = 1u

    :cpp:`BIT_SCAN_REVERSE` : スキャン方向用ビットマスク

  .. cpp:member:: 静的 constexpr 符号なし MOVE_HINT_BACKWARD = 2u

    :cpp:`MOVE_HINT_BACKWARD` : ヒント方向用ビットマスク

  .. cpp:member:: 静的 constexpr 符号なし BIT_SCAN_FORWARD_MOVE_HINT_FORWARD = 0u

    :cpp:`BIT_SCAN_FORWARD_MOVE_HINT_FORWARD` : :cpp:`find_any_set_near(...)` または :cpp:`find_any_reset_near(...)` の :cpp:`scan_direction` として渡された場合、 前方（インデックスが増加する方向）方向に向けてビットをスキャンします。 ビットが見つからなかった場合、現在のヒントの先にある新しいヒントを選択します。

  .. cpp:member:: 静的 constexpr 符号なし BIT_SCAN_REVERSE_MOVE_HINT_FORWARD = BIT_SCAN_REVERSE

    :cpp:`BIT_SCAN_REVERSE_MOVE_HINT_FORWARD`: :cpp:`find_any_set_near(...)` または :cpp:`find_any_reset_near(...)` の :cpp:`scan_direction` として渡された場合、 逆（減少するインデックス）方向のビットをスキャンします。 ビットが見つからなかった場合、現在のヒントの先にある新しいヒントを選択します。

  .. cpp:member:: 静的 constexpr 符号なし BIT_SCAN_FORWARD_MOVE_HINT_BACKWARD = MOVE_HINT_BACKWARD

    :cpp:`BIT_SCAN_FORWARD_MOVE_HINT_BACKWARD`: :cpp:`find_any_set_near(...)` または :cpp:`find_any_reset_near(...)` に対して :cpp:`scan_direction` として渡された場合、前方（インデックスが増加する方向）方向に向けてビットをスキャンします。

  .. cpp:member:: 静的 constexpr 符号なし BIT_SCAN_REVERSE_MOVE_HINT_BACKWARD = BIT_SCAN_REVERSE | MOVE_HINT_BACKWARD

    :cpp:`BIT_SCAN_REVERSE_MOVE_HINT_BACKWARD`: :cpp:`find_any_set_near(...)` または :cpp:`find_any_reset_near(...)` に対して :cpp:`scan_direction` として渡された場合、逆（減少するインデックス）方向のビットをスキャンします。 ビットが見つからなかった場合、現在のヒントの先にある新しいヒントを選択します。

  .. rubric:: コンストラクタ

  .. cpp:function:: ビットセット(符号なし arg_size = 0u)

    ホスト/デバイス: :cpp:`arg_size` ビットを持つビットセットを構築します。

  .. rubric:: データアクセス関数

  .. cpp:function:: 符号なしsize() const

    ホスト/デバイス: ビット数を返します。

  .. cpp:function:: 符号なし count() const

    ホスト: ``1``　に設定されたビット数を返します。

  .. cpp:function:: void set()

    ホスト:  ``1``　に設定されたビット数を返します。

  .. cpp:function:: void reset();
  .. cpp:function:: void clear();

    ホスト/デバイス:  ``0``　。　すべてのビットを　``0``　に設定します。

  .. cpp:function:: void set(符号なし i)

    デバイス:  ``i``\ 'th ビットを　``1``　に設定します。

  .. cpp:function:: void reset(符号なし i)

    Device: ``i``\ 'th ビットを to ``0``　に設定します。

  .. cpp:function:: ブール テスト(符号なし i) const

    デバイス: return :cpp:　``i``\ 'th が　``1``　に設定されている場合に限り、`真`　となります。

  .. cpp:function:: 符号なし max_hint() const

    ホスト/デバイス:  :cpp:`find_any_set_near(...)` および :cpp:`find_any_reset_near(...)` 関数により使用。

    利用可能なビットを検索する際に、それらの関数を呼び出すべき最大回数を返します。

  .. cpp:function:: Kokkos::pair<bool, unsigned> find_any_set_near(unsigned hint, unsigned scan_direction = BIT_SCAN_FORWARD_MOVE_HINT_FORWARD) const

    ホスト/デバイス: :cpp:`hint` 位置で開始し、 最初のビットが　``1``　に設定されている位置を検出します。

     :cpp:`pair<bool, unsigned>`　を返します。

    :cpp:`result.first` が　:cpp:`true`  の場合、:cpp:`result.second` は検出されたビット位置です。

    :cpp:`result.first` が :cpp:`false` の場合、:cpp:`result.second` は新しいヒント位置です。

    :cpp:`scan_direction & BIT_SCAN_REVERSE`\の場合、ビットのスキャンはインデックスの降順で行われます;
    それ以外の場合は、インデックスの昇順で発生します。

    `scan_direction & MOVE_HINT_BACKWARDS`\の場合、 その後、新しいヒント位置は :cpp:`hint`\ よりも小さいインデックスで発生します;
   　それ以外の場合は、:cpp:`hint`より大きいインデックス位置で発生します。

  .. cpp:function:: Kokkos::pair<bool, unsigned> find_any_unset_near(符号なし hint, 符号なし scan_direction = BIT_SCAN_FORWARD_MOVE_HINT_FORWARD) const;

    ホスト/デバイス: :cpp:`hint` 位置から開始し、最初に ``0`` に設定されたビットを検出します。

    :cpp:`pair<ブール, 符号なし>`　を返します。

    :cpp:`result.first`　が　:cpp:`true` の場合、 :cpp:result.second` は検出されたビット位置です。

    :cpp:`result.first`が　:cpp:`false`　の場合、:cpp:`result.second`　は、新しいヒント位置です。

    :cpp:`scan_direction & BIT_SCAN_REVERSE`\　の場合、ビットのスキャンはインデックスの降順で行われます;それ以外の場合は、インデックスの昇順で発生します。

    :cpp:`scan_direction & MOVE_HINT_BACKWARDS`\　の場合には、その後新しいヒント位置は :cpp:`hint`\　よりも小さいインデックスで発生します; それ以外の場合は、:cpp:`hint`より大きいインデックス位置で発生します。

  .. cpp:function:: constexpr bool is_allocated() const

    ホスト/デバイス: ビットはデバイス上に割り当てられます。

``ConstBitset``
===============

クラスインターフェイス
---------------

.. cpp:class:: テンプレート <型名　デバイス> ConstBitset

  :tparam Device: 物理的にビットを含むデバイス。

  .. rubric:: コンストラクタ / 代入

  .. cpp:function:: ConstBitset()

    ホスト/: ビットを持たないビットセットを構築します。

  .. cpp:function:: ConstBitset(ConstBitset const& rhs) = デフォルト
  .. cpp:function:: ConstBitset& operator=(ConstBitset const& rhs) = デフォルト

    コンストラクタ/代入 演算子をコピー。

  .. cpp:function:: ConstBitset(Bitset<Device> const& rhs)
  .. cpp:function:: ConstBitset& operator=(Bitset<Device> const& rhs)

    ホスト/デバイス: :cpp:`Bitset`を a :cpp:`ConstBitset`　にコピー/代入します。

  .. cpp:function:: 符号なし size() const

    ホスト/デバイス: ビット数を返します。

  .. cpp:function:: 符号なし count() const

     ホスト/デバイス:  ``1``　に設定されたビット数を返します。

  .. cpp:function:: ブール テスト(符号なし i) const

    ホスト/デバイス: ``i``\ 'thビットが　``1``　に設定されている場合、またはその場合に限り、``真``　を返します。

非メンバー関数
--------------------

  .. cpp:function:: テンプレート <typename DstDevice, typename SrcDevice> void deep_copy(Bitset<DstDevice>& dst, Bitset<SrcDevice> const& src)

    　``SrcDevice``　上の　``src``　から　``DstDevice``　上の　``dst``　に　``Bitset``　をコピーします。

  .. cpp:function:: テンプレート <typename DstDevice, typename SrcDevice> void deep_copy(Bitset<DstDevice>& dst, ConstBitset<SrcDevice> const& src)

    　``SrcDevice``　上の　``src``　から ``DstDevice``　上の　``Bitset`` ``dst``に　``ConstBitset``　をコピーします。
