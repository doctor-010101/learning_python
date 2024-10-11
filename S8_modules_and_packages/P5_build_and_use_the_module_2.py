# Using modules in Python can be done in several different ways. Below are some common methods:

### 1. **Importing the Entire Module with import:**
# In this method, you import the entire module and must use the module name to access its functions, classes, or variables.

import math

result = math.sqrt(16)  # Using the sqrt function from the math module
### 2. **Using import with an Alias (as):**
# You can assign an alias to the imported module, which makes it easier to write code.
# 
import numpy as np

array = np.array([1, 2, 3])  # Using numpy with the alias np
### 3. **Importing Specific Functions or Classes with from ... import:**
# This method allows you to import only specific functions, classes, or variables from a module and use them directly.

from math import sqrt

result = sqrt(25)  # Using the sqrt function directly without math.
### 4. **Importing Multiple Functions or Classes with from ... import and Commas:**
# You can import several functions or classes with a single statement.

from math import sqrt, pi

result = sqrt(9)
circle_circumference = 2 * pi * 3  # Using pi to calculate the circumference of a circle
### 5. **Importing All Contents of a Module with from ... import *:**
# This method imports all the functions, classes, and variables from a module. It is generally less recommended because it can cause name conflicts.

from math import *

result = sqrt(64)  # Using the sqrt function directly
### 6. **Importing a Module Inside a Function or Code Block:**
# Sometimes you might want to import a module only within a specific function or code block.

def calculate():
    import math  # Importing the module only within this function
    return math.sqrt(16)

result = calculate()
### Summary:
# - import module_name: Import the entire module.
#  - import module_name as alias: Import the entire module with an alias.
# - from module_name import function_name: Import a specific function or class.
# - from module_name import *: Import all contents of the module.