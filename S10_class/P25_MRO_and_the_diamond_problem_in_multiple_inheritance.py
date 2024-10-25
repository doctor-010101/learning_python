
# Method Resolution Order (MRO) and the Diamond Problem in Multiple Inheritance

# 1. Method Resolution Order (MRO)

# Method Resolution Order (MRO) defines the order in which classes are searched when executing a method call on an object. In Python, the MRO is crucial in multiple inheritance scenarios to avoid ambiguity and ensure consistent behavior.

# Python uses the C3 linearization algorithm to determine the MRO. This algorithm ensures that:

# The order respects the hierarchy of the classes.

# Each class appears before its parent classes.

# A class does not appear before its parents or before itself.


# You can view the MRO of a class using the mro() method or the mro attribute.

# Example of MRO

# Let’s illustrate MRO with a simple example:

# class A:
#     def method(self):
#         print("Method from A")

# class B(A):
#     def method(self):
#         print("Method from B")

# class C(A):
#     def method(self):
#         print("Method from C")

# class D(B, C):
#     pass

# # Check the MRO of class D
# print(D.mro())

# Output:

# [<class 'main.D'>, <class 'main.B'>, <class 'main.C'>, <class 'main.A'>, <class 'object'>]

# Explanation:

# The MRO shows that when you call a method on an instance of D, Python will first look for method() in D, then in B, followed by C, and finally in A before looking in the base object class.

# In this case, if you create an instance of D and call method(), it will call B's method because B appears before C in the MRO.


# Example of Method Call Using MRO

# # Create an instance of D
# d = D()
# d.method()  # Output: Method from B

# Explanation:

# When we call d.method(), Python follows the MRO and calls method() from class B, since it is the first class in the MRO that defines the method.


# 2. The Diamond Problem

# The Diamond Problem occurs in multiple inheritance when a class inherits from two classes that both inherit from a common base class. This creates ambiguity about which inherited method should be called when the derived class attempts to use the method.

# Example of the Diamond Problem

# Let’s see how the diamond problem arises:

# class Grandparent:
#     def greet(self):
#         print("Hello from Grandparent")

# class Parent1(Grandparent):
#     def greet(self):
#         print("Hello from Parent1")

# class Parent2(Grandparent):
#     def greet(self):
#         print("Hello from Parent2")

# class Child(Parent1, Parent2):
#     pass

# # Create an instance of Child class
# child = Child()

# # Call the greet method
# child.greet()

# Output:

# Hello from Parent1

# Explanation:

# The Child class inherits from both Parent1 and Parent2, which both inherit from Grandparent.

# The MRO for Child will ensure that when greet() is called on an instance of Child, Python first looks in Parent1 (since it appears first in the inheritance list), so it executes Parent1's greet() method.

# If you check the MRO:


# print(Child.mro())

# You will see:

# [<class 'main.Child'>, <class 'main.Parent1'>, <class 'main.Parent2'>, <class 'main.Grandparent'>, <class 'object'>]

# This shows the order of class resolution.

# Solving the Diamond Problem

# Python’s C3 linearization algorithm effectively handles the diamond problem by determining the MRO. It ensures that:

# Child calls Parent1's method instead of Parent2's method, avoiding ambiguity.


# If we change the order of inheritance in Child, the output will change as follows:

# class Child(Parent2, Parent1):
#     pass

# child = Child()
# child.greet()

# Output:

# Hello from Parent2

# Explanation:

# In this case, Child inherits from Parent2 first, so Parent2's greet() method is called.


# Summary

# Method Resolution Order (MRO) is crucial in multiple inheritance scenarios, ensuring a consistent method lookup order and resolving conflicts.

# The Diamond Problem illustrates the ambiguity that can arise when multiple classes share a common ancestor. Python's MRO resolves this ambiguity by following a specific order, allowing developers to understand and control the behavior of their classes.
# By using the MRO and understanding the diamond problem, you can effectively design and implement class hierarchies in Python without facing unexpected behavior.
