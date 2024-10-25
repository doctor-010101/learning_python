# In Python, operator overloading (also known as operator overloading) allows you to define custom behavior for standard operators (like +, -, *, etc.) when they are applied to objects of your own classes. This is achieved by defining special methods in your class that correspond to the operators you want to overload.

# Special Methods for Operator Overloading

# Each operator corresponds to a specific special method in Python. Here are some commonly used operators and their associated special methods:

# +: add(self, other)

# -: sub(self, other)

# *: mul(self, other)

# /: truediv(self, other)

# //: floordiv(self, other)

# %: mod(self, other)

# **: pow(self, other)

# ==: eq(self, other)

# !=: ne(self, other)

# <: lt(self, other)

# <=: le(self, other)

# >: gt(self, other)

# >=: ge(self, other)


# Example of Operator Overloading

# Let’s create a simple Vector class that supports vector addition and subtraction using operator overloading.

# Step 1: Define the Vector Class

# class Vector:
#     def init(self, x, y):
#         self.x = x
#         self.y = y

#     def add(self, other):
#         """Overload the + operator to add two vectors."""
#         return Vector(self.x + other.x, self.y + other.y)

#     def sub(self, other):
#         """Overload the - operator to subtract two vectors."""
#         return Vector(self.x - other.x, self.y - other.y)

#     def mul(self, scalar):
#         """Overload the * operator to scale a vector by a scalar."""
#         return Vector(self.x * scalar, self.y * scalar)

#     def str(self):
#         """Provide a string representation of the vector."""
#         return f"Vector({self.x}, {self.y})"

# Step 2: Using the Vector Class

# Now, let's create some instances of the Vector class and use the overloaded operators.

# # Create two vector instances
# v1 = Vector(2, 3)
# v2 = Vector(5, 7)

# # Use the overloaded + operator
# v3 = v1 + v2
# print(f"v1 + v2 = {v3}")  # Output: v1 + v2 = Vector(7, 10)

# # Use the overloaded - operator
# v4 = v1 - v2
# print(f"v1 - v2 = {v4}")  # Output: v1 - v2 = Vector(-3, -4)

# # Use the overloaded * operator
# v5 = v1 * 3
# print(f"v1 * 3 = {v5}")  # Output: v1 * 3 = Vector(6, 9)

# Explanation of the Example

# 1. Vector Class: The Vector class represents a mathematical vector in two-dimensional space.


# 2. Operator Overloading:

# add: This method defines the behavior of the + operator. It adds two vectors and returns a new Vector instance.

# sub: This method defines the behavior of the - operator. It subtracts one vector from another and returns a new Vector instance.

# mul: This method allows for scalar multiplication, where a vector can be scaled by a number.



# 3. String Representation: The str method provides a readable string representation of the vector for printing.



# Additional Operators

# You can also overload other operators as needed. Here’s an example of overloading the equality operator (==):

# class Vector:
#     # ... (other methods remain the same)

#     def eq(self, other):
#         """Overload the == operator to compare two vectors."""
#         return self.x == other.x and self.y == other.y

# # Create two vectors and compare them
# v1 = Vector(2, 3)
# v2 = Vector(2, 3)
# v3 = Vector(5, 7)

# print(v1 == v2)  # Output: True
# print(v1 == v3)  # Output: False

# Summary

# Operator Overloading allows you to define custom behavior for standard operators for your own classes.

# You define special methods (like add, sub, etc.) to implement this functionality.

# This makes your classes more intuitive and easier to use, as they can interact with Python’s built-in operators.


# Using operator overloading can significantly improve the readability and usability of your classes, especially in mathematical or data structure contexts.
