# Documentation is a crucial aspect of software development, as it helps developers understand how to use and interact with code. In Python, there are several ways to document classes and functions, as well as tools to check the correctness and type safety of the code. Two useful tools for this purpose are doctest and mypy.

# 1. Documentation in Python

# Python provides a straightforward way to document classes, methods, and functions using docstrings. A docstring is a string literal that appears right after the definition of a function, method, class, or module. It is accessible through the doc attribute and can be used to provide information about the purpose of the function or class, its parameters, and its return values.

# Example of Documenting a Class

# class Rectangle:
#     """
#     A class to represent a rectangle.

#     Attributes:
#     ----------
#     width : float
#         Width of the rectangle
#     height : float
#         Height of the rectangle

#     Methods:
#     -------
#     area():
#         Returns the area of the rectangle.
#     perimeter():
#         Returns the perimeter of the rectangle.
#     """

#     def init(self, width: float, height: float):
#         """
#         Constructs all the necessary attributes for the rectangle object.

#         Parameters:
#         ----------
#         width : float
#             The width of the rectangle.
#         height : float
#             The height of the rectangle.
#         """
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         """Returns the area of the rectangle."""
#         return self.width * self.height

#     def perimeter(self) -> float:
#         """Returns the perimeter of the rectangle."""
#         return 2 * (self.width + self.height)

# Key Points about Docstrings:

# Triple Quotes: Docstrings are typically written using triple quotes (""" or ''').

# Format: A common format is to provide a short summary, followed by a description of the parameters and return values.

# Accessibility: You can access the docstring of a class or function using the doc attribute, which is helpful for interactive help systems.


# 2. doctest

# doctest is a module in Python that allows you to write test cases within the docstrings of your classes and functions. This way, you can ensure that the examples in your documentation are correct and that your code behaves as expected.

# Example of Using doctest

# def add(a: int, b: int) -> int:
#     """
#     Returns the sum of a and b.

#     Example:
#     >>> add(2, 3)
#     5
#     >>> add(-1, 1)
#     0
#     """
#     return a + b

# if name == "main":
#     import doctest
#     doctest.testmod()

# Explanation:

# In the add function, the docstring contains examples of how the function should behave.

# Each example starts with >>>, and the expected output follows on the next line.

# When you run the script, doctest.testmod() checks the examples in the docstrings against the actual output of the function.


# 3. mypy

# mypy is a static type checker for Python. It checks the type hints you provide in your code and verifies that they are consistent. This helps catch type-related errors before runtime.

# Example of Using mypy

# Using the Rectangle class from the earlier example, let’s see how mypy can be used:

# # rectangle.py
# class Rectangle:
#     """
#     A class to represent a rectangle.
#     """
    
#     def init(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

#     def perimeter(self) -> float:
#         return 2 * (self.width + self.height)

# Running mypy

# 1. First, make sure you have mypy installed. You can install it via pip:

# pip install mypy


# 2. Run mypy on your Python file:

# mypy rectangle.py


# 3. mypy will analyze the file and report any type errors. If your code is type-safe according to the hints provided, you will see no output, indicating success.



# Benefits of Using doctest and mypy

# doctest:

# Ensures that examples in your documentation are accurate.
# Provides a simple way to write and run tests without a separate testing framework.


# mypy:

# Enhances code reliability by catching type errors before runtime.

# Improves code readability and maintainability by enforcing type hints.



# Conclusion

# Proper documentation and type checking are essential for writing maintainable and reliable code. Using docstrings to document classes and functions, along with tools like doctest and mypy, can significantly improve the quality of your Python code. These tools encourage best practices and make your code easier to understand and less prone to errors.