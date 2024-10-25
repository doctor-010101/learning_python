# Definition: The os module in Python provides a way to interact with the operating system. It includes functions for file manipulation, process management, and environment variable access.

# Detailed Explanation: This module allows you to perform operating system tasks such as creating or removing directories, fetching environment variables, and executing shell commands. It is essential for developing scripts that require OS-level interactions.

# Useful Methods:

# 1. os.getcwd(): Returns the current working directory.


# 2. os.listdir(path): Lists the files and directories in the specified path.


# 3. os.mkdir(path): Creates a new directory.



# Example:

# import os

# # Current working directory
# current_directory = os.getcwd()
# print(f"Current working directory: {current_directory}")

# # List files in the current directory
# files = os.listdir(current_directory)
# print(f"Files in the current directory: {files}")

# # Create a new directory
# new_directory = "test_dir"
# os.mkdir(new_directory)
# print(f"Created directory: {new_directory}")

# Explanation of the example: In this script, we first retrieve and print the current working directory. Then, we list the files present in that directory. Finally, we create a new directory named test_dir. Note that if you run this multiple times, it will raise an error if the directory already exists.
