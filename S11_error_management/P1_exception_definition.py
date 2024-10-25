# Definition: 
# An exception is a signal that an error or unexpected condition has occurred in the program. When an exception is raised, the normal flow of execution is interrupted, and Python attempts to find a way to handle this error. If not handled properly, the program will terminate and display an error message.

# Detailed Explanation: Exceptions can occur for various reasons, such as invalid user input, file not found errors, or network issues. Python categorizes exceptions into built-in exceptions (like ValueError, TypeError, etc.) and user-defined exceptions that you can create based on your program's needs.

# Example:

# def divide(x, y):
#     if y == 0:
#         raise ValueError("Cannot divide by zero.")
#     return x / y

# try:
#     result = divide(10, 0)
# except ValueError as e:
#     print(f"Error: {e}")

# Explanation of the example: In this code, we define a function divide that checks if the denominator y is zero. If it is, a ValueError is raised with a specific message. The try block attempts to call this function, and if an error occurs, the except block catches the exception and prints a friendly error message.
