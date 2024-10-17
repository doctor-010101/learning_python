# Relationships in Object-Oriented Programming: Association, Composition, and Aggregation

# In object-oriented programming (OOP), understanding how classes and objects interact with each other is crucial for designing effective and modular systems. Three important concepts that describe these interactions are association, composition, and aggregation. Let’s explore each of these concepts with definitions and examples in Python.


# ---

# 1. Association

# Definition: Association represents a relationship between two classes where one class uses or interacts with another. This is a "uses-a" relationship, meaning that one class may use or reference another class but does not manage its lifecycle.

# Characteristics:

# It can be one-to-one, one-to-many, or many-to-many.

# The involved classes maintain their own lifecycle.


# Example of Association

# class Driver:
#     def init(self, name):
#         self.name = name

#     def drive(self, car):
#         print(f"{self.name} is driving a {car.model}.")

# class Car:
#     def init(self, model):
#         self.model = model

# # Creating instances
# driver = Driver("Alice")
# car = Car("Toyota")

# # Establishing association
# driver.drive(car)  # Output: Alice is driving a Toyota.

# Explanation:

# In this example, the Driver class has a method drive that takes an instance of the Car class as a parameter. The Driver class does not own or control the Car instance, which illustrates an association relationship.



# ---

# 2. Composition

# Definition: Composition is a strong form of association where one class contains references to one or more instances of another class, indicating a "part-of" relationship. In composition, the contained class (part) cannot exist independently of the containing class (whole).

# Characteristics:

# Represents a strong relationship (lifetime dependency).

# If the containing class is destroyed, the contained class instances are also destroyed.


# Example of Composition

# class Engine:
#     def init(self, horsepower):
#         self.horsepower = horsepower

# class Car:
#     def init(self, model, horsepower):
#         self.model = model
#         self.engine = Engine(horsepower)  # Car contains an Engine

#     def display_info(self):
#         print(f"{self.model} has an engine with {self.engine.horsepower} horsepower.")

# # Creating a Car object
# car = Car("Ford Mustang", 450)
# car.display_info()  # Output: Ford Mustang has an engine with 450 horsepower.

# Explanation:

# The Car class contains an instance of the Engine class. In this case, the Engine cannot exist without a Car, illustrating a composition relationship. If the Car object is destroyed, so is its Engine.



# ---

# 3. Aggregation

# Definition: Aggregation is a weaker form of association where one class can contain references to instances of another class, indicating a "has-a" relationship. Unlike composition, the contained class can exist independently of the containing class.

# Characteristics:

# Represents a weaker relationship (lifetime independence).

# The contained class can exist independently of the containing class.


# Example of Aggregation

# class Department:
#     def init(self, name):
#         self.name = name

# class Employee:
#     def init(self, name, department):
#         self.name = name
#         self.department = department  # Employee belongs to a Department

# # Creating instances
# department = Department("Sales")
# employee = Employee("John", department)

# # Accessing attributes
# print(f"{employee.name} works in the {employee.department.name} department.")  
# # Output: John works in the Sales department.

# Explanation:

# In this example, the Employee class has a reference to the Department class. The Department can exist without any employees, indicating an aggregation relationship. If the Employee is deleted, the Department can still exist.



# ---

# Summary of Relationships


# ---

# Conclusion
# Understanding these relationships—association, composition, and aggregation—is essential for designing robust object-oriented systems. They help clarify how objects interact and depend on each other, leading to better code organization and maintainability.