# In Python, access control for class attributes and methods is typically managed using naming conventions involving underscores (_). Understanding these conventions helps define how attributes and methods can be accessed from outside the class and encourages encapsulation, which is a fundamental principle of object-oriented programming.

# Levels of Access Control

# 1. Public Attributes and Methods:

# Definition: Attributes and methods that are accessible from outside the class. They are defined without any leading underscores.

# Usage: Public members are typically the primary interface of a class and are meant to be accessible to users of the class.


# class Example:
#     def init(self):
#         self.public_attribute = "I am public"

#     def public_method(self):
#         return "This is a public method"

# obj = Example()
# print(obj.public_attribute)  # Output: I am public
# print(obj.public_method())    # Output: This is a public method


# 2. Protected Attributes and Methods:

# Definition: Attributes and methods that are intended to be protected from outside access, but not strictly enforced. They are defined with a single leading underscore (_).

# Usage: This is a convention indicating that these members are intended for internal use within the class and its subclasses. While they can be accessed from outside, it is generally discouraged.


# class Base:
#     def init(self):
#         self._protected_attribute = "I am protected"

#     def _protected_method(self):
#         return "This is a protected method"

# class Derived(Base):
#     def access_protected(self):
#         return self._protected_attribute  # Accessible in subclasses

# obj = Derived()
# print(obj.access_protected())  # Output: I am protected
# print(obj._protected_method())  # This is technically accessible, but discouraged


# 3. Private Attributes and Methods:

# Definition: Attributes and methods that are intended to be private to the class. They are defined with a double leading underscore (__), which triggers name mangling.

# Usage: This prevents access from outside the class, except through methods defined within the class. This is useful for ensuring that certain internal behaviors and states are not accidentally modified from outside.


# class Example:
#     def init(self):
#         self.__private_attribute = "I am private"

#     def __private_method(self):
#         return "This is a private method"

#     def access_private(self):
#         return self.__private_attribute

# obj = Example()
# print(obj.access_private())  # Output: I am private

# # Accessing private attribute directly will raise an AttributeError
# # print(obj.__private_attribute)  # Raises AttributeError

# # However, name mangling allows access via the mangled name
# print(obj._Example__private_attribute)  # Output: I am private



# Summary of Underscore Conventions

# Single Underscore (_): Indicates that the attribute or method is intended for internal use (protected). It is a convention and does not prevent access.

# Double Underscore (__): Causes name mangling, which changes the name of the attribute to include the class name. This makes it harder (but not impossible) to access from outside the class, emphasizing that the member is private.


# Applications and Use Cases

# Encapsulation: Using these naming conventions helps encapsulate the internal state of a class, making it less likely to be altered inappropriately. This leads to more robust and maintainable code.

# Inheritance: Protected members can be used in subclasses, allowing for extensibility while keeping the interface clean. Private members ensure that the base class's internal logic is not overridden or misused in subclasses.

# Data Hiding: The use of private members allows you to hide certain implementation details from users of the class, promoting a cleaner and more understandable API.

# Avoiding Name Collisions: Name mangling with private attributes helps avoid naming collisions in subclasses, as the mangled name includes the class name.


# Conclusion

# Understanding access control in classes using underscores is crucial for writing clean, maintainable, and robust object-oriented Python code. By properly using public, protected, and private attributes and methods, you can effectively manage how your class's internal state is accessed and modified, fostering better software design principles.