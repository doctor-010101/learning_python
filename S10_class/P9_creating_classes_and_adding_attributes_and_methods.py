# In Python, creating a class involves defining the class using the class keyword, adding attributes to it (usually initialized through a constructor), and defining methods that operate on those attributes. Here’s a step-by-step explanation with examples to illustrate how to create a class, add attributes, and define methods.

# Step 1: Create a Class

# You define a class using the class keyword followed by the class name (conventionally in CamelCase).

# Step 2: Define the Constructor

# The constructor method init is defined to initialize the object's attributes when an instance of the class is created. Attributes are usually defined using self, which represents the instance of the class.

# Step 3: Add Attributes

# Attributes are the data stored in an object. You can add as many attributes as needed within the constructor.

# Step 4: Define Methods

# Methods are functions defined within a class that operate on the attributes of the class. You also use self to refer to the attributes within the methods.

# Example: Creating a Class

# Let's create a simple class called Book that has attributes for the title, author, and publication year, and a method to display the book's information.

# # Step 1: Define the class
# class Book:
#     # Step 2: Define the constructor
#     def init(self, title, author, year):
#         # Step 3: Add attributes
#         self.title = title
#         self.author = author
#         self.year = year

#     # Step 4: Define a method
#     def display_info(self):
#         return f"'{self.title}' by {self.author}, published in {self.year}"

# # Creating instances of the Book class
# book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book2 = Book("1984", "George Orwell", 1949)

# # Accessing attributes
# print(book1.title)  # Output: To Kill a Mockingbird
# print(book2.author)  # Output: George Orwell

# # Calling the method to display information
# print(book1.display_info())  # Output: 'To Kill a Mockingbird' by Harper Lee, published in 1960
# print(book2.display_info())  # Output: '1984' by George Orwell, published in 1949

# Breakdown of the Example:

# 1. Class Definition: We define a class named Book.


# 2. Constructor (init method):

# The constructor takes three parameters: title, author, and year.

# The attributes self.title, self.author, and self.year are initialized with the values passed when an instance of the class is created.



# 3. Attributes:

# self.title, self.author, and self.year are attributes that store the book's title, author, and publication year, respectively.



# 4. Method (display_info):

# The display_info method returns a formatted string containing the book's details.



# 5. Creating Instances:

# We create two instances of the Book class: book1 and book2.



# 6. Accessing Attributes:

# We can access the attributes directly (e.g., book1.title) to get the book title.



# 7. Calling Methods:

# We can call the display_info method on each book instance to print the book information.




# Conclusion

# Creating a class in Python is straightforward. You define a class with a constructor to initialize its attributes and methods to define its behaviors. This allows you to encapsulate data and functionality, promoting better organization and reusability in your code.