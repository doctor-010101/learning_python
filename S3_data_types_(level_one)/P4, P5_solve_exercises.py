# 1 => Write a program that takes the radius of a circle from the user and calculates its area and perimeter.
radius = int(input("Enter radius of circle : "))
area = radius**2 * 3.14
perimeter = (radius * 2) * 3.14
print("Area:", area, "perimeter:", perimeter)


# -------------------------------------------------------------------------------------------------------- #

# 2 => Write a program that takes a number from the user and prints its square and cube.
main_number = int(input("Enter any number : "))
square = main_number**2
cube = main_number**3
print("square and cube =", square, "and", cube)


# -------------------------------------------------------------------------------------------------------- #

# 3 => Write a program that takes two numbers from the user and increases the first to the power of the second.
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
power = pow(number1, number2)
print(power)


# -------------------------------------------------------------------------------------------------------- #
# 4 => Write a program that takes three numbers from the user and prints their average.

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
number3 = int(input("Enter third number : "))
average = (number1 + number2 + number3) // 3
print("Average numbers is :", average)
