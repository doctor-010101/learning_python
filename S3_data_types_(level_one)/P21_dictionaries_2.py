# Delete Items
d = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50,
     "u": 101, "f": 121, "z": 201, "h": 180}
del d["a"]
# output => {'b': 20, 'c': 30, 'd': 40, 'e': 50, 'u': 101, 'f': 121, 'z': 201, 'h': 180}
print(d)


# Change Key
x = d["c"]
del d["c"]
d["x"] = x
# output => {'b': 20, 'd': 40, 'e': 50, 'u': 101, 'f': 121, 'z': 201, 'h': 180, 'x': 30}
print(d)


# "sorted() method"
print(sorted(d.keys()))  # output => ['b', 'd', 'e', 'f', 'h', 'u', 'x', 'z']
print(sorted(d.values()))  # output => [20, 30, 40, 50, 101, 121, 180, 201]
print(sorted(d.keys(), reverse=True))
# output => ['z', 'x', 'u', 'h', 'f', 'e', 'd', 'b']
print(sorted(d.values(), reverse=True))
# output => [201, 180, 121, 101, 50, 40, 30, 20]


dictionary = dict([("a", 10), ("b", 20), ("c", 30), ("d", 40)])
print(dictionary)  # output => {'a': 10, 'b': 20, 'c': 30, 'd': 40}

dictionary2 = dict(a=10, b=20, c=30)
print(dictionary2)  # output => {'a': 10, 'b': 20, 'c': 30}


# dictionary in dictionary
dictionary3 = {
    "user": {"name": "Hassan", "age": 29},
    "list": [1, 2, 3, 4, 5]
}
print(dictionary3["user"]["name"])  # output => Hassasn
print(dictionary3["list"][2])  # output => 3
print(len(dictionary3))  # output => 2


# "+", "*" operators unsupported
# print(dictionary3 + 10)  #TypeError: unsupported operand type(s) for +: 'dict' and 'int'
# print(dictionary3 * 10)  #TypeError: unsupported operand type(s) for *: 'dict' and 'int'


# "==", "in", "is"... operators supported
print("user" in dictionary3)  # output => True


# "zip()" function
key = ("a", "b", "c")
value = (1, 2, 3)
dictionary4 = dict(zip(key, value))
print(dictionary4)  # output => {'a': 1, 'b': 2, 'c': 3}

key = "a", "b", "c"
value = 1, 2, 3
dictionary4 = dict(zip(key, value))
print(dictionary4)  # output => {'a': 1, 'b': 2, 'c': 3}

key = ["a", "b", "c"]
value = (1, 2, 3)
dictionary4 = dict(zip(key, value))
print(dictionary4)  # output => {'a': 1, 'b': 2, 'c': 3}