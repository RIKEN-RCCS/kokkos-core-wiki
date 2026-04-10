# Built-In-Reducers

Kokkos は最も一般的なリダプションタイプ用のリデューサーを提供しています:
* [BAnd](../API/core/builtinreducers/BAnd): バイナリ “and” リダクションを行います
* [BOr](../API/core/builtinreducers/BOr): バイナリ “or” リダクションを行います
* [LAnd](../API/core/builtinreducers/LAnd): 論理的 “and” リダクションを行います
* [LOr](../API/core/builtinreducers/LOr): 論理的 “or” リダクションを行います
* [Max](../API/core/builtinreducers/Max): 最大値を求めます
* [MaxLoc](../API/core/builtinreducers/MaxLoc): 最大値とそれに関連するインデックスを取得します
* [Min](../API/core/builtinreducers/Min): 最小値を求めます
* [MinLoc](../API/core/builtinreducers/MinLoc): 最小値とそれに関連するインデックスを取得します
* [MinMax](../API/core/builtinreducers/MinMax): 最小値および最大値を求めます
* [MinMaxLoc](../API/core/builtinreducers/MinMaxLoc): 最大値および最小値の両方、ならびにその関連インデックスを求めます
* [Prod](../API/core/builtinreducers/Prod): すべての入力値の積を計算します
* [Sum](../API/core/builtinreducers/Sum): 単純な総和のため

これらのリデューサーはスカラーデータにのみ機能し、つまり実行時間の長さの配列を還元タイプにすることはできません(例えば、多ベクトル内の各ベクトルの最小値を同時に求めるなど)。 
一般的にリデューサーは還元のためにスカラー型にテンプレート化されており、結果のメモリ空間にもオプションのテンプレートパラメータが設定されています(詳細は後述します)。  [`MinLoc`](../API/core/builtinreducers/MinLoc), [`MaxLoc`](../API/core/builtinreducers/MaxLoc) and [`MinMaxLoc`](../API/core/builtinreducers/MinMaxLoc) のリデューサーは、さらにインデックス型上でテンプレート化されています。

以下は、たとえ話の離散化における最小値を求める単純な最小還元を行う例です。


```c++
double min;

Kokkos::parallel_reduce( "MinReduce", N, KOKKOS_LAMBDA (const int& x, double& lmin) {
  double val = (1.0*x- 7.2) * (1.0*x- 7.2) + 3.5;
  if( val < lmin ) lmin = val; 
}, Kokkos::Min<double>(min));

printf("Min: %lf\n", min);
```

本例では、 [`Min`](../API/core/builtinreducers/Min) リデューサーは、リッショニング型 `double` にテンプレート化され、結果を格納する変数は参照として取り込まれました。 リデューサーは異なるスレッドの値を組み合わせるためだけに使われることに注意してください。スレッドごとの削減は、明示的に実行されています。 リデューサーをリデューサーインスタンスを通じて使うこともできました：

```c++
double min;

Kokkos::Min<double> min_reducer(min);
Kokkos::parallel_reduce( "MinReduce", N, KOKKOS_LAMBDA (const int& x, double& lmin) {
  double val = (1.0*x- 7.2) * (1.0*x- 7.2) + 3.5;
  min_reducer.join(lmin, val); 
}, min_reducer);

printf("Min: %lf\n", min);
```

 [`MinLoc`](../API/core/builtinreducers/MinLoc), [`MaxLoc`](../API/core/builtinreducers/MaxLoc) および [`MinMaxLoc`](../API/core/builtinreducers/MinMaxLoc) リデューサーについては、 還元型は、  `value_type` 型定義によりアクセス可能な複素スカラー型です。
 [`MinLoc`](../API/core/builtinreducers/MinLoc) および [`MaxLoc`](../API/core/builtinreducers/MaxLoc) は、それぞれ還元値とインデックスを格納する `val` および `loc` のメンバーを含む値型を持っています。例えば、多次元インデックス結果を格納するためのものであることに注意してください(後述)。

```c++
typedef Kokkos::MinLoc<double,int>::value_type minloc_type;
minloc_type minloc;

Kokkos::parallel_reduce( "MinLocReduce", N, KOKKOS_LAMBDA (const int& x, minloc_type& lminloc) {
  double val = (1.0*x- 7.2) * (1.0*x- 7.2) + 3.5;
  if( val < lminloc.val ) { lminloc.val = val; lminloc.loc = x; }
}, Kokkos::MinLoc<double,int>(minloc));

printf("Min: %lf at %i\n", minloc.val, minloc.loc);
```

リデューサーは、ネスト型リダクションにおいて、使用できます。本例では、マトリクスの最小値と最大値、そしてそれらのインデックス求めるために、2次元インデックス型も用いています。

```c++
Kokkos::View<double**> A("A",N,M);
//  A を満たします

// 結果の変数を作成します
typedef Kokkos::MinMaxLoc<double, Kokkos::pair<int,int>> reducer_type;
typedef reducer_type::value_type value_type;
value_type minmaxloc

typedef Kokkos::TeamPolicy<>::member_type team_type;

// チーム並列還元を開始します
Kokkos::parallel_reduce( "MinLocReduce", Kokkos::TeamPolicy<>(N,AUTO), 
    KOKKOS_LAMBDA (const team_type& team, value_type& team_minmaxloc) {

  // 列の還元値を保存するための一時的なインスタンスを作成します
  value_type row_minmaxloc;
  int n = team.league_rank();

  // 列全体で、チームを使って、ネスト並行還元を実行します
  Kokkos::parallel_reduce( Kokkos::TeamThreadRange(team, M), 

  Kokkos::parallel_reduce( Kokkos::TeamThreadRange(team, M), 
      [=] (const int& m, value_type& thread_minmaxloc) {
    double val = A(n,m);
    
    // これが新しい最小値か最大値かを確認します
    if(val < thread_minmaxloc.min_val) {
      thread_minmaxloc.min_val = val;
      thread_minmaxloc.min_loc = Kokkos::pair<int,int>(n,m);
    }
    if(val > thread_minmaxloc.max_val) {
      thread_minmaxloc.max_val = val;
      thread_minmaxloc.max_loc = Kokkos::pair<int,int>(n,m);
    }

  }, reducer_type(row_minmaxloc));
  
  // チームの一人が全体に貢献すべきです
  // 注意事項: 最小または最大還元について、
  // あらゆるチームメンバーがこれを行った場合、それは損なわれません
  Kokkos::single(Kokkos::PerTeam(team), [=] () {
    if( row_minmaxloc.min_val < team_minmaxloc.min_val ) {
      team_minmaxloc.min_val = row_minmaxloc.min_val;
      team_minmaxloc.min_loc = row_minmaxloc.min_loc;
    }
    if( row_minmaxloc.max_val > team_minmax.max_val ) {
      team_minmaxloc.max_val = row_minmaxloc.max_val;
      team_minmaxloc.max_loc = row_minmaxloc.max_loc;
    }
  }
}, reducer_type(minmaxloc));

printf("Min %lf at (%i, %i)\n",minmaxloc.min_val, minmaxloc.min_loc.first, minmaxloc.min_loc.second);
printf("Max %lf at (%i, %i)\n",minmaxloc.max_val, minmaxloc.max_loc.first, minmaxloc.max_loc.second);
```
