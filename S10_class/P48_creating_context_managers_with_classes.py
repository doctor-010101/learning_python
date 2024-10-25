# In Python, a context manager is a convenient way to set up a runtime context for your code, typically for resource management tasks like file handling, network connections, or database connections. It ensures that resources are properly acquired and released. The most common way to define a context manager is by using the with statement.

# You can create a context manager in two main ways:

# 1. Using the enter and exit methods in a class.


# 2. Using the contextlib module with a generator function.



# Example 1: Creating a Context Manager Using a Class

# Let’s create a context manager that opens a file, writes to it, and automatically closes it when done.

# Step 1: Define the Context Manager Class

# class FileManager:
#     def init(self, filename, mode='w'):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def enter(self):
#         self.file = open(self.filename, self.mode)  # Open the file
#         return self.file  # Return the file object

#     def exit(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()  # Close the file
#         # Handle exceptions if needed (optional)
#         if exc_type:
#             print(f"An error occurred: {exc_value}")
#         return True  # Suppress the exception if handled

# Step 2: Using the Context Manager

# Now, let’s use the FileManager context manager to write to a file.

# # Using the context manager to write to a file
# with FileManager('example.txt', 'w') as f:
#     f.write("Hello, world!\n")
#     f.write("This is a context manager example.")

# # Check the contents of the file
# with open('example.txt', 'r') as f:
#     print(f.read())  # Output: Hello, world!\nThis is a context manager example.

# Explanation of the Example

# 1. Context Manager Class (FileManager):

# The init method initializes the context manager with the filename and mode.

# The enter method opens the file and returns the file object, allowing you to use it within the with block.

# The exit method ensures the file is closed when the block is exited, regardless of whether an exception occurred. You can also handle exceptions in this method if needed.



# 2. Using the Context Manager:

# The with FileManager(...) as f: statement opens the file and allows you to write to it.

# Once the block is exited, the exit method is called, closing the file automatically.




# Example 2: Creating a Context Manager Using a Generator Function

# You can also create a context manager using the contextlib module, which provides the contextmanager decorator to simplify this process.

# Step 1: Define the Context Manager with a Generator

# from contextlib import contextmanager

# @contextmanager
# def file_manager(filename, mode='w'):
#     file = open(filename, mode)
#     try:
#         yield file  # Yield the file object to the context
#     finally:
#         file.close()  # Ensure the file is closed

# Step 2: Using the Context Manager

# Now, let’s use the file_manager context manager to write to a file.

# # Using the context manager to write to a file
# with file_manager('example2.txt', 'w') as f:
#     f.write("Hello from contextlib!\n")
#     f.write("This is another context manager example.")

# # Check the contents of the file
# with open('example2.txt', 'r') as f:
#     print(f.read())  # Output: Hello from contextlib!\nThis is another context manager example.

# Explanation of the Generator Example

# 1. Context Manager Function:

# The file_manager function is decorated with @contextmanager, which allows it to be used as a context manager.

# The try block opens the file and yields the file object, allowing you to use it within the with block.

# The finally block ensures that the file is closed when the block is exited.



# 2. Using the Context Manager:

# The usage is similar to the class-based context manager, providing a clean and readable way to manage file resources.
# Summary

# Context Managers provide a convenient way to manage resources, ensuring they are properly acquired and released.

# You can create context managers using:

# A class with enter and exit methods.
# A generator function with the contextlib module's contextmanager decorator.


# Using context managers enhances code readability and helps prevent resource leaks, making your code more robust and maintainable.
