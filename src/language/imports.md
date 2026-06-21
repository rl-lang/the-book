# Imports

import a single stdlib function with `get std::<module>::<function>`

```rl
get std::math::sqrt

sqrt(9.0)  // 3.0
```

import multiple stdlib functions with `get <fn1>, <fn2> from std::<module>`

```rl
get sin, cos from std::math

sin(0.0)  // 0.0
cos(0.0)  // 1.0
```

import a local file with `get <filename>` and loads `<filename>.rl` from the same directory

```rl
get utils
// loads utils.rl
```

import named items from a local file with `get <fn> from <path>::<file>`

```rl
get add from math::utils
// imports add from math/utils.rl
```