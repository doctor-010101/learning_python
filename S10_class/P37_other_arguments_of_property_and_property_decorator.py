# In Python, the property decorator provides a convenient way to manage attribute access while allowing additional functionality. Besides the basic usage we discussed earlier, the property decorator can also take additional arguments and support the use of different property types.

# Additional Arguments for the property Decorator

# When defining properties, you can use additional arguments to specify behavior for the property in terms of its getter, setter, and deleter methods. The syntax for using property is as follows:

# property(fget=None, fset=None, fdel=None, doc=None)

# fget: A function for getting the value of the property.

# fset: A function for setting the value of the property.

# fdel: A function for deleting the property.

# doc: A string for the documentation of the property.


# Example of Using All Arguments with Property

# Let's create a class that demonstrates how to use all arguments of the property decorator:

# class Circle:
#     def init(self, radius):
#         self.__radius = radius

#     # Getter for radius
#     @property
#     def radius(self):
#         """Get the radius of the circle."""
#         return self.__radius

#     # Setter for radius
#     @radius.setter
#     def radius(self, value):
#         """Set the radius of the circle, must be non-negative."""
#         if value < 0:
#             raise ValueError("Radius cannot be negative.")
#         self.__radius = value

#     # Deleter for radius
#     @radius.deleter
#     def radius(self):
#         """Delete the radius of the circle."""
#         print("Deleting radius...")
#         del self.__radius

#     # Method to calculate area
#     @property
#     def area(self):
#         """Calculate the area of the circle."""
#         import math
#         return math.pi * (self.__radius ** 2)

# Using the Circle Class

# Now let's create an instance of the Circle class and demonstrate the use of the property methods.

# # Create an instance of Circle
# circle = Circle(5)

# # Access radius using the getter
# print(f"Radius: {circle.radius}")  # Output: Radius: 5

# # Access area using the area property
# print(f"Area: {circle.area}")  # Output: Area: 78.53981633974483

# # Modify radius using the setter
# circle.radius = 10
# print(f"New Radius: {circle.radius}")  # Output: New Radius: 10

# # Access new area
# print(f"New Area: {circle.area}")  # Output: New Area: 314.1592653589793

# # Attempting to set a negative radius
# # circle.radius = -3  # Uncommenting this will raise ValueError

# # Deleting the radius
# del circle.radius  # Output: Deleting radius...
# # Trying to access radius after deletion will raise an AttributeError
# # print(circle.radius)  # Uncommenting this will raise an AttributeError

# Explanation of the Circle Class

# 1. Getter:

# The radius property allows access to the private attribute __radius.



# 2. Setter:

# The radius setter ensures that the radius cannot be set to a negative value.



# 3. Deleter:

# The radius deleter allows you to delete the radius attribute and can include additional logic, such as printing a message.



# 4. Area Property:

# The area property calculates the area of the circle based on the current radius without needing a setter because the area should not be directly set by the user.




# Advantages of Using property with Arguments

# Encapsulation: You can control how attributes are accessed and modified.

# Readability: The use of properties makes the class interface cleaner, allowing attribute-like access.

# Validation and Logic: You can implement validation or additional logic when getting, setting, or deleting an attribute.


# Summary

# The property decorator in Python provides a powerful way to manage attribute access with the ability to include getter, setter, and deleter methods. By using the additional arguments of the property decorator, you can create a more robust and maintainable interface for your classes.
