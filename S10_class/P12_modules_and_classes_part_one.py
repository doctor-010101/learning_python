# In Python, modules are files that contain Python code, and they can include functions, classes, and variables. You can use modules in your classes to enhance functionality, organize your code, and keep your projects modular. Here's how to use modules within classes effectively.

# Steps to Use Modules in Classes

# 1. Import the Module: You need to import the module at the beginning of your script or within the class if you want to keep it scoped to that class.


# 2. Use Module Functions/Classes: Inside your class methods, you can use the functions or classes defined in the imported module.



# Example 1: Using Standard Library Modules

# Let's see an example where we use the math module to create a class that calculates the area of a circle.

# import math

# class Circle:
#     """
#     A class to represent a circle.
    
#     Attributes:
#     ----------
#     radius : float
#         The radius of the circle.

#     Methods:
#     -------
#     area():
#         Returns the area of the circle.
#     circumference():
#         Returns the circumference of the circle.
#     """
    
#     def init(self, radius: float):
#         """
#         Initializes the Circle with the given radius.
        
#         Parameters:
#         ----------
#         radius : float
#             The radius of the circle.
#         """
#         self.radius = radius

#     def area(self) -> float:
#         """Returns the area of the circle."""
#         return math.pi * (self.radius ** 2)

#     def circumference(self) -> float:
#         """Returns the circumference of the circle."""
#         return 2 * math.pi * self.radius

# # Creating an instance of Circle
# circle = Circle(5)

# # Calling methods
# print(f"Area: {circle.area():.2f}")             # Output: Area: 78.54
# print(f"Circumference: {circle.circumference():.2f}")  # Output: Circumference: 31.42

# Explanation:

# 1. Importing the math Module: The math module is imported to use mathematical constants and functions.


# 2. Using math.pi: Inside the area and circumference methods, we use math.pi to calculate the area and circumference of the circle.


# 3. Creating an Instance: An instance of the Circle class is created, and methods are called to calculate and print the area and circumference.



# Example 2: Using Custom Modules

# You can also create your own modules. For example, let’s say you have a module named shapes.py that contains a class for a rectangle:

# shapes.py

# # shapes.py
# class Rectangle:
#     """
#     A class to represent a rectangle.
    
#     Attributes:
#     ----------
#     width : float
#         The width of the rectangle.
#     height : float
#         The height of the rectangle.

#     Methods:
#     -------
#     area():
#         Returns the area of the rectangle.
#     perimeter():
#         Returns the perimeter of the rectangle.
#     """
    
#     def init(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         """Returns the area of the rectangle."""
#         return self.width * self.height

#     def perimeter(self) -> float:
#         """Returns the perimeter of the rectangle."""
#         return 2 * (self.width + self.height)

# main.py

# Now, you can use this Rectangle class in another file:

# # main.py
# from shapes import Rectangle

# class Box:
#     """
#     A class to represent a box using a rectangle base.

#     Attributes:
#     ----------
#     rectangle : Rectangle
#         An instance of the Rectangle class representing the base of the box.
#     height : float
#         The height of the box.

#     Methods:
#     -------
#     volume():
#         Returns the volume of the box.
#     """
    
#     def init(self, width: float, height: float, depth: float):
#         self.rectangle = Rectangle(width, depth)
#         self.height = height

#     def volume(self) -> float:
#         """Returns the volume of the box."""
#         return self.rectangle.area() * self.height

# # Creating an instance of Box
# box = Box(4, 5, 3)

# # Calling the volume method
# print(f"Volume of the box: {box.volume()}")  # Output: Volume of the box: 60

# Explanation:
# 1. Creating a Custom Module: The shapes.py module contains the Rectangle class with methods to calculate area and perimeter.


# 2. Importing the Rectangle Class: In main.py, we import the Rectangle class from the shapes module using from shapes import Rectangle.


# 3. Using the Rectangle Class: Inside the Box class, we create an instance of Rectangle to represent the base, and we calculate the volume of the box using the area of the rectangle.



# Conclusion

# Using modules in classes allows you to:

# Organize Code: Keep related functionality together.

# Reuse Code: Avoid duplication by importing existing modules.

# Maintain Separation of Concerns: Different modules can handle different parts of your application, making it easier to manage.


# Whether you use built-in modules or create custom ones, incorporating them into your classes enhances the functionality and readability of your Python code.