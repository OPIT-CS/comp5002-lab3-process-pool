# COMP-5002 – Lab 3 • Parallel Computation with Process Pools

**Module** Module 4. Parallelism via Multiprocessing  
**Objective** Build a parallel program using `multiprocessing.Pool` to accelerate a CPU-bound task and compare it with sequential execution.

## Prerequisites

- Python 3 installed.
- Git installed and basic familiarity with `clone`, `add`, `commit`, `push`.
- Concepts from Module 4:
  - Why multiprocessing can help CPU-bound work.
  - Process creation (`multiprocessing.Process`).
  - Process pools (`multiprocessing.Pool`) and `map`.
  - Pool lifecycle and the `with` context manager.
  - Pickling and inter-process communication.
  - The need for an `if __name__ == "__main__":` guard in multiprocessing programs.

## Files Provided

- `README.md` this file
- `lab3_parallel_map.py` starter with function skeletons and a `main` block
- `analysis.md` where you record timings and answer the analysis questions

## Tasks

**General instructions**

- Clone your GitHub Classroom repository.
- Modify `lab3_parallel_map.py` to complete the tasks.
- Keep the supplied benchmark structure so sequential and parallel runs process the same data.
- Record results in `analysis.md`.
- Commit frequently and push before the deadline.

---

### Task 1 — Implement the CPU-intensive task

1. Open `lab3_parallel_map.py`.
2. Complete `cpu_intensive_task(n)` with a deterministic CPU-bound calculation.
3. A suitable implementation is `math.factorial(n)`.
4. Keep the worker function at module scope. Functions passed to a process pool must be serializable by the multiprocessing machinery.

Do not add sleeps or I/O to this function. The purpose of this lab is to measure CPU-bound parallelism.

---

### Task 2 — Implement sequential execution

In `run_sequential(data)`:

1. Process every value in `data` with `cpu_intensive_task`.
2. Preserve the input order.
3. Return the complete list of results.

The sequential run and the pool run must perform the same work.

---

### Task 3 — Implement parallel execution with `Pool.map`

In `run_parallel_map(data, pool_size)`:

1. Create a `multiprocessing.Pool` with `pool_size` workers using a `with` block.
2. Apply `pool.map(cpu_intensive_task, data)`.
3. Return the complete result list.

Do not create one process manually for every input value. This task is specifically about process pools.

---

### Task 4 — Run and verify

1. Run `python lab3_parallel_map.py`.
2. The script reports:
   - Python version;
   - multiprocessing start method;
   - number of tasks;
   - pool size;
   - sequential time;
   - parallel time;
   - speedup.
3. The script also verifies that the sequential and parallel result lists are identical.
4. If your machine is unusually slow or fast, you may adjust `VALUES_UPPER_BOUND` modestly. Keep `NUMBER_LIST_SIZE` large enough to provide multiple tasks to the pool.

The supplied defaults are intended to make process-pool overhead small enough for the experiment to be meaningful while keeping runtime practical on typical student hardware. A speedup is not guaranteed on every machine.

---

### Task 5 — Analysis (`analysis.md`)

Answer the following:

1. **Speedup** Compute `Sequential / Parallel`. Interpret the result, including the possibility of no speedup.
2. **Why processes can help** Explain how separate Python processes can execute CPU-bound work concurrently and how this differs from normal GIL-enabled threading.
3. **`Pool.map`** Explain why `Pool.map` is convenient for data-parallel workloads and what ordering guarantee it provides.
4. **Overheads** Identify process startup, task scheduling, serialization/pickling, inter-process data transfer, result collection, and load imbalance.
5. **Pool size** Explain why creating more worker processes than useful CPU resources or tasks can reduce performance.
6. **Correctness** Explain why timing alone is insufficient and why the sequential and parallel outputs must be checked for equality.

---

## Submission

1. Ensure `lab3_parallel_map.py` runs successfully and the result verification passes.
2. Ensure `analysis.md` includes your recorded environment, timings, speedup, and answers.
3. Stage: `git add lab3_parallel_map.py analysis.md` (or `git add .`)
4. Commit: `git commit -m "Complete Lab 3 Parallel Map"`
5. Push: `git push origin main` (or your default branch)
6. Verify on GitHub that `lab3_parallel_map.py` and `analysis.md` are updated.
