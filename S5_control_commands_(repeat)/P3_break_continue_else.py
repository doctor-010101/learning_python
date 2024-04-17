"""
continue:
When the "continue" statement is encountered within a "while" loop, the current iteration of the loop is terminated,
 and the program execution jumps back to the beginning of the loop. In other words,
 it skips the rest of the code in the loop and starts the next iteration.

else:
The "else" clause in a "while" loop in Python is executed when the loop condition becomes false.
 In other words, when the loop naturally terminates due to the condition being false, the code block under the "else" clause is executed.

break:
The "break" statement is used within a "while" loop to immediately terminate the loop's execution. When the code encounters a "break" statement,
 the loop is exited, and the program continues execution from the next statement after the loop.

These statements help control the flow of execution within loops and allow you to tailor the behavior of the loop according to your requirements.

"""


# break
# i = 1
# while i <= 100:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# # Controlling the infinite loop (First Way)
# input_num = float(input("Enter a num : "))
# smallest_num = input_num
# while True:
#     confirm_to_continue = input("do you want to continue?")
#     if confirm_to_continue.lower() == "no":
#         break
#     input_num = float(input("Enter a num again : "))
#     if input_num < smallest_num:
#         smallest_num = input_num
# print("smallest_num is : ", smallest_num)


# # Controlling the infinite loop (Second Way)
# smallest_number = float("inf")
# while True:
#     input_number = float(input("Enter a number : "))
#     if input_number < smallest_number:
#         smallest_number = input_number
#         continue_or_no = input("do you want to continue?")
#     if continue_or_no.lower() == "no":
#         break
# print("smallest_number is : ", smallest_number)


# continue
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)


# else
number = int(input("Enter a number : "))
i = 2
if number > 1:
    while i < (number//2) + 1:
        if number % i == 0:
            print(number, "is not a prime number!")
            break
        i += 1
    else:
        print(number, "is a prime number!")
else:
    print(number, "is not a prime number!")
