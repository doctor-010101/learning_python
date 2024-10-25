# Definition: 
# The shutil module in Python provides a higher-level interface for file operations. It includes functions for copying, moving, and deleting files and directories.

# Detailed Explanation: This module is particularly useful for tasks that involve file manipulation, such as copying files or entire directories, removing files, and managing file permissions.

# Useful Methods:

# 1. shutil.copy(src, dst): Copies a file from src to dst.


# 2. shutil.move(src, dst): Moves a file or directory to a new location.


# 3. shutil.rmtree(path): Removes a directory and all its contents.



# Example:

# import shutil
# import os

# # Copy a file
# shutil.copy('source_file.txt', 'destination_file.txt')
# print("File copied.")
# # Move a file
# shutil.move('destination_file.txt', 'moved_file.txt')
# print("File moved.")

# # Remove a directory (make sure it exists)
# if os.path.exists('some_directory'):
#     shutil.rmtree('some_directory')
#     print("Directory removed.")
