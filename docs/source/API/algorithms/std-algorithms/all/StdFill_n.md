
# `fill_n`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
namespace Kokkos{
namespace Experimental{

template <class ExecutionSpace, class IteratorType, class SizeType, class T>
IteratorType fill_n(const ExecutionSpace& exespace,                             (1)
                    IteratorType first,
                    SizeType n, const T& value);

template <class ExecutionSpace, class IteratorType, class SizeType, class T>
IteratorType fill_n(const std::string& label, const ExecutionSpace& exespace,   (2)
                    IteratorType first,
                    SizeType n, const T& value);

template <class ExecutionSpace, class DataType, class... Properties, class SizeType, class T>
auto fill_n(const ExecutionSpace& exespace,                                     (3)
            const Kokkos::View<DataType, Properties...>& view,
            SizeType n, const T& value);

template <class ExecutionSpace, class DataType, class... Properties, class SizeType, class T>
auto fill_n(const std::string& label, const ExecutionSpace& exespace,           (4)
            const Kokkos::View<DataType, Properties...>& view,
            SizeType n, const T& value);

} //　エンド　名前空間 実験的
} //　エンド　名前空間 Kokkos
```

# ディスクリプション

 `first` で始まる範囲内の最初の　`n`　個の要素　(オーバーロード 1,2)　または
`view` 内の最初の　`n`　個の要素　(オーバーロード 3,4)　に　`値` をコピー割り当てします。

## パラメータおよび要件

- `exespace`,  `first`, `view`, `value`: same as in 　[`fill`](./StdFill)　内と同様。
- `label`:
  - バッグ目的で実装カーネルに名付けるために使用。
  - 1　について、デフォルト文字列は、: "Kokkos::fill_n_iterator_api_default"
  - 3　について、デフォルト文字列は、: "Kokkos::fill_n_view_api_default"
- `n`:
  - 変更する要素数　（0以上でなければなりません）


## 戻り値

 `n > 0`　であれば、 最後の要素がコピーされた *後*　の宛先へのイテレータを返します。

そうでなければ、それは、`first` (1,2について) または、`Kokkos::begin(view)` (3,4について)　を返します。


## 例

```c++
名前空間 KE = Kokkos::Experimental;
Kokkos::View<double*> a("a", 13);
//  a　を使って、何かを行います
// ...

const double newValue{4};
KE::fill_n(Kokkos::DefaultExecutionSpace(), KE::begin(a), 10, newValue);

// passing the view directly　ビューを直接渡します。
KE::fill_n(Kokkos::DefaultExecutionSpace(), a, 10, newValue);

// 明示的に実行空間を設定します。 (アクティブを仮定)
KE::fill_n(Kokkos::OpenMP(), KE::begin(a), 10, newValue);
```
