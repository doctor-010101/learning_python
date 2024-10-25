# Multiple Inheritance in Python refers to a situation where a child class (subclass) inherits from more than one parent class. This means that the child class can access attributes and methods from all of the parent classes, enabling the reuse of code from multiple sources.

# While powerful, multiple inheritance can introduce complexity, such as method resolution order (MRO), ambiguity, and potential conflicts between parent classes, particularly when they share methods with the same name.

# Key Points:

# A class can inherit from more than one base class, gaining access to all methods and attributes from all parent classes.

# Python follows a specific method resolution order (MRO) to determine the order in which parent classes are searched when invoking a method.

# You can access methods of any parent class using the super() function, which is aware of the MRO and resolves conflicts between parent classes.


# Syntax of Multiple Inheritance:

# class Parent1:
#     def method1(self):
#         print("Method from Parent1")

# class Parent2:
#     def method2(self):
#         print("Method from Parent2")

# # Child class inheriting from both Parent1 and Parent2
# class Child(Parent1, Parent2):
#     def method3(self):
#         print("Method from Child")

# # Create an instance of Child class
# child = Child()

# # Call methods from both parents
# child.method1()  # Inherited from Parent1
# child.method2()  # Inherited from Parent2
# child.method3()  # Defined in Child class

# Explanation:

# The Child class inherits from both Parent1 and Parent2, meaning it has access to methods from both classes.

# The child object can call method1() from Parent1, method2() from Parent2, and method3() from its own class.


# Method Resolution Order (MRO):

# When multiple inheritance is involved, Python uses the Method Resolution Order (MRO) to determine which class's method to call when there are multiple possibilities. This is critical when there are conflicts, such as multiple parent classes having methods with the same name.

# To inspect the MRO, you can use the mro() method or the mro attribute.

# print(Child.mro())  # Method Resolution Order

# In the above example, Child.mro() would return something like:

# [<class 'main.Child'>, <class 'main.Parent1'>, <class 'main.Parent2'>, <class 'object'>]

# This means that when you call a method on a Child object, Python will first look in the Child class, then in Parent1, followed by Parent2, and finally in the base object class.

# Example of Multiple Inheritance with Overlapping Methods

# Let’s consider a case where both parent classes have a method with the same name. This scenario demonstrates how Python resolves conflicts using the MRO.

# class Parent1:
#     def greet(self):
#         print("Hello from Parent1")

# class Parent2:
#     def greet(self):
#         print("Hello from Parent2")

# # Child class inheriting from both Parent1 and Parent2
# class Child(Parent1, Parent2):
#     pass

# # Create an instance of Child class
# child = Child()

# # Call the greet method
# child.greet()

# Output:

# Hello from Parent1

# Explanation:

# Both Parent1 and Parent2 have a greet() method.

# Since Child inherits from both classes, Python checks the MRO to determine which greet() method to call.

# According to the MRO, Python searches Parent1 first, so it calls Parent1's greet() method.


# If we change the order of inheritance in the Child class definition, it would affect the MRO and which method gets called:

# # Child class with reversed inheritance order
# class Child(Parent2, Parent1):
#     pass

# child = Child()
# child.greet()

# Output:

# Hello from Parent2

# Using super() in Multiple Inheritance

# In multiple inheritance, super() is aware of the MRO and allows you to call the next method in the inheritance hierarchy, without needing to explicitly name the parent class. This helps to avoid issues when dealing with diamond inheritance (explained below).

# Let’s extend the previous example and see how super() works:

# class Parent1:
#     def greet(self):
#         print("Hello from Parent1")

# class Parent2:
#     def greet(self):
#         print("Hello from Parent2")
# # Child class inheriting from both Parent1 and Parent2
# class Child(Parent1, Parent2):
#     def greet(self):
#         super().greet()  # Calls the next class in the MRO
#         print("Hello from Child")

# # Create an instance of Child class
# child = Child()

# # Call the overridden greet method
# child.greet()

# Output:

# Hello from Parent1
# Hello from Child

# Explanation:

# In the Child class, we override the greet() method.

# By using super().greet(), we call the greet() method of the next class in the MRO, which in this case is Parent1.

# After calling the parent’s method, the Child class adds its own behavior by printing "Hello from Child".


# The Diamond Problem in Multiple Inheritance

# A common issue in multiple inheritance is the diamond problem, which occurs when a class inherits from two classes that both inherit from the same parent class. This creates ambiguity about which parent class’s method should be inherited.

# class Grandparent:
#     def greet(self):
#         print("Hello from Grandparent")

# class Parent1(Grandparent):
#     def greet(self):
#         print("Hello from Parent1")

# class Parent2(Grandparent):
#     def greet(self):
#         print("Hello from Parent2")

# # Child class inherits from both Parent1 and Parent2
# class Child(Parent1, Parent2):
#     pass

# child = Child()
# child.greet()

# Output:

# Hello from Parent1

# Explanation:

# The Child class inherits from both Parent1 and Parent2, which in turn both inherit from Grandparent.

# The MRO ensures that Child first looks at Parent1, so it calls Parent1's version of greet().

# Python’s MRO resolves this ambiguity by following the inheritance hierarchy in a depth-first, left-to-right order (known as the C3 linearization algorithm).


# If you check the MRO:

# print(Child.mro())

# It will show:

# [<class 'main.Child'>, <class 'main.Parent1'>, <class 'main.Parent2'>, <class 'main.Grandparent'>, <class 'object'>]

# This shows the order in which Python searches for methods when there’s a conflict.

# Key Takeaways:

# Multiple Inheritance allows a class to inherit from more than one parent class, enabling the reuse of methods and attributes from all parents.

# Method Resolution Order (MRO) ensures Python resolves method calls in a predictable manner when multiple parent classes have methods with the same name.

# The super() function works with MRO to allow you to call the next method in the inheritance hierarchy, even in multiple inheritance scenarios.

# Diamond Problem occurs when multiple classes share the same ancestor, but Python resolves this through its MRO, ensuring clarity in inheritance chains.


# While multiple inheritance is powerful, it can be complex and should be used carefully, especially in large or complicated systems.
