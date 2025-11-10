# lab3_parallel_map.py
import multiprocessing
import time
import math
import os

# Constants (adjust as needed for your machine)
# NUMBER_LIST_SIZE = 200_000  # How many numbers to process
# VALUES_UPPER_BOUND = 10_000  # Max value for numbers (affects factorial complexity)
NUMBER_LIST_SIZE = 20  # Reduced for quick testing; increase for real measurement
VALUES_UPPER_BOUND = 20_000  # Increase/decrease based on runtime

# Determine a reasonable pool size
DEFAULT_POOL_SIZE = os.cpu_count()

# ==================================
# CPU-Intensive Task Function
# ==================================

def cpu_intensive_task(n):
    """
    Performs a CPU-bound calculation on n.
    Example: Calculate factorial.
    """
    # --- TODO: Task 1 - Implement CPU-intensive task ---
    # Using math.factorial(n) is a good choice for CPU-bound work.
    if n < 0:
        return -1  # Factorial not defined for negative numbers
    try:
        result = math.factorial(n)
        # print(f"Processed {n}")  # Optional: for debugging, remove for timing
        return result
    except (ValueError, OverflowError):
        return -2  # Handle potential errors if needed
    # --- End TODO ---

# ==================================
# Sequential Execution Function
# ==================================

def run_sequential(data):
    """Runs the CPU-intensive task sequentially on the data."""
    print("Running sequentially...")
    results = []
    # --- TODO: Task 2 - Implement sequential execution ---
    for item in data:
        results.append(cpu_intensive_task(item))
    # --- End TODO ---
    return results

# ==================================
# Parallel Execution Function (using Pool.map)
# ==================================

def run_parallel_map(data, pool_size):
    """Runs the CPU-intensive task in parallel using Pool.map."""
    print(f"Running in parallel using Pool.map with {pool_size} processes...")
    results = []
    # --- TODO: Task 3 - Implement parallel execution with Pool.map ---
    with multiprocessing.Pool(processes=pool_size) as pool:
        results = pool.map(cpu_intensive_task, data)
    # --- End TODO ---
    return results

# ==================================
# Main Execution Logic
# ==================================

if __name__ == "__main__":
    # Ensure this runs only in the main process
    multiprocessing.freeze_support()  # Needed for Windows executable support

    # Generate some data (list of numbers)
    # Using a fixed range for consistency in testing factorial calculation time
    data_to_process = list(range(max(1, VALUES_UPPER_BOUND - NUMBER_LIST_SIZE), VALUES_UPPER_BOUND + 1))
    actual_list_size = len(data_to_process)  # Use actual size if range logic changes it
    print(f"Generated {actual_list_size} numbers to process (up to {VALUES_UPPER_BOUND}).")
    print(f"Using Default Pool Size: {DEFAULT_POOL_SIZE}")
    print("-" * 30)

    # --- Sequential Run ---
    start_seq = time.perf_counter()
    results_seq = run_sequential(data_to_process)
    end_seq = time.perf_counter()
    time_seq = end_seq - start_seq
    print(f"Sequential execution time: {time_seq:.4f} seconds")
    # print(f"Sequential results sample (first 1): {str(results_seq[0])[:60]}...")  # Optional
    print("-" * 30)

    # --- Parallel Run using map ---
    start_par_map = time.perf_counter()
    results_par_map = run_parallel_map(data_to_process, DEFAULT_POOL_SIZE)
    end_par_map = time.perf_counter()
    time_par_map = end_par_map - start_par_map
    print(f"Parallel execution time (map): {time_par_map:.4f} seconds")
    # print(f"Parallel map results sample (first 1): {str(results_par_map[0])[:60]}...")  # Optional

    # --- Verification (Optional) ---
    # if results_seq == results_par_map:
    #     print("Verification: Sequential and Parallel results match.")
    # else:
    #     print("Verification ERROR: Sequential and Parallel results DO NOT match!")
    # print("-" * 30)

    # --- Speedup Calculation ---
    if time_par_map > 0:
        speedup = time_seq / time_par_map
        print(f"Speedup (Sequential / Parallel Map): {speedup:.2f}x")
    else:
        print("Parallel execution was too fast to measure speedup.")

    print("-" * 30)
    print("Lab 3 finished.")
