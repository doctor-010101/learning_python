# Buffering in Python refers to the process of temporarily storing data before writing it to an output source(such as a file or the screen). This helps improve the performance and efficiency of a program. Buffering is typically used in input/output(I/O) operations.

# ▎Types of Buffering

# 1. Default Buffering: Python uses buffering by default for files and I/O. This means that data is temporarily stored in memory and then sent to the output source all at once.

# 2. No Buffering: Buffering can be disabled so that data is written immediately.

# 3. Custom Buffering: The buffer size can be set according to preference.

# ▎Examples

# ▎1. Default Buffering

# # Creating and writing to a file with default buffering
# with open('example.txt', 'w') as f:
# f.write('Hello, World!')
# f.write('This is a test.')


# In this example, the data is temporarily stored in memory and then written to the file example.txt.

# ▎2. No Buffering

# # Writing to a file without buffering
# with open('example_no_buffer.txt', 'w', buffering=1) as f:
#     f.write('Hello, World!')
#     f.flush()   # Ensure that the data is written immediately


# In this example, buffering = 1 is used, which disables buffering and ensures that data is written immediately.

# ▎3. Custom Buffering

# # Writing to a file with a custom buffer size
# buffer_size = 8   # Size of the buffer in bytes
# with open('example_custom_buffer.txt', 'w', buffering=buffer_size) as f:
# f.write('Hello, World!')
# f.write('This is a test.')


# In this example, the buffer size is set to 8 bytes. This means that data will remain in memory until 8 bytes are filled.

# ▎Important Notes

# - Buffering can improve program performance, but in some cases, such as programs that require immediate output display(like interactive programs), it may be necessary to disable buffering.
# - Using flush() can ensure that all data in the buffer is written to the output source.
# - Buffering also exists when reading files and can help improve read speed.

# With these concepts and examples, you can better understand how buffering works in Python and how you can take advantage of it.
