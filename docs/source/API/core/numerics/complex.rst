``complex``
===========

.. role:: cpp(code)
    :language: cpp

 ``<Kokkos_Core.hpp>`` に含まれる ヘッダー ``<Kokkos_Complex.hpp>`` に定義。

ディスクリプション
-----------

``complex`` は、複素数を表し操作するためのクラステンプレートです。

* これは、 std::complex<T の代替を目的としています。
* 注意事項: もし ``z`` が、Kokkos::complex<T> 型を持つ場合、 ``reinterpret_cast<T(&)[2]>(z)`` のようなキャストは未定義の挙動を引き起こします (これはstd::complexとは異なります)。

インターフェイス
---------

.. cpp:class:: template<class T> complex


  :tparam T: 実数成分と虚数成分の型。

  * :cpp:any:`T` は浮動小数点型 (``float``, ``double``, ``long double``) か拡張浮動小数点型でなければなりません。

  * :cpp:any:`T` を、 ``const`` および/または ``volatile`` により修飾されることはできません。

  * 特定のバックエンド(CUDA または SYCL の``long double`` 等）では動作しないタイプもあります。

  .. rubric:: Public Types:

  .. cpp:type:: value_type = T

  .. rubric:: コンストラクタおよび代入演算子:

  .. cpp:function:: complex()

    デフォルトの構成子ゼロは実成分と虚成分を初期化します。

  .. cpp:function:: template<class U> complex(complex<U> z) noexcept

     変換コンストラクタは、実成分を ``static_cast<T>(z.real())`` に、虚数成分を ``static_cast<T>(z.imag())`` に初期化します。

    制約: ``U`` は、 ``T` に変換可能です。

  .. cpp:function:: complex(std::complex<T> z) noexcept
  .. cpp:function:: complex& operator=(std::complex<T> z) noexcept

    ``std::complex`` からの暗示的変換は、実成分を ``z.real()`` に、虚数成分を ``z.imag()`` に初期化します。

  .. cpp:function:: constexpr complex(T r) noexcept
  .. cpp:function:: constexpr complex& operator=(T r) noexcept

    実成分を ``r`` に初期化  し、ゼロは虚成分を初期化します。

  .. cpp:function:: constexpr complex(T r, T i) noexcept

    実成分を ``r`` に、虚成分を ``i`` に初期化します。

  .. cpp:function:: template<class U> complex(const volatile complex<U>&) noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator=(const complex&) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: volatile complex& operator=(const volatile complex&) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: complex& operator=(const volatile complex&) noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator=(const volatile T&) noexcept
  
    .. deprecated:: 4.0.0

  .. cpp:function:: void operator=(const T&) volatile noexcept
  
    .. 非推奨:: 4.0.0

    .. note:
      
      一部の非推奨の割り当て演算子は、コピー割り当て演算子にならないようにテンプレート化された実装になっています。

  .. rubric:: パブリックメンバー関数:

  .. cpp:function:: operator std::complex<T>() const noexcept

     ``std::complex`` への変換演算子

  .. cpp:function:: constexpr T& real() noexcept
  .. cpp:function:: constexpr T real() const noexcept

    :return: 実成分の値。

  .. cpp:function:: constexpr void real(T r) noexcept

    ``r`` を実成分に代入します。

  .. cpp:function:: constexpr T& imag() noexcept
  .. cpp:function:: constexpr T imag() const noexcept

    :return: 虚数成分の値。

  .. cpp:function:: constexpr void imag(T i) noexcept

    虚数成分に ``i`` を代入します。

  .. cpp:function:: constexpr complex& operator+=(complex v) noexcept
  .. cpp:function:: constexpr complex& operator+=(T v) noexcept

    Adds the complex value ``complex(v)`` to the complex value ``*this`` and stores the sum in ``*this``.

  .. cpp:function:: constexpr complex& operator-=(complex v) noexcept
  .. cpp:function:: constexpr complex& operator-=(T v) noexcept

     複素値 ''complex(v)''  を複素値 '*this'' に加え、その和を '*this' に保存します。

  .. cpp:function:: constexpr complex& operator*=(complex v) noexcept
  .. cpp:function:: constexpr complex& operator*=(T v) noexcept

    複素値 '*this'' から ``complex(v)`` を差し引き、差分を '*this' に格納します。

  .. cpp:function:: constexpr complex& operator/=(complex v) noexcept
  .. cpp:function:: constexpr complex& operator/=(T v) noexcept

    複素値 ``complex(v)`` に複素値を``*this`` 掛け、積を ``*this`` に格納します。

  .. cpp:function:: volatile T& real() volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: T real() const volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: volatile T& imag() volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: T imag() const volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator+=(const volatile complex& v) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator+=(const volatile T& v) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator-=(const volatile complex& v) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator-=(const volatile T& v) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator*=(const volatile complex& v) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator*=(const volatile T& v) volatile noexcept
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator/=(const volatile complex& v) volatile noexcept(noexcept(T{}/T{}))
  
    .. 非推奨:: 4.0.0

  .. cpp:function:: void operator/=(const volatile T& v) volatile noexcept(noexcept(T{}/T{}))
  
    .. 非推奨:: 4.0.0


  .. rubric:: 非メンバー関数:

  .. cpp:function:: template<typename T1, typename T2> bool operator==(complex<T1> x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator==(complex<T1> x, T2 y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator==(T1 x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator==(complex<T1> x, std::complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator==(std::complex<T1> x, complex<T2> y) noexcept

    :返し: ``true`` とは、 ``complex(x)`` の実成分が ``complex(y)`` の実成分に等しく、``complex(x)`` の虚成分が ``complex(y)`` の虚成分に等しい場合に限ります。

  .. cpp:function:: template<typename T1, typename T2> bool operator!=(complex<T1> x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator!=(complex<T1> x, T2 y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator!=(T1 x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator!=(complex<T1> x, std::complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> bool operator!=(std::complex<T1> x, complex<T2> y) noexcept

    :retrun: ``!(x == y)``

  .. cpp:function:: template<typename T> complex<T> operator+(complex<T> x) noexcept

    :return: ``x``

  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator+(complex<T1> x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator+(complex<T1> x, T2 y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator+(T1 x, complex<T2> y) noexcept

    :返し: 複素値 ``complex(x)`` は複素値 ``complex(y)`` に加算されます。

  .. cpp:function:: template<typename T> complex<T> operator-(complex<T> x) noexcept

    :返し: ``complex(-x.real(), -x.imag())``

  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator-(complex<T1> x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator-(complex<T1> x, T2 y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator-(T1 x, complex<T2> y) noexcept

    :retrun: 複素値 ``complex(y)`` は複素値「complex(x)」 ``complex(x)`` から差し引かれます。

  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator*(complex<T1> x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator*(complex<T1> x, T2 y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator*(T1 x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator*(std::complex<T1> x, complex<T2> y) noexcept

    :retrun: 複素値 ``complex(x)`` に複素値 ``complex(y)`` を掛けたものです。

  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator/(complex<T1> x, complex<T2> y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator/(complex<T1> x, T2 y) noexcept
  .. cpp:function:: template<typename T1, typename T2> complex<std::common_type_t<T1, T2>> operator/(T1 x, complex<T2> y) noexcept

    :return: 複素値 ``complex(y)`` は複素値 ``complex(x)`` に分割されます。

  .. cpp:function:: template<typename T> std::istream& operator>>(std::ostream& i, complex<T>& x)

    複素数 'x'  を抽出:'u',  '(u)' または   ``(u,v)`` の形で、ここで ``u``  は実部、''v'' は虚数部で、 ``i`` を返します。

  .. cpp:function:: template<typename T> std::ostream& operator<<(std::ostream& o, complex<T> x)

    :return: ``o << std::complex(x)``

  .. cpp:function:: template<typename T> T real(complex<T> x) noexcept

    :return: ``x.real()``.

  .. cpp:function:: template<typename T> T imag(complex<T> x) noexcept

    :return: ``x.imag()``.

  .. cpp:function:: template<typenmame T> complex<T> polar(T rho, T theta = T())

    :return: ``complex``の値は、大きさが ``rho`` 、位相角が ``theta`` である複素数に対応します。

  .. cpp:function:: template<typename T> T abs(complex<T> x)

    :return:  ``x`` の大きさ

  .. cpp:function:: template<typename T1, typename T2> complex<U> pow(complex<T1> x, complex<T2> y)
  .. cpp:function:: template<typename T1, typename T2> complex<U> pow(complex<T1> x, T2 y)
  .. cpp:function:: template<typename T1, typename T2> complex<U> pow(T1 x, complex<T2> y)

    :return: The complex power of baseraised to the-th power,
             defined as.底数 ``x`` の複素冪を ``y`` の乗に上げると、 ``exp(y * log(x))`` と定義されます。
             ``U`` は ``float`` であり、 ``T1`` と ``T2`` が ``float`` である場合、 そうでなければ、は` `long double`` であり、``T1`` または ``T2`` が ``long double`` である場合に使われます。 そうでなければ ``U`` は ``double`` となります。

  .. cpp:function:: template<typename T> complex<T> sqrt(complex<T> x)

    :return: 右半平面の域にある複素平方根  ``x`` 。

  .. cpp:function:: template<typename T> complex<T> conj(complex<T> x) noexcept

    :return: 複素共役 ``x``。

  .. cpp:function:: template<typename T> complex<T> exp(complex<T> x)
  .. cpp:function:: template<typename T> complex<T> exp(std::complex<T> x)

    :return: 複素 e 底指数関数  ``complex(x)``。

  .. cpp:function:: template<typename T> complex<T> log(complex<T> x)

    :retrun:  x の複素自然対数(基数e)。

  .. cpp:function:: template<typename T> complex<T> log10(complex<T> x)

    :return: ``x`` の複素共通(10進底)対数は ``log(x) / log(10)``と定義されます。

  .. cpp:function:: template<typename T> complex<T> sin(complex<T> x)

    :return:  ``x``の複素正弦。

  .. cpp:function:: template<typename T> complex<T> cos(complex<T> x)

    :return:  ``x`` の複素余弦。 

  .. cpp:function:: template<typename T> complex<T> tan(complex<T> x)

    :return:  ``x`` の複素接線。

  .. cpp:function:: template<typename T> complex<T> sinh(complex<T> x)

    :return: ``x`` の複素双曲正弦。

  .. cpp:function:: template<typename T> complex<T> cosh(complex<T> x)

    :return:  ``x`` の複素双曲余弦。

  .. cpp:function:: template<typename T> complex<T> tanh(complex<T> x)

    :return:  ``x`` の複素双曲接線。

  .. cpp:function:: template<typename T> complex<T> asinh(complex<T> x)

    :return:  ``x`` の複素弧双曲正弦。

  .. cpp:function:: template<typename T> complex<T> acosh(complex<T> x)

    :return:  ``x`` の複素弧双曲余弦。

  .. cpp:function:: template<typename T> complex<T> atanh(complex<T> x)

    :return:  ``x`` の複素弧の双曲接線。

  .. cpp:function:: template<typename T> complex<T> asin(complex<T> x)

    :return:  ``x`` の複素弧正弦。

  .. cpp:function:: template<typename T> complex<T> acos(complex<T> x)

    :return:  ``x`` の複素弧余弦。

  .. cpp:function:: template<typename T> complex<T> atan(complex<T> x)

    :return:  ``x`` の複素弧接線。

  .. cpp:function:: template<size_t I, typename T> constexpr T& get(complex<T>& z) noexcept
  .. cpp:function:: template<size_t I, typename T> constexpr T&& get(complex<T>&& z) noexcept
  .. cpp:function:: template<size_t I, typename T> constexpr const T& get(const complex<T>& z) noexcept
  .. cpp:function:: template<size_t I, typename T> constexpr const T&& get(complex<T>&& z) noexcept

   タプルプロトコル/構造化バインディングサポート。

    :返し:  ``I == 0`` が ``true`` である場合、``z``  の実部への参照;
             これは ``I == 0`` が ``true`` である場合に ``z`` の虚部への参照です。

