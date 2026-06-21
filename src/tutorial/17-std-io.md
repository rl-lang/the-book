# 17. std::io

console output with `print`/`println`, input with `read`/`read_int`/`read_float`

```rl
get println, read from std::io

println("hello")
dec string name = read("enter your name: ")
```

file I/O: reading, writing, and appending

```rl
get write_file, read_file, append_file from std::io

write_file("index.html", "<p>hello</p>")
append_file("info.txt", "name: Mohamed")
dec string data = read_file("backup_info.txt")
```
