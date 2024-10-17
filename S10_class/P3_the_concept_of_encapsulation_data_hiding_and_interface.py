# These concepts are fundamental to Object-Oriented Programming (OOP) and play a significant role in ensuring that your code is modular, maintainable, and secure.


# ---

# 1. Encapsulation

# Definition: Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, or class. This means that the internal representation of an object is hidden from the outside, and access to it is controlled.

# Purpose: The main goal of encapsulation is to protect the integrity of the object’s state by restricting direct access to some of its components. This reduces the risk of unintended interference and misuse of the methods and data.

# Implementation in Python:

# In Python, encapsulation is typically achieved using public, protected, and private attributes.


# Example of Encapsulation

# class BankAccount:
#     def init(self, account_number, initial_balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = initial_balance         # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount}. New balance: {self.__balance}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: {amount}. Remaining balance: {self.__balance}.")
#         else:
#             print("Invalid withdraw amount.")

#     def get_balance(self):
#         return self.__balance  # Accessing the private balance

# # Using the BankAccount class
# account = BankAccount("123456", 1000)
# account.deposit(500)        # Deposited: 500. New balance: 1500.
# account.withdraw(200)       # Withdrew: 200. Remaining balance: 1300.
# print(account.get_balance())  # Output: 1300

# Explanation:

# The BankAccount class encapsulates the account number and balance.

# The attributes account_number and balance are private (indicated by the double underscores) and cannot be accessed directly from outside the class.

# The class provides methods (deposit, withdraw, and get_balance) to interact with these attributes, ensuring that the balance cannot be manipulated directly.



# ---

# 2. Data Hiding

# Definition: Data hiding is a principle closely related to encapsulation. It involves restricting access to certain parts of an object, hiding its internal state, and requiring all interaction to be performed through well-defined methods.

# Purpose: The primary goal of data hiding is to protect the internal state of an object from unintended modifications and to ensure that an object can only be manipulated in a controlled manner.

# Example of Data Hiding

# In the previous example, the attributes account_number and balance are hidden from outside access, demonstrating data hiding. Attempting to access them directly would raise an error:

# # Attempt to access private attributes
# # print(account.balance)  # AttributeError: 'BankAccount' object has no attribute 'balance'


# ---

# 3. Interfaces

# Definition: An interface is a contract that defines a set of methods that a class must implement. In Python, while there is no formal interface keyword like in some other programming languages (such as Java), you can achieve a similar effect using abstract base classes (ABCs) provided by the abc module.

# Purpose: Interfaces allow for polymorphism and help define a consistent API for different classes, enabling them to be used interchangeably.

# Example of an Interface

# from abc import ABC, abstractmethod

# # Defining an abstract base class (interface)
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass  # Abstract method

#     @abstractmethod
#     def perimeter(self):
#         pass  # Abstract method

# # Implementing the interface in a derived class
# class Rectangle(Shape):
#     def init(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height