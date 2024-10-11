# Akın, [15.08.24 22:28]

# In Python programming (and programming in general), several concepts are used to organize and manage code. These concepts include Script, Module, Package, Library, and Framework. Below is an explanation of each concept and the differences between them.

### 1. Script:
# A script is a text file containing Python code that can be executed directly. Scripts are usually designed to perform specific and immediate tasks.

# Example:

# script.py
print("Hello, World!")


# If you run this file (e.g., using python script.py), the message "Hello, World!" will be displayed on the screen.

### 2. Module:
# A module is a Python file (usually with a .py extension) that contains functions, classes, or variables and can be imported and used in other Python files. Any Python script can also be used as a module.

# Example:


# my_module.py
def greet(name):
    return f"Hello, {name}!"


# This module can be imported and used in another script or module:


# script.py
import my_module

message = my_module.greet("Alice")
print(message)


### 3. Package:
# A package is a directory that contains one or more modules and can also contain sub-packages. Each package must include an __init__.py file, which indicates that the directory is a package.

# Example:

# Suppose we have a package named mypackage that includes two modules: module1.py and module2.py:


# mypackage/
    # __init__.py
    # module1.py
    # module2.py


# Content of module1.py:


# module1.py
def hello():
    return "Hello from module 1"


# Content of module2.py:


# module2.py
def hello():
    return "Hello from module 2"


# Now, you can use this package in a script:


# script.py
# from mypackage import module1, module2

# print(module1.hello())
# print(module2.hello())


### 4. Library:
# A library is a collection of modules and packages developed to solve specific problems and can be reused across different projects. Libraries are pre-built and available for programmers to use. For example, NumPy is a popular Python library for numerical computations.

# Example:


# import numpy as np

# array = np.array([1, 2, 3, 4])
# print(array.mean())


### 5. Framework:
# A framework is a software structure that provides a foundation for developing applications. Frameworks consist of a set of libraries, modules, and tools that help developers build more complex applications. For example, Django is a web framework in Python used to develop websites and web applications.

# Example:

# In Django, you can quickly build a website using the structures and tools provided by the framework:

# views.py in Django
# from django.http import HttpResponse

# def hello_world(request):
    # return HttpResponse("Hello, World!")


### Summary of Differences:
# - Script: A Python file designed for direct execution.
# - Module: A Python file containing reusable code that can be imported into other scripts and modules.
# - Package: A directory containing modules (and possibly other packages), providing more structure to projects.
# - Library: A collection of modules and packages designed for use in projects.
# - Framework: A comprehensive structure that provides a foundation for developing complex applications.