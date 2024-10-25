# Definition: 
# When multiple threads access shared data, it can lead to race conditions and data corruption. Proper synchronization techniques are needed to prevent these issues.

# Detailed Explanation: Without synchronization, threads may read and write shared data at the same time, leading to inconsistent or corrupted states. Python provides mechanisms such as Lock to manage access to shared resources.

# Example:

# import threading

# # Shared resource
# shared_counter = 0
# lock = threading.Lock()

# def increment_counter():
#     global shared_counter
#     for _ in range(100000):
#         with lock:
#             shared_counter += 1

# threads = [threading.Thread(target=increment_counter) for _ in range(2)]

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# print(f"Final counter value: {shared_counter}")

# Explanation of the example: In this example, two threads increment a shared counter. The Lock ensures that only one thread can increment the counter at a time, preventing race conditions and ensuring accurate results.
