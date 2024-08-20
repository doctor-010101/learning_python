
# 1. Difference Between a Module and a Package:
# - Module: A module is any Python file with a .py extension. Modules contain Python code, which can include functions, classes, variables, and other elements.

#   For example, consider a file named math_functions.py that contains some mathematical functions:

  # math_functions.py
def add(a, b):
      return a + b

def subtract(a, b):
      return a - b

# - Package: A package is a collection of modules organized in a hierarchical manner. Packages are essentially directories containing Python files(modules) along with a special file named __init__.py. The __init__.py file allows the directory to be recognized as a package.

#   For instance, consider a directory named math_package that contains thinit__init__.py and math_functions.py:

#   math_package/
      __init__.py
      math_functions.py

# 2. How to Create a Package:
# To create a package, you need to create a directory and place Python files(modules) inside it. You should alsoinit an __init__.py file(even if it's empty) in the directory.

# Example:
# my_package/
#     __init__.py
#     module1.py
#     module2.py
# Here, my_package is a package that contains two modules: module1.py and module2.py.

### 3. Difference Between import and from ... import ...:
# - **import**: Used when you want to import an entire module or package. When using this approach, you need to use the module's name as a prefix to access its functions or classes.
  
#   Example:
 
#   import math_functions

#   result = math_functions.add(2, 3)
  
# - **`from ... import ...**: Used when you want to import only a specific part of a module (such as a particular function or class). In this case, you don't need to use the module's name as a prefix.

#   Example:
#   ``python
#   from math_functions import add

#   result = add(2, 3)
 

# ### 4. Comprehensive Example with a Package:
# Let's say we have a package named `math_package` that contains the following files:
# mainitge/
#     __init__.py
#     math_functions.py
#     advanced_math.py

# Contents of `math_functions.py`:
# python
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# Contents of `advanced_math.py`:
# python
# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return None

# Now, we can use this package in another Python file:

# Example with `import`:
# python
# import math_package.math_functions
# import math_package.advanced_math

# result1 = math_package.math_functions.add(2, 3)
# result2 = math_package.advanced_math.multiply(4, 5)

# Example with `from ... import ...`:
# python
# from math_package.math_functions import add
# from math_package.advanced_math import multiply

# result1 = add(2, 3)
# result2 = multiply(4, 5)


# In this example, `import` allows you to bring in the entire module and use it as a separate namespace, whereas `from ... import ...` gives you direct access to specific functions or classes within the module.