# Arrays

declare a mutable array with `dec arr[<type>] <name> = [<items>]`

```rl
dec arr[int]   nums  = [1, 2, 3]
```

```rl
dec arr[string]   words = ["hello", "world"]
```

```rl
dec arr[float] vals  = [1.0, 2.0, 3.0]
```

```rl
dec arr[char]  chars = ['.', 'r', 'l']
```

```rl
dec arr[bool] bools = [true, false, true]
```

access an element by index with `arr[i]` zero-based

```rl
dec arr[int] nums = [10, 20, 30]
println(nums[0])  // 10
println(nums[2])  // 30
```

assign to an index with `arr[i] = value`

```rl
dec arr[int] nums = [1, 2, 3]
nums[1] = 99
println(nums)  // [1, 99, 3]
```

arrays are typed and all elements must be the same type

```rl
dec arr[int] nums = [1, 2, 3]
// dec arr[int] bad = [1, "two"]  // error: type mismatch
```

nested arrays are supported

```rl
dec arr[arr[int]] matrix = [[1, 2], [3, 4]]
println(matrix[0][1])  // 2
```