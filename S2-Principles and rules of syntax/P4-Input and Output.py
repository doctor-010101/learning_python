"""
- Sometimes as programmers, we need to get information from the users, process it, and display the result back to them.
The information we get from the users and they enter is called input,
and the information we display to the users after processing operations is called output.

- Full explanations abou input and output will come in the next chapters

"""

print(2 * 5)

"""
- 2, 5 are inputs and result (10) is output.

"""


"""
- When displaying the results we can specify which seperator the results should be displayed with.

- This is done by the sep="seperator".

"""


print(2, 6, 8, 9, 0, 5, sep="_")

"""
- Result : 2_6_8_9_0_5
- If we don't use seperator by default because of the space after the comma, a space is placed between the values.
- Result without seperator 👉 "2 6 8 9 0 5"
- If you don't want a space, use sep=""

"""


"""
If we have several prints in a row, by default, the result of each print is displayed in a separate line. And if there is no input print, an empty line will be spaced.

"""
print("a")
print("c")
print()
print(12)
print()
print(10)

"""
Result: 👇

a
c

12

10

"""

""" If we use end="seperator", we can control the distance between prints 👇"""

print("a", end="/")
print(12)
print("c", end=":")
print()
print(end="_")
print(10)

"""
Result: 👇

a/12
c:
_10

"""

# We can use "/n" to go to the next line 👇

print(5, "\n", 6, "\n", 8, 9, sep="")

"""
Result: 👇

5
6
89

"""



"""
We can use input() function to get information from user 👇
If you run this code, after executing the first line,
the interpreter will wait for you to enter the requested information and then execute the next line.

"""

x = input("Enter you name: ")

print("Your name is:", x)
