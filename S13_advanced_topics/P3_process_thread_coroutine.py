# Definition:

# Process: An independent program in execution with its own memory space.

# Thread: A lightweight subprocess that shares memory space with other threads within the same process.

# Coroutine: A special type of function that can pause and resume its execution, allowing for cooperative multitasking.


# Detailed Explanation:

# Processes are used for CPU-bound tasks where you want true parallelism since they run in separate memory spaces.

# Threads are useful for I/O-bound tasks and are lighter than processes. They can share data but also introduce complexity with concurrent access to shared resources.

# Coroutines are designed for asynchronous programming and allow more efficient management of I/O-bound tasks without the overhead of threading.


# Example:

# import threading
# import asyncio

# # Example of Thread
# def thread_task():
#     print("Thread is running")

# # Example of Coroutine
# async def coroutine_task():
#     await asyncio.sleep(1)
#     print("Coroutine is running")

# # Running the thread
# thread = threading.Thread(target=thread_task)
# thread.start()
# thread.join()

# # Running the coroutine
# asyncio.run(coroutine_task())

# Explanation of the example: The example illustrates how to create and run a thread that executes a simple task. It also demonstrates how to define and run a coroutine that waits asynchronously before executing its task.

