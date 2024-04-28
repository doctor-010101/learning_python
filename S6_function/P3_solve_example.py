# 🍀 Example 1 👇

# First Way 👇

# def repeat(number, digit):
#     counter = 0
#     while number > 0:
#         if number % 10 == digit:
#             counter += 1
#         number = number // 10
#     return counter

# number = int(input("Enter the number : "))
# digit = int(input("Enter the digit : "))
# print(digit, "is repeat", repeat(number, digit), "times")


# Second Way 👇
# def repeat(number, digit):
#     return str(number).count(str(digit))

# number = int(input("Enter the number : "))
# digit = int(input("Enter the digit : "))
# print(digit, "is repeat", repeat(number, digit), "times")


# 🍀 Example 2 👇
# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f


# def sum_fact(n):
#     sum_ = 0
#     for i in range(1, n + 1):
#         sum_ += fact(i)
#     return sum_


# number = int(input("Enter the number : "))
# print("sum : ", sum_fact(number))


# 🍀 Example 3 👇
# First Way 👇
def max_(first_num, second_num, third_num):
    return max(first_num, second_num, third_num)


first_num = int(input("Enter first_num : "))
second_num = int(input("Enter second_num : "))
third_num = int(input("Enter third_num : "))
print("Max : ", max_(first_num, second_num, third_num))


# Second Way 👇
def max_():
    first_num = int(input("Enter first_num : "))
    second_num = int(input("Enter second_num : "))
    third_num = int(input("Enter third_num : "))
    return max(first_num, second_num, third_num)


print("Max : ", max_())


# Third Way 👇
def max_():
    first_num = int(input("Enter first_num : "))
    second_num = int(input("Enter second_num : "))
    third_num = int(input("Enter third_num : "))
    print("Max : ", max(first_num, second_num, third_num))


max_()