# In Python, data classes are a feature introduced in Python 3.7 (via the dataclasses module) that provide a simple way to create classes used primarily for storing data. Data classes automatically generate common special methods like init(), repr(), eq(), and others, saving you from writing boilerplate code.

# The main goal of a data class is to make the class definition shorter and more readable when its primary purpose is to store values (similar to a C-like structure). Data classes are defined using the @dataclass decorator.

# Key Features of Data Classes

# 1. Automatic method generation:

# init(): Automatically generates an initializer based on the class attributes.

# repr(): Provides a readable string representation of the class.

# eq(): Implements equality comparison based on attribute values.



# 2. Optional default values: You can define default values for fields.


# 3. Immutability: By setting the frozen=True parameter, you can make the class immutable (similar to namedtuple).


# 4. Type annotations: Data classes require type annotations for all fields.



# Example of a Data Class

# Let’s define a data class that represents a Person with attributes name, age, and job.

# from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str
#     age: int
#     job: str

# # Create an instance of Person
# person = Person(name="John Doe", age=30, job="Engineer")

# # Automatically generated repr
# print(person)  # Output: Person(name='John Doe', age=30, job='Engineer')

# # Access attributes
# print(person.name)  # Output: John Doe

# # Equality comparison based on attribute values
# person2 = Person(name="John Doe", age=30, job="Engineer")
# print(person == person2)  # Output: True (because they have the same values)

# Explanation of the Example

# 1. Data Class Declaration:

# The @dataclass decorator tells Python to treat this class as a data class.

# We define the class attributes name, age, and job with type annotations (str for name and job, int for age).



# 2. Automatic Method Generation:

# The init() method is automatically created for you, so you don’t need to define it yourself.

# The repr() method provides a readable string representation of the object, so when you print person, you see all its attributes.

# The eq() method compares two instances based on their values, so person == person2 returns True if their attributes are the same.




# Default Values and Field Options

# You can assign default values to fields in data classes, just like in regular classes. You can also use the field() function to customize field behavior.

# Example: Using Default Values

# from dataclasses import dataclass, field

# @dataclass
# class Car:
#     make: str
#     model: str
#     year: int = 2020  # Default value for year
#     mileage: int = field(default=0, repr=False)  # Not shown in repr

# # Create a Car instance
# car = Car(make="Toyota", model="Camry")

# # Print car details (mileage is not shown in repr)
# print(car)  # Output: Car(make='Toyota', model='Camry', year=2020)

# # Access default value
# print(car.mileage)  # Output: 0

# Explanation of Default Values Example

# Default Values:

# year is given a default value of 2020, so it’s optional when creating a Car instance.

# mileage is hidden from the repr() output because of repr=False, but it’s still accessible.


# Field Options with field():

# The field() function allows you to control behavior like whether a field should appear in repr(), whether it has a default factory, and other customizations.



# Immutability with frozen=True

# You can make data classes immutable, meaning that once an instance is created, you cannot modify its fields. This is useful when you want to ensure that the data stored in a class doesn't change.

# Example: Immutable Data Class

# from dataclasses import dataclass

# @dataclass(frozen=True)
# class Point:
#     x: int
#     y: int

# # Create an instance of Point
# point = Point(1, 2)

# # Access attributes
# print(point.x)  # Output: 1
