# Callable Objects in Python

# In Python, callable objects are those that can be invoked like functions. This means you can use parentheses () after the object to call it. The built-in types that are inherently callable include functions, methods, and classes. However, you can also create your own callable objects by implementing the special method call() in a class.

# Key Concepts of Callable Objects

# 1. Functions: Regular functions defined using the def keyword are callable.


# 2. Methods: Instance methods of classes are callable.


# 3. Classes: When you call a class, it returns a new instance of that class.


# 4. Custom Callable Objects: You can create objects of a class that can be called like a function by defining the call() method.



# Example of Callable Objects

# Let’s create a custom callable object by defining a class with the call() method.

# Step 1: Define a Callable Class

# class Adder:
#     def init(self, value):
#         self.value = value

#     def call(self, x):
#         return self.value + x

# Explanation:

# Adder Class: This class takes a number during initialization and stores it as an instance variable.

# call Method: The call method is defined to allow instances of the class to be called as if they were functions. It takes one argument x and returns the sum of self.value and x.


# Step 2: Use the Callable Class

# Now, let’s create an instance of the Adder class and use it like a function.

# # Create an instance of Adder with a value of 10
# add_ten = Adder(10)

# # Call the instance like a function
# result = add_ten(5)  # This will call the call method
# print(result)  # Output: 15

# Complete Code Example

# Here’s the complete code for reference:

# class Adder:
#     def init(self, value):
#         self.value = value

#     def call(self, x):
#         return self.value + x

# # Create an instance of Adder
# add_ten = Adder(10)

# # Call the instance like a function
# result = add_ten(5)
# print(result)  # Output: 15

# Explanation of the Example

# 1. Creating an Instance: We create an instance of Adder called add_ten, initialized with a value of 10.


# 2. Calling the Instance: We call add_ten(5), which invokes the call() method, adding 10 to 5 and returning 15.



# Other Callable Examples

# 1. Callable Functions

# def multiply(x, y):
#     return x * y

# # Calling a function
# result = multiply(3, 4)
# print(result)  # Output: 12

# 2. Callable Classes

# class Multiplier:
#     def init(self, factor):
#         self.factor = factor

#     def call(self, x):
#         return self.factor * x

# # Using the Multiplier class
# double = Multiplier(2)
# print(double(10))  # Output: 20

# Summary

# Callable objects in Python can be functions, methods, classes, or instances of classes that implement the call() method.

# By defining the call() method in a class, you can make instances of that class callable like regular functions, allowing for flexible and dynamic behavior.

# This feature is often used in design patterns, such as the Factory pattern, and is useful for creating more complex behaviors in your applications.


# Callable objects enhance the functionality and flexibility of Python programming, allowing for a more intuitive and expressive coding style.
