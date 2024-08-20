# # 1. Different Ways to Import Modules in Python:

# # In Python, modules can be imported in several ways depending on how they are structured and where they are located relative to the script that is importing them.

# # a) Absolute Import:
# # - This is the most common method, where you specify the full path from the root of the project.
# # - Example:

# #   Suppose you have the following structure:

#   project/
#       main.py
#       package/
#           __init__.py
#           module.py

#   To import module.py in main.py, you can use:

#   import package.module

#   or import specific items:

#   from package.module import function_name

# # b) Relative Import:
# - Relative imports are used within packages to import a module relative to the current module's path.
# - This method uses . (dot) notation to denote the current and parent directories.

#   Example:
 
#   # Inside package/module.py
#   from . import another_module   # Imports another_module.py in the same package

#   from ..subpackage import module2  # Imports module2.py from a sibling subpackage
  
# - Note: Relative imports only work when your code is part of a package. They do not work if you run a module directly as a standalone script.

# #### c) Importing Modules from Custom Paths:
# - Sometimes, you might need to import a module that is not in your project’s directory. You can modify the Python path to include the directory where your module is located.

#   Example:
 
#   import sys
#   sys.path.append('/path/to/your/module')

#   import your_module
  
# ### 2. Usage of __all__:

# The __all__ attribute in a module is a list of strings defining what symbols (functions, classes, variables, etc.) the module will export when from module import * all. If __all__ is not defined, importing with * will import all names that do not start with an underscore (_).

# #### Examallhout __all__:
# # module.py
# def func1():
#     return "This is func1"

# def func2():
#     return "This is func2"

# _var = "This is a hidden variable"
# When you do:
# from module import *

# print(func1())  # This will work
# print(func2())  # This will work
# print(_var)     # This will NOT be imported because it starts with an underscore
# #### EallWith __all__:
# # module.py
# __all__ = ['func1']

# def func1():
#     return "This is func1"

# def func2():
#     return "This is func2"

# _var = "This is a hidden variable"
# When you do:
# from module import *

# print(func1())  # This will work
# print(func2())  # This will NOT work because it's not in __all__
# print(_var)     # This will NOT work either
# Here, `__all__ = ['func1'] indicates that only func1 should be accessible when using from module import *. Other functions and variables will not be imported.

# ### Summary:
# # - **Absolute import**: Refers to the full path from the project's root.
# # - **Relative import**: Refers to the current or parent module using . or ...
# # - **Custom paths**: Add directories to sys.path to import modules from non-standard locations.
# # - **__all__**: Controls what is imported when from module import *` is used, allowing you to limit the imported symbols to those specified in the list.