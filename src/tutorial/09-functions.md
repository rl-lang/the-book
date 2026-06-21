# 9. Functions

declare with `fn <name>(<type> <param>, ...) -> <type> { <body> }`

```rl
fn add(int a, int b) -> int {
    return a + b
}
println(add(3, 4)) // 7
```

functions are first-class values and can be stored in variables

```rl
fn double(int x) -> int {
    return x * 2
}
dec fn f = double
println(f(5)) // 10
```

---

[<- Previous: For Loops](Tutorial-For-Loops) · [Tutorial](Tutorial) · [Next: Lambdas ->](Tutorial-Lambdas)
