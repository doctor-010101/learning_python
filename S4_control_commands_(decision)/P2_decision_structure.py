# if Statement:
# The if statement is used to execute a block of code conditionally based on a single condition.
# If the condition is true, the code inside the if block will be executed; otherwise, the execution of the if block will be skipped.
x = 10
if x > 5:
    print("x is greater than 5")
# elif Statement:
# The elif statement (short for "else if") is used to add additional conditions after an if statement.
# If the if condition is false, the next elif condition is evaluated, and if it's true, the corresponding block of code is executed.
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than 15")
# else Statement:
# The else statement comes at the end of a chain of if and elif statements and its block of code is executed if none of the previous conditions are true.
x = 3
if x > 5:
    print("x is greater than 5")
elif x > 2:
    print("x is greater than 2 but less than or equal to 5")
else:
    print("x is less than or equal to 2")
# In the above example, the if condition is checked first, and if it's true, the corresponding block of code is executed.
# Otherwise, the elif condition is evaluated, and if it's true, its block of code is executed. If neither the if nor the elif conditions are true, the else block is executed.
# Using these conditional statements, you can control the flow of execution in your programs and write dynamic and flexible code.


# Another example 👇
score = int(input("Enter score : "))
if score <= 20 and score >= 15:
    print("A")
elif score < 15 and score >= 10:
    print("B")
elif score < 10 and score >= 5:
    print("C")
elif score < 5 and score >= 0:
    print("D")
else:
    print("Wrong!")


# or
score = int(input("Enter score : "))
if 20 >= score >= 15:
    print("A")
elif 15 > score >= 10:
    print("B")
elif 10 > score >= 5:
    print("C")
elif 5 > score >= 0:
    print("D")
else:
    print("Wrong!")
