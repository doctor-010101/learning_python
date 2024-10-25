# In object-oriented programming, aggregation and composition are both relationships that describe how classes interact with one another. They help to model real-world relationships between objects. Here’s a breakdown of each concept and how to implement them in Python.

# 1. Aggregation

# Aggregation is a "has-a" relationship where one class contains references to objects of another class. In aggregation, the lifecycle of the contained objects is independent of the lifecycle of the containing object. This means that if the containing object is destroyed, the contained objects can still exist.

# Example of Aggregation

# Let's create an example where a Library contains multiple Books. The Library can exist without the Books.

# class Book:
#     def init(self, title, author):
#         self.title = title
#         self.author = author

#     def str(self):
#         return f"'{self.title}' by {self.author}"

# class Library:
#     def init(self, name):
#         self.name = name
#         self.books = []  # A list to hold references to Book objects

#     def add_book(self, book):
#         self.books.append(book)

#     def display_books(self):
#         print(f"Books in {self.name} Library:")
#         for book in self.books:
#             print(book)

# # Creating instances of Book
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")

# # Creating an instance of Library
# library = Library("City Library")

# # Adding books to the library
# library.add_book(book1)
# library.add_book(book2)

# # Displaying books in the library
# library.display_books()

# # Demonstrating that books can exist independently
# del library  # Deleting the library does not affect the books
# print(book1)  # Output: '1984' by George Orwell
# print(book2)  # Output: 'To Kill a Mockingbird' by Harper Lee

# Explanation of Aggregation Example

# Book Class: Represents a book with a title and author.

# Library Class: Contains a list of Book objects. It has methods to add books and display them.

# Independent Lifecycle: Books exist independently of the library; deleting the library does not delete the books.


# 2. Composition

# Composition is a stronger form of association, also known as a "part-of" relationship. In composition, the contained objects’ lifecycle is tied to the lifecycle of the containing object. If the containing object is destroyed, the contained objects are also destroyed.

# Example of Composition

# Let's create an example where a Car is composed of Engine and Wheel objects. The Engine and Wheels cannot exist without the Car.

# class Engine:
#     def init(self, horsepower):
#         self.horsepower = horsepower

#     def str(self):
#         return f"Engine with {self.horsepower} HP"

# class Wheel:
#     def init(self, size):
#         self.size = size

#     def str(self):
#         return f"Wheel size: {self.size} inches"

# class Car:
#     def init(self, make, model):
#         self.make = make
#         self.model = model
#         self.engine = Engine(150)  # Composition: Engine is part of Car
#         self.wheels = [Wheel(15) for _ in range(4)]  # Four wheels for the car

#     def display_info(self):
#         print(f"{self.make} {self.model}")
#         print(self.engine)
#         for wheel in self.wheels:
#             print(wheel)

# # Creating an instance of Car
# car = Car("Toyota", "Corolla")

# # Displaying car information
# car.display_info()

# # Demonstrating that wheels and engine do not exist independently
# del car  # Deleting the car also deletes its engine and wheels
# # Trying to access engine or wheels will raise an AttributeError
# # print(car.engine)  # Uncommenting this will raise an error

# Explanation of Composition Example

# Engine Class: Represents an engine with horsepower.

# Wheel Class: Represents a wheel with a size.

# Car Class: Composed of an Engine and a list of Wheel objects. These objects cannot exist without the Car.

# Dependent Lifecycle: When the Car object is deleted, its Engine and Wheel objects are also deleted.


# Summary
# Aggregation: Represents a weak relationship where contained objects can exist independently of the containing object. Example: A Library has Books.

# Composition: Represents a strong relationship where contained objects cannot exist independently of the containing object. Example: A Car has an Engine and Wheels.


# Both relationships are essential in modeling real-world systems in object-oriented programming, and understanding the differences helps design better systems.
