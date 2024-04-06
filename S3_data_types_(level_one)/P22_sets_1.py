# In Python, sets are collections of unique and immutable elements. To create a set, you can use the set() function or curly braces {}.

# Example:
# Creating an empty set
my_set = set()

# Creating a set with specific elements
my_set = {1, 2, 3, 4, 5}

print(my_set)  # output: {1, 2, 3, 4, 5}


# Sets in Python can perform various operations such as adding new elements, removing elements, union of two sets, difference of two sets, and more.


# Sets are mutable objects (add and delete elements)
set1 = {1, 2, 3, 4}


# In add by "add()" we can not use list but in add by "update() we can use"
set1.add(5)
set1.add((1,2))
set1.update([1,2,3,4,11],[99,100,200])  # set1.add([1,2])  # => TypeError: unhashable type: 'list'
print(set1)  # output => {1, 2, 3, 4, 5, (1, 2), 99, 100, 200, 11}


# Remove by "remove()" and "discard()"
set1.remove(1)
# set1.remove(12)  # KeyError: 12
set1.discard(99)
set1.discard(1001)
print(set1)  # output => {2, 3, 4, 5, (1, 2), 1, 100, 200, 11}


# Sets do not accept duplicate elements
set1.add(1)
print(set1)  # output => {1, 2, 3, 4, 5, (1, 2), 99, 100, 200, 11}


# Slicing and indexing not done in sets
# print(set1[2])  # output => TypeError: 'set' object is not subscriptable


# "{}" => this is a dict, "{""}" => this is a set
dictionary = {}
set2 = {""}


# "set()"
set3 = set("python")
print(set3)  # output => {'o', 'y', 'p', 'n', 't', 'h'}
set4 = set([1, 2, 3, 3, 2, 5, 6, 4, 3, 4, 3])
print(set4)  # output => {1, 2, 3, 4, 5, 6}


# Mutable elements are not used in sets
# set5 = {1, 2, 3, 4, [1, 2, 3]} #  output => TypeError: unhashable type: 'list' 
# set6 = {1, 2, 3, 4, (1, 2, 3, [1, 2])} #  output => TypeError: unhashable type: 'list'


set7 = {1,1,1,1,1}
print(len(set7))  # output => 1
print(1 in set7)  # output => True
print(set1 is set7)  # output => False
print(set1 == set7)  # output => False
 

