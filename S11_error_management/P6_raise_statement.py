# Definition: 
# The raise statement allows you to trigger an exception intentionally. It can be used to signal an error condition or to enforce certain constraints in your program.

# Detailed Explanation: Using raise enables developers to create custom checks and balances within their code, enhancing code reliability. By raising exceptions, you can communicate specific issues in your logic or input data, which is essential for robust error handling.

# Example:

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")

# try:
#     check_age(-5)
# except ValueError as e:
#     print(f"Error: {e}")

# Explanation of the example: The function check_age raises a ValueError if the age is less than zero. In this case, when we call check_age(-5), the exception is triggered, caught in the try block, and an appropriate message is displayed.
