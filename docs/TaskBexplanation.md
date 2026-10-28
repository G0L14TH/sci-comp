# Task B: Mathematical Functions and Vectorization

## Task overview
Vectorization applies an operation to many values at once. The goal is to show it is simpler and much faster than a Python loop, with identical results.

## The existing solution
- Identity: sin²(x) + cos²(x) = 1 for every x; NumPy checks a whole vector in one expression.
- Example: `x = [0, π/2, π]` gives `sin(x) ≈ [0, 1, 0]`.
- Problem: 1,000,000 latency measurements (ms) must be converted to seconds and squared. A loop version and a vectorized version are timed with `timeit`.

## Code walkthrough
| Line | Purpose |
|---|---|
| `default_rng(42)` | Seeded generator, so values are reproducible |
| `rng.uniform(5, 250, 1_000_000)` | 1M latencies between 5 and 250 ms |
| `loop_version()` | One value at a time (slow) |
| `latency_ms / 1000.0`, `seconds ** 2` | Whole-array operations (fast) |
| `timeit.timeit(f, number=N)` | Total time for N runs; the vectorized time is divided by 3 for an average |

## Demonstration of changes
| Change | Approx. speed-up | Why |
|---|---|---|
| n = 10 | ~1x | too little work; overhead dominates |
| n = 1,000 | ~37x | loop cost starts to add up |
| n = 100,000 | ~73x | gap widens with size |
| n = 1,000,000 | ~50x | baseline |
| different seed | similar | new values, same amount of work |
| range 100–500 ms | similar | speed depends on count, not on values |

Timings vary by machine and run; the numbers above were measured once.

## Conclusion
Vectorized code gives the same answers with less code and far better speed on large data. The speed-up grows with array size.
