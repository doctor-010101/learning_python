# Definition:

# The else block runs only if no exception was raised in the try block.

# The finally block runs no matter what, allowing you to execute cleanup actions or final statements.


# Detailed Explanation: Using else allows you to separate the normal execution path from error handling, making your code cleaner and easier to understand. The finally block is useful for resource management (like closing files or network connections) that should happen regardless of whether an error occurred.

# Example:

# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     print("That was not a valid number.")
# else:
#     print(f"You entered: {x}")
# finally:
#     print("Execution complete.")

# Explanation of the example: In this code, the try block attempts to convert the user input to an integer. If successful, the else block runs to print the valid number. Regardless of whether an exception occurs, the finally block executes to indicate the end of the program’s execution flow.
