必要要件
############

コンパイラバージョン
=================

一般的に、Kokkos　は最低限のコンパイラバージョンより新しいすべてのコンパイラで動作することになっています。
また、可能な限り、最新のコンパイラを使用することを推奨します。
しかし、複雑なコードでは、コンパイラのバグを回避しなければなりません。 そのため、テストしないコンパイラバージョンには、気付かれていない問題があるかもしれません。

さらに、ここに挙げていないコンパイラも動作する場合があります。


Kokkos 5.x
----------

.. リスト表::
    :幅: 30 35
    :header-rowsヘッダー列: 1
    :配列: 中央

    * - コンパイラ
      - 最小バージョン

    * * GCC 
      * 10.4.0

    * * Clang (CPU)
      * 14.0.0

    * * Clang (CUDA)
      * 15.0.0

    * * AppleClang 
      * 8.0

    * * IntelLLVM (CPU)
      * 2022.0.0

    * * IntelLLVM (SYCL)
      * 2024.2.1

    * * NVCC 
      * 12.2

    * * NVC++ 
      * 22.3

    * * NVC++ (OpenACC) (実験的) 
      * 23.7

    * * ROCM 
      * 6.2.0 

    * * MSVC 
      * 19.30
 
    * * ARM/Clang 
      * 20.1

Kokkos 4.x
----------

.. リスト表::
    :幅: 30 35 35
    :ヘッダー列: 1
    :配列: 中央

    * - コンパイラ
      - 最小バージョン
      - 主要テスト済みバージョン

    * * GCC 
      * 8.2.0
      * 8.4.0, 最新

    * * Clang (CPU)
      * 8.0.0
      * 8.0.0, 最新

    * * Clang (CUDA)
      * 10.0.0
      * 12.0.0, 14.0.0

    * * AppleClang 
      * 8.0
      * latest

    * * Intel Classic (非推奨)  :red:`[ 4.5まで]`
      * 19.0.5
      * 2021.8.0

    * * IntelLLVM (CPU)
      * 2021.1.1
      * 2023.2.4

    * * IntelLLVM (SYCL)
      * 2023.0.0
      * 2024.2.1 2025.0.0

    * * NVCC 
      * 11.0
      * 11.0, 11.6, 11.7

    * * NVC++ 
      * 22.3
      * 22.9

    * * NVC++ (OpenACC) (実験的) 
      * 23.7
      * 23.7

    * * ROCM 
      * 5.2.0
      * 5.2.0 

    * * MSVC 
      * 19.29
      * Latest
 
    * * ARM/Clang 
      * 20.1
      * 20.1

Kokkos 3.x
----------

.. リスト表::
    :幅: 30 35 35
    :header-rowsヘッダー列: 1
    :配列: 中央

    * - コンパイラ
      - 最小バージョン
      - 主要テスト済みバージョン

    * * GCC 
      * 5.3.0
      * 5.3.0, 6.1.0, 7.3.0, 8.3, 9.2, 10.0
    
    * * Clang 
      * 4.0.0
      * 8.0.0, 9.0.0, 10.0.0, 12.0.0
    
    * * Intel 
      * 17.0.1
      * 17.4, 18.1, 19.5
    
    * * NVCC 
      * 9.2.88
      * 9.2.88, 10.1, 11.0
    
    * * NVC++ 
      * 21.5
      * NA
    
    * * ROCM 
      * 4.5
      * 4.5.0
    
    * * MSVC 
      * 19.29
      * 19.29
    
    * * IBM XL 
      * 16.1.1
      * 16.1.1
    
    * * Fujitsu 
      * 4.5.0
      * NA
    
    * * ARM/Clang 
      * 20.1
      * 20.1

構築システム:
=============

* CMake >= 3.16: が必須
* CMake >= 3.18: Fortranリンク。これは、ほとんどの　Fortran/Kokkos　混合構築には、影響しません。 既知の構築問題<https://github.com/kokkos/kokkos/blob/master/BUILD.md#known-issues>`_　を参照してください。
* CMake >= 3.21.1 for NVC++

主要テスト済みコンパイラは、リリースモードにおいて、エラーとして警告を出して、合格しています。 包括的なバックエンドの組み合わせでテストされます（つまり、OpenMP、Pthreads、Serial、OpenMP+Serial　等）。
以下のフラッグセットを使用しています:


* GCC:

.. code-block:: bash

  -Wall -Wunused-parameter -Wshadow -pedantic
  -Werror -Wsign-compare -Wtype-limits
  -Wignored-qualifiers -Wempty-body
  -Wclobbered -Wuninitialized

* Intel:

.. code-block:: bash

  -Wall -Wunused-parameter -Wshadow -pedantic
  -Werror -Wsign-compare -Wtype-limits
  -Wuninitialized

* Clang:

.. code-block:: bash

  -Wall -Wunused-parameter -Wshadow -pedantic
  -Werror -Wsign-compare -Wtype-limits
  -Wuninitialized

* NVCC:

.. code-block:: bash

  -Wall -Wunused-parameter -Wshadow -pedantic
  -Werror -Wsign-compare -Wtype-limits
  -Wuninitialized

.. 注意事項:: 

  他のコンパイラも、時折、特に、開発ブランチからマスターブランチへのプッシュ時にテストされます。 これらは、``-Werror`` なしで、限られたバックエンドに対しては、あまり厳密なテストは行われていません。
