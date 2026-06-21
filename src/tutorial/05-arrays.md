# 5. Arrays

typed, zero-indexed, mutable — declare with `dec arr[<type>] <name> = [<items>]`

```rl
dec arr[int] nums = [10, 20, 30]
println(nums[0]) // 10
nums[1] = 99
println(nums) // [10, 99, 30]
```

nested arrays are supported

```rl
dec arr[arr[int]] matrix = [[1, 2], [3, 4]]
println(matrix[0][1]) // 2
```

all elements must share the same type

```rl
dec arr[int] nums = [1, 2, 3]
// dec arr[int] bad = [1, "two"] // error: type mismatch
```
