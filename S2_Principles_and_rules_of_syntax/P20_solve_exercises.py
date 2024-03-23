"""
exercises 1 => Define two variables x and y and assign values to them then,
change the values of x and y without using the third variable.

"""

x = 10
y = 20
x, y = y, x  # Change values


"""
exercises 2 => Write a program to find the area of a rectangle using Calculate the variables.
Store the length and width in variables.
Then calculate and print the area.

"""

length = 2
width = 6
area = length * width
print("Area:", area)


"""
exercises 3 => Create a program that converts temperature from Celsius to Fahrenheit
store the temperature in Celsius in a variable, convert
and print the result.

The formula for converting Celsius to Fahrenheit => Fahrenheit = 1.8 * Celsius + 32

"""
celsius_temperature = 50
fahrenheit_temperature = 1.8 * celsius_temperature + 32
print(celsius_temperature, " °C = ", fahrenheit_temperature, " °F", sep="")


"""

exercises 4 => Calculate the area and perimeter of the circle.
Saveadius in a variable and then calculate and print the area and perimeter.

"""
radius = 15
area = radius**2 * 3.14
perimeter = (radius * 2) * 3.14
print("Area:", area, "perimeter:", perimeter)


"""

Exercise 5 => Create a program that calculates the sum, difference, product and power of two numbers.

"""
x = 2
y = 5

additional = x + y
subtraction = x - y
multiplication = x * y
exponentiation = x**y

print("Additional:", additional)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Exponentiation:", exponentiation)


"""

Exercise 6 => Write a program that calculates the average of three numbers.

"""
x = 20
y = 19
z = 18

average = (x + y + z) // 3

print("Average:", average)


"""

Exercise 7 => Write a program to calculate the area of a triangle.

"""
base = 12
height = 6

area = (base // 2) * 6

print("Area:", area)


"""

Exercise 8 => Create a variable and write your age in it, then calculate in which year you will be 100 years old.

"""
my_age = 23
main_year = (100 - my_age) + 1402

print('Main year I 100 years old:', main_year)


"""

Exercise 9 => Change the variables in the given code snippet according to Pep 8.

num1 = 42
Num2 = 13
ReSuLt = num1 Num2
print(ReSuLt)
"""

# Changed 👇

num1 = 42
num2 = 13
result = num1, num2
print(result)
