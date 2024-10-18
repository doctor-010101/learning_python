# In Python, objects are instances of classes, and they are the fundamental building blocks of Python's object-oriented programming (OOP) paradigm. Almost everything in Python is an object, including data types like strings, integers, lists, and even functions. Each object belongs to a class that defines the properties (attributes) and behaviors (methods) that the object will have.

# Key Concepts Related to Objects in Python:

# 1. Class: A blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that the objects created from the class will have.


# 2. Object: An instance of a class. When a class is defined, no memory is allocated until an object of that class is created.


# 3. Attributes: Variables that store data specific to an object.


# 4. Methods: Functions defined within a class that describe the behaviors of the objects.



# Example of Creating and Using Objects:

# # Defining a class
# class Car:
#     # Constructor (initializer) to set attributes
#     def init(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     # Method to display car information
#     def display_info(self):
#         return f"Car: {self.year} {self.brand} {self.model}"

# # Creating an object (instance) of the Car class
# my_car = Car("Toyota", "Corolla", 2020)

# # Accessing object attributes
# print(my_car.brand)  # Output: Toyota

# # Calling an object method
# print(my_car.display_info())  # Output: Car: 2020 Toyota Corolla

# Explanation:

# 1. Class Definition (Car): We define a class Car that has attributes (brand, model, year) and a method display_info.


# 2. Constructor (init): The init method is a special method used to initialize the object's attributes when it is created. This is where we assign values to the object's attributes.


# 3. Object Creation (my_car): We create an object my_car by calling the class Car and passing the values for its attributes (brand, model, year).


# 4. Accessing Attributes: We can access the attributes of an object using dot notation (my_car.brand).


# 5. Calling Methods: Similarly, we can call the method display_info() on the object to get a formatted string with the car's details.



# Everything is an Object in Python:

# In Python, even primitive data types like integers and strings are objects. For example:

# # Integer object
# x = 10
# print(x.class)  # Output: <class 'int'>

# # String object
# s = "Hello"
# print(s.class)  # Output: <class 'str'>

# This shows that even simple types like int and str are objects of their respective classes.

# Summary:

# An object is an instance of a class.

# Objects have attributes (data) and methods (behaviors) defined by their class.

# Python is a highly object-oriented language where everything (even numbers and functions) is an object.


# Objects in Python help you encapsulate and organize data and functions in a clean, reusable way.