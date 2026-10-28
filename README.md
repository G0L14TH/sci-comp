# BIT 2118 Scientific Computing: NumPy Tasks

Explanations and demonstrations for two NumPy tasks.

| Task | Topic | Solution file | Explanation |
|---|---|---|---|
| A (Task 02) | NumPy arrays and numerical computation | `code/Task_02_numpy_arrays.py` | `docs/Task_02_explanation.md` |
| B (Task 03) | Mathematical functions and vectorization | `code/Task_03_vectorization.py` | `docs/Task_03_explanation.md` |

## Structure
```
.
├── code/    # the original solutions
├── demos/   # same logic run with modified inputs and variables
├── docs/    # explanation of each task
├── requirements.txt
└── README.md
```

## Setup
Requires Python 3.9+.
```bash
pip install -r requirements.txt
```

## Run
```bash
python code/Task_02_numpy_arrays.py
python code/Task_03_vectorization.py
python demos/task_02_variations.py
python demos/task_03_variations.py
```

## Notes
- Task 03 prints timings and a speed-up that vary by machine and run. Only the first five squared values are reproducible (seed 42).
- The Task 02 and Task 03 solution files follow the coursework solutions as provided.
