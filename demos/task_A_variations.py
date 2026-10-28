"""Task A demo: same logic as code/Task_02_numpy_arrays.py, run on different inputs."""

# NumPy Arrays and Numerical Computation

import numpy as np


def analyse(name, temps):
    t = np.array(temps)
    f = 1.8 * t + 32
    print(f"--- {name} ---")
    print(f"Readings: {len(t)}")
    print(f"Mean: {np.mean(t):.2f} C | Min: {np.min(t):.2f} C | Max: {np.max(t):.2f} C")
    print("First six F:", f[:6])


original = [18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
            29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0]

analyse("Original", original)
analyse("Simple case [20,22,24,26]", [20, 22, 24, 26])
analyse("Cold day (original - 15)", [x - 15 for x in original])
analyse("Constant 25 C", [25.0] * 24)
analyse("One outlier (sensor fault 80 C)", original[:11] + [80.0] + original[12:])
analyse("Freezing/negative", [-5, -3, 0, 2, -1, -4])

x = np.array([1, 2, 3])
print("x**2 =", x ** 2)
