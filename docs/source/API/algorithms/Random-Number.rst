乱数
====

.. role:: cpp(code)
    :language: cpp

Rand
----

ヘッダーファイル: ``<Kokkos_Core.hpp>``, ``<Kokkos_Random.hpp>``

.. code-block:: cpp

   template<class Generator>
   struct rand<Generator, gen_data_type>
   {
     KOKKOS_INLINE_FUNCTION
      gen_func_type max(){
       return type_value;
     }

     KOKKOS_INLINE_FUNCTION
     static gen_func_type draw(Generator& gen){
       return gen_data_type((gen.rand()&gen_return_value)
     }

     KOKKOS_INLINE_FUNCTION
     static gen_func_type draw(Generator& gen,
                               const gen_data_type& range){
       return gen_data_type((gen.rand(range));
     }

     KOKKOS_INLINE_FUNCTION
     static gen_func_type draw(Generator& gen,
                               const gen_data_type& start,
			       const gen_data_type& end){
        gen_data_type(gen.rand(start,end));
     }

``gen_data_type``、 ``gen_func_type`` および ``type_value`` は、機能仕様です。この一覧にあるすべての関数およびクラスは、 ``Kokkos::`` 名前空間の一部です。

+-------------------+-------------------+---------------------------+-----------------------+
| gen_data_type     | gen_func_type     | type_value                | gen_return_value      |
+===================+===================+===========================+=======================+
| char              | short             | 127                       | (&0xff+256)%256       |
+-------------------+-------------------+---------------------------+-----------------------+
| short             | short             | 32767                     | (&0xffff+65536)%32768 |
+-------------------+-------------------+---------------------------+-----------------------+
| int               | int               | MAX_RAND                  |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| uint              | uint              | MAX_URAND                 |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| long              | long              | MAX_RAND or MAX_RAND64    |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| ulong             | ulong             | MAX_RAND or MAX_RAND64    |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| long long         | long long         | MAX_RAND64                |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| ulong long        | ulong long        | MAX_URAND64               |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| float             | float             | 1.0f                      |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| double            | double            | 1.0                       |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| complex<float>    | complex<float>    | 1.0,1.0                   |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+
| complex<double>   | complex<double>   | 1.0,1.0                   |  ?                    |
+-------------------+-------------------+---------------------------+-----------------------+

ここで、XorShift関数の値の最大値が、以下の列挙型によって与えられる。

* enum {MAX_URAND = 0xffffffffU};
* enum {MAX_URAND64 = 0xffffffffffffffffULL-1};
* enum {MAX_RAND = static_cast<int>(0xffffffffU/2)};
* enum {MAX_RAND64 = static_cast<int64_t>(0xffffffffffffffffULL/2-1)};

ジェネレータ
============

ヘッダーファイル: ``<Kokkos_Core.hpp>`` ``<Kokkos_Random.hpp>``

概要
----

Kokkos_Randomは、擬似乱数ジェネレータに必要な構造を提供します。Kokkosは現在、2つのジェネレータファミリーを提供しています。

* XorShiftジェネレータ（``Random_XorShift64_Pool``、``Random_XorShift1024_Pool``）。Vigna, Sebastiano (2014) に基づいています。[*"マルサーリアのXORシフト生成器に関する実験的探求、スクランブル処理されています。" 以下を参照: http://arxiv.org/abs/1402.6246*]
* ``Random_SFC64_Pool``。Chris Doty-HumphreyのSmall Fast Counting（SFC64）ジェネレータを実装しています（その特徴的な性質については、以下の :ref:`専用セクション <random_sfc64_pool>` を参照してください）。

これらはすべて、本ページで説明する同一の ``Pool``/``Generator`` インターフェースを共有しており、相互に置き換えて使用できます。

乱数生成器自体には、ステートプールと実際のジェネレータの二つの構成要素があります:
ステートプールは複数のジェネレータを管理し、各アクティブなスレッドが自身のジェネレータを取得できるようにします。
これにより、スレッド間で独立した乱数を生成することが可能になります。
**CuRAND** とは対照的に、プール（またはジェネレータ）の関数はいずれも集合関数ではないことに注意してください。
つまり、すべての関数は条件式内で呼び出すことができます。

.. code-block:: cpp

    template<class DeviceType>
    class  {
      public:

      using device_type = DeviceType;
      using generator_type = Generator<DeviceType>;

      Pool();
      Pool(uint64_t seed);
      Pool(uint64_t seed, uint64_t num_states);
      Pool(const typename DeviceType::execution_space& exec, uint64_t seed);
      Pool(const typename DeviceType::execution_space& exec, uint64_t seed, uint64_t num_states);

      void init(uint64_t seed, uint64_t num_states);  //  Kokkos 5.0より非推奨
      generator_type get_state();
      void free_state(generator_type Gen);
    }

構築および初期化
----------------

ジェネレータのプールは、開始シードおよび num_states の pool_size を設定して初期化されます。この初期化プロセスは常にプラットフォームに依存せず決定論的ですが、その実行は基盤となるジェネレータファミリーによって異なります。

* XorShiftジェネレータの場合、単一の ``Random_XorShift64`` ジェネレータが（ホスト上で）\ **シリアル**\ に実行され、プール内のすべての状態を次々にシードします。ある状態のシードは前の状態のものから導出されます。
* ``Random_SFC64_Pool`` の場合、各ストリームの初期状態は ``(seed, stream index)`` のペアのみに依存するため、プールの状態は、対象バックエンドが利用可能な場合、そのバックエンドによって\ **並列**\ に初期化できます。以下の :ref:`並列初期化 <random_sfc64_pool>` を参照してください。これは大規模なプールにおいて著しく高速になる可能性があります。

どちらの場合でも、ジェネレータを要求するとその状態がロックされ、各スレッドが専用の（独立した）ジェネレータを持つことが保証されます。（Cudaデバイス上で状態を取得するにはアトミック操作が必要であり、非決定的になることにご注意ください！）完了後、ジェネレータはstateプールに戻され、それを解除し、その状態の更新時に再びプール内で利用可能になります。

実行空間インスタンスを選択しないプールジェネレータは同期的であり、指定された `DeviceType` のデフォルトの実行スペースインスタンスを使用します。
実行空間インスタンスを選択するプールコンストラクタは非同期的です

使用方法
--------

プールおよびそのプール内でのジェネレータの選択を前提とすれば、
次の段階で、ジェネレータを使用して、所望する型の乱数を生成するファンクターを
開発します。

.. code-block:: cpp

    template<class Device>
    class Generator {
      public:

      typedef DeviceType device_type;

      //各 [X]rand[S]() 関数 (XorShift) の最大戻し値
      enum {MAX_URAND = 0xffffffffU};
      enum {MAX_URAND64 = 0xffffffffffffffffULL-1};
      enum {MAX_RAND = static_cast<int>(0xffffffffU/2)};
      enum {MAX_RAND64 = static_cast<int64_t>(0xffffffffffffffffULL/2-1)};

      //状態を伴うInit および pool に関するidx。 注意事項: 順次に、
      //ジェネレータは、必要な状態引数を渡すだけで利用可能です。
      KOKKOS_INLINE_FUNCTION
      Generator (STATE_ARGUMENTS, int state_idx = 0);

      //[0,MAX_URAND)の範囲で等間隔に分布したuint32_tを1つ生成します。
      KOKKOS_INLINE_FUNCTION
      uint32_t urand();

      //[0, range) の範囲で等間隔に分布した uint32_t を生成します。
      KOKKOS_INLINE_FUNCTION
      uint32_t urand(const uint32_t& range);

      //[start,end) の範囲で等間隔に分布した uint32_t を生成します。
      KOKKOS_INLINE_FUNCTION
      uint32_t urand(const uint32_t& start, const uint32_t& end );
    }

選択された32ビット符号なし整数型に対して、3つの範囲オプションが表示されます: [0,MAX_URAND), 
[0,range) および [start,end)。
最初の（デフォルトの）オプションは、そのデータ型の最大可能な範囲を超える符号なし整数を選択します。MAX_URAND の定義値は、上記の列挙型として示されています 。(また64ビット符号なし整数用のmaX_URANDも示されてます。) 後者の2つのオプションは、ユーザー定義の整数の範囲をカバーします。

他のデータ型についての詳細情報: Scalar, uint64_t, int, int32_t, int64_t, float, double; また正規分布と、[0, range) および [start, end) オプション用のView-fillオプション。

例
--

.. code-block:: cpp

    #include <Kokkos_Core.hpp>
    #include <Kokkos_Random.hpp>

    int main(int argc, char *argv[]) {
        Kokkos::ScopeGuard guard(argc, argv);

        Kokkos::Random_XorShift64_Pool<> random_pool(/*seed=*/12345);

        int total = 1000000;
        int count;
        Kokkos::parallel_reduce(
            "approximate_pi", total,
            KOKKOS_LAMBDA(int, int& local_count) {
                // 乱数生成エンジンの状態を取得
                auto generator = random_pool.get_state();

                double x = generator.drand(0., 1.);
                double y = generator.drand(0., 1.);

                // エンジン状態の解放を忘れない
                random_pool.free_state(generator);

                if (x * x + y * y <= 1.) {
                    ++local_count;
                }
            },
            count);

        printf("pi = %f\n", 4. * count / total);
    }

.. _random_sfc64_pool:

Random_SFC64_Pool
-----------------

ヘッダファイル: ``<Kokkos_Core.hpp>``、``<Kokkos_Random.hpp>``

``Random_SFC64_Pool`` は、Chris Doty-HumphreyのSmall Fast Counting（SFC64）擬似乱数ジェネレータを実装した代替のプール/ジェネレータのペアであり、パブリックドメインで公開されています。（注: このジェネレータは、たとえばNumPyのドキュメントなどで、"Small Fast Chaotic" と呼ばれることがあります）
これは上記で説明した同一の ``Pool``/``Generator`` インターフェース（``get_state()``、``free_state()`` など）に従っており、``Random_XorShift64_Pool`` の置き換えとしてそのまま使用できます。

XorShiftジェネレータとは異なり、SFC64は内部状態に64ビットのカウンタを組み込んでいます。単一の64ビットシードから、2\ :sup:`64`\  個の独立したストリームにアクセスでき、それぞれ少なくとも 2\ :sup:`64`\  の周期を持ちます（期待される周期は 2\ :sup:`255`\  のオーダーです）。

.. code-block:: cpp

  template<class DeviceType>
  class Random_SFC64_Pool {
    public:

    using device_type = DeviceType;
    using generator_type = Random_SFC64<DeviceType>;

    Random_SFC64_Pool();
    Random_SFC64_Pool(uint64_t seed);
    Random_SFC64_Pool(uint64_t seed, uint64_t num_states);
    // Useful in distributed settings to be reproducible
    Random_SFC64_Pool(uint64_t seed, uint64_t seed_offset, uint64_t num_states);

    // Asynchronous constructors :
    Random_SFC64_Pool(const execution_space& exec, uint64_t seed);
    Random_SFC64_Pool(const execution_space& exec, uint64_t seed, uint64_t num_states);
    Random_SFC64_Pool(const execution_space& exec, uint64_t seed,
                       uint64_t seed_offset, uint64_t num_states);

    generator_type get_state();
    void free_state(generator_type gen);
  }

並列初期化
~~~~~~~~~~

各SFC64ストリームはそのインデックス（seed、カウンタオフセット）から独立してシードできるため、プールの状態は対象バックエンドによって並行して初期化できます。これは、状態が相互に連鎖しており、したがってシリアルに初期化しなければならない ``Random_XorShift64_Pool`` および ``Random_XorShift1024_Pool`` とは対照的です。並列バックエンドが有効な場合、``Random_SFC64_Pool`` を構築すると、その状態が並列に初期化され、大規模なプールにおいて著しく高速になる可能性があります。

再現可能なストリーム分割
~~~~~~~~~~~~~~~~~~~~~~~~

各ストリームは ``(seed, stream_index)`` によって一意に決定されるため、ビット単位の再現性を維持しながら複数のプール（たとえばMPIランクごとに1つ）に計算を分割するには、すべてのプールに同じシードと、前のプールにすでに割り当てられたストリーム数に等しい ``seed_offset`` を与えるだけで済みます。たとえば、単一のプールから1000個の状態を要求することは、``seed_offset = 0`` の1つのプールから500個の状態を要求し、同じシードと ``seed_offset = 500`` の2番目のプールから500個の状態を要求することと等価です。両方の構成は、まったく同じ1000個のストリームを生成します。

.. code-block:: cpp

  #include <Kokkos_Core.hpp>
  #include <Kokkos_Random.hpp>

  int main(int argc, char *argv[]) {
      Kokkos::ScopeGuard guard(argc, argv);

      uint64_t seed = 12345;

      // Pool 0 handles streams [0, 500), pool 1 handles streams [500, 1000)
      // — identical results to a single pool of 1000 states with seed_offset 0.
      Kokkos::Random_SFC64_Pool<> pool0(seed, /*seed_offset=*/0, /*num_states=*/500);
      Kokkos::Random_SFC64_Pool<> pool1(seed, /*seed_offset=*/500, /*num_states=*/500);

      // ... use pool0 / pool1 exactly like Random_XorShift64_Pool
  }

使用方法
~~~~~~~~

他のプールと同様に、ジェネレータオブジェクト自体に付属するレガシーメソッドに頼るのではなく、特定の型または特定の分布内の数値を生成するために、汎用の ``Kokkos::rand`` 構造体を使用することを強く推奨します。

.. code-block:: cpp

  #include <Kokkos_Core.hpp>
  #include <Kokkos_Random.hpp>

  int main(int argc, char* argv[]) {
      Kokkos::initialize(argc, argv);
      {
          // 1. Initialize the SFC64 generator pool with a seed
          uint64_t seed = 123456789;
          Kokkos::Random_SFC64_Pool<Kokkos::DefaultExecutionSpace> rand_pool(seed);

          int N = 1000;
          Kokkos::View<double*> random_numbers("random_numbers", N);

          // 2. Use the pool in a parallel kernel
          Kokkos::parallel_for("GenerateRandomNumbers", N, KOKKOS_LAMBDA(const int i) {
              // Get a state/generator from the pool
              auto generator = rand_pool.get_state();

              // Generate a random double (e.g., between 0.0 and 1.0)
              // Recommended API using the Kokkos::rand struct:
              random_numbers(i) = Kokkos::rand<decltype(generator), double>::draw(generator);

              // Alternatively, generate a number in a specific range [min, max)
              double val_range = Kokkos::rand<decltype(generator), double>::draw(generator, 10.0, 20.0);

              // Return the state back to the pool to avoid deadlocks
              rand_pool.free_state(generator);
          });
      }
      Kokkos::finalize();
      return 0;
  }
