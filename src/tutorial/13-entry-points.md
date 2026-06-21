# 13. Entry Points

source files work as scripts when no entry function is present

```rl
get println from std::io

println("hello") // runs top to bottom, no main() needed
```

if a file declares `fn main()`, `rl run` registers declarations and runs `main()` instead

```rl
fn main() {
    std::io::println("hello")
}
```

a different zero-argument function can be selected as the entry point with `!#[entry]`

```rl
!#[entry]
fn start() {
    std::io::println("hello")
}
```

---

[<- Previous: Imports](Tutorial-Imports) · [Tutorial](Tutorial) · [Next: std::math ->](Tutorial-Std-Math)
