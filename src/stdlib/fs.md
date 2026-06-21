
# std::fs

functions for working with the filesystem

## `copy_file(src, dst)`

copies a file from src to dst, returns the number of bytes copied

```rl
get std::fs::copy_file

copy_file("a.txt", "b.txt") // 1024
```

## `file_modified(path)`

returns the last modification time of the file as a unix timestamp (seconds since epoch)

```rl
get std::fs::file_modified

file_modified("./Cargo.toml") // 1750000000
```

## `file_size(path)`

returns the size of the file in bytes

```rl
get std::fs::file_size

file_size("./Cargo.toml") // 215
```

## `list_dir(path)`

returns an array of paths for the entries in the directory

```rl
get std::fs::list_dir

list_dir("./src") // ["./src/main.rl", "./src/html_tags"]
```

## `mkdir(path)`

creates a directory, fails if the parent directory does not exist

```rl
get std::fs::mkdir

mkdir("./build")
```

## `mkdir_all(path)`

creates a directory along with any missing parent directories

```rl
get std::fs::mkdir_all

mkdir_all("./build/assets/css")
```

## `move_file(src, dst)`

moves a file from src to dst

```rl
get std::fs::move_file

move_file("/tmp/a.txt", "/tmp/b.txt")
```

## `rename_file(path, new_name)`

renames a file, keeping it in its current directory, and returns the new path

```rl
get std::fs::rename_file

rename_file("/usr/bin/rl", "rl-old") // "/usr/bin/rl-old"
```

## `rmdir(path)`

removes an empty directory, fails if it is not empty

```rl
get std::fs::rmdir

rmdir("./build")
```

## `rmdir_all(path)`

removes a directory and all of its contents recursively

```rl
get std::fs::rmdir_all

rmdir_all("./build")
```

## `temp_dir()`

returns the path of the system's temporary directory

```rl
get std::fs::temp_dir

temp_dir() // "/tmp"
```

