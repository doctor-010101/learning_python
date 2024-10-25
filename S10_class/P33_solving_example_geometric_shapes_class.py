# Let’s create a Python example using classes to represent different geometric shapes. We’ll define a base class called Shape and derived classes for specific shapes such as Circle, Rectangle, and Triangle. Each shape will have its own method to calculate the area.

# Step 1: Define the Base Class

# The Shape class will serve as a base class, and we will define a method for calculating the area, which will be overridden in the derived classes.

# class Shape:
#     def area(self):
#         raise NotImplementedError("This method should be overridden by subclasses")

# Step 2: Define Derived Classes

# Now, we will define specific shape classes that inherit from Shape and implement their own area methods.

# Circle Class

# import math

# class Circle(Shape):
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# Rectangle Class

# class Rectangle(Shape):
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# Triangle Class

# class Triangle(Shape):
#     def init(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# Step 3: Create a Function to Calculate Area

# We can now create a function that takes any shape and prints its area. This function will utilize polymorphism, allowing it to accept any object derived from the Shape class.

# def print_area(shape):
#     print(f"The area is: {shape.area()}")

# Step 4: Use the Classes

# Now, let’s create instances of each shape and print their areas.

# # Create instances of the shapes
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# triangle = Triangle(3, 4)

# # Calculate and print the areas
# print_area(circle)      # Output: The area is: 78.53981633974483
# print_area(rectangle)   # Output: The area is: 24
# print_area(triangle)    # Output: The area is: 6.0

# Complete Code Example

# Here’s the complete code for reference:

# import math

# class Shape:
#     def area(self):
#         raise NotImplementedError("This method should be overridden by subclasses")

# class Circle(Shape):
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# class Rectangle(Shape):
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def init(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# def print_area(shape):
#     print(f"The area is: {shape.area()}")

# # Create instances of the shapes
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# triangle = Triangle(3, 4)

# # Calculate and print the areas
# print_area(circle)      # Output: The area is: 78.53981633974483
# print_area(rectangle)   # Output: The area is: 24
# print_area(triangle)    # Output: The area is: 6.0

# Explanation:

# 1. Base Class: The Shape class serves as a base class with an abstract area() method, which must be overridden by any subclass.


# 2. Derived Classes: The Circle, Rectangle, and Triangle classes inherit from Shape and implement their own logic for calculating the area.


# 3. Polymorphism: The print_area function demonstrates polymorphism, as it can take any object of a class that derives from Shape and call its area() method.



# This example showcases how to use classes and inheritance in Python to model geometric shapes while leveraging polymorphism to operate on different shapes seamlessly.
