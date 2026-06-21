# 3. Constants

declare an immutable value with `CONST <type> <name> = <value>`, convention is UPPER_CASE

```rl
CONST int MAX_RETRIES = 3
CONST string LANG = "rl"
println(MAX_RETRIES, LANG) // 3 rl
```

constant arrays use `CONST arr[<type>]`

```rl
CONST arr[int] PRIMES = [2, 3, 5, 7, 11]
println(PRIMES[0]) // 2
```

---

[<- Previous: Variables](Tutorial-Variables) · [Tutorial](Tutorial) · [Next: Types ->](Tutorial-Types)