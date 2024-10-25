# Definition: 
# You can place try and except blocks within each other, allowing for granular control over error handling at different layers of your code.
# Detailed Explanation: Nested exception handling is useful when a block of code has its own error handling needs but is also part of a larger error handling mechanism. This allows for more specific error handling without losing the overall control flow of the program.

# Example:

# def safe_divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print("Caught division by zero!")
#         return None

# try:
#     result = safe_divide(10, 0)
#     print(f"Result: {result}")
# except Exception as e:
#     print(f"An error occurred: {e}")
# Explanation of the example: In this example, the safe_divide function attempts to divide x by y. If y is zero, a ZeroDivisionError is raised, and the function handles it by printing a message and returning None. The outer try block captures any other unforeseen exceptions that might arise when calling safe_divide, ensuring that the program remains robust.
