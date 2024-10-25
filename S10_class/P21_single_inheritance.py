# Single Inheritance in Python refers to a situation where a class (child or derived class) inherits properties and behavior from a single parent (or base) class. This is one of the most fundamental types of inheritance, where the derived class can use or modify the attributes and methods of the base class.

# Key Points:

# The child class can access all non-private members (methods and attributes) of the parent class.

# It enables code reusability and reduces redundancy.

# The child class can override methods from the parent class if necessary.


# Syntax:

# class Parent:
#     # Parent class constructor
#     def init(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, I am {self.name}")

# # Child class inheriting from Parent class
# class Child(Parent):
#     def display(self):
#         print(f"{self.name} is a child.")

# # Create an object of the Child class
# child = Child("Alice")
# child.greet()  # Inherited from Parent class
# child.display()  # Child class's own method

# Explanation:

# The Parent class defines a constructor (init) and a method greet.

# The Child class inherits the Parent class, meaning it can access all non-private members of Parent, like the greet() method.

# The Child class also defines its own method display().

# An object of the Child class can call both the inherited greet() method and the new display() method.

# This is an example of single inheritance, as the Child class inherits from only one parent class (Parent).
