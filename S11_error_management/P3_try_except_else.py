# In Python, try, except, and else work together in error handling, allowing you to write code that can deal with exceptions (errors) and manage the flow based on whether an error occurred.

# Here’s what each block does:

# 1. try block: This is where you put the code that might raise an exception. Python will try to execute the code here.


# 2. except block: If an error occurs in the try block, the except block will run instead of stopping the program. You can handle specific types of exceptions if you want (e.g., except ValueError).


# 3. else block: This block runs only if no exceptions were raised in the try block. It allows you to write code that should only execute when everything goes smoothly.



# Here’s a simple example to demonstrate:

# try:
#     # Attempting to divide by a number
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter a valid integer.")
# else:
#     # Runs only if no exceptions occurred
#     print(f"Division successful! The result is {result}")

# Explanation of the Example:

# If the user enters a number and it’s not zero, the program divides 10 by that number and prints the result.

# If the user enters zero, it triggers a ZeroDivisionError, and the except ZeroDivisionError block will handle it.

# If the user enters something that isn’t a number, a ValueError will occur, and the except ValueError block will handle it.

# The else block executes only if no errors happen, which means the division was successful.


# This structure allows handling specific errors and performing different actions depending on the outcome of the try block.
