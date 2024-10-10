# # The code snippet you provided explains how to work with files in Python and manage the file
# # pointer's position using the `seek()` method. It demonstrates opening a file in different modes,
# # changing the pointer position, reading and writing data, and closing the file.
# In Python, to work with files and manage the file pointer's position, we can use various methods. These methods allow us to change the reading and writing position in the file.

# ▎Opening a File

# To start, we need to open the file. We can use different modes such as 'r' (read-only), 'w' (write), 'a' (append), etc.

# file = open('example.txt', 'r')


# ▎Changing the Pointer Position

# To change the pointer position in a file, we can use the seek() method. This method takes two parameters:

# • offset: The number of bytes to move forward or backward.

# • whence: The reference point for the offset, which can be one of the following values:

#   • 0: from the beginning of the file (default)

#   • 1: from the current position

#   • 2: from the end of the file

# ▎Example 1: Using seek()

# # Opening the file
# file = open('example.txt', 'r')

# # Reading the first line
# line1 = file.readline()
# print(line1)

# # Changing the pointer position to the beginning of the file
# file.seek(0)

# # Reading the first line again
# line1_again = file.readline()
# print(line1_again)

# # Closing the file
# file.close()


# ▎Example 2: Writing to a File

# If you want to write to a file and change the pointer position, you can use seek() before writing.

# # Opening the file for writing
# file = open('example.txt', 'w+')

# # Writing data
# file.write("Hello, World!n")
# file.write("This is a test.n")

# # Changing the pointer position to the beginning of the file
# file.seek(0)

# # Reading the contents of the file
# content = file.read()
# print(content)

# # Closing the file
# file.close()


# ▎Conclusion

# Using the seek() method allows you to easily change the pointer position in files and have more control over reading and writing operations.
# This method enables you to navigate to specific points in the file and read or write data as desired.