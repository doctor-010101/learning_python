# 🍀 -> "Positional(normal)" Syntax
def max_(a, b, c):
    print(max(a, b, c))


max_(1, 2, 3)


# 🍀🍀 -> "Name = Value (keyword)" Syntax
def max_(a, b, c):
    print(max(a, b, c))


max_(b=5, a=2, c=3)


# 🍀🍀🍀 -> "Positional(normal)" Syntax + "Name = Value" Syntax
# Tip => 1- positional argument follows keyword argument.
def max_(a, b, c):
    print(max(a, b, c))


max_(5, 2, c=10)  # ->Correct
# max_(a=2, b=5, 13)  # ->Wrong (positional argument follows keyword argument.)
# max_(2, a=5, c=13)  # ->Wrong (max_() got multiple values for argument 'a')


# 🍀🍀🍀🍀 -> "Iterable" Syntax
# Tip => 1- Not too much or too little.
def max_(a, b, c):
    print(max(a, b, c))


w = "586"
x = [1, 2, 3]
y = {4, 5, 6}
z = (7, 8, 9)

max_(*[7, 9, 10])
max_(*w)
max_(*x)
max_(*y)
max_(*z)


# 🍀🍀🍀🍀🍀 -> "Dictionary" Syntax
def max_(a, b, c):
    print(max(a, b, c))


d = {"c": 20, "b": 17, "a": 21}
max_(**d)
max_(**{"c": 20, "b": 17, "a": 21})
