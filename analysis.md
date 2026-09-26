# Lab 3 Analysis

## Environment and recorded timings

- Python version: [enter version]
- Multiprocessing start method: [enter value printed by the script]
- Available CPU count reported by the script: [enter value]
- Number of tasks: [enter value]
- Pool size used: [enter value]
- Sequential execution time: [enter time] s
- Parallel execution time: [enter time] s
- Speedup (Sequential / Parallel): [enter value]×
- Result verification passed: [yes/no]

## Analysis questions

1. **Speedup calculation**
   Compute `Sequential Time / Parallel Time`. Did you observe a meaningful speedup? If not, explain why a parallel implementation can legitimately be slower.

2. **Reason processes can help**
   Explain why a process pool can execute CPU-bound Python work concurrently across CPU resources. Contrast this with normal GIL-enabled CPython threading.

3. **`Pool.map` behaviour**
   Describe advantages of `Pool.map` for data-parallel tasks compared with creating and joining many `multiprocessing.Process` objects manually. What order are the returned results in?

4. **Overheads**
   Explain how process startup/teardown, pickling and IPC, task scheduling, result transfer, and load imbalance can limit scaling.

5. **Pool size**
   Explain why using more worker processes than available CPU resources or useful tasks can increase overhead rather than improve performance.

6. **Correctness verification**
   Why should the sequential and parallel result lists be compared before interpreting the timing results?
