# Constants

declare a constant with `CONST <type> <name> = <value>` but it cannot be reassigned, convention is UPPER_CASE (but anything works)

```rl
CONST int    MAX_SIZE  = 100
```

```rl
CONST float  EULER     = 2.71828
```

```rl
CONST bool   DEBUG     = false
```

```rl
CONST string LANG      = "rl"
```

```rl
CONST char   NEWLINE   = '\n'
```

constant arrays use `CONST arr[<type>]`

```rl
CONST arr[int]    PRIMES = [2, 3, 5, 7, 11]
```

```rl
CONST arr[string] DAYS   = ["sat", "sun", "mon"]
```
