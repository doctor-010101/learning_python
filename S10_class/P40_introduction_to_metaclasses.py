# In Python, metaclasses are a deep and powerful aspect of the language that allow you to customize class creation. Metaclasses are the "classes of a class." In other words, just as a class defines the behavior of its instances, a metaclass defines the behavior of classes themselves. This can be useful for enforcing rules, adding attributes or methods, or modifying class definitions.

# What is a Metaclass?

# A metaclass is a class whose instances are classes. You can think of it as a blueprint for creating classes. By default, Python uses the type metaclass to create all classes. However, you can define your own metaclass to customize class creation.

# Basic Example of a Metaclass

# Here’s a simple example to demonstrate how to create and use a metaclass.

# Step 1: Define a Metaclass

# # Define a metaclass
# class MyMeta(type):
#     def new(cls, name, bases, attrs):
#         # Print information about class creation
#         print(f"Creating class: {name}")
        
#         # Modify class attributes
#         attrs['greeting'] = "Hello, World!"
        
#         # Call the superclass to create the class
#         return super().new(cls, name, bases, attrs)

# Step 2: Use the Metaclass in a Class Definition

# # Use the metaclass in a class
# class MyClass(metaclass=MyMeta):
#     def say_hello(self):
#         return self.greeting

# # Create an instance of MyClass
# my_instance = MyClass()
# print(my_instance.say_hello())  # Output: Hello, World!

# Explanation of the Example

# 1. Defining the Metaclass:

# MyMeta is defined as a subclass of type.

# The new method is overridden, which is responsible for creating the new class.

# Inside new, you can modify the class attributes, add methods, or enforce constraints.



# 2. Using the Metaclass:

# When defining MyClass, you specify metaclass=MyMeta.

# When MyClass is created, the new method of MyMeta is called, and it prints a message.

# The greeting attribute is added to MyClass during its creation.



# 3. Instance Creation:

# An instance of MyClass is created, and the say_hello method accesses the greeting attribute, which was added by the metaclass.




# Use Cases for Metaclasses

# Metaclasses can be used for various purposes, including:

# Validation: Ensure that class attributes or methods meet certain criteria.

# Automatic Registration: Automatically register classes when they are created.

# Customizing Class Behavior: Add or modify methods or properties dynamically.

# Singleton Pattern: Enforce that only one instance of a class is created.


# More Advanced Example

# Here’s a more advanced example that demonstrates validation of class attributes.

# # Define a metaclass that enforces certain constraints
# class ValidateAttributes(type):
#     def new(cls, name, bases, attrs):
#         # Check if 'name' attribute is present
#         if 'name' not in attrs:
#             raise ValueError(f"{name} must have a 'name' attribute.")
#         # Ensure 'age' is an integer if present
#         if 'age' in attrs and not isinstance(attrs['age'], int):
#             raise TypeError(f"'age' must be an integer in class {name}.")
        
#         return super().new(cls, name, bases, attrs)

# # Define a class using the metaclass
# class Person(metaclass=ValidateAttributes):
#     name = "Alice"
#     age = 30

# # This will work fine
# person = Person()

# # Uncommenting the following will raise an error
# # class InvalidPerson(metaclass=ValidateAttributes):
# #     pass  # Raises ValueError

# # class InvalidPerson2(metaclass=ValidateAttributes):
# #     name = "Bob"
# #     age = "thirty"  # Raises TypeError

# Explanation of the Advanced Example

# 1. Custom Metaclass:

# ValidateAttributes checks if the name attribute is present and verifies that age, if present, is an integer.

# If these conditions are not met, it raises an error.



# 2. Defining Classes:

# The Person class is defined with valid attributes and will work without issues.

# If you try to define InvalidPerson without a name attribute or InvalidPerson2 with a non-integer age, it raises the appropriate error.




# Summary
# Metaclasses are a powerful feature in Python that allow you to control the creation of classes.

# You define a metaclass by inheriting from type and overriding the new method.

# Metaclasses can be used for validation, automatic registration, and modifying class behavior.

# They provide a way to implement patterns and constraints that apply to all classes created with that metaclass.


# Understanding metaclasses can greatly enhance your ability to write flexible and reusable code in Python, especially in frameworks and libraries where dynamic class behavior is often needed.
