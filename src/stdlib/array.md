# std::array

functions for array manipulation

## `arr_concat(arr1, arr2)`

concatenates two arrays of the same type into one

```rl
get std::array::arr_concat

arr_concat([1, 2], [3, 4]) // [1, 2, 3, 4]
```

## `arr_contains(arr, value)`

true if the array contains the given value

```rl
get std::array::arr_contains

arr_contains([1, 2, 3], 2) // true
```

## `arr_count(arr)`

returns the number of elements in the array

```rl
get std::array::arr_count

arr_count([1, 2, 3]) // 3
```

## `arr_fill(value, count)`

creates an array filled with value repeated count times

```rl
get std::array::arr_fill

arr_fill(0, 3) // [0, 0, 0]
```

## `arr_first(arr)`

returns the first element of the array

```rl
get std::array::arr_first

arr_first([1, 2, 3]) // 1
```

## `arr_flatten(arr)`

flattens a nested array into a single array

```rl
get std::array::arr_flatten

arr_flatten([[1, 2], [3, 4]]) // [1, 2, 3, 4]
```

## `arr_index_of(arr, index)`

returns the element at the given index

```rl
get std::array::arr_index_of

arr_index_of([10, 20, 30], 1) // 20
```

## `arr_insert(arr, value, index)`

inserts value at the given index, shifting elements right

```rl
get std::array::arr_insert

arr_insert([1, 3], 2, 1) // [1, 2, 3]
```

## `arr_is_empty(arr)`

true if the array has no elements

```rl
get std::array::arr_is_empty

arr_is_empty([]) // true
```

## `arr_last(arr)`

returns the last element of the array

```rl
get std::array::arr_last

arr_last([1, 2, 3]) // 3
```

## `arr_max(arr)`

returns the largest element in an int or float array

```rl
get std::array::arr_max

arr_max([3, 1, 4, 1, 5]) // 5
```

## `arr_min(arr)`

returns the smallest element in an int or float array

```rl
get std::array::arr_min

arr_min([3, 1, 4, 1, 5]) // 1
```

## `arr_pop(arr)`

removes the last element and returns the updated array

```rl
get std::array::arr_pop

arr_pop([1, 2, 3]) // [1, 2]
```

## `arr_product(arr)`

returns the product of all elements in an int or float array

```rl
get std::array::arr_product

arr_product([1, 2, 3, 4]) // 24
```

## `arr_push(arr, value)`

appends value to the end of the array and returns the updated array

```rl
get std::array::arr_push

arr_push([1, 2], 3) // [1, 2, 3]
```

## `arr_range(start, end, step)`

creates an int array from start to end (exclusive) with the given step

```rl
get std::array::arr_range

arr_range(0, 6, 2) // [0, 2, 4]
```

## `arr_remove(arr, index)`

removes the element at the given index and returns the updated array

```rl
get std::array::arr_remove

arr_remove([1, 2, 3], 1) // [1, 3]
```

## `arr_reverse(arr)`

reverses the order of elements in the array

```rl
get std::array::arr_reverse

arr_reverse([1, 2, 3]) // [3, 2, 1]
```

## `arr_slice(arr, start, end)`

returns a sub-array from start to end (exclusive)

```rl
get std::array::arr_slice

arr_slice([1, 2, 3, 4], 1, 3) // [2, 3]
```

## `arr_sort(arr)`

returns the array sorted in ascending order, only int or float arrays

```rl
get std::array::arr_sort

arr_sort([3, 1, 2]) // [1, 2, 3]
```

## `arr_sum(arr)`

returns the sum of all elements in an int or float array

```rl
get std::array::arr_sum

arr_sum([1, 2, 3, 4]) // 10
```

## `arr_unique(arr)`

returns the array with duplicate values removed, preserving order

```rl
get std::array::arr_unique

arr_unique([1, 2, 2, 3, 1]) // [1, 2, 3]
```

## `len(x)`

length of string or array

```rl
get std::array::len

len("hello") // 5
```

## `arr_all(arr, fn)`

true if every element satisfies the predicate

```rl
get std::array::arr_all

arr_all([2, 4, 6], fn(int x) -> bool { return mod(x, 2) == 0 }) // true
```

## `arr_any(arr, fn)`

true if at least one element satisfies the predicate

```rl
get std::array::arr_any

arr_any([1, 2, 3], fn(int x) -> bool { return x > 2 }) // true
```

## `arr_filter(arr, fn)`

returns a new array containing only elements where the predicate returns true

```rl
get std::array::arr_filter

arr_filter([1, 2, 3, 4], fn(int x) -> bool { return x > 2 }) // [3, 4]
```

## `arr_find(arr, fn)`

returns the first element where the predicate returns true, or null if none match

```rl
get std::array::arr_find

arr_find([1, 2, 3, 4], fn(int x) -> bool { return x > 2 }) // 3
```

## `arr_find_index(arr, fn)`

returns the index of the first element where the predicate returns true, or -1 if none match

```rl
get std::array::arr_find_index

arr_find_index([10, 20, 30], fn(int x) -> bool { return x == 20 }) // 1
```

## `arr_flat_map(arr, fn)`

maps each element to an array via the callback then flattens the results one level

```rl
get std::array::arr_flat_map

arr_flat_map([1, 2, 3], fn(int x) -> arr[int] { return [x, x * 10] }) // [1, 10, 2, 20, 3, 30]
```

## `arr_for_each(arr, fn)`

calls the callback on every element for side effects, returns null

```rl
get std::array::arr_for_each

arr_for_each([1, 2, 3], fn(int x) { println(x) })
```

## `arr_map(arr, fn)`

returns a new array with each element transformed by the callback

```rl
get std::array::arr_map

arr_map([1, 2, 3], fn(int x) -> int { return x * 2 }) // [2, 4, 6]
```

## `arr_reduce(arr, fn, initial)`

folds the array into a single value using the callback and a starting accumulator

```rl
get std::array::arr_reduce

arr_reduce([1, 2, 3, 4], fn(int acc, int x) -> int { return acc + x }, 0) // 10
```

## `arr_sort_by(arr, fn)`

sorts the array using a comparator callback that returns -1, 0, or 1

```rl
get std::array::arr_sort_by

arr_sort_by([3, 1, 2], fn(int a, int b) -> int { return a - b }) // [1, 2, 3]
```
