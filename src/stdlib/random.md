# std::random

functions for random number and value generation

## `rand_int()`

returns a random int across the full int range

```rl
get std::random::rand_int

rand_int() // 4650267523947147985
```

## `rand_int_range(min, max)`

returns a random int between min and max (inclusive)

```rl
get std::random::rand_int_range

rand_int_range(1, 6) // 4
```

## `rand_float()`

returns a random float between 0.0 and 1.0

```rl
get std::random::rand_float

rand_float() // 0.3528
```

## `rand_float_range(min, max)`

returns a random float between min and max

```rl
get std::random::rand_float_range

rand_float_range(1.0, 2.0) // 1.5124
```

## `rand_bool()`

returns a random bool, using an internally randomized probability

```rl
get std::random::rand_bool

rand_bool() // true
```

## `rand_bool_weighted(probability)`

returns a random bool that is true with the given probability (0.0 to 1.0) values smaller than 0.0 will be 0.0 and values bigger than 1.0 will be 1.0

```rl
get std::random::rand_bool_weighted

rand_bool_weighted(0.8) // true
```

## `rand_dice(sides)`

rolls a single die with the given number of sides and returns the result

```rl
get std::random::rand_dice

rand_dice(6) // 5
```

## `rand_dices(count, sides)`

rolls count dice with the given number of sides and returns the individual results as an array

```rl
get std::random::rand_dices

rand_dices(3, 6) // [4, 1, 6]
```

## `rand_range(stop)`

returns a random int from 0 to stop (exclusive), stop must be greater than zero

```rl
get std::random::rand_range

rand_range(10) // 7
```

## `rand_range_step(start, end, step)`

returns a random int from start to end, aligned to step; reaches end only if step divides (end - start) evenly, otherwise caps at the highest reachable multiple below end

```rl
get std::random::rand_range_step

rand_range_step(0, 9, 2) // 8 (max possible, since 9 isn't reachable)
```

## `rand_choice(arr)`

returns a random element from the array

```rl
get std::random::rand_choice

rand_choice([1, 2, 3]) // 1
```

## `rand_choices(arr, count)`

returns an array of count random elements from arr, with replacement

```rl
get std::random::rand_choices

rand_choices([1, 2, 3], 5) // [1, 1, 3, 1, 1]
```

## `rand_sample(arr, count)`

returns an array of count random elements from arr, without replacement (count must not exceed arr's length)

```rl
get std::random::rand_sample

rand_sample([1, 2, 3, 4], 2) // [4, 2]
```

## `rand_shuffle(arr)`

returns the array with its elements in random order

```rl
get std::random::rand_shuffle

rand_shuffle([1, 2, 3, 4, 5]) // [3, 5, 1, 4, 2]
```

## `rand_byte()`

returns a random byte (0 to 255)

```rl
get std::random::rand_byte

rand_byte() // 110
```

## `rand_bytes(count)`

returns an array of count random bytes

```rl
get std::random::rand_bytes

rand_bytes(4) // [226, 232, 81, 178]
```

## `rand_char()`

returns a random printable ascii character (32 to 126)

```rl
get std::random::rand_char

rand_char() // 'c'
```

## `rand_string(count)`

returns a random printable ascii string of the given length

```rl
get std::random::rand_string

rand_string(8) // "oNU7'=^:"
```

