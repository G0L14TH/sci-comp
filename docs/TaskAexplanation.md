# Task A: NumPy Arrays and Numerical Computation

## Task overview
Store a group of numbers as one NumPy array and compute on all of it at once, without writing a loop for each value. A vector is a 1-D array; a matrix is a 2-D array.

## The existing solution
- Squaring: `x = [1,2,3]` gives `x**2 = [1,4,9]`.
- Mean: `[20,22,24,26]` has mean (20+22+24+26)/4 = 23 °C, which `np.mean` computes in one call.
- Problem: 24 hourly temperatures. Find the daily mean, minimum and maximum, and convert everything to Fahrenheit with F = 1.8C + 32.

## Code walkthrough
| Line | Purpose |
|---|---|
| `np.array([...])` | Converts the list into a NumPy array |
| `np.mean / np.min / np.max` | Reduce the array to a single number |
| `1.8 * temperatures_c + 32` | Converts all 24 values at once (vectorized) |
| `temperatures_f[:6]` | Slice: first six elements |
| `:.2f` | Format to 2 decimal places |

## Demonstration of changes
| Test case | Mean | Min | Max | Why |
|---|---|---|---|---|
| Original | 23.12 | 17.50 | 29.40 | baseline |
| `[20,22,24,26]` | 23.00 | 20.00 | 26.00 | matches the hand calculation |
| Cold day (all values - 15) | 8.12 | 2.50 | 14.40 | everything shifts by exactly 15; spread unchanged |
| Constant 25 | 25.00 | 25.00 | 25.00 | mean = min = max; every F value is 77 |
| One 80 °C sensor fault | 25.25 | 17.50 | 80.00 | the mean is sensitive to outliers; the min is not |
| Below zero `[-5,-3,0,2,-1,-4]` | -1.83 | -5.00 | 2.00 | 0 °C = 32 °F; formula works for negatives |

## Conclusion
One array plus whole-array expressions replaces loops for statistics and unit conversion. Results respond predictably to shifts and outliers.
