import copy


# Copy in pythin
# 1 => shallow copy (Internal components are not copied) like copy list 4 from list 1 and copy list 7 from list 6.
# 2 => deep copy ((Internal components are copied)) like copy list 8 from list 9

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


list4 = list1.copy()  # shallow copy
print(list4)
print(id(list4))


# List in list...
list5 = [1, 2, 3, 4, ["a", "b", ["aa", "bb", [1.5, 2.5], "python"], "c"], 5]
# output => bb (in list5 index 4, in index 4 index 2, in index 2 index 1)
print(list5[4][2][1])
# output => n (in list5 index 4, in index 4 index 2, in index 2 index 3, in index 3(python) index -1)
print(list5[4][2][3][-1])


# Change list in list in shallow copy
list6 = [1, 2, 3, ["a", "b"]]
list7 = list6.copy()  # shallow copy
# when changed index 1 in index 3 in list 7, this index in list 6 changed too.
list7[3][1] = "c"
print(list6)
print(list7)

# Change list in list in deep copy
list8 = [1, 2, 3, ["a", "b"]]
list9 = copy.deepcopy(list8)  # deep copy
# when changed index 1 in index 3 in list 7, this index in list 6 does not change.
list9[3][1] = "c"
print(list8)
print(list9)
