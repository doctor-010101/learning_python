# Definition: 
# Multithreading allows the execution of multiple threads concurrently within a single process, enabling efficient use of CPU resources, especially for I/O-bound operations.

# Detailed Explanation: Using multithreading can help in tasks where waiting is common (like I/O operations), allowing the program to perform other tasks while waiting for I/O to complete.

# Example:

# import threading
# import time

# def worker(thread_number):
#     print(f"Thread {thread_number} starting.")
#     time.sleep(2)
#     print(f"Thread {thread_number} finished.")

# threads = []

# for i in range(5):
#     thread = threading.Thread(target=worker, args=(i,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("All threads have finished.")

# Explanation of the example: This program creates and starts five threads that simulate a worker task, sleeping for two seconds each. The main thread waits for all worker threads to complete using join(), ensuring all tasks are finished before printing the final message.