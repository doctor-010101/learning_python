"""

--- A string is a sequence of characters in programming languages.
In other words, a string is a set of characters such as alphabets, numbers, periods, dashes, spaces, and other symbols arranged in a specific order.

In Python, you can create a string using single quotes (' ') or double quotes (" "). for example: 

my_string_single = 'Hello, World!'
my_string_double = "Hello, World!"

-----------------------------------------------------------------------------------------------------------------

--- Also, you can use string operators like plus (+) to concatenate two strings. for example:

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

--- Strings can be multiplied by a number to repeat. for example:
x = "srting "
repeat = x * 5
print(repeat) # Output: srting srting srting srting srting 

------------------------------------------------------------------------------------------------------------------

--- In order to know whether a variable type is, for example, a number or a string or...,
the isinstance(x, int) function is used for example:
x = 'string'
print(isinstance(x, int)) => result : False

-------------------------------------------------------------------------------------------------------------------
\n It does the work of the enter button in Word
\t Used for a space tab

The two above are special characters and their full explanations will be given in the next sections.

"\" If it comes after special characters, it cancels their action for example:

x = "C: download\tables\new-table"
print(x) output : 👇

C: download     ables
ew-table

x = "C: download\\tables\\new-table"
print(x) output : 👇

C: download\tables\new-table


"""
