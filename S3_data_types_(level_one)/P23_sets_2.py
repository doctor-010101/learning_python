set1 = {3, 15, 9, 12, 6, 18}
set2 = {12, 6, 18, 10, 2, 14, 16, 4, 8}


# The difference function
print(set1-set2)  # output : {9, 3, 15}
print(set1.difference(set2))  # output : {9, 3, 15}
print(set2.difference(set1))  # output : {2, 4, 8, 10, 14, 16}


# The union function
print(set1 | set2)  # output : {2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18}
print(set1.union(set2))  # output : {2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18}
print(set2.union(set1))  # output : {2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18}


# The intersection function
print(set1 & set2)  # output : {18, 12, 6}
print(set1.intersection(set2))  # output : {18, 12, 6}
print(set2.intersection(set1))  # output : {18, 12, 6}


# The symmetric_difference function
print(set1 ^ set2)  # output : {2, 3, 4, 8, 9, 10, 14, 15, 16}
print((set1 | set2) - (set1 & set2))  # output : {2, 3, 4, 8, 9, 10, 14, 15, 16}
print((set1 - set2) | (set2 - set1))  # output : {2, 3, 4, 8, 9, 10, 14, 15, 16}
print(set1.symmetric_difference(set2))  # output : {2, 3, 4, 8, 9, 10, 14, 15, 16}
print(set2.symmetric_difference(set1))  # output : {2, 3, 4, 8, 9, 10, 14, 15, 16}


# issubset, issuperset functions
print(set1 < set2)  # output : False
print(set1 > set2)  # output : False
print(set1.issubset(set2))  # output : {18, 12, 6}
print(set1.issuperset(set2))  # output : {18, 12, 6}
