# Inheritance from Built-in Classes in Python refers to the ability to extend or customize the functionality of Python's built-in data types, such as list, dict, set, and str, by creating a subclass that inherits from these types.

# This is a powerful feature in Python's object-oriented programming (OOP) model, as it allows developers to modify the behavior of standard types to suit specific needs while still maintaining the fundamental structure and properties of the built-in class.

# Key Points:

# When inheriting from a built-in class, the subclass gains all the methods and attributes of the parent (built-in) class.

# You can override or extend the functionality of these methods to customize behavior.

# This promotes code reusability, as you don't need to write complex data structures from scratch.


# Example 1: Inheriting from list

# Let's create a custom class CustomList that inherits from the built-in list class. We'll add a new method called sum_elements that calculates the sum of the list's elements.

# # Custom class inheriting from Python's built-in list
# class CustomList(list):
#     def sum_elements(self):
#         return sum(self)

# # Create an instance of CustomList
# my_list = CustomList([1, 2, 3, 4, 5])

# # Use built-in list methods
# my_list.append(6)
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# # Use the new method in CustomList
# print(my_list.sum_elements())  # Output: 21

# Explanation:

# CustomList inherits all methods of the list class, like append, extend, etc.

# We added a custom method sum_elements to sum all the elements in the list.

# The object my_list behaves like a normal list (supporting operations like append), but it also has the additional functionality provided by the custom method.


# Example 2: Inheriting from dict

# Now, let's extend the dict class and add a method that allows us to invert the key-value pairs in a dictionary.

# # Custom class inheriting from the built-in dict class
# class InvertibleDict(dict):
#     def invert(self):
#         # Invert key-value pairs
#         return {v: k for k, v in self.items()}

# # Create an instance of InvertibleDict
# my_dict = InvertibleDict({"a": 1, "b": 2, "c": 3})

# # Use built-in dict methods
# my_dict["d"] = 4
# print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# # Use the new method to invert the dictionary
# print(my_dict.invert())  # Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Explanation:

# InvertibleDict inherits from the built-in dict class, meaning it retains all the dictionary operations (such as adding or updating key-value pairs).

# We added a method invert that returns a new dictionary with the keys and values swapped.

# The my_dict instance behaves like a normal dictionary but also has the added ability to invert itself.


# Benefits of Inheriting from Built-in Classes:

# 1. Code Reusability: You don't need to write complex data structures from scratch. You can inherit the functionality of built-in classes and extend them as needed.


# 2. Custom Behavior: By overriding methods, you can alter how the built-in methods work for your subclass.


# 3. Seamless Integration: Your subclass objects can be used in contexts where the built-in type is expected, since they are still considered instances of that type.



# Example 3: Overriding Methods

# In some cases, you may want to override certain built-in methods. For instance, let's override the setitem method in a dict to ensure that the keys must always be strings.

# # Custom class to enforce string keys in a dictionary
# class StringKeyDict(dict):
#     def setitem(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError("Keys must be strings!")
#         super().setitem(key, value)

# # Create an instance of StringKeyDict
# my_dict = StringKeyDict()

# # Adding valid key-value pair
# my_dict["name"] = "Alice"
# print(my_dict)  # Output: {'name': 'Alice'}

# # Attempting to add a non-string key raises an error
# my_dict[1] = "Bob"  # Raises TypeError: Keys must be strings!

# Explanation:

# We subclassed dict and overrode the setitem method, which controls how key-value pairs are added to the dictionary.

# In this case, we ensure that all keys must be strings by checking the type before calling the original method (super().setitem(...)).

# This prevents adding keys of other types, as shown by the error raised when trying to add 1 as a key.


# Key Takeaways:

# Inheritance from built-in classes allows you to extend and modify the behavior of fundamental Python types.

# This technique is highly useful for customizing standard behaviors and adding new functionality while retaining the existing features of the built-in class.
