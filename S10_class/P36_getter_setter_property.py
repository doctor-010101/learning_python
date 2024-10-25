# In Python, getters, setters, and properties are used to manage access to instance attributes in a class, allowing for encapsulation and controlled access. Here’s a detailed explanation of each concept along with examples.

# Getters and Setters

# Getters and setters are methods that allow you to access and modify the attributes of a class while encapsulating the internal representation of the data. They help to enforce encapsulation and provide a way to add logic when getting or setting a value.

# 1. Getter: A method that retrieves the value of an attribute.


# 2. Setter: A method that sets the value of an attribute, often with validation or additional logic.



# Example of Getters and Setters

# Let’s create a Person class with private attributes for name and age, and use getters and setters to manage these attributes.

# class Person:
#     def init(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age    # Private attribute

#     # Getter for name
#     def get_name(self):
#         return self.__name

#     # Setter for name
#     def set_name(self, name):
#         self.__name = name

#     # Getter for age
#     def get_age(self):
#         return self.__age

#     # Setter for age with validation
#     def set_age(self, age):
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         self.__age = age

# Using Getters and Setters

# # Create an instance of Person
# person = Person("Alice", 30)

# # Access name using getter
# print(person.get_name())  # Output: Alice

# # Modify name using setter
# person.set_name("Bob")
# print(person.get_name())  # Output: Bob

# # Access age using getter
# print(person.get_age())  # Output: 30

# # Modify age using setter
# person.set_age(35)
# print(person.get_age())  # Output: 35

# # Attempting to set a negative age
# # person.set_age(-5)  # Uncommenting this will raise ValueError

# Properties in Python

# Properties provide a more Pythonic way to use getters and setters. Instead of explicitly defining getter and setter methods, you can use the property decorator to manage access to attributes.

# Example Using Properties

# Here’s the same Person class, but this time using properties:

# class Person:
#     def init(self, name, age):
#         self.__name = name
#         self.__age = age

#     # Getter for name using property decorator
#     @property
#     def name(self):
#         return self.__name

#     # Setter for name
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     # Getter for age using property decorator
#     @property
#     def age(self):
#         return self.__age

#     # Setter for age with validation
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         self.__age = age

# Using Properties

# # Create an instance of Person
# person = Person("Alice", 30)

# # Access name using property
# print(person.name)  # Output: Alice

# # Modify name using property setter
# person.name = "Bob"
# print(person.name)  # Output: Bob

# # Access age using property
# print(person.age)  # Output: 30

# # Modify age using property setter
# person.age = 35
# print(person.age)  # Output: 35

# # Attempting to set a negative age
# # person.age = -5  # Uncommenting this will raise ValueError

# Summary

# 1. Getters and Setters: Allow controlled access to private attributes but require explicit method calls to access or modify values.


# 2. Properties: Provide a cleaner and more Pythonic way to manage access to attributes. They allow you to use attribute-like access syntax while still providing the benefits of encapsulation.



# Advantages of Using Properties

# Encapsulation: Properties encapsulate the internal representation of an object.

# Validation: You can add validation logic in the setter methods to ensure the integrity of the data.

# Simplicity: Properties make your code cleaner and easier to read by allowing attribute access without needing to call methods.

# This way, using properties can help create a more maintainable and understandable interface for your classes in Python.
