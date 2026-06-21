# std::math

functions for math

## `abs(number)`

returns the absolute value of number

```rl
get std::math::abs

dec int x = -1
x.abs() // 1
```

## `acos(x)`

arc cosine of x in radians

```rl
get std::math::acos

acos(1.0) // 0.0
```

## `asin(x)`

arc sine of x in radians

```rl
get std::math::asin

asin(1.0) // 1.5707...
```

## `atan(x)`

arc tangent of x in radians

```rl
get std::math::atan

atan(1.0) // 0.7853...
```

## `atan2(a, b)`

arc tangent of a/b using signs to determine quadrant

```rl
get std::math::atan2

atan2(1.0, 1.0) // 0.7853...
```

## `ceil(x)`

smallest integer greater than or equal to x

```rl
get std::math::ceil

ceil(2.12) // 3.0
```

## `clamp(x, min, max)`

clamps x between min and max, returning min if x < min, max if x > max

```rl
get std::math::clamp

clamp(12, 15, 20) // 15
```

## `cos(x)`

cosine of x in radians

```rl
get std::math::cos

cos(0.0) // 1.0
```

## `degrees(x)`

convert radians to degrees

```rl
get std::math::degrees

degrees(3.14159) // 180.0
```

## `exp(x)`

e raised to the power x

```rl
get std::math::exp

exp(1.0) // 2.718...
```

## `factorial(x)`

product of all integers from 1 to x

```rl
get std::math::factorial

factorial(5) // 120
```

## `fibonacci(x)`

xth fibonacci number

```rl
get std::math::fibonacci

fibonacci(7) // 13
```

## `floor(x)`

largest integer less than or equal to x

```rl
get std::math::floor

floor(1.23) // 1.0
```

## `gcd(a, b)`

greatest common divisor of a and b

```rl
get std::math::gcd

gcd(12, 8) // 4
```

## `hypot(a, b)`

length of the hypotenuse given two sides: √(a² + b²)

```rl
get std::math::hypot

hypot(3.0, 4.0) // 5.0
```

## `is_prime(x)`

true if x is a prime number

```rl
get std::math::is_prime

is_prime(7) // true
```

## `lcm(a, b)`

least common multiple of a and b

```rl
get std::math::lcm

lcm(4, 6) // 12
```

## `lerp(x, y, t)`

linear interpolation between x and y by factor t

```rl
get std::math::lerp

lerp(0.0, 10.0, 0.5) // 5.0
```

## `log(x, base)`

logarithm of x in the given base

```rl
get std::math::log

log(100.0, 10.0) // 2.0
```

## `log2(x)`

base-2 logarithm of x

```rl
get std::math::log2

log2(8.0) // 3.0
```

## `log10(x)`

base-10 logarithm of x

```rl
get std::math::log10

log10(1000.0) // 3.0
```

## `map_range(x, in_min, in_max, out_min, out_max)`

re-map x from one range to another

```rl
get std::math::map_range

map_range(5.0, 0.0, 10.0, 0.0, 100.0) // 50.0
```

## `max(a, b)`

returns the larger of a and b

```rl
get std::math::max

max(4, 6) // 6
```

## `min(a, b)`

returns the smaller of a and b

```rl
get std::math::min

min(4, 6) // 4
```

## `mod(a, b)`

remainder of a divided by b

```rl
get std::math::mod

mod(10, 3) // 1
```

## `pow(a, b)`

raises a to the power of b

```rl
get std::math::pow

pow(2, 2) // 4.0
```

## `radians(x)`

convert degrees to radians

```rl
get std::math::radians

radians(180.0) // 3.14159...
```

## `round(x)`

rounds x to the nearest integer

```rl
get std::math::round

round(2.2) // 2.0
```

## `sign(x)`

returns -1, 0, or 1 based on the sign of x

```rl
get std::math::sign

sign(-5) // -1
```

## `sin(x)`

sine of x in radians

```rl
get std::math::sin

sin(0.0) // 0.0
```

## `sqrt(x)`

square root of x

```rl
get std::math::sqrt

sqrt(4) // 2.0
```

## `tan(x)`

tangent of x in radians

```rl
get std::math::tan

tan(0.0) // 0.0
```
