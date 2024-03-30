# Exercise 1 => Get sentences, words, characters and letters from user input.

user_input = input("Enter your text...")
sentences = (
    user_input.count(".")
    + user_input.count("!")
    + user_input.count("?")
    + user_input.count(";")
)
words = user_input.count(" ") + 1
characters = len(user_input)
letters = characters - (
    user_input.count(".")
    + user_input.count("!")
    + user_input.count("?")
    + user_input.count(";")
    + user_input.count("-")
    + user_input.count(",")
    + user_input.count("-")
    + user_input.count(":")
    + user_input.count(" ")
)
print("Number of sentences : ", sentences)
print("Number of words : ", words)
print("Number of characters : ", characters)
print("Number of letters : ", letters)


# Exercise 2 => Get a character form user and print it unicode.
user_character = input("Enter a character...")
print(ord(user_character))


# Exercise 3 => Is user input number or not?
user_phone_number = input("Enter yout phone number...")
print(user_phone_number.isnumeric())
print(user_phone_number.isdigit())
print(user_phone_number.isdecimal())