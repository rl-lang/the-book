# 18. std::path

build and inspect filesystem paths without touching the filesystem

```rl
get path_join, path_extension, path_stem, path_filename from std::path

println(path_join("src", "main.rl")) // "src/main.rl"
println(path_extension("main.rl"))    // "rl"
println(path_stem("main.rl"))         // "main"
println(path_filename("/usr/bin/rl")) // "rl"
```

---

[<- Previous: std::io](Tutorial-Std-Io) · [Tutorial](Tutorial) · [Next: std::fs ->](Tutorial-Std-Fs)
