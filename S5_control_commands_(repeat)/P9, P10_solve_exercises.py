# 1 -> Write a program that takes two numbers from the user and prints the numbers between them.
# num_1 = int(input("num_1 : "))
# num_2 = int(input("num_2 : "))

# min_ = min(num_1, num_2)
# max_ = max(num_1, num_2)

# while min_ <= max_:
#     print(min_, end=" ")
#     min_ += 1


# for i in range(min_ , max_ + 1):
#     print(i, end=" ")

# 2 -> Write a program that takes two integers from the user and prints their common divisors.
# num_1 = int(input("num_1 : "))
# num_2 = int(input("num_2 : "))

# min_ = min(num_1, num_2)

# for i in range(1, min_+1):
#     if num_1 % i == 0 and num_2 % i == 0:
#         print(i, end=" ")


# 3 -> Write a program that takes two integers from the user and prints their greatest common divisor.
# num_1 = int(input("num_1 : "))
# num_2 = int(input("num_2 : "))

# min_ = min(num_1, num_2)

# for i in range(min_, 0, -1):
#     if num_1 % i == 0 and num_2 % i == 0:
#         print(i)
#         break


# 4 -> Write a program that takes two integers from the user and prints their least common multiple.
# first way 👇
# num_1 = int(input("num_1 : "))
# num_2 = int(input("num_2 : "))

# min_ = min(num_1, num_2)
# max_ = max(num_1, num_2)

# for i in range(1, min_ + 1):
#     if (max_ * i) % min_ == 0:
#         print(max_ * i)
#         break

# second way 👇
# num_1 = int(input("num_1 : "))
# num_2 = int(input("num_2 : "))

# min_ = min(num_1, num_2)
# max_ = max(num_1, num_2)

# i = max_
# while i % min_ != 0:
#     i += max_
# print(i)


# 5 -> Get a number from the user and print the number of digits
# num = int(input("num: "))
# i = 0
# while num > 0:
#     num //= 10
#     i += 1
# print(i)


# 6
# first way 👇
# rows = int(input("rows : "))
# for i in range(1, rows + 1):
#     print(" " * (rows - i), end="")
#     print("*" * i)

# second way 👇
# n = int(input("rows : "))
# for i in range(1, n + 1):
#     for j in range(0, n - 1):
#         print(" ", end="")
#     for z in range(0, i):
#         print("*", end="")
#     print()


# 7
from random import choice
names_list = ["Hassan","Ali","Lida","Hasti","Zahra","Reza","Qadir","Amin","Asghar","Shila"]
names_list_copy = names_list.copy()
while True:
    if len(names_list_copy) == 0:
        break
    my_pc_choice = choice(names_list_copy)
    answer = input(f"Is your choice {my_pc_choice}? y/n: ")
    if "y" in answer.lower():
        print("You win!")
        break
    names_list_copy.remove(my_pc_choice)