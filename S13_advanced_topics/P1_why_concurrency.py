# Definition:
# Concurrency refers to the ability of a program to manage multiple tasks at the same time, allowing for more efficient use of resources, particularly in I/O-bound tasks. It does not necessarily mean that tasks are being executed simultaneously but rather that they are being executed in overlapping time periods.

# Detailed Explanation: Concurrency helps improve the responsiveness and efficiency of applications, especially in scenarios where tasks are waiting for resources (like file I/O or network requests). By allowing other tasks to run while one task is waiting, the overall throughput of the program can increase.

# Example:

# import time

# def task(name, duration):
#     print(f"Task {name} starting...")
#     time.sleep(duration)
#     print(f"Task {name} completed after {duration} seconds.")

# def run_concurrently():
#     tasks = [
#         ("A", 2),
#         ("B", 3),
#         ("C", 1)
#     ]
#     for name, duration in tasks:
#         task(name, duration)

# run_concurrently()

# Explanation of the example: In this example, tasks A, B, and C run sequentially. Although this is a simple simulation, true concurrency would involve allowing these tasks to overlap in execution, improving efficiency by waiting on I/O operations or similar tasks.
