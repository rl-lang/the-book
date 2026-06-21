# 10. Lambdas

anonymous functions, defined inline with `fn(<type> <param>, ...) { <body> }`

```rl
dec fn square = fn(int x) -> int {
    return x * x
}
println(square(5)) // 25
```

closures capture variables from the surrounding scope

```rl
dec int factor = 3
dec fn triple = fn(int x) -> int {
    return x * factor
}
println(triple(4)) // 12
```
