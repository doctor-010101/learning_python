# First way
list1 = [1, 2, 4, "python"]
print(list1, "\n", type(list1))  # output => [1, 2, 4, 'python']


# Second way
list2 = list("123456789")
list3 = list("python")
# output => ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(list2, "\n", type(list2))
print(list3, "\n", type(list3))  # output => ['p', 'y', 't', 'h', 'o', 'n']
print(list1 == list2) # output => False
print(list1 in list2) # output => False


# Third way
str = "p y t h o n"
list4 = str.split(" ")  # Return a list
print(list4, "\n", type(list4))


# Indexes in lists like indexes in strings
l1 = [1, 2, 3, 4, 5]
print(l1[0])  # output => 1


# Slicing in lists like indexes in strings
print(l1[0:2]) # output => [1, 2]


l2 = l1 * 2
print(l2) # output => [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l3 = [0, 0]
l4 = l2 + ["a", "b"] + l3
print(l4) # output => [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'a', 'b', 0, 0]


# miutable, immutable
l = [1, 2, 3, 4, 5]
l[2] = 20
print(l) # output => [1, 2, 20, 4, 5]

