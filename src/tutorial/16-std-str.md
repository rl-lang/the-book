# 16. std::str

inspecting and searching strings

```rl
get contains, starts_with, ends_with, index_of from std::str

println(contains("hello", "ell"))    // true
println(starts_with("hello", "he"))  // true
println(index_of("hello", "ll"))     // 2
```

transforming strings

```rl
get to_upper, trim, replace, split, join from std::str

println("  hi  ".trim().to_upper()) // HI
println(replace("foo bar foo", "foo", "baz")) // baz bar baz
println(split("a,b,c", ",")) // ["a", "b", "c"]
println(join(["a", "b", "c"], "-")) // a-b-c
```

`format` substitutes `{}` placeholders in order

```rl
get format from std::str

println(format("{} is {}", "age", 30)) // age is 30
```
