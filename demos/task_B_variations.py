"""Task B demo: vary array size, seed and range; verify the sin^2 + cos^2 identity."""

# Mathematical Functions and Vectorization

import numpy as np
import timeit


def run(n, seed=42, lo=5, hi=250):
    rng = np.random.default_rng(seed)
    lat = rng.uniform(lo, hi, n)

    def loop():
        sq = []
        for v in lat:
            s = v / 1000.0
            sq.append(s ** 2)
        return sq

    def vec():
        s = lat / 1000.0
        return s ** 2

    lt = timeit.timeit(loop, number=1)
    vt = timeit.timeit(vec, number=3) / 3
    same = np.allclose(vec(), np.array(loop()))
    print(f"n={n:>9,} range=({lo},{hi}) seed={seed} first3={vec()[:3]} "
          f"loop={lt:.4f}s vec={vt:.6f}s speedup={lt/vt:.1f}x identical={same}")


run(10)
run(1_000)
run(100_000)
run(1_000_000)
run(1_000_000, seed=7)
run(1_000_000, lo=100, hi=500)

# Mathematical concept: sin and the identity sin^2 + cos^2 = 1
x = np.array([0, np.pi / 2, np.pi])
print("sin(x):", np.round(np.sin(x), 6))
print("sin^2 + cos^2:", np.sin(x) ** 2 + np.cos(x) ** 2)

x = np.linspace(0, 10, 1_000_000)
print("Identity holds for 1M values:", np.allclose(np.sin(x) ** 2 + np.cos(x) ** 2, 1))
