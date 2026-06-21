# For Loops

C-style for loop: `for [<type> <var> = <init>, <condition>, <increment>] { }`

```rl
for [int i = 0, i < 5, i += 1] {
    println(i)
}
```

range-based for loop iterates from start to end (exclusive): `for <var> in <start>..<end>`

```rl
for i in 0..5 {
    println(i)  // 0 1 2 3 4
}
```

iterate over an inline array literal

```rl
for x in [10, 20, 30] {
    println(x)
}
```

iterate over an array variable with `for <var> in <array>`

```rl
dec arr[string] names = ["ali", "bob", "carl"]

for name in names {
    println(name)
}
```