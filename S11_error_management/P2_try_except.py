# Definition: 
# The try block contains code that might cause an exception. The except block is used to catch and handle the exception that occurs.

# Detailed Explanation: Using try and except allows you to anticipate potential errors and prevent the program from crashing. Instead of letting the program fail, you can provide alternate code paths or graceful error handling. You can also specify multiple except blocks to handle different types of exceptions distinctly.

# Example:

# try:
#     x = int(input("Enter a number: "))
#     print(f"You entered: {x}")
# except ValueError:
#     print("That was not a valid number.")

# Explanation of the example: Here, the user is prompted to enter a number. If the input cannot be converted to an integer (e.g., the user types "hello"), a ValueError is raised. The program catches this error in the except block, allowing for a user-friendly error message instead of crashing.
