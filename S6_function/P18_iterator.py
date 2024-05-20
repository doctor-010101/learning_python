# iterate
# iteration
# itrable
# iterator


i = [1, 3, 4]
print("__next__" in dir(i))
print("__iter__" in dir(i))
i = iter(i)
# i.__iter__()
print("__next__" in dir(i))
print(next(i))
print(i.__next__())