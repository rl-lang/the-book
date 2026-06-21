# Lambdas

lambdas are anonymous functions defined inline with `fn(<type> <param>, ...) { <body> }`

```rl
dec fn square = fn(int x) -> int {
    return x * x
}

println(square(5))  // 25
```

lambdas capture variables from their surrounding scope (closures)

```rl
dec int factor = 3

dec fn triple = fn(int x) -> int {
    return x * factor
}

println(triple(4))  // 12
```