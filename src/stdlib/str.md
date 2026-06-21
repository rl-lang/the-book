# std::str

functions for string manipulation

## `bytes(str)`

returns an int array of the UTF-8 byte values of each character

```rl
get std::str::bytes

bytes("hi") // [104, 105]
```

## `char_at(str, index)`

returns the character at the given index

```rl
get std::str::char_at

char_at("hello", 1) // 'e'
```

## `chars(str)`

returns a char array of each character in the string

```rl
get std::str::chars

chars("hi") // ['h', 'i']
```

## `concat(a, b, ...)`

concatenates any number of values into a single string

```rl
get std::str::concat

concat("hello", " ", "world") // hello world
```

## `contains(str, sub)`

true if str contains the substring sub

```rl
get std::str::contains

contains("hello", "ell") // true
```

## `count(str, sub)`

returns the number of non-overlapping occurrences of sub in str

```rl
get std::str::count

count("banana", "an") // 2
```

## `ends_with(str, sub)`

true if str ends with sub

```rl
get std::str::ends_with

ends_with("hello", "lo") // true
```

## `index_of(str, sub)`

returns the character index of the first occurrence of sub, or -1 if not found

```rl
get std::str::index_of

index_of("hello", "ll") // 2
```

## `is_empty(str)`

true if the string has no characters

```rl
get std::str::is_empty

is_empty("") // true
```

## `join(arr, delim)`

joins an array into a string with delim between each element

```rl
get std::str::join

join(["a", "b", "c"], "-") // a-b-c
```

## `pad_left(str, width, char)`

pads str on the left with char until the total length reaches width

```rl
get std::str::pad_left

pad_left("5", 3, '0') // 005
```

## `pad_right(str, width, char)`

pads str on the right with char until the total length reaches width

```rl
get std::str::pad_right

pad_right("hi", 5, '.') // hi...
```

## `repeat(str, count)`

returns str repeated count times

```rl
get std::str::repeat

repeat("ab", 3) // ababab
```

## `replace(str, from, to)`

replaces all occurrences of from with to in str

```rl
get std::str::replace

replace("foo bar foo", "foo", "baz") // baz bar baz
```

## `reverse(str)`

returns str with characters in reverse order

```rl
get std::str::reverse

reverse("hello") // olleh
```

## `slice(str, start, end)`

returns a substring from start to end (exclusive)

```rl
get std::str::slice

slice("hello", 1, 4) // ell
```

## `split(str, delim)`

splits str by delim and returns a string array

```rl
get std::str::split

split("a,b,c", ",") // ["a", "b", "c"]
```

## `starts_with(str, sub)`

true if str starts with sub

```rl
get std::str::starts_with

starts_with("hello", "he") // true
```

## `to_lower(str)`

returns str with all characters converted to lowercase

```rl
get std::str::to_lower

to_lower("HELLO") // hello
```

## `to_upper(str)`

returns str with all characters converted to uppercase

```rl
get std::str::to_upper

to_upper("hello") // HELLO
```

## `trim(str)`

removes leading and trailing whitespace from str

```rl
get std::str::trim

trim("  hi  ") // hi
```

## `trim_end(str)`

removes trailing whitespace from str

```rl
get std::str::trim_end

trim_end("hi  ") // hi
```

## `trim_start(str)`

removes leading whitespace from str

```rl
get std::str::trim_start

trim_start("  hi") // hi
```

## `format(template, ...)`

replaces each "{}" in template with the corresponding argument, in order

```rl
get std::str::format

format("{} is {}", "age", 30) // age is 30
```
