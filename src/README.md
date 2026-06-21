<div align="center">
<img src="https://raw.githubusercontent.com/rl-lang/rl-lang/dev/logo-circle.svg" width="200">

# rl wiki

**rl** is a statically-typed interpreted language written in Rust with a clean syntax, a TUI REPL, and a growing standard library.
</div>

```rl
get println from std::display
get factorial, is_prime, fibonacci from std::math

println(factorial(10))   // 3628800
println(fibonacci(15))   // 610
println(is_prime(97))    // true
```

## Installation

**From source**
```bash
git clone https://github.com/rl-lang/rl-lang
cd rl-lang
cargo build --release
```

**Via cargo**
```bash
cargo install rl-lang
```

## Usage
```bash
rl run <file.rl>   # run a source file
rl repl            # start the TUI REPL
rl check <file.rl> # check for errors
rl docs            # print language reference
rl dev             # run project via rl.toml
rl new <name>      # create a new project
```

---

## New to rl?

Start with the [Tutorial](tutorial/index.md) - a step-by-step walkthrough of every language feature and stdlib module, in order.

---

## Language Concepts

| Page | Description |
|------|-------------|
| [Types](language/types.md) | Primitive types: int, float, bool, str, char |
| [Variables](language/variables.md) | Mutable variable declaration with `dec` |
| [Constants](language/constants.md) | Immutable values with `CONST` |
| [Arrays](language/arrays.md) | Typed arrays, indexing, and mutation |
| [Functions](language/functions.md) | Declaration, return types, first-class functions |
| [Lambdas](language/lambdas.md) | Anonymous functions and closures |
| [Control-Flow](language/control-flow.md) | if / else if / else / while / break / continue |
| [For-Loops](language/for-loops.md) | C-style, range, and iterable for loops |
| [Operators](language/operators.md) | Arithmetic, comparison, logical, method call |
| [Imports](language/imports.md) | Importing from stdlib and local files |
| [Comments](language/comments.md) | Single-line comments |
| [Null](language/null.md) | The null value |
| [Entry-Points](language/entry-points.md) | Script entry points: top-level execution, `fn main()`, and `!#[entry]` |

---

## Standard Library

| Page | Description |
|------|-------------|
| [std-io](stdlib/io.md) | `input`, `input(prompt)`, `print`, `println` |
| [std-math](stdlib/math.md) | Math functions: trig, log, rounding, primes, etc. |
| [std-math-consts](stdlib/math-consts.md) | Math constants: `PI()`, `E()`, `PHI()`, `TAU()`, etc. |
| [std-array](stdlib/array.md) | Array manipulation: len, push, pop, sort, slice, etc. |
| [std-str](stdlib/str.md) | String manipulation: split, join, trim, replace, etc. |
| [std-types](stdlib/types.md) | Type conversion and inspection: `to_int`, `is_bool`, etc. |
| [std-path](stdlib/path.md) | Path manipulation: join, extension, basename, etc. |
| [std-fs](stdlib/fs.md) | Filesystem operations: copy, move, mkdir, list_dir, etc. |
| [std-random](stdlib/random.md) | Random generation: ints, floats, bools, dice, shuffle, etc. |

---

## Editor Support

| Editor | Link |
|--------|------|
| VS Code | [vscode-rl](https://github.com/rl-lang/vscode-rl) — syntax highlighting |
| Neovim / Helix / Zed | [tree-sitter-rl](https://github.com/rl-lang/tree-sitter-rl) — Tree-sitter grammar |

---

## Resources

- [GitHub Repository](https://github.com/rl-lang/rl-lang)
- [Report an Issue](https://github.com/rl-lang/rl-lang/issues)