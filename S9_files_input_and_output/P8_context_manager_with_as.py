# In Python, the with statement along with as is used for resource management, especially when working with files. This statement allows you to automatically manage resources and helps prevent issues like forgetting to close a file.

# ▎Using with

# The with statement lets you execute a block of code and automatically release resources afterward. This is particularly useful when dealing with files.

# ▎Example 1: Reading from a File

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# In this example:

# • open('example.txt', 'r'): Opens the file in read mode.

# • as file: Allows us to access the file using the name file.

# • After the with block ends, the file is automatically closed, even if an error occurs.

# ▎Example 2: Writing to a File

# with open('example.txt', 'w') as file:
#     file.write("Hello, World!n")
#     file.write("This is a test.n")


# In this example:

# • The file example.txt is opened in write mode.

# • New content is written to the file, and after the with block ends, the file is automatically closed.

# ▎Advantages of Using with

# 1. Automatic Resource Management: You don’t have to manually close files.

# 2. Reduced Error Probability: Using with decreases the chance of forgetting to close files.

# 3. Better Readability: Your code becomes cleaner and more organized.

# ▎Example 3: Working with Multiple Files

# You can also use with to open multiple files at once:

# with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
#     content1 = file1.read()
#     content2 = file2.read()
#     print(content1)
#     print(content2)


# Here, both files are opened simultaneously, and after the with block ends, both files are automatically closed.

# ▎Conclusion

# Using the with statement along with as in Python is a safe and effective way to manage files and other resources. This approach helps you write cleaner and less error-prone code.