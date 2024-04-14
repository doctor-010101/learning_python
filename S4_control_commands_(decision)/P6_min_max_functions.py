# "min()" function : Returns the smallest its input value.
list1 = [21, 11, 12, 13, 58]
tuple1 = (21, 11, 12, 13, 58)
set1 = {21, 11, 12, 13, 58}
list2 = []
tuple2 = ()
print(min(set1, default=10))  # result : 11
print(min(list1, default=10))  # result : 11
print(min(tuple1, default=5))  # result : 11
print(min(list2, default=10))  # result : 10
print(min(tuple2, default=5))  # result : 15
print(min(21, 11, 12, 13, 58))  # result : 11
print(min([21, 11, 12, 13, 58]))  # result :max
print(min((21, 11, 12, 13, 58)))  # result : 11
print(min("Ali", "Hassan", "Aynaz", "Angel"))  # result : Ali


# max() function : Returns the largest its input value.
print(max(set1, default=10))  # result : 58
print(max(list1, default=10))  # result : 58
print(max(tuple1, default=5))  # result : 58
print(max(list2, default=10))  # result : 10
print(max(tuple2, default=5))  # result : 5
print(max(21, 11, 12, 13, 58))  # result : 58
print(max([21, 11, 12, 13, 58]))  # result 58
print(max((21, 11, 12, 13, 58)))  # result 58
print(max("Ali", "Hassan", "Aynaz", "Angel"))  # result : Hassan


# sum() function : Sums up its input values.
print(sum(list1, start=1))  # result : 116
print(sum([10, 20, 30, 40], start=99))  # result : 199
print(sum((10, 20, 30, 40), start=88))  # result : 188
print(sum({10, 20, 30, 40}, start=77))  # result : 177
# print(sum(10, 20, 30, 40))  # result : TypeError: sum() takes at most 2 arguments (4 given)
