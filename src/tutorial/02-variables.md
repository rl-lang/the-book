# 2. Variables

declare a mutable variable with `dec <type> <name> = <value>`

```rl
dec bool   is_ready = true
dec int    count    = 1
dec string label    = "rl"
dec float  ratio    = 1.5
dec char   letter   = 'x'
```

reassign with `=`, mutate in place with `+=`, `-=`, `*=`, `/=`

```rl
dec int count = 1
count += 4 // 5
count -= 2 // 3
count *= 3 // 9
count /= 3 // 3
```

---

[<- Previous: Comments](Tutorial-Comments) · [Tutorial](Tutorial) · [Next: Constants ->](Tutorial-Constants)