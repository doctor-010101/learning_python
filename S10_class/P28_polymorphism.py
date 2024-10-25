# Polymorphism in Python

# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common super class. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism can be implemented through:

# 1. Method Overriding: A derived class can provide a specific implementation of a method that is already defined in its base class.


# 2. Duck Typing: Python uses duck typing, meaning that the type or class of an object is less important than the methods it defines or the behaviors it exhibits.



# Key Aspects of Polymorphism

# 1. Method Overriding: In method overriding, a subclass provides a specific implementation of a method that is already defined in its parent class. This allows the subclass to customize or extend the behavior of the method.


# 2. Duck Typing: In Python, if an object behaves like a certain type (i.e., it implements the required methods), it can be treated as that type. This means that you don’t need to check the actual type of an object, making Python very flexible.



# Examples of Polymorphism

# 1. Method Overriding

# Let's look at an example with classes representing different shapes:

# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class Rectangle(Shape):
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# # Function to calculate area of different shapes
# def print_area(shape):
#     print(f"The area is: {shape.area()}")

# # Create instances of shapes
# rectangle = Rectangle(5, 10)
# circle = Circle(7)

# # Using polymorphism to calculate areas
# print_area(rectangle)  # Output: The area is: 50
# print_area(circle)     # Output: The area is: 153.86

# Explanation:

# The Shape class has a method area() that is overridden by the Rectangle and Circle classes.

# The print_area() function can take any shape and call its area() method without needing to know what type of shape it is, demonstrating polymorphism.


# 2. Duck Typing

# In Python, you can use duck typing to create functions that accept any object that has a specific method, regardless of its type:

# class Dog:
#     def sound(self):
#         return "Woof!"

# class Cat:
#     def sound(self):
#         return "Meow!"

# class Duck:
#     def sound(self):
#         return "Quack!"

# def animal_sound(animal):
#     print(animal.sound())

# # Create instances of different animals
# dog = Dog()
# cat = Cat()
# duck = Duck()

# # Call the animal_sound function
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!
# animal_sound(duck) # Output: Quack!

# Explanation:

# The animal_sound() function accepts any object and calls its sound() method.

# It works with Dog, Cat, and Duck because all of them implement the sound() method, regardless of their actual types.


# Summary of Polymorphism

# Polymorphism allows methods to do different things based on the object calling them, which enhances flexibility and maintainability in code.

# Method Overriding allows subclasses to provide specific implementations of methods defined in base classes.

# Duck Typing emphasizes the behavior of an object over its type, allowing for a more dynamic and flexible coding style in Python.


# Polymorphism is a powerful concept that can make your code more modular and easier to maintain by allowing different types of objects to be processed through the same interface.
