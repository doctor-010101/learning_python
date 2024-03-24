# 1 => Write a program that converts weight from kilograms to grams.

weight_kilograms = int(input("Enter you weight :) "))
weight_grams = weight_kilograms * 1000
print(type(weight_grams))
print("Your weight in grams : ", weight_grams, "g", sep=(""))

# ------------------------------------------------------------------------------------------------------ #

# 2 => Write a program to calculate the area of a triangle.

base = int(input("Enter base :) "))
height = int(input("Enter height :) "))
area = (base * height) / 2
print("Area:", area)

#  ------------------------------------------------------------------------------------------------------ #

# 3 => Write a calculator.

num1 = int(input("Enter num 1 "))
num2 = int(input("Enter num 2 "))
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
print(num1, "**", num2, "=", num1**num2)
print(num1, "%", num2, "=", num1 % num2)

# ------------------------------------------------------------------------------------------------------ #

# 4 => Write a program that takes a number from the user and prints its digits individually.

main_num = int(input("Enter any number : "))
digit = main_num % 10
print(digit)
main_num = main_num // 10
digit = main_num % 10
print(digit)
main_num = main_num // 10
digit = main_num % 10
print(digit)

# ------------------------------------------------------------------------------------------------------ #

# 5 => Write a program that converts degrees to radians.

deg = int(input("Enter deg : "))
radian = deg * (3.14 / 180)
print("deg to radian =", radian)
