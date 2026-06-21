# 4. Types

rl is statically typed: `int`, `float`, `bool`, `string`, `char`

```rl
dec int    x = 42
dec float  y = 3.14
dec bool   b = true
dec string s = "hello"
dec char   c = 'a'
```

std::types covers checking (`is_int`, `is_bool`, ...) and conversion (`to_int`, `to_float`, ...)

```rl
get is_int, to_int, to_string from std::types

println(is_int(42))      // true
println(to_int("0xff"))  // 255
println(to_string(42))   // "42"
```

base conversions: `to_bin`, `to_hex`, `to_oct`

```rl
get to_bin, to_hex, to_oct from std::types

println(to_bin(10)) // "1010"
println(to_hex(255)) // "ff"
println(to_oct(8)) // "10"
```
