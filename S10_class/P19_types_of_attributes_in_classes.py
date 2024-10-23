# In Python, attributes in a class can be classified into several types based on their scope, accessibility, and behavior. Here are the main types of attributes you will encounter in a class:

# 1. Instance Attributes

# Definition: Instance attributes are tied to a specific instance (object) of the class. They are defined within the init method (or other instance methods) using the self keyword.

# Accessibility: Each instance of the class can have different values for its instance attributes.


# Example:

# class Dog:
#     def init(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

# # Creating instances
# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)

# print(dog1.name)  # Output: Buddy
# print(dog2.name)  # Output: Max

# 2. Class Attributes

# Definition: Class attributes are shared among all instances of a class. They are defined directly within the class body, outside of any instance methods.

# Accessibility: All instances share the same value for class attributes unless overridden by instance attributes.


# Example:

# class Dog:
#     species = "Canis familiaris"  # Class attribute

#     def init(self, name, age):
#         self.name = name
#         self.age = age

# # Creating instances
# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)

# print(dog1.species)  # Output: Canis familiaris
# print(dog2.species)  # Output: Canis familiaris

# 3. Static Attributes

# Definition: Static attributes are similar to class attributes but are often used in conjunction with @staticmethod. They are not tied to instances or class methods.

# Accessibility: These attributes are accessed through the class name or an instance, but they are not typically modified.


# Example:

# class Math:
#     pi = 3.14159  # Static attribute

#     @staticmethod
#     def calculate_circle_area(radius):
#         return Math.pi * radius ** 2

# print(Math.pi)  # Output: 3.14159
# print(Math.calculate_circle_area(5))  # Output: 78.53975

# 4. Private Attributes

# Definition: Private attributes are intended to be hidden from outside access. They are defined with a double underscore prefix (__), which triggers name mangling.

# Accessibility: These attributes can only be accessed from within the class and should not be accessed directly from outside.


# Example:

# class BankAccount:
#     def init(self, balance):
#         self.__balance = balance  # Private attribute

#     def get_balance(self):
#         return self.__balance

# # Creating an instance
# account = BankAccount(1000)

# print(account.get_balance())  # Output: 1000
# # print(account.__balance)    # Raises AttributeError

# 5. Protected Attributes

# Definition: Protected attributes are intended to be accessible only within the class and its subclasses. They are defined with a single underscore prefix (_).

# Accessibility: Although they can be accessed from outside, it is a convention to indicate that they should not be accessed directly.


# Example:

# class Parent:
#     def init(self):
#         self._protected_attr = "I am protected"  # Protected attribute

# class Child(Parent):
#     def show_protected_attr(self):
#         return self._protected_attr  # Accessible in subclass

# # Creating an instance
# child = Child()
# print(child.show_protected_attr())  # Output: I am protected

# Summary of Attribute Types

# Instance Attributes: Specific to each object; defined in init with self.

# Class Attributes: Shared across all instances; defined in the class body.

# Static Attributes: Similar to class attributes, often used with @staticmethod.

# Private Attributes: Hidden from outside access; defined with __ prefix.

# Protected Attributes: Intended for internal use; defined with _ prefix.


# Understanding these different types of attributes helps you design your classes more effectively, control access to the internal state, and promote encapsulation in your object-oriented programming practices.