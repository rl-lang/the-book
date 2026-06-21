# Control Flow

`if` runs a block when the condition is true

```rl
dec int x = 10

if (x > 5) {
    println("big")
}
```

`else if` and `else` add additional branches

```rl
dec int x = 5

if (x > 10) {
    println("big")
} else if (x == 5) {
    println("five")
} else {
    println("small")
}
```

`while` loops as long as the condition is true

```rl
dec int i = 0

while (i < 5) {
    println(i)
    i += 1
}
```

`break` exits a loop early, `continue` skips to the next iteration

```rl
dec int i = 0
while (true) {
    if (i == 3) { break }
    i += 1
}
```

```rl
dec int i = 0
while (i < 5) {
    i += 1
    if (i == 3) { continue }
    println(i)  // prints 1, 2, 4, 5
}
```