# In Python, class decorators are a powerful tool that allows you to modify or extend the behavior of classes in a clean and readable way. A class decorator is a function that takes a class as an argument, modifies it, and returns a new class (or the same class).

# Use Cases for Class Decorators

# Adding new methods or properties to a class.

# Modifying existing methods.

# Adding validation logic.

# Implementing caching or logging.


# Creating a Class Decorator

# To create a class decorator, follow these steps:

# 1. Define a function that takes a class as an argument.


# 2. Inside this function, modify the class as needed.


# 3. Return the modified (or original) class.



# Example of a Class Decorator

# Let’s create a class decorator that adds a method to a class that calculates the area of a rectangle.

# Step 1: Define the Class Decorator

# def add_area_method(cls):
#     """Class decorator that adds an area method to a Rectangle class."""
#     def area(self):
#         return self.width * self.height

#     cls.area = area  # Add the new method to the class
#     return cls  # Return the modified class

# Step 2: Apply the Decorator to a Class

# Now, we can create a Rectangle class and use our decorator to add the area method.

# @add_area_method
# class Rectangle:
#     def init(self, width, height):
#         self.width = width
#         self.height = height

# # Create an instance of Rectangle
# rect = Rectangle(4, 5)

# # Call the area method added by the decorator
# print(f"Area of the rectangle: {rect.area()}")  # Output: Area of the rectangle: 20

# Explanation of the Example

# 1. Decorator Function:

# add_area_method(cls) is the class decorator. It takes a class cls as an argument.

# Inside the decorator, we define the area method, which calculates the area of the rectangle.

# The new method is added to the class using cls.area = area.



# 2. Applying the Decorator:

# The @add_area_method syntax above the Rectangle class applies the decorator, modifying the Rectangle class to include the area method.



# 3. Usage:

# We create an instance of Rectangle, and now it has the area method available, which returns the area based on the width and height.




# More Complex Example: Logging Decorator

# Let’s create a class decorator that logs the creation of instances.

# Step 1: Define the Logging Decorator

# def log_instance_creation(cls):
#     """Class decorator that logs when an instance is created."""
#     class NewClass(cls):
#         def init(self, *args, **kwargs):
#             print(f"Creating instance of {cls.name} with args: {args} and kwargs: {kwargs}")
#             super().init(*args, **kwargs)  # Call the original class constructor

#     return NewClass  # Return the new class

# Step 2: Apply the Logging Decorator

# Now, let’s apply this decorator to a Circle class.

# @log_instance_creation
# class Circle:
#     def init(self, radius):
#         self.radius = radius

# # Create an instance of Circle
# circle = Circle(10)  # Output: Creating instance of Circle with args: (10,) and kwargs: {}

# Explanation of the Logging Example

# 1. Logging Decorator:

# The log_instance_creation function defines a new class NewClass that inherits from the original class cls.

# Inside the init method of NewClass, it prints a message with the arguments used to create the instance before calling the original class constructor with super().init(*args, **kwargs).



# 2. Applying the Decorator:

# The @log_instance_creation decorator is applied to the Circle class. When an instance of Circle is created, it logs the creation.




# Summary

# Class decorators provide a clean way to modify or extend classes in Python.

# You can add methods, modify behavior, or add logging with class decorators.

# The syntax for applying decorators is simple and integrates seamlessly with class definitions.


# Class decorators are a powerful feature in Python that allows for flexible and reusable code modification, making them invaluable for many design patterns and frameworks.
