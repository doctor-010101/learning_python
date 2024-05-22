# 1
# list_ = [1, 2, 3, 6, 66, 145, 12, 96, 89]
# print("len list: ", len(list_))
# odd = list(filter(lambda x: x % 2 != 0, list_))
# print("len odd: ", len(odd))
# even = list(filter(lambda x: x % 2 == 0, list_))
# print("len even: ", len(even))
# print("\n")


# 2
users = [("Hassan", 24),("Akin", 22),("Ali", 73),("Ebrahim", 63),("Ana", 18)]
print("before sort :", users)
users.sort(key=lambda x : x[1], reverse=True)
print("sorted list :", users)
print("\n")


# 3
fruits_list = [
    {"name": "apple", "price": 10_000, "color": "green"},
    {"name": "banana", "price": 50_000, "color": "yellow"},
    {"name": "orange", "price": 20_000, "color": "orange"},
    {"name": "coconut", "price": 100_000, "color": "brown"}
]
print("before sort :", fruits_list)
fruits_list.sort(key=lambda x : x["name"])
print("sorted list :", fruits_list)
print("\n")


# 4
# list_ = [1, 2, 3, 6, 66, 145, 12, 96, 89]
# print("list: ", list_)
# odd = list(filter(lambda x: x % 2 != 0, list_))
# print("odd: ", odd)
# even = list(filter(lambda x: x % 2 == 0, list_))
# print("even: ", even)
# print("\n")


# 5
list_ = [1, 2, 3, 6, 66, 145, 12, 96, 89]
print("list: ", list_)
square = list(map(lambda x : x**2, list_))
print("square: ", square)
cube = list(map(lambda x : x**3, list_))
print("cube: ", cube)
print("\n")


# 6
string = "python"
starts_with = lambda s: s.startswith("p")
print(starts_with("p"))
print("\n")


# 7
is_num = lambda s : s.replace(".", "", 1).isdigit()
print(is_num("4.5"))
print(is_num("4..5"))
print(is_num("4.a5"))
print(is_num("4"))