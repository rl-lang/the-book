# 20. std::random

random ints, floats, and bools

```rl
get rand_int_range, rand_float, rand_bool from std::random

println(rand_int_range(1, 6)) // e.g. 4
println(rand_float())         // e.g. 0.3528
println(rand_bool())          // e.g. true
```

dice, array choice, and shuffling

```rl
get rand_dice, rand_choice, rand_shuffle from std::random

println(rand_dice(6))               // e.g. 5
println(rand_choice([1, 2, 3]))     // e.g. 2
println(rand_shuffle([1, 2, 3, 4])) // e.g. [3, 1, 4, 2]
```
