
# Let's create a simple example of a Bank Account class in Python. This class will have the following features:

# 1. Attributes for account holder name, account balance, and account number.


# 2. Methods to deposit and withdraw money.


# 3. Methods to get account information.


# 4. String representation methods using str and repr.



# Example Implementation of a Bank Account Class

# Here's a full implementation of a BankAccount class:

# class BankAccount:
#     """
#     A class to represent a bank account.

#     Attributes:
#     ----------
#     account_holder : str
#         Name of the account holder.
#     account_number : str
#         Unique account number.
#     balance : float
#         Current balance in the account.

#     Methods:
#     -------
#     deposit(amount: float):
#         Adds the specified amount to the account balance.
#     withdraw(amount: float):
#         Subtracts the specified amount from the account balance if sufficient funds exist.
#     get_balance() -> float:
#         Returns the current balance of the account.
#     get_account_info() -> str:
#         Returns a string containing account holder's name, account number, and balance.
#     """
    
#     def init(self, account_holder: str, account_number: str, initial_balance: float = 0.0):
#         """
#         Initializes the BankAccount with the account holder's name, account number, and optional initial balance.

#         Parameters:
#         ----------
#         account_holder : str
#             The name of the account holder.
#         account_number : str
#             The unique account number.
#         initial_balance : float, optional
#             The initial balance of the account (default is 0.0).
#         """
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = initial_balance

#     def deposit(self, amount: float):
#         """Adds the specified amount to the account balance."""
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
#         else:
#             print("Deposit amount must be positive!")

#     def withdraw(self, amount: float):
#         """Subtracts the specified amount from the account balance if sufficient funds exist."""
#         if amount > self.balance:
#             print("Insufficient funds!")
#         elif amount <= 0:
#             print("Withdrawal amount must be positive!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

#     def get_balance(self) -> float:
#         """Returns the current balance of the account."""
#         return self.balance

#     def get_account_info(self) -> str:
#         """Returns account holder's name, account number, and balance as a formatted string."""
#         return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.balance:.2f}"

#     def str(self) -> str:
#         """Returns a user-friendly string representation of the account."""
#         return self.get_account_info()

#     def repr(self) -> str:
#         """Returns a string representation of the account for debugging."""
#         return f"BankAccount(account_holder='{self.account_holder}', account_number='{self.account_number}', balance={self.balance})"

# # Example usage
# if name == "main":
#     # Creating a bank account
#     account = BankAccount("John Doe", "123456789", 1000.00)
    
#     # Displaying account information
#     print(account)  # Output: Account Holder: John Doe, Account Number: 123456789, Balance: $1000.00

#     # Depositing money
#     account.deposit(500.00)  # Output: Deposited: $500.00. New balance: $1500.00

#     # Withdrawing money
#     account.withdraw(200.00)  # Output: Withdrew: $200.00. New balance: $1300.00

#     # Attempting to withdraw more than the balance
#     account.withdraw(1500.00)  # Output: Insufficient funds!

#     # Getting balance
#     print(f"Current balance: ${account.get_balance():.2f}")  # Output: Current balance: $1300.00


# # Displaying account info using repr
#     print(repr(account))  # Output: BankAccount(account_holder='John Doe', account_number='123456789', balance=1300.0)

# Explanation of the Implementation

# 1. Attributes:

# account_holder: A string representing the name of the account holder.

# account_number: A string representing the unique account number.

# balance: A float representing the current balance in the account.



# 2. Methods:

# init: Initializes the account with the holder's name, account number, and an optional initial balance (default is 0.0).

# deposit: Adds a specified amount to the account balance. It checks if the amount is positive before adding.

# withdraw: Subtracts a specified amount from the balance. It checks if there are sufficient funds before withdrawing and ensures the amount is positive.

# get_balance: Returns the current balance of the account.

# get_account_info: Returns a formatted string with the account holder's name, account number, and balance.

# str: Provides a user-friendly string representation of the account (used in print()).

# repr: Provides a detailed string representation of the account, useful for debugging (used in repr()).



# 3. Usage:

# An instance of BankAccount is created for "John Doe" with an initial balance of $1000.00.

# Methods are called to deposit and withdraw amounts, and the balance is displayed.




# Output of the Example

# When you run the provided example code, the output will be as follows:

# Account Holder: John Doe, Account Number: 123456789, Balance: $1000.00
# Deposited: $500.00. New balance: $1500.00
# Withdrew: $200.00. New balance: $1300.00
# Insufficient funds!
# Current balance: $1300.00
# BankAccount(account_holder='John Doe', account_number='123456789', balance=1300.0)

# This simple implementation covers the basics of a bank account class, including encapsulation and the use of string representation methods to enhance readability and debugging. You can expand on this by adding more features, such as transaction history, interest calculations, or integration with a user interface.