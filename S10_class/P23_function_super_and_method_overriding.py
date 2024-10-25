
# Method Overriding and the super() Function in Python are key concepts in Object-Oriented Programming (OOP), especially in inheritance.

# 1. Method Overriding:

# Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. The method in the child class overrides (replaces) the method from the parent class.

# The overridden method in the child class can have different functionality or behavior, but it must have the same name and signature (parameters) as the method in the parent class.

# Method overriding is useful when the child class needs to extend or modify the behavior of an inherited method without changing it for the parent class.


# 2. super() Function:

# The super() function is used to call a method from the parent class inside the child class. It’s particularly useful in method overriding, where the child class wants to add some behavior to the parent class's method instead of completely replacing it.

# super() gives access to methods and properties of the parent class without explicitly referring to the parent class's name.

# It ensures that the parent class is properly initialized and prevents calling the parent class’s method more than once in complex multiple inheritance scenarios.


# Example of Method Overriding with super()

# Let’s look at an example where we have a base class Animal and a derived class Dog that overrides the sound() method of Animal. In the derived class, we’ll use super() to still access the parent class's constructor.

# # Base class
# class Animal:
#     def init(self, name):
#         self.name = name

#     def sound(self):
#         print(f"{self.name} makes a sound.")

# # Derived class
# class Dog(Animal):
#     def init(self, name, breed):
#         # Call the constructor of the parent class (Animal)
#         super().init(name)  # Initialize 'name' attribute
#         self.breed = breed

#     # Overriding the sound() method from the parent class
#     def sound(self):
#         print(f"{self.name}, the {self.breed}, barks.")

# # Create an instance of the Dog class
# dog = Dog("Rex", "Labrador")

# # Call the overridden method
# dog.sound()  # Output: Rex, the Labrador, barks.

# Explanation:

# The Animal class has a sound() method that prints a general message.

# The Dog class inherits from Animal and overrides the sound() method to print a more specific message (barking).

# The super().init(name) in the Dog class's constructor calls the init method of the Animal class, so the name attribute is initialized by the parent class.


# In this case, the Dog class extends the functionality of the Animal class by overriding the sound() method, providing a more specific behavior for dogs, while still retaining access to the parent class’s constructor.

# Another Example: Using super() with Overridden Methods

# Sometimes, you want to override a method in the child class but still execute the parent class’s version of the method as part of the process. Let’s demonstrate this with an example:

# # Parent class
# class Vehicle:
#     def init(self, brand):
#         self.brand = brand
    
#     def start(self):
#         print(f"{self.brand} is starting.")

# # Child class
# class Car(Vehicle):
#     def start(self):
#         # Call the parent class's start method using super()
#         super().start()
#         # Add additional functionality
#         print("Car is now ready to drive.")

# # Create an instance of the Car class
# my_car = Car("Toyota")

# # Call the overridden start method
# my_car.start()

# Output:

# Toyota is starting.
# Car is now ready to drive.

# Explanation:

# The Car class overrides the start() method of the Vehicle class.

# Inside the overridden start() method in Car, the super().start() calls the start() method of the parent class (Vehicle), which prints a message.

# After calling the parent class method, the Car class adds its own message, demonstrating how you can extend the behavior of the parent class without completely replacing it.
# Why Use super()?
# 1. Avoiding Code Duplication: Instead of rewriting the logic of the parent class method, you can reuse it via super() and extend or modify only what’s necessary in the child class.


# 2. Maintainability: If the parent class method is updated in the future, your child class automatically benefits from those changes.


# 3. Multiple Inheritance: In cases of multiple inheritance, super() is critical because it ensures that the right method from the correct class in the inheritance hierarchy is called.



# Key Takeaways:

# Method overriding allows a child class to modify or extend the behavior of a method from its parent class.

# The super() function is used to call methods or constructors from the parent class, enabling reuse of functionality.

# You can override methods and still access the parent class’s version of the method to enhance or modify it.

# super() is particularly important in complex inheritance scenarios, ensuring proper initialization and method resolution.
