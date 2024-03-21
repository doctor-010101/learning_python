# Variables are locations in memory that store a specific type of data.
#
# To define the variables, we write the desired name and then use the assignment sign "=" to set the value.
#
# When defining variables, it is not necessary to specify its type, Python will recognize this automatically.

variable = 20


# id(variable) function used to get memory address (id) of variables.

print(id(variable))


# We can use multiple assignment when defining variables, that is, we can assign a value to several variables, but not the other way around.

a = b = c = 10  # Multiple assignment
# z = 10 = 11 = 12 TypeError: cannot unpack non-iterable int object.


# We can define several variables in one line

a, b, c = 1, 2, 3  # The right and left sides must be equal in number.
# 1, 3, 6 = a, b, x SyntaxError: cannot assign to literal.


# We can exchange variable values in one line.

x = 5
y = 10
x, y = y, x


# "del" used to delete varianles.

del variable
