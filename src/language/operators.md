# Operators

arithmetic: `+`, `-`, `*`, `/`

```rl
dec int x = 10 + 5   // 15
```

```rl
dec int y = 10 - 3   // 7
```

```rl
dec int z = 4  * 3   // 12
```

```rl
dec int w = 10 / 2   // 5
```

comparison: `==`, `!=`, `<`, `<=`, `>`, `>=` and always return bool

```rl
5 == 5    // true
```

```rl
5 != 3    // true
```

```rl
3 < 10    // true
```

```rl
10 >= 10  // true
```

logical: `!`

```rl
!true           // false
```

unary negation with `-`

```rl
dec int x = 5
dec int y = -x  // -5
```

method-style call with `.` — calls a function with the value as first argument

```rl
get std::str::to_upper

dec string s = "hello"
s.to_upper()  // "HELLO"
```

```rl
get std::array::arr_push

dec arr[int] nums = [1, 2]
nums = nums.arr_push(3)  // [1, 2, 3]
```

grouping with `()` controls evaluation order

```rl
dec int x = (2 + 3) * 4  // 20
dec int y = 2 + 3 * 4    // 14
```