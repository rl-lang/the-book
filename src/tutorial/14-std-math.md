# 14. std::math

core math: rounding, powers, roots, primes, sequences

```rl
get factorial, is_prime, fibonacci, pow, sqrt, mod from std::math

println(factorial(10)) // 3628800
println(fibonacci(15)) // 610
println(is_prime(97))  // true
println(pow(2, 2))     // 4.0
println(sqrt(4))       // 2.0
println(mod(10, 3))    // 1
```

trig functions operate in radians; `degrees`/`radians` convert between units

```rl
get sin, cos, degrees, radians from std::math

println(sin(0.0))         // 0.0
println(cos(0.0))         // 1.0
println(degrees(3.14159)) // 180.0
```

math constants live in std::math::consts and are called like functions

```rl
get PI, TAU, PHI, E from std::math::consts

println(PI())  // ~3.14159
println(TAU()) // ~6.283
println(PHI()) // ~1.618
println(E())   // ~2.718
```
