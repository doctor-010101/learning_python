# In Python, methods are functions that are defined within a class and operate on instances of that class. There are several types of methods in Python classes:

# Types of Methods in Python

# 1. Instance Methods:

# These are the most common type of methods. They take self as the first parameter, which refers to the instance of the class.

# They can access and modify the instance attributes.



# 2. Class Methods:

# Defined using the @classmethod decorator.

# They take cls as the first parameter, which refers to the class itself.

# They can modify class state that applies across all instances of the class.



# 3. Static Methods:

# Defined using the @staticmethod decorator.

# They do not take self or cls as the first parameter.

# They can be called on the class or an instance, but they cannot modify class or instance state.




# Example of a Comment Class

# Let’s create a simple Comment class that demonstrates these three types of methods. This class will represent a comment on a post with attributes like author, content, and timestamp.

# Step 1: Define the Comment Class

# from datetime import datetime

# class Comment:
#     comment_count = 0  # Class attribute to count the number of comments

#     def init(self, author, content):
#         self.author = author       # Instance attribute for the author's name
#         self.content = content     # Instance attribute for the comment content
#         self.timestamp = datetime.now()  # Instance attribute for the timestamp
#         Comment.comment_count += 1  # Increment the comment count whenever a new comment is created

#     # Instance method
#     def display_comment(self):
#         return f"{self.timestamp}: {self.author} said: {self.content}"

#     # Class method
#     @classmethod
#     def get_comment_count(cls):
#         return cls.comment_count

#     # Static method
#     @staticmethod
#     def is_valid_content(content):
#         return isinstance(content, str) and len(content) > 0

# Explanation of the Comment Class

# 1. Instance Attributes:

# author, content, and timestamp are instance attributes initialized in the constructor.



# 2. Class Attribute:

# comment_count is a class attribute that keeps track of the total number of Comment instances created.



# 3. Instance Method:

# display_comment(): Returns a formatted string with the comment details.



# 4. Class Method:

# get_comment_count(): Returns the total number of comments created. It accesses the class attribute comment_count.



# 5. Static Method:

# is_valid_content(content): Checks if the provided content is a valid non-empty string.




# Step 2: Use the Comment Class

# Now, let’s create some instances of the Comment class and demonstrate how to use the methods.

# # Create instances of Comment
# comment1 = Comment("Alice", "This is a great post!")
# comment2 = Comment("Bob", "Thanks for sharing!")

# # Display the comments
# print(comment1.display_comment())  # Output: [Timestamp]: Alice said: This is a great post!
# print(comment2.display_comment())  # Output: [Timestamp]: Bob said: Thanks for sharing!

# # Get the total number of comments
# print(f"Total comments: {Comment.get_comment_count()}")  # Output: Total comments: 2

# # Check if a comment is valid
# print(Comment.is_valid_content(comment1.content))  # Output: True
# print(Comment.is_valid_content(""))  # Output: False

# Complete Code Example

# Here’s the complete code for reference:

# from datetime import datetime

# class Comment:
#     comment_count = 0  # Class attribute to count the number of comments

#     def init(self, author, content):
#         self.author = author       # Instance attribute for the author's name
#         self.content = content     # Instance attribute for the comment content
#         self.timestamp = datetime.now()  # Instance attribute for the timestamp
#         Comment.comment_count += 1  # Increment the comment count whenever a new comment is created

#     # Instance method
#     def display_comment(self):
#         return f"{self.timestamp}: {self.author} said: {self.content}"

#     # Class method
#     @classmethod
#     def get_comment_count(cls):
#         return cls.comment_count
# # Static method
#     @staticmethod
#     def is_valid_content(content):
#         return isinstance(content, str) and len(content) > 0


# # Create instances of Comment
# comment1 = Comment("Alice", "This is a great post!")
# comment2 = Comment("Bob", "Thanks for sharing!")

# # Display the comments
# print(comment1.display_comment())  # Output: [Timestamp]: Alice said: This is a great post!
# print(comment2.display_comment())  # Output: [Timestamp]: Bob said: Thanks for sharing!

# # Get the total number of comments
# print(f"Total comments: {Comment.get_comment_count()}")  # Output: Total comments: 2

# # Check if a comment is valid
# print(Comment.is_valid_content(comment1.content))  # Output: True
# print(Comment.is_valid_content(""))  # Output: False

# Summary

# Instance Methods: Can access and modify instance attributes. Used for instance-specific behavior.

# Class Methods: Can access class attributes. Used for behavior that applies to the class as a whole.

# Static Methods: Do not access instance or class attributes. Used for utility functions that relate to the class but do not require access to its data.


# This Comment class demonstrates how to use different types of methods to manage comments effectively, illustrating the concepts of instance attributes, class attributes, and method types in Python.
