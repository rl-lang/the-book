# Entry points

source files work as scripts when no entry function is present

if a file declares `fn main()`, `rl run` registers declarations and runs `main()` instead of evaluating top-level expressions

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