# Definition: 
# Custom exceptions are user-defined exception classes that allow you to create specific types of errors tailored to your application’s needs.

# Detailed Explanation: By creating custom exceptions, you can convey more meaningful error messages and conditions specific to your application's domain. This helps in differentiating between various error states and can improve error handling.

# Example:

# class CustomError(Exception):
#     pass

# def do_something():
#     raise CustomError("This is a custom error!")

# try:
#     do_something()
# except CustomError as e:
#     print(f"Caught an error: {e}")

# Explanation of the example: In this code, CustomError inherits from the built-in Exception class. The function do_something raises this custom exception, which is caught in the try block. This allows for more contextual error handling, making your code clearer.
