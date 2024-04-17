# break => The loop will no longer repeat when it reaches the break command.
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


# continue =>
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)


# else =>
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
