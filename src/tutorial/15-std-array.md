# 15. std::array

basic manipulation: push, pop, slice, sort, unique

```rl
get arr_push, arr_sort, arr_slice, arr_unique from std::array

println(arr_push([1, 2], 3))         // [1, 2, 3]
println(arr_sort([3, 1, 2]))         // [1, 2, 3]
println(arr_slice([1, 2, 3, 4], 1, 3)) // [2, 3]
println(arr_unique([1, 2, 2, 3, 1])) // [1, 2, 3]
```

aggregates: sum, max, min, product, count

```rl
get arr_sum, arr_max, arr_min, arr_product from std::array

println(arr_sum([1, 2, 3, 4]))     // 10
println(arr_max([3, 1, 4, 1, 5]))  // 5
println(arr_min([3, 1, 4, 1, 5]))  // 1
println(arr_product([1, 2, 3, 4])) // 24
```

higher-order functions take a predicate or callback lambda

```rl
get arr_filter, arr_map, arr_reduce from std::array

println(arr_filter([1, 2, 3, 4], fn(int x) -> bool { return x > 2 })) // [3, 4]
println(arr_map([1, 2, 3], fn(int x) -> int { return x * 2 }))        // [2, 4, 6]
println(arr_reduce([1, 2, 3, 4], fn(int acc, int x) -> int { return acc + x }, 0)) // 10
```
