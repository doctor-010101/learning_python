# Definition:

# Concurrency is about dealing with lots of tasks at once (interleaving execution).

# Parallelism is about doing lots of tasks at the same time (executing tasks simultaneously).


# Detailed Explanation: Concurrency allows programs to manage multiple tasks by breaking them into smaller tasks that can be interleaved, whereas parallelism involves utilizing multiple processors or cores to run tasks simultaneously. They are related but serve different purposes.

# Example:

# import concurrent.futures
# import time

# def long_running_task(n):
#     time.sleep(n)
#     return f"Task completed after {n} seconds."

# # Using concurrency
# def run_concurrent_tasks():
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = [executor.submit(long_running_task, i) for i in [2, 3, 1]]
#         for future in concurrent.futures.as_completed(futures):
#             print(future.result())

# # Simulate parallelism by running tasks simultaneously
# run_concurrent_tasks()

# Explanation of the example: Here, we use ThreadPoolExecutor to simulate concurrent execution of tasks that run for different durations. The tasks do not run in parallel but are interleaved in a way that utilizes the waiting time for I/O or sleep.
