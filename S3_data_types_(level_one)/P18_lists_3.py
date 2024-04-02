# append method
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list.append(10)
print(list)  # output => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# len
print(len(list))  # output => 10
print(list[:len(list)])  # output => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[len(list) - 1])  # output => 10

# # Change or replace by slicing
# list[3:6] = ["a", "b", "c"]
# print(list)  # output => [1, 2, 3, 'a', 'b', 'c', 7, 8, 9, 10]

# # more
# list[3:6] = ["a", "b", "c", "d"]
# print(list)  # output => [1, 2, 3, 'a', 'b', 'c', 'd', 7, 8, 9, 10]

# # less
# list[3:6] = ["a", "b"]
# print(list)  # output => [1, 2, 3, 'a', 'b', 7, 8, 9, 10]

# # empty
# list[3:6] = []
# print(list)  # output => [1, 2, 3, 7, 8, 9, 10]
# list[:] = []
# print(list)  # output => []

# del
del list[3:6]
print(list)  # output => [1, 2, 3, 7, 8, 9, 10]


a, b, c = [1, 2, 3]
print(a)  # output => 1
print(b)  # output => 2
print(c)  # output => 3


d, e, *f = [4, 5, 6, 7, 8, 9]
print(d)  # output => 4
print(e)  # output => 5
print(f)  # output => [6, 7, 8, 9]


*d, e, f = [4, 5, 6, 7, 8, 9]
print(d)  # output => [4, 5, 6, 7]
print(e)  # output => 8
print(f)  # output => 9


d, *e, f = [4, 5, 6, 7, 8, 9]
print(d)  # output => 4
print(e)  # output => [5, 6, 7, 8]
print(f)  # output => 9


l, k, *p = [1, 2], [3, 4], [5, 6], [7, 8]
print(l)  # output => [1, 2]
print(k)  # output => [3, 4]
print(p)  # output => [[5, 6], [7, 8]]
