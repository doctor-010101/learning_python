# --- All characters in the world of programming have a unique code.
#
# --- Two of the most common codes are ascii and unicode.
#
# --- These codes are used to print characters that are not in the keyboard.
#
# --- Ascii are limited because Skies only supports Latin letters and Latin numbers, but Unicode supports other languages as well.
#
# --- All ASCII codes exist in Unicode and are common to it, for example, the Unicode code for the letter a and its ASCII code are the same.
#
# --- https://www.asciitable.com => ascii code table   |   https://www.utf8-chartable.de => unicode table
#
# ---"ord("character")" function is used to get ASCII code or Unicode.
print(ord("A"))  # output => 97
print(ord("a"))  # output => 65
print(ord("+"))  # output => 43
# --- "chr(ascii_value)" function is used to see the character of ascii code.
print(chr(96))  # output => `
print(chr(97))  # output => a
# --- This syntax "\uunicode" is used to show Unicode characters.
print("character : \u002B")  # output => +


print("character : \053")  # output => + (octal)
print("character : \x2b")  # output => + (hex)


print("I lo\nve python")  # \n => enter
print("I lo\bve python")  # \b => back space output : I lve python
print("I lo\tve python")  # \t => one tab space output : I lo    ve python
print("I lo\rve python")  # \r => Removes the previous \r output : ve python
# Note: Using \r in the pycharm deletes the entire string and writes the string after \r.
#  But in terminal and interactive environments, usually only the length of the string after r\ is deleted, not the whole string.
print(r"I l\tove py\ntho\nn")  # output : "I l\tove py\ntho\nn" If you putting up "r" , "R" before string, it considers everything that is inside the string, no less, no more
