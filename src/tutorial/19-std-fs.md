# 19. std::fs

inspect files and directories

```rl
get path_exists, file_size, list_dir from std::fs

println(path_exists("./Cargo.toml")) // true
println(file_size("./Cargo.toml"))   // 215
println(list_dir("./src"))           // ["./src/main.rl", ...]
```

create, copy, move, and clean up

```rl
get mkdir_all, copy_file, move_file, rmdir_all from std::fs

mkdir_all("./build/assets/css")
copy_file("a.txt", "b.txt") // 1024 (bytes copied)
move_file("/tmp/a.txt", "/tmp/b.txt")
rmdir_all("./build")
```
