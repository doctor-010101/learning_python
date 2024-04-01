list1 = [1, 2, 3, 4, 5]
list2 = list1
print(id(list1))
print(id(list2))


list2[0] = 0
print(list1)
print(list2)
print(id(list1))
print(id(list2))


list3 = list1[:]
print(list3)
print(id(list3))


list4 = list1.copy()
print(list4)
print(id(list4))


# List in list...
list5 = [1, 2, 3, 4, ["a", "b", ["c", "d", [10, 11], "f"], "e"], 5]
print(list5)
