# Dictionaries (keys and values)
dictionary = {"key": "value", 1: "python"}
print(dictionary)  # output => {'key': 'value', 1: 'python'}
print(type(dictionary))  # output => <class 'dict'>
print(dictionary["key"])  # output => value
print(dictionary[1])  # output => python


# Keys must be immutable types like strings, numbers, tuples. So, it cannot be a list or a tuple inside that list.
# Values can be any type and  the keys should not be duplicated.
dictionary2 = {"a": 10, "b": 15, "a": 20, "a": 25}
print(dictionary2)  # output => {'a': 25, 'b': 15}


# We can change values.
dictionary2["a"] = 100
print(dictionary2)  # output => {'a': 100, 'b': 15}
# If the key does not exist when changing the value, it will add it to the dictionary
dictionary2["c"] = 200
print(dictionary2)  # output => {'a': 100, 'b': 15, 'c': 200}


# "get()" method
# print(dictionary2["d"]) # output => KeyError: 'd'
print(dictionary2.get("d"))  # output => None


# "keys() method"
print(dictionary2.keys())  # output => dict_keys(['a', 'b', 'c'])
print(type(dictionary2.keys()))  # output => <class 'dict_keys'>
print(list(dictionary2.keys()))  # output => ['a', 'b', 'c']


# "values() method"
print(dictionary2.values())  # output => dict_values([100, 15, 200])
print(type(dictionary2.values()))  # output => <class 'dict_values'>


# "items() method"
print(dictionary2.items())
# output => dict_items([('a', 100), ('b', 15), ('c', 200)])
print(type(dictionary2.items()))  # output => <class 'dict_items'>
