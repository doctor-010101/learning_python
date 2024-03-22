"""
Identity operators in programming are used to compare the identity of two expressions or values.
 There are two identity operators:

1. is: The is operator checks if two expressions or values are identical or not.
 In other words, if two variables point to the same memory address, the is operator will return True.

2. is not: The is not operator is the opposite of the is operator and checks if two expressions or values are not identical.
 If two variables point to different memory addresses, the is not operator will return True.

These operators are commonly used in object-oriented programming languages to compare the identity of objects and values.
"""

a = 10
b = 5
c = 10
d = a
# is
print(a is b)  # False
print(a is c)  # True
print(a is a)  # True
# is not
print(a is not b)  # True
print(a is not c)  # False
print(a is not a)  # False


# Identity is different from equality 👇
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

print(x is y)  # False
print(x == y)  # True

# is not
print(x is not y)  # True
print(x != y)  # False
