# std::types

functions for type checking and conversion

## `is_bool(x)`

true if x is a bool

```rl
get std::types::is_bool

is_bool(true) // true
```

## `is_char(x)`

true if x is a char

```rl
get std::types::is_char

is_char('a') // true
```

## `is_float(x)`

true if x is a float

```rl
get std::types::is_float

is_float(3.14) // true
```

## `is_int(x)`

true if x is an int

```rl
get std::types::is_int

is_int(42) // true
```

## `is_null(x)`

true if x is null

```rl
get std::types::is_null

is_null(null) // true
```

## `is_string(x)`

true if x is a string

```rl
get std::types::is_string

is_string("hi") // true
```

## `to_bin(x)`

converts int, char, or string to a binary string representation

```rl
get std::types::to_bin

to_bin(10) // "1010"
```

## `to_bool(x)`

converts int, float, string, or null to bool — 0/0.0/""/null are false, everything else is true

```rl
get std::types::to_bool

to_bool(0) // false
```

## `to_char(x)`

converts an int (unicode codepoint) or single-character string to char

```rl
get std::types::to_char

to_char(65) // 'A'
```

## `to_float(x)`

converts int, bool, or numeric string to float

```rl
get std::types::to_float

to_float(3) // 3.0
```

## `to_hex(x)`

converts int, char, or string to a hexadecimal string representation

```rl
get std::types::to_hex

to_hex(255) // "ff"
```

## `to_int(x)`

converts float, bool, char, or string (including 0x hex strings) to int

```rl
get std::types::to_int

to_int("0xff") // 255
```

## `to_oct(x)`

converts int, char, or string to an octal string representation

```rl
get std::types::to_oct

to_oct(8) // "10"
```

## `to_string(x)`

converts int, float, bool, or char to string

```rl
get std::types::to_string

to_string(42) // "42"
```
