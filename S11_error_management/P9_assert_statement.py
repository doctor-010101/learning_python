# Definition: 
# The assert statement is a debugging aid that tests a condition as true. If the condition is false, it raises an AssertionError.

# Detailed Explanation: Assertions are primarily used for debugging purposes. They allow developers to verify that certain conditions hold true during development, and if they don’t, they provide immediate feedback. Assertions can be globally disabled with the -O (optimize) switch when running the Python interpreter, making them non-intrusive for production environments.

# Example:

# def square_root(x):
#     assert x >= 0, "Cannot compute the square root of a negative number."
#     return x ** 0.5

# try:
#     result = square_root(-9)
# except AssertionError as e:
#     print(f"AssertionError: {e}")
# Explanation of the example: The square_root function checks if the input x is non-negative using an assert statement. If the input is negative, it raises an AssertionError with a custom message. This assertion is useful during development to ensure that invalid inputs are caught early, making it clear where the error occurred.
