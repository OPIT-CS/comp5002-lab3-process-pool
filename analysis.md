# Lab 3 Analysis

## Recorded timings

- Pool size used: [enter number, e.g., os.cpu_count()]
- Sequential execution time: [enter time] s
- Parallel execution time (map): [enter time] s
- Speedup (Sequential / Parallel): [enter value]×

## Analysis questions

1. **Speedup calculation**  
   Compute `Sequential Time / Parallel Time`. Did you observe a meaningful speedup?

2. **Reason for speedup**  
   Explain why `multiprocessing.Pool` can speed up CPU-bound work while `threading` typically cannot under the GIL (separate processes, separate interpreters).

3. **`Pool.map` vs manual processes**  
   Describe advantages of `Pool.map` for data-parallel tasks compared with creating/joining many `multiprocessing.Process` objects manually.

4. **Overheads**  
   List overheads that limit linear scaling: process start-up/teardown, pickling and IPC data transfer, task scheduling/coordination, load imbalance.
