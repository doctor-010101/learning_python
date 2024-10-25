# In Python, an abstract class is a class that cannot be instantiated and is meant to be subclassed. Abstract classes are used to define a common interface for a group of related classes. They can contain abstract methods that must be implemented by subclasses, as well as concrete methods with actual implementations.

# To create an abstract class in Python, you typically use the abc module, which stands for "Abstract Base Classes." Here’s how you can create and use abstract classes in Python.

# Steps to Create an Abstract Class

# 1. Import the abc Module: You need to import ABC and abstractmethod from the abc module.


# 2. Define the Abstract Class: Subclass ABC to create your abstract class.


# 3. Define Abstract Methods: Use the @abstractmethod decorator to define methods that must be implemented in any subclass.



# Example of an Abstract Class

# Let's create an example of an abstract class representing a general Shape. Different shapes like Circle and Rectangle will inherit from this abstract class and implement the required methods.

# Step 1: Create the Abstract Class

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         """Calculate the area of the shape."""
#         pass

#     @abstractmethod
#     def perimeter(self):
#         """Calculate the perimeter of the shape."""
#         pass

# Step 2: Create Subclasses

# Now, let’s implement subclasses for Circle and Rectangle that inherit from Shape and implement the abstract methods.

# class Circle(Shape):
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Rectangle(Shape):
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# Step 3: Using the Abstract Class and Subclasses

# Now, you can create instances of Circle and Rectangle and use their methods.

# # Create instances of Circle and Rectangle
# circle = Circle(5)
# rectangle = Rectangle(4, 6)

# # Calculate area and perimeter for Circle
# print(f"Circle Area: {circle.area():.2f}")        # Output: Circle Area: 78.54
# print(f"Circle Perimeter: {circle.perimeter():.2f}")  # Output: Circle Perimeter: 31.42

# # Calculate area and perimeter for Rectangle
# print(f"Rectangle Area: {rectangle.area()}")      # Output: Rectangle Area: 24
# print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Perimeter: 20

# Explanation of the Example

# 1. Abstract Class Shape:

# The Shape class is defined as an abstract class by inheriting from ABC.

# It contains two abstract methods, area() and perimeter(), which do not have implementations (pass).



# 2. Concrete Classes:

# The Circle class inherits from Shape and implements both the area() and perimeter() methods.

# The Rectangle class also inherits from Shape and provides its own implementations of area() and perimeter().



# 3. Instantiation and Usage:

# You can create instances of Circle and Rectangle, but you cannot instantiate the Shape class directly because it’s abstract.




# Attempting to Instantiate the Abstract Class

# If you try to create an instance of the abstract class, you will get a TypeError.

# # This will raise an error
# # shape = Shape()  # Uncommenting this will raise TypeError: Can't instantiate abstract class Shape

# Summary

# Abstract Class: Use the ABC module to define an abstract class.

# Abstract Methods: Define methods using the @abstractmethod decorator that subclasses must implement.

# Inheritance: Subclasses implement the abstract methods and can also have their own additional methods and attributes.


# Abstract classes are useful for defining common interfaces in a program, allowing for polymorphism and ensuring that derived classes implement specific methods.
