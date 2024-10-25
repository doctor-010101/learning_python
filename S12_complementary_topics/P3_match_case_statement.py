# Definition: 
# The match statement, introduced in Python 3.10, allows you to perform pattern matching on values, similar to switch-case statements in other programming languages.

# Detailed Explanation: The match statement evaluates a value against a series of patterns and executes the block of code associated with the first matching pattern. This provides a more readable and organized way to handle multiple conditions.

# Example:

# def handle_command(command):
#     match command:
#         case "start":
#             return "Starting the system."
#         case "stop":
#             return "Stopping the system."
#         case "restart":
#             return "Restarting the system."
#         case _:
#             return "Unknown command."

# # Example usage
# print(handle_command("start"))
# print(handle_command("pause"))

# Explanation of the example: In this code, the handle_command function uses a match statement to determine what action to take based on the value of command. If the command is "start", it returns a specific message. The underscore (_) acts as a wildcard, catching any values not explicitly matched, similar to a default case.
