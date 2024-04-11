# In consecutive conditions like the example below, if the first condition is true, the following conditions are not checked.
x = 7
if x < 10:
    print("x is less than 10")
elif x == 7:
    print("x is equal to 7")
elif x > 5:
    print("x is greater than 5")
else:
    print("")
# So the output is only "x is less than 10"


# If we want to check the conditions separately, they are written separately.
if x < 10:
    print("x is less than 10")
if x == 7:
    print("x is equal to 7")
if x > 5:
    print("x is greater than 5")

"""
So the output is : 👇
x is less than 10
x is equal to 7
x is greater than 5

"""


# We can use nested conditionals 👇
score = int(input("Enter the score : "))
if score > 10:
    print("Accepted!")
    if 15 <= score <= 20:
        print("A")
    elif 10 < score < 15:
        print("B")
else:
    print("Rejected!")


# Linear conditions 😂
x = 10
y = 20 + 10 if x > 7 else 20
print(y)  # output : 30 (because x is greater than 7)


# Solve Examples
# 1 => Checking whether the user's input is even or odd
input_number = int(input("Enter the number : "))
if input_number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2 => between  the user inputs, which one is greater?
# if we have two inputs 👇
input1 = int(input("Enter first number : "))
input2 = int(input("Enter second number : "))
if input1 > input2:
    print("input_1 grater than input_2!") 
elif input1 == input2:
    print("input_1 equal to input_2!") 
else:
    print("input_2 grater than input_1!")


# if we have more than two inputs 👇
num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
num3 = int(input("Enter the number : "))
less_number = num1 
if num2 < less_number:
    less_number = num2
if num3 < less_number:
    less_number = num3
print("Less number is :", less_number)
