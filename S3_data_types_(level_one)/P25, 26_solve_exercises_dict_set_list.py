# Exercise 1 => Write a program that takes the word and the meaning of that word from the user and stores it in the dictionary (first way) 👇
dictionary = {}
key = input("Enter a word : ")
mean1 = input("Enter mean1 : ")
mean2 = input("Enter mean2 : ")
mean3 = input("Enter mean3 : ")
mean4 = input("Enter mean4 : ")
dictionary[key] = [mean1, mean2, mean3, mean4]
print(dictionary)
# second way 👇
meanings = input("Enter meanings : ").split(",")
dictionary[key] = meanings
print(dictionary)


# Exercise 2  👇 (Find the meaning of the word input from the above dictionary)
word = input("Enter main word : ")
meaning_input_word = dictionary.get(word)
print("meanings : ",meaning_input_word ) 


# Exercise 3  👇 (We have two lists of phone numbers of users, write a program that removes duplicate numbers)
user_phone_number1 = ["0930", "0903", "0914", "0912"]
user_phone_number2 = ["0913", "0933", "0912", "0933"]
new_list = list(set(user_phone_number1 + user_phone_number2))
print(new_list)  # output => ['0930', '0903', '0914', '0912', '0913', '0933']

