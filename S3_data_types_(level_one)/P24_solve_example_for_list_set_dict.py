# 1 => Get the name and scores from the user and calculate the average.
#
# step 1 : get name and scores so append in list
scores_list = []
name = input("Please enter your name...")
physics_score = float(input("Enter your physics score..."))
scores_list.append(physics_score)
math_score = float(input("Enter your math score..."))
scores_list.append(math_score)
literature_score = float(input("Enter your literature score..."))
scores_list.append(literature_score)

# Step two : calculate average
average = (scores_list[1] + scores_list[1] + scores_list[1]) / 3
print("Your scores average is :", average)


# --------------------------------------------------------------------------------------------------------- #


# 2 => Get the phone number from the user and turn it into a list.
user_phone_number = input("Please enter your Phone number : ")
numbers_list = list(user_phone_number)
print("numbers list :", numbers_list)


# --------------------------------------------------------------------------------------------------------- #


# 3 => Replace the last index of the first list with the second list.
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list1[-1:] = list2
print(list1)  # result : [1, 2, 'a', 'b', 'c']


# --------------------------------------------------------------------------------------------------------- #


# 4 => Store the names and score of two students in a dictionary as keys and values.
students_dict = {}
student_name = input("Enter name : ")
student_score = input("Enter score : ")
students_dict[student_name] = student_score
student_name2 = input("Enter name : ")
student_score2 = input("Enter score : ")
students_dict[student_name2] = student_score2
print(students_dict)


# --------------------------------------------------------------------------------------------------------- #


# 5 => Get a string from the user and store its characters in the set and count its number.
string = input("Enter a string...")
characters = set(string)
print(characters)
print(len(characters))
