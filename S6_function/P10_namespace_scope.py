import math


# 1. print(dir(__builtins__)): This command prints a list of all names available in the Built-in namespace. These names include standard Python functions and methods that are available by default without the need to import modules.

# 2. print(globals()): This command prints a dictionary of all names available in the Global namespace. These names include all variables, functions, and classes defined at a higher level in the program and are accessible throughout the program.

# 3. print(locals()): This command prints a dictionary of all names available in the Local namespace within the current execution scope. These names include all variables and parameters defined within a specific function or execution block.

# 4. print(dir(math)): This command prints a list of all names available in the math module. These names include functions, methods, and variables defined within the math module, which can be used for advanced mathematical operations.


# Namespaces 👇

# 1️⃣ Built-in Namespace:
# This namespace includes the standard Python functions and methods that are readily available in any program without the need to import modules. For example, functions like print(), len(), and methods like append() for lists reside in this namespace.

# 2️⃣ Global Namespace:
# This namespace comprises all variables, functions, and classes defined at a higher level in the program and are accessible. It is generally defined at the module (file) level and accessible to all parts of the program.

# 3️⃣ Enclosed Namespace:
# This namespace pertains to the inner functions of a function, encompassing the variables and parameters of the parent function. In Python, functions can be defined within other functions, and these namespaces are confined to these inner functions.

# 4️⃣ Local Namespace:
# This namespace includes all variables and parameters defined within a function. Variables defined within a function are accessible only within the scope of that function and are recognized as local variables.

# In code, access to variables and objects is based on these namespaces. Each specific namespace determines a scope of accessibility and provides ways for inheritance and interaction with one another.
