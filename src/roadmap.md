# Roadmap

## v0.1.2
- [x] statically typed interpreter
- [x] variables and constants (`dec`, `CONST`)
- [x] all primitive types (`int`, `float`, `bool`, `string`, `char`, `null`)
- [x] typed arrays with index access and mutation
- [x] control flow (`if`, `else if`, `else`, `while`, `break`, `continue`)
- [x] for loops (C-style, range, iterable)
- [x] functions with return types
- [x] first-class functions and lambdas (closures)
- [x] import system (`get`, `get from`, file imports)
- [x] TUI REPL (ratatui, syntax highlighting, multiline, history, commands)
- [x] `std::math` - full math library
- [x] `std::math::consts` - math constants
- [x] `std::display` - print, println, len
- [x] `std::io` - input std overhaul
- [x] `std::array` - push, pop, insert, remove, reverse, sort, concat, unique, sum, product, min_of, max_of, first, last, is_empty, fill, range, slice, contains, index_of, count, flatten
- [x] `std::str` - string manipulation
- [x] `std::types` - type conversion and inspection
- [x] ariadne error reporting with spans
- [x] VS Code syntax highlight extension
- [x] tree-sitter grammar
- [x] `rl new` / `rl dev` / `rl check` / `rl docs` CLI commands
- [x] Criterion benchmarks
- [x] LSP skeleton (diagnostics only)
- [x] small roadmap
- [x] `std::path` - path_join, path_parent, path_filename, path_absolute
- [x] `std::io`
- [x] string interpolation

### v0.1.4 - current

- [x] HOF array (`map`, `filter`, `reduce`, `sort_by`, `any`, `all`, `find`)
- [x] `if` collapse (merge `ConditionalBranch` + `Conditional` into one AST node)
- [x] `random` stdlib (`rand_int`, `rand_float`, `rand_bool`, `rand_choice`, `shuffle`)
- [ ] `time` stdlib (`now`, `year`, `month`, `day`, etc.)
- [ ] `process` stdlib (`args`, `exit`, `env`, `cwd`, `exec`, `sleep`, etc.)
- [ ] tuple type (`(string, int)` etc.)
- [ ] `arr_zip`
- [ ] `byte` operations
- [ ] `bitwise` stdlib (`bit_and`, `bit_or`, `bit_xor`, `bit_not`, `bit_shift_left`, `bit_shift_right`, etc.)
- [ ] `error` type
- [ ] `result` type
- [ ] `option` type
- [ ] refactor stdlib fns to return error values where applicable
- [ ] lexical addressing
- [ ] push v0.1.4
- [x] type checker
- [x] LSP: hover
- [x] simple entry points
- [x] tutorial

## long term
- [ ] better error messages (did you mean, type hints)
- [ ] LSP: completions
- [ ] structs (named fields, methods)
- [ ] enums (ADTs)
- [ ] `match` expression
- [ ] `std::env` - environment variables, args
- [ ] `std::process` - exec, pid, sleep
- [ ] LSP: go-to-definition, rename, find references
- [ ] `rl fmt` - formatter
- [ ] package / module system
- [ ] bytecode VM (`vm` feature)
- [ ] Cranelift JIT backend (`cranelift` feature)
- [ ] WASM target
- [ ] persistent REPL history file