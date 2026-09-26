# lab3_parallel_map.py
import math
import multiprocessing
import os
import sys
import time

# Benchmark configuration.
# The defaults are intended to produce a meaningful CPU-bound workload on
# typical student hardware while keeping the lab reasonably quick to run.
NUMBER_LIST_SIZE = 16
VALUES_UPPER_BOUND = 100_000


def available_cpu_count():
    """Return the CPU count available to this process, with compatibility fallback."""
    process_cpu_count = getattr(os, "process_cpu_count", None)
    if process_cpu_count is not None:
        count = process_cpu_count()
    else:
        count = os.cpu_count()

    return count or 1


# ==================================
# CPU-Intensive Task Function
# ==================================


def cpu_intensive_task(n):
    """Perform a deterministic CPU-bound calculation for one input value."""
    # --- TODO: Task 1 - Implement CPU-intensive task ---
    # A suitable implementation is:
    # return math.factorial(n)
    # --- End TODO ---
    raise NotImplementedError("Complete Task 1: cpu_intensive_task")


# ==================================
# Sequential Execution Function
# ==================================


def run_sequential(data):
    """Run cpu_intensive_task on every input value sequentially."""
    # --- TODO: Task 2 - Implement sequential execution ---
    # Process each item in order and return the complete result list.
    # --- End TODO ---
    raise NotImplementedError("Complete Task 2: run_sequential")


# ==================================
# Parallel Execution Function
# ==================================


def run_parallel_map(data, pool_size):
    """Run cpu_intensive_task over data with multiprocessing.Pool.map."""
    # --- TODO: Task 3 - Implement parallel execution with Pool.map ---
    # Create a multiprocessing.Pool using a with block.
    # Use pool.map(cpu_intensive_task, data).
    # Return the complete result list.
    # --- End TODO ---
    raise NotImplementedError("Complete Task 3: run_parallel_map")


def build_input_data(list_size, upper_bound):
    """Build exactly list_size positive integers ending at upper_bound."""
    if list_size <= 0:
        raise ValueError("NUMBER_LIST_SIZE must be > 0")
    if upper_bound < list_size:
        raise ValueError("VALUES_UPPER_BOUND must be >= NUMBER_LIST_SIZE")

    start = upper_bound - list_size + 1
    return list(range(start, upper_bound + 1))


def choose_pool_size(task_count):
    """Choose no more workers than available CPUs or useful tasks."""
    if task_count <= 0:
        raise ValueError("task_count must be > 0")
    return max(1, min(available_cpu_count(), task_count))


# ==================================
# Main Execution Logic
# ==================================

if __name__ == "__main__":
    multiprocessing.freeze_support()

    data_to_process = build_input_data(NUMBER_LIST_SIZE, VALUES_UPPER_BOUND)
    pool_size = choose_pool_size(len(data_to_process))

    print(f"Python: {sys.version.split()[0]} ({sys.implementation.name})")
    print(f"Multiprocessing start method: {multiprocessing.get_start_method()}")
    print(f"Available CPU count: {available_cpu_count()}")
    print(f"Number of tasks: {len(data_to_process)}")
    print(f"Pool size: {pool_size}")
    print("-" * 40)

    start_seq = time.perf_counter()
    results_seq = run_sequential(data_to_process)
    time_seq = time.perf_counter() - start_seq
    print(f"Sequential execution time: {time_seq:.4f} seconds")

    print("-" * 40)

    start_par = time.perf_counter()
    results_par = run_parallel_map(data_to_process, pool_size)
    time_par = time.perf_counter() - start_par
    print(f"Parallel execution time (map): {time_par:.4f} seconds")

    if results_seq != results_par:
        raise RuntimeError(
            "Verification failed: sequential and parallel results differ"
        )
    print("Verification: sequential and parallel results match.")

    if time_par > 0:
        print(f"Speedup (Sequential / Parallel Map): {time_seq / time_par:.2f}x")

    print("-" * 40)
    print("Lab 3 finished.")
