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

---

[<- Previous: std::fs](Tutorial-Std-Fs) · [Tutorial](Tutorial)

That's the full tour - you've seen every language feature and stdlib module rl has to offer.

**Next steps:**
- Browse the [Language Concepts](Home) and [Standard Library](Home) reference tables for quick lookups
- Check out the [GitHub Repository](https://github.com/rl-lang/rl-lang) and try writing your own `.rl` file
- Hit a bug or have a question? [Report an Issue](https://github.com/rl-lang/rl-lang/issues)
