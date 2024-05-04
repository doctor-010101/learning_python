"""

🍀👉 In programming languages, the concept of "first-class" means that an element (usually a variable or a function) is usable as a value, just like any other value in the language.

🍀👉 In other words, these elements can be passed as arguments to functions, used as return values from functions, stored in lists or dictionaries, and so on.

🍀👉 In languages that support this concept, it applies to functions, variables, data structures, and other language elements.

🍀👉 In Python, all variables, functions, classes, and even modules are first-class citizens.

🍀👉 This means that you can pass them as arguments to functions, use them as return values from functions, store them in lists or dictionaries, and interact with them just like any other object.

"""


# Features of "first class functions" 👇

# ✅ 1 can be created at run time.

# Define a function that dynamically generates arithmetic operations based on the input operation
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    else:
        raise ValueError("Invalid operation")


# Create a new operation dynamically
multiply = create_operation("multiply")

# Use the dynamically created operation
result = multiply(3, 4)
print(result)  # Output will be 12 (3 * 4)


# ✅ 2 can be assigned to a variable.

# # Assigning the function add to a variable func
# func = add

# # Calling the function from the variable
# result = func(3, 4)  # Equivalent to add(3, 4)
# print(result)  # 7

# # ✅ 3 can be passed as a argument to a function.

# # Define a function that accepts another function as an argument and calls it


# def apply_operation(operation, x, y):
#     return operation(x, y)


# # Calling the function using the add function as an argument
# result = apply_operation(add, 5, 2)
# print(result)  # 7

# ✅ 4 can be returned as a result from a function.

# Define a function that creates a new function and returns it


def create_adder():
    def adder(x, y):
        return x + y
    return adder


# Calling the function and storing the result in a variable

new_adder = create_adder()
result = new_adder(3, 4)
print(result)  # 7

# ✅ 5 can have properties and methods.

# Define a function that returns a property


def get_author():
    return get_author.author


# Define a property within the function
get_author.author = "John Doe"

print(get_author())  # John Doe
