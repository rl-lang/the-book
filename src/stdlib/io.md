# std::io

functions for input and output

## `read()`

read a line from stdin

```rl
get std::io::read

dec str name = read()
```

## `read(prompt)`

prints prompt and reads a line from stdin

```rl
get std::io::read

dec str name = read("enter your name: ")
```

## `read_int()`

read a line from stdin then parses to integer

```rl
get std::io::read_int

dec int age = read()
```

## `read_int(prompt)`

prints prompt and reads a line from stdin then parses to integer

```rl
get std::io::read_int

dec int age = read_float("enter your age: ")
```

## `read_float()`

read a line from stdin then parses to float

```rl
get std::io::read_float

dec float pi = read_float()
```

## `read_float(prompt)`

prints prompt and reads a line from stdin then parses to float

```rl
get std::io::read_float

dec float pi = read_float("enter your pi: ")
```

## `append_file(path, content)`

appends content to a file creating it if it does not exist

```rl
get std::io::append_file

append_file("info.txt", "name: Mohamed")
```

## `delete_file(path)`

deletes a file at the given path

```rl
get std::io::delete_file

delete_file("info.txt")
```

## `read_file(path)`

reads the entire contents of a file as a string

```rl
get std::io::read_file

dec string data = read_file("backup_info.txt")
```

## `read_lines(path)`

reads a file and returns its lines as an array of strings

```rl
get std::io::read_lines

dec arr[string] data = read_lines("index.html")
```

## `write_file(path, contents)`

writes content to a file overwriting it if it already exists

```rl
get std::io::write_file

write_file("index.html", "<p>hello \"Mohamed\"</p>")
```

## `print(x)`

print without newline

```rl
get std::io::print

print("hello")
```

## `println(x)`

print with newline

```rl
get std::io:println

println("hello")
```

## `eprint(string)`

halts evaluation with an error containing the given message

```rl
get std::io::eprint

eprint("something went wrong") // x error: something went wrong
```