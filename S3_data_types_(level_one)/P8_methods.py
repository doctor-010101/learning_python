string = "I love python"
x = ("a ", " 2 ", " b")
print(len(string))  # output : 13 => Return the number of characters in the string.

print(
    string.upper()
)  # output : I LOVE PYTHON => Converts all letters of the string to uppercase.

print(
    string.lower()
)  # output : i love python => Converts all letters of the string to lowercase.

print(
    string.count("o")
)  # output : 2 => Returns the number of characters of its own input in the string.

print(
    string.endswith("n")
)  # output : True => Checks whether the string ends with the input character of the method or not.

print(
    string.startswith("i")
)  # output : False => Checks whether the string starts with the input character of the method or not

print(
    string.find("l")
)  # output : 2 => It starts from the left side and when it reaches its own input character in the string, it returns nput character index.

print(
    string.rfind("o")
)  # output : 11 => It does the work of the previous method, but starts from the right side.

print(
    string.isalnum()
)  # output : False => Checks if there is something else besides letters and numbers in the string, such as space, $, #, etc., if it is, it returns false, and if not, it returns true.

print(
    string.isnumeric()
)  # output : False => Checks whether all the characters of the string are numbers or not, returns true if it is a number and false if not.

# print(string.isnumeric()) # output :

print(
    string.join(x)
)  # output : a I love python 2 I love python b => Joins the desired string into the input of the method.

print(
    string.split()  # output : ['I', 'love', 'python']
)  # Splits the string according to the input it takes. Here, the input of the method is space, so it separates the characters of the string according to the space and returns them.

print(
    string.replace("o", "n")
)  # output : I lnve pythnn => The second entry replaces the first entry.

strip_string = "#####Hi Hi#####"
print(
    strip_string.strip("#")
)  # output : Hi Hi => If the first and last characters of the desired string is the input character of the method, it will be deleted.

print(strip_string.lstrip("#")) # output : Hi Hi##### => It does the work of the above method, but with the difference that it does it from the left side

print(strip_string.rstrip("#")) # output : #####Hi Hi => It does the work of the above method, but with the difference that it does it from the right side

print(string.capitalize()) # output : I love python => Only the first character of the desired string is converted to uppercase.
