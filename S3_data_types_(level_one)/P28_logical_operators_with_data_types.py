x = 5
y = None
# in "and" if x is False => x
# in "and" if x is True => y
print(x and y)  # output : None
print("python" and 0)  # output : 0
print([] and x == 5)  # output : []


# in "or" if x is False => y
# in "or" if x is True => x
print(x or y)  # output : 5
print("python" or 0)  # output : python
print([] or x > 10)  # output : False
