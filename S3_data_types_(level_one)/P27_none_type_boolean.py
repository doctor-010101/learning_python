# None Type
"""
In Python, None is a special data type that represents an "empty" or "invalid" value.      
None is used as a default value for variables or functions to indicate that they have no specific value or output.

"""
n = None
print(n)  # output : None
print(type(n))  # output : <class 'NoneType'>

# ---------------------------------------------------------------------------------------------------------- #


# boolean Type (True, False)
t = True
f = False
print(t, type(t))  # output : True <class 'bool'>
print(f, type(f))  # output : False <class 'bool'>
print(int(t))  # output : 1
print(int(f))  # output : 0
print(t * 5)  # output : 5
print(f + 10)  # output : 10
print(t == 1)  # output : Ture
print(f == 0)  # output : Ture


# Only zero (0, 0.0, 0j) is considered false in "if , else" other numbers (all of them) are True.
# Empty objects are considered False too ("False", "None", (), {}, [], "", set())


print(bool("python"))  # output : True
print(bool(0))  # output : False
