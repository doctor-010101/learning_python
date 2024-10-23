# In Python, the repr and str methods are special methods that define how an object should be represented as a string. These methods are often used for debugging and logging purposes, and they provide a way to control how your objects appear when printed or converted to strings.

# 1. str Method

# Purpose: The str method is intended to provide a "pretty" or user-friendly string representation of an object. It is called by the built-in str() function and when you use print() on an object.

# Usage: It should return a string that is easy to read and provides a clear description of the object.


# Example of str

# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.age = age

#     def str(self):
#         return f"{self.name}, age {self.age}"

# # Creating an instance of Person
# person = Person("Alice", 30)

# # Using str() and print()
# print(person)  # Output: Alice, age 30
# print(str(person))  # Output: Alice, age 30

# 2. repr Method

# Purpose: The repr method is intended to provide a more formal string representation of an object that is mainly used for debugging and development. It should return a string that, when passed to the eval() function, would ideally recreate the object. If that's not possible, it should at least provide enough information to identify the object.

# Usage: It is called by the built-in repr() function and is also used when you inspect the object in an interactive session.


# Example of repr

# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.age = age

#     def repr(self):
#         return f"Person(name='{self.name}', age={self.age})"

# # Creating an instance of Person
# person = Person("Alice", 30)

# # Using repr()
# print(repr(person))  # Output: Person(name='Alice', age=30)

# How They Work Together

# If you define both methods in your class, the following rules apply:

# If you use print() or str() on an object, Python will call the str method if it exists. If str is not defined, it will fall back to repr.

# If you use repr() or inspect the object in the interactive interpreter, Python will call the repr method.


# Example Combining Both Methods

# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.age = age

#     def str(self):
#         return f"{self.name}, age {self.age}"

#     def repr(self):
#         return f"Person(name='{self.name}', age={self.age})"

# # Creating an instance of Person
# person = Person("Alice", 30)

# # Using print (calls str)
# print(person)  # Output: Alice, age 30

# # Using repr (calls repr)
# print(repr(person))  # Output: Person(name='Alice', age=30)

# Summary

# str:

# Intended for a user-friendly representation of the object.

# Used by str() and print().

# Should return a readable string that conveys the essential information.


# repr:

# Intended for an unambiguous representation of the object.

# Used by repr() and in the interactive interpreter.

# Should return a string that can ideally recreate the object or provide useful debugging information.



# By implementing these methods, you can improve how your objects are represented as strings, making your code more user-friendly and easier to debug.