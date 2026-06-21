# std::path

functions for working with filesystem paths

## `path_exists(path)`

returns true if the path exists on the filesystem

```rl
get std::path::path_exists

path_exists("./Cargo.toml") // true
```

## `path_extension(path)`

returns the file extension of the path

```rl
get std::path::path_extension

path_extension("main.rl") // "rl"
```

## `path_filename(path)`

returns the final component of the path

```rl
get std::path::path_filename

path_filename("/usr/bin/rl") // "rl"
```

## `path_is_dir(path)`

returns true if the path is a directory

```rl
get std::path::path_is_dir

path_is_dir("./src") // true
```

## `path_is_file(path)`

returns true if the path is a file

```rl
get std::path::path_is_file

path_is_file("./Cargo.toml") // true
```

## `path_join(path, other)`

joins two paths together

```rl
get std::path::path_join

path_join("src", "main.rl") // "src/main.rl"
```

## `path_parent(path)`

returns the parent directory of the path

```rl
get std::path::path_parent

path_parent("/usr/bin/rl") // "/usr/bin"
```

## `path_pop(path)`

removes the last component of the path and returns the result

```rl
get std::path::path_pop

path_pop("/usr/bin/rl") // "/usr/bin"
```

## `path_push(path, target)`

appends a component to the path and returns the result

```rl
get std::path::path_push

path_push("/usr/bin", "rl") // "/usr/bin/rl"
```

## `path_set_extension(path, extension)`

sets or replaces the extension of the path and returns the result

```rl
get std::path::path_set_extension

path_set_extension("main.rl", "txt") // "main.txt"
```

## `path_stem(path)`

returns the filename without its extension

```rl
get std::path::path_stem

path_stem("main.rl") // "main"
```

