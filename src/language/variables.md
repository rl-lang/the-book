# Variables

declare a mutable variable with `dec <type> <name> = <value>`

```rl
dec int x = 10
dec float y = 3.14
dec bool flag = true
dec string name = "Mohamed"
dec char c = 'a'
```

reassign a mutable variable with `=`

```rl
dec int x = 1
x = 2
```

compound assignment: `+=`, `-=`, `*=`, `/=`

```rl
dec int x = 10
x += 5   // 15
x -= 3   // 12
x *= 2   // 24
x /= 4   // 6
```