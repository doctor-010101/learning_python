# Main Operations on Files:

# 1. Opening a File: To access a file, you first need to open it. Python uses the open() function to open a file.

# file = open("filename.txt", "r")  # To read a file
# file = open("filename.txt", "w")  # To write to a file (if it doesn't exist, it will be created)


# 2. File Opening Modes:

# "r": Read (the file must exist).

# "w": Write (overwrites the file if it exists).

# "a": Append (adds content to the end of the file).

# "rb": Read in binary mode.

# "wb": Write in binary mode.



# 3. Reading from a File:

# read(): Reads the entire content of the file as a string.

# readline(): Reads a single line from the file.

# readlines(): Reads all lines from the file as a list of strings.


# file = open("filename.txt", "r")
# content = file.read()  # Reads the entire content


# 4. Writing to a File:

# write(): Writes a string to the file.

# writelines(): Writes a list of strings to the file.


# file = open("filename.txt", "w")
# file.write("Hello, World!")  # Writes to the file


# 5. Closing a File: After working with a file, you should close it to free up system resources.

# file.close()


# 6. Using the with Block: The best practice for handling files in Python is to use the with block, which automatically closes the file when done.

# with open("filename.txt", "r") as file:
#     content = file.read()
# # The file is automatically closed after the block



# Practical Examples:

# Reading a Text File:

# with open("example.txt", "r") as file:
#     data = file.read()
#     print(data)

# Writing to a Binary File:

# with open("image.jpg", "wb") as file:
#     file.write(image_data)


# These methods provide a complete set of tools for working with files in Python.