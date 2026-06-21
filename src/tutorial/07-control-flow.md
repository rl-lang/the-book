# 7. Control Flow

`if` / `else if` / `else` branch on conditions

```rl
dec int score = 75
if (score >= 90) {
    println("A")
} else if (score >= 75) {
    println("B")
} else {
    println("F")
}
```

`while` loops as long as the condition is true

```rl
dec int i = 0
while (i < 3) {
    println(i)
    i += 1
}
```

`break` exits a loop early, `continue` skips to the next iteration

```rl
dec int i = 0
while (i < 5) {
    i += 1
    if (i == 3) { continue }
    println(i) // 1 2 4 5
}
```

---

[<- Previous: Operators](Tutorial-Operators) · [Tutorial](Tutorial) · [Next: For Loops ->](Tutorial-For-Loops)