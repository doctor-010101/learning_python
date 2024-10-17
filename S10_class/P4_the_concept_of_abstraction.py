# Definition: Abstraction is a fundamental concept in object-oriented programming (OOP) that involves hiding the complex implementation details of a system while exposing only the essential features. This simplifies the interaction with the system and allows the programmer to focus on high-level functionalities without worrying about the underlying complexities.

# Purpose: The main goals of abstraction are to reduce complexity, increase efficiency, and improve code readability and maintainability. By exposing only the necessary components, abstraction allows users to interact with an object through a simplified interface.

# How Abstraction Works

# Abstraction can be implemented in Python using abstract classes and interfaces. Python provides the abc module, which allows you to define abstract base classes (ABCs). An abstract class can have both abstract methods (methods without implementation) and concrete methods (methods with implementation).

# Example of Abstraction

# Let’s illustrate the concept of abstraction using a practical example with an abstract class for a geometric shape:

# from abc import ABC, abstractmethod

# # Abstract base class for shapes
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         """Calculate the area of the shape."""
#         pass  # Abstract method

#     @abstractmethod
#     def perimeter(self):
#         """Calculate the perimeter of the shape."""
#         pass  # Abstract method

# # Concrete class for Rectangle
# class Rectangle(Shape):
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# # Concrete class for Circle
# class Circle(Shape):
#     def init(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14159 * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * 3.14159 * self.radius

# # Using the abstract class
# shapes = [Rectangle(3, 4), Circle(5)]

# for shape in shapes:
#     print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# Explanation of the Example

# 1. Abstract Class: The Shape class is defined as an abstract class that includes two abstract methods, area and perimeter. These methods do not have implementations and serve as placeholders for any concrete class that inherits from Shape.


# 2. Concrete Classes: The Rectangle and Circle classes inherit from the Shape class and provide specific implementations for the area and perimeter methods. This demonstrates abstraction, as users of these classes only need to know how to call these methods without needing to understand the underlying calculations.


# 3. Usage: When creating a list of shapes and iterating through it, we can call area and perimeter on each shape without knowing what specific type of shape it is. This encapsulates the complexity and provides a simple interface to work with different shapes.



# Advantages of Abstraction

# Simplifies Code: By focusing on high-level functionalities, abstraction reduces the complexity of the code.

# Enhances Code Reusability: Abstract classes can be reused in different contexts, allowing for more flexible and scalable designs.

# Improves Maintainability: Changes made to the implementation details of an abstract class do not affect the code that uses it, provided the interface remains the same.

# Promotes Separation of Concerns: It separates the definition of operations from the implementation, allowing different developers to work on different aspects of a program.


# Conclusion

# Abstraction is a powerful concept in object-oriented programming that helps manage complexity by hiding implementation details and exposing only the necessary features. By using abstract classes and interfaces, you can create flexible and maintainable code structures in Python.