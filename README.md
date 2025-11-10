# COMP-5002 – Lab 3 • Parallel Computation with Process Pools

**Module** Module 4. Parallelism via Multiprocessing  
**Objective** Build a parallel program using `multiprocessing.Pool` to accelerate a CPU-bound task and compare against sequential execution.

## Prerequisites

- Python 3 installed.
- Git installed and basic familiarity with `clone`, `add`, `commit`, `push`.
- Concepts from Module 4:
  - Why multiprocessing helps CPU-bound work under the GIL.
  - Process creation (`multiprocessing.Process`).
  - Process pools (`multiprocessing.Pool`) and `map`.
  - Pool lifecycle (`with` context, `close`, `join`).
  - Pickling for inter-process communication.

## Files Provided

- `README.md` this file
- `lab3_parallel_map.py` starter with function skeletons and a `main` block
- `analysis.md` where you record timings and answers

## Tasks

**General instructions**

- Clone your GitHub Classroom repository.
- Modify `lab3_parallel_map.py` to complete the tasks.
- Adjust constants if runs are too short or too long on your machine.
- Record results in `analysis.md`.
- Commit frequently and push before the deadline.

---

### Task 1 — Implement the CPU-intensive task

1. Open `lab3_parallel_map.py`.
2. In `cpu_intensive_task(n)`, implement a non-trivial CPU calculation (for example `math.factorial(n)` or an arithmetic loop).

---

### Task 2 — Implement sequential execution

1. In `run_sequential(data)`, iterate over `data`, call `cpu_intensive_task` for each element, collect results, and return them.

---

### Task 3 — Implement parallel execution with `Pool.map`

1. In `run_parallel_map(data, pool_size)`, create a pool with `pool_size` processes using a `with` block.
2. Apply `pool.map(cpu_intensive_task, data)` and return the result list.

---

### Task 4 — Run and record timings

1. Review the `main` block to see how timing is measured.
2. Run `python lab3_parallel_map.py`.
3. Record **Sequential execution time**, **Parallel execution time (map)**, and **Pool size** in `analysis.md`.

---

### Task 5 — Analysis (`analysis.md`)

1. **Speedup** Compute `Sequential / Parallel` and note whether speedup is significant.  
2. **Why processes help** Explain why processes can speed up CPU-bound work while threads typically do not under the GIL.  
3. **`Pool.map` vs manual processes** State benefits of `map` for data-parallel workloads.  
4. **Overheads** List sources of overhead that limit linear scaling (process start-up, pickling, scheduling).

---

## Submission

1. Ensure `lab3_parallel_map.py` runs and prints timing output.
2. Ensure `analysis.md` includes your recorded timings and answers.
3. Stage: `git add lab3_parallel_map.py analysis.md` (or `git add .`)
4. Commit: `git commit -m "Complete Lab 3 Parallel Map"`
5. Push: `git push origin main` (or your default branch)
6. Verify on GitHub that `lab3_parallel_map.py` and `analysis.md` are updated.
