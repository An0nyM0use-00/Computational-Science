# Simple Bisection Method Root Finder

A Python implementation of the bisection method to approximate the root of a continuous function.

## How It Works

1. You enter a mathematical function as a string (e.g., `x**2 - 4`).
2. You provide an interval `[a, b]` where the function changes sign.
3. The program repeatedly halves the interval until it approximates the root.
4. It outputs the root and the value of the function at that root.

## How To Use

1. Run the program.
2. Enter a function in terms of `x` (e.g., `x**3 + x - 1`).
3. Enter the start (`a`) and end (`b`) of the interval.
4. See the computed approximate root and the function value at that root.

### Example Run

1. Enter function: `x**2 - 4`
2. Enter a: `0`
3. Enter b: `5`
4. Output:
  - Approximate root: x ≈ 2.0000000002328306
  - f(x) at root: 0.0
