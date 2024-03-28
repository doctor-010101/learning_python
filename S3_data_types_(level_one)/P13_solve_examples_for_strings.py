# Get from user a character and find it count in string
my_str = "Hello i'm Hassan seyfali pour I love python and 01 world"
user_character = input("Enter character...")
print(my_str.count(user_character))
# # ----------------------------------------------------------------------------------------------------------- #


# Find the last word of the user's sentence
user_sentence = input("Enter a sentence...")
user_sentence = user_sentence.strip()
last_space = user_sentence.rfind(" ")
print(user_sentence[last_space + 1 :])
# # ----------------------------------------------------------------------------------------------------------- #


# Are there words from the second string inside the first string or not?
string1 = input("Enter str 1...")
string2 = input("Enter str 2...")
print(string1 in string2)
# ----------------------------------------------------------------------------------------------------------- #


# Remove tabs and spaces from user input
user_string = input("Enter string... :) ")
print(user_string.replace(" ", "").replace("\t", ""))
# ----------------------------------------------------------------------------------------------------------- #


# Remove zero frome user phone number
user_phone_number = input("Enter your phone number :) ")
print(user_phone_number.lstrip("0"))