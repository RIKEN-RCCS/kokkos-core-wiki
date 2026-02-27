
# `fill_n`

ヘッダーファイル: `Kokkos_StdAlgorithms.hpp`

```c++
名前空間 Kokkos{
名前空間 Experimental{

テンプレート <class ExecutionSpace, class IteratorType, class SizeType, class T>
IteratorType fill_n(const ExecutionSpace& exespace,                             (1)
                    IteratorType first,
                    SizeType n, const T& value);

テンプレート <class ExecutionSpace, class IteratorType, class SizeType, class T>
IteratorType fill_n(const std::string& label, const ExecutionSpace& exespace,   (2)
                    IteratorType first,
                    SizeType n, const T& value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class SizeType, class T>
auto fill_n(const ExecutionSpace& exespace,                                     (3)
            const Kokkos::View<DataType, Properties...>& view,
            SizeType n, const T& value);

テンプレート <class ExecutionSpace, class DataType, class... Properties, class SizeType, class T>
auto fill_n(const std::string& label, const ExecutionSpace& exespace,           (4)
            const Kokkos::View<DataType, Properties...>& view,
            SizeType n, const T& value);

} //　エンド　名前空間 実験的
} //　エンド　名前空間 Kokkos
```

# ディスクリプション

Copy-assigns `value` to the first `n` elements in the range starting at `first` (overloads 1,2)
or the first `n` elements in `view` (overloads 3,4).

## Parameters and Requirements

- `exespace`,  `first`, `view`, `value`: same as in [`fill`](./StdFill)
- `label`:
  - used to name the implementation kernels for debugging purposes
  - for 1, the default string is: "Kokkos::fill_n_iterator_api_default"
  - for 3, the default string is: "Kokkos::fill_n_view_api_default"
- `n`:
  - number of elements to modify (must be non-negative)


## Return

If `n > 0`, returns an iterator to the element *after* the last element assigned.

Otherwise, it returns `first` (for 1,2) or `Kokkos::begin(view)` (for 3,4).


## Example

```c++
namespace KE = Kokkos::Experimental;
Kokkos::View<double*> a("a", 13);
// do something with a
// ...

const double newValue{4};
KE::fill_n(Kokkos::DefaultExecutionSpace(), KE::begin(a), 10, newValue);

// passing the view directly
KE::fill_n(Kokkos::DefaultExecutionSpace(), a, 10, newValue);

// explicitly set execution space (assuming active)
KE::fill_n(Kokkos::OpenMP(), KE::begin(a), 10, newValue);
```
