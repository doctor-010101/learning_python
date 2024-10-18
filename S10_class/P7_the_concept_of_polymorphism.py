# Polymorphism in Python refers to the ability of different classes to provide different implementations for the same method. It allows functions to use objects of different types as long as they share a common interface. This concept is a core part of Object-Oriented Programming (OOP) and emphasizes that "one interface can have multiple forms."

# In Python, polymorphism is often demonstrated with methods that have the same name across different classes. Python is a dynamically typed language, so it doesn't require explicit declaration of types, making it easier to apply polymorphism.

# Example of Polymorphism:

# Let's look at an example where two different classes (Dog and Cat) both have a speak method, but their implementations are different:

# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# # A function that uses polymorphism
# def animal_sound(animal):
#     print(animal.speak())

# # Creating objects of Dog and Cat
# dog = Dog()
# cat = Cat()

# # Calling the same function with different types of objects
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!

# Explanation:

# We define two classes Dog and Cat, each with a speak method that returns a different string.

# The function animal_sound takes an object (could be any object with a speak method) and calls its speak method.

# Even though the function animal_sound is the same, when we pass a Dog object, it prints "Woof!" and when we pass a Cat object, it prints "Meow!".

# This demonstrates polymorphism, where a single interface (speak) is implemented differently by different classes.


# Benefits of Polymorphism:

# Code Reusability: You can write more general code that works with objects of various types.

# Maintainability: New classes can be added without changing existing code that uses polymorphic functions.