# What is scope? 👇

"""

Scope in Python refers to a region where a variable is valid or accessible. Scopes are usually nested and defined in various ways. In Python, the types of scopes include:

1. **Local Scope**:
   - This scope is within locally defined blocks, typically created by functions, class methods, or conditional blocks like if, else, etc.
   - Variables defined in this scope are only accessible within the respective block and cannot be accessed by blocks outside of that scope.

2. **Enclosing Function Local Scope**:
   - This scope is for variables defined within a function and accessible through an Enclosing Function.
   - Variables defined in this scope are also only accessible within the respective function.

3. **Global Scope**:
   - This scope is for variables defined at a higher level than all blocks and functions, such as at the program level or in the main Python file.
   - Variables defined in this scope are accessible throughout the program and can be used in any part of the program.

4. **Built-in Scope**:
   - This scope includes standard Python functions and variables that are available by default in any program, such as `print()` or `len()`.

Note that access to variables prioritizes from outer to inner scopes, meaning it first checks the local scope and then goes to higher scopes. If a variable with the same name is not found in higher scopes, it raises an error.

"""


# Example 👇

# 1️⃣ Built-in Scope
# 2️⃣ Global Scope
# 3️⃣ Enclosing Function Local Scope
# 4️⃣ Local Scope


global_variable = 10


def outer_function():
    enclosing_function_variable = 20

    def inner_function():
        local_variable = 30
        print("Value of local variable:", local_variable)
        print("Value of enclosing function variable:",
              enclosing_function_variable)
        print("Value of global variable:", global_variable)
        print("Value of built-in variable:", len("Hello"))

    inner_function()


outer_function()


# In this example:

# - `local_variable` is a local variable that is only accessible within the `inner_function`.
# - `enclosing_function_variable` is a variable associated with the calling function, defined in the outer function `outer_function`, and accessible within the `inner_function`.
# - `global_variable` is a global variable accessible throughout the program.
# - `len()` is a built-in variable referring to standard Python functions and variables, accessible in any Python program.

# All four scopes are utilized within the `inner_function`, and the values of variables from each scope are printed.


# 🍀🍀 global, nonlocal

# 1 -> global:

#    - The `global` keyword is used to declare that a local variable should be treated as a global variable. This means that the variable inside a function is considered a global variable, and any changes made to it will affect the corresponding variable throughout the program.

# Example:

x = 10


def change_global():
    global x
    x = 20


change_global()
print(x)  # Output: 20


# 2. ** nonlocal **:
# - The `nonlocal ` keyword is used to refer to variables defined in the enclosing function and modified inside an inner function. This means that we can modify the values of enclosing function variables within inner functions.

# Example**:

def outer_function():
    y = 5

    def inner_function():
        nonlocal y
        y = 20
        print("Value of y in Enclosing Function:", y)

    inner_function()


outer_function()


# In this example, the value of the variable `y` in the enclosing function changes from 5 to 20, and the new value is printed.

# Using these keywords, we can manipulate variables in different scopes and manage their accessibility.
