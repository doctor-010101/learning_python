# Example 1 => We take a number from the user and print the even numbers between that number and one hundred.
num = int(input("Enter a number : "))
while num < 100:
    if num % 2 == 0:
        print(num)
    num += 1


# Example 2 => Print all numbers divisible by 3 and 7 between 1 and 1000
desired_number = 1
while desired_number < 1000:
    if (desired_number % 7 == 0) and (desired_number % 3 == 0):
        print(desired_number)
    desired_number += 1


# Example 3
row = 1
n = int(input("rows : "))
while row <= n:
    print("*" * row)
    row += 1


# Example 4
n = int(input("rows : "))
while n >= 1:
    print("*" * n)
    n -= 1


# Example 5 => Get a number from the user and store its divisors in a list And check whether the number is whole or not?
# input_num = int(input("Enter a number : "))
# divisors = []
# i = 1
# while i <= input_num:
#     if input_num % i == 0:
#         divisors.append(i)
#     i += 1
# print(divisors)
# if sum(divisors) - input_num == input_num:
#     print("Complete!")
# else:
#     print("No Complete!")


# Another way for example above
input_num = int(input("Enter a number : "))
i = 1
c = 0
while i < input_num:
    if input_num % i == 0:
        c += i
    i += 1
if c == input_num:
    print("Complete!")
else:
    print("No Complete!")


# Example 6 => Print the numbers of the Fibonacci series up to 20 sentences.
i = 1
a, b = 0, 1
while i <= 20:
    print(a)
    a, b = b, a + b
    i += 1
