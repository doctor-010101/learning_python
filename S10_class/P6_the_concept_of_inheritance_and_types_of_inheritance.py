# Definition: Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (known as the child or derived class) to inherit the properties and methods of an existing class (known as the parent or base class). This promotes code reusability and establishes a hierarchical relationship between classes.

# Purpose of Inheritance

# Code Reusability: Allows the child class to reuse the methods and attributes of the parent class, reducing redundancy.

# Hierarchical Classification: Establishes a clear hierarchy among classes, making the design easier to understand.

# Extensibility: New functionality can be added to existing classes without modifying them, promoting better maintainability.


# Types of Inheritance

# There are several types of inheritance in Python, including:

# 1. Single Inheritance


# 2. Multiple Inheritance


# 3. Multilevel Inheritance


# 4. Hierarchical Inheritance


# 5. Hybrid Inheritance



# Let’s explore each type with examples.


# ---

# 1. Single Inheritance

# Definition: In single inheritance, a child class inherits from only one parent class.

# Example:

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         return "Dog barks"

# # Creating an instance of Dog
# dog = Dog()
# print(dog.speak())  # Output: Animal speaks
# print(dog.bark())   # Output: Dog barks

# Explanation:

# The Dog class inherits the speak method from the Animal class. It also has its own method, bark.



# ---

# 2. Multiple Inheritance

# Definition: In multiple inheritance, a child class can inherit from more than one parent class.

# Example:

# class Flyer:
#     def fly(self):
#         return "Flying"

# class Swimmer:
#     def swim(self):
#         return "Swimming"

# class Duck(Flyer, Swimmer):  # Duck inherits from Flyer and Swimmer
#     def quack(self):
#         return "Quack"

# # Creating an instance of Duck
# duck = Duck()
# print(duck.fly())   # Output: Flying
# print(duck.swim())  # Output: Swimming
# print(duck.quack()) # Output: Quack

# Explanation:

# The Duck class inherits methods from both Flyer and Swimmer, demonstrating multiple inheritance.



# ---

# 3. Multilevel Inheritance

# Definition: In multilevel inheritance, a class is derived from another derived class, forming a chain of inheritance.

# Example:

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         return "Dog barks"

# class Puppy(Dog):  # Puppy inherits from Dog
#     def whimper(self):
#         return "Puppy whimpers"

# # Creating an instance of Puppy
# puppy = Puppy()
# print(puppy.speak())   # Output: Animal speaks
# print(puppy.bark())    # Output: Dog barks
# print(puppy.whimper()) # Output: Puppy whimpers

# Explanation:

# The Puppy class inherits from Dog, which in turn inherits from Animal. Thus, it can access methods from both its parent (Dog) and grandparent (Animal).



# ---

# 4. Hierarchical Inheritance

# Definition: In hierarchical inheritance, multiple child classes inherit from a single parent class.

# Example:

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         return "Dog barks"

# class Cat(Animal):  # Cat also inherits from Animal
#     def meow(self):
#         return "Cat meows"

# # Creating instances
# dog = Dog()
# cat = Cat()
# print(dog.speak())  # Output: Animal speaks
# print(cat.speak())  # Output: Animal speaks
# print(dog.bark())   # Output: Dog barks
# print(cat.meow())   # Output: Cat meows

# Explanation:

# Both Dog and Cat inherit from the Animal class, demonstrating hierarchical inheritance.



# ---

# 5. Hybrid Inheritance

# Definition: Hybrid inheritance is a combination of two or more types of inheritance. It can be complex and often involves a mix of different inheritance types.

# Example:

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Flyer:
#     def fly(self):
#         return "Flying"
    

# class Bat(Animal, Flyer):  # Bat inherits from both Animal and Flyer
#     def screech(self):
#         return "Bat screeches"

# class Sparrow(Flyer):
#     def chirp(self):
#         return "Sparrow chirps"

# # Creating instances
# bat = Bat()
# sparrow = Sparrow()
# print(bat.speak())     # Output: Animal speaks
# print(bat.fly())       # Output: Flying
# print(bat.screech())   # Output: Bat screeches
# print(sparrow.fly())    # Output: Flying
# print(sparrow.chirp())  # Output: Sparrow chirps

# Explanation:

# The Bat class demonstrates hybrid inheritance as it inherits from both Animal and Flyer, while Sparrow inherits from Flyer.



# ---

# Conclusion

# Inheritance is a powerful feature in object-oriented programming that allows for code reusability, extensibility, and a clear hierarchical structure. Understanding the different types of inheritance helps in designing robust and maintainable systems.