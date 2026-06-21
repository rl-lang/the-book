# Functions

declare a function with `fn <name>(<type> <param>, ...) { <body> }`

```rl
fn greet(string name) {
    println(name)
}

greet("Mohamed")
```

specify a return type with `-> <type>` and use `return` to return a value

```rl
fn add(int a, int b) -> int {
    return a + b
}

dec int result = add(3, 4)  // 7
```

functions are first-class values and can be stored in variables

```rl
fn double(int x) -> int {
    return x * 2
}

dec fn f = double
println(f(5))  // 10
```