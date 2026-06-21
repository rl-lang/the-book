# 6. Operators

arithmetic (`+ - * /`), grouping with `()` controls order

```rl
dec int x = (2 + 3) * 4 // 20
dec int y = 2 + 3 * 4   // 14
```

comparison (`== != < <= > >=`) always returns bool, logical `!` negates

```rl
println(5 == 5, 5 != 3, 3 < 10) // true true true
println(!true) // false
```

method-style call with `.` passes the value as the first argument

```rl
get arr_push from std::array
dec arr[int] nums = [1, 2, 3]
println(nums.arr_push(4)) // [1, 2, 3, 4]
```
