# In Python, there are several methods for reading from and writing to files, allowing you to easily manage file content. Below is a detailed explanation of the main methods along with examples.

# Methods for Reading from a File

# 1. read(): This method reads the entire content of a file as a string.

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# In this example, the entire content of the file is stored in the content variable and then printed.

# You can also pass a number to the read() method to read a specific number of characters:


# with open("example.txt", "r") as file:
#     content = file.read(100)  # Reads the first 100 characters
#     print(content)


# 2. readline(): This method reads a single line from the file. If called multiple times, it reads the next line each time.

# with open("example.txt", "r") as file:
#     line = file.readline()
#     print(line)

# Each time this method is called, one line from the file is read. When the end of the file is reached, it returns an empty string ('').



# 3. readlines(): This method reads all lines of a file and returns them as a list of strings.

# with open("example.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# Each line in the file is stored as an element in a list. This method is useful for reading all lines at once.




# Methods for Writing to a File

# 1. write(): This method writes a string to a file. If the file already contains data and is opened in write mode ("w"), the previous content is erased.

# with open("example.txt", "w") as file:
#     file.write("Hello, World!")

# In this example, the string "Hello, World!" is written to the file. If the file does not exist, it will be created.



# 2. writelines(): This method writes a list of strings to the file. The strings must be provided as a list.

# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("example.txt", "w") as file:
#     file.writelines(lines)

# In this example, three lines are written to the file. Note that you need to manually add \n (newline character) to each line.




# Advanced Examples

# 1. Reading a File Line by Line and Processing Each Line

# If you want to read a file line by line and process each line, you can use a for loop:

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # .strip() removes extra characters like \n

# This method is efficient and avoids reading the entire file into memory at once.


# 2. Appending to a File (Append Mode)

# By using append mode ("a"), you can add new content to the end of the file without erasing the previous content.

# with open("example.txt", "a") as file:
#     file.write("\nNew line appended.")

# This adds a new line to the end of the file.


# File Open Modes

# "r": Read (the file must exist).

# "w": Write (overwrites the file if it exists).

# "a": Append (adds content to the end of the file).

# "rb": Read in binary mode.

# "wb": Write in binary mode.

# "r+": Read and write.

# "w+": Write and read (the file is cleared).

# "a+": Append and read.


# Practical Examples

# 1. Writing a Binary File

# To write binary files like images or audio, you should open the file in "wb" mode:

# with open("image.jpg", "wb") as file:
#     file.write(binary_data)

# binary_data should be the binary data that you want to write to the file.


# 2. Reading a Binary File

# To read binary files such as images, you should open the file in "rb" mode:

# with open("image.jpg", "rb") as file:
#     binary_content = file.read()

# In this example, the binary data of the file is read and stored in the binary_content variable.


# Error Handling

# Sometimes, when working with files, you may encounter errors (e.g., the file does not exist). In such cases, you can use a try-except block:

# try:
#     with open("non_existent_file.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("The file does not exist.")

# This code checks if the file exists, and if it doesn’t, it prints an appropriate message.


# Summary:

# For reading from a file, you use methods like read(), readline(), and readlines().


# For writing to a file, you use write() and writelines().

# Different file modes (read, write, append) control how files are opened and manipulated.

# Using with to open files is the best practice, as it automatically closes the file after the block ends.