# 8. For Loops

C-style for loop: explicit init, condition, increment

```rl
dec int sum = 0
for [int j = 1, j < 6, j += 1] {
    sum += j
}
println(sum) // 15
```

range-based for loop: `for <var> in <start>..<end>` (exclusive)

```rl
dec int product = 1
for k in 1..5 {
    product *= k
}
println(product) // 24
```

iterable for loop walks an array directly

```rl
dec arr[int] evens = [2, 4, 6]
dec int even_sum = 0
for n in evens {
    even_sum += n
}
println(even_sum) // 12
```
