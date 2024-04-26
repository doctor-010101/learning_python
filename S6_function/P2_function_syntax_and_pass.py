# # define
# def cube(x):
#     return x**3

# # call
# print(cube(3))  # output : 27


# Example 👇
# def print_text():
#     input_text = input("Enter a text : ")
#     print(input_text)


# print_text()


# Example 👇
# def cube():
#     x = int(input("Enter a num : "))
#     return x**3
# n = cube()
# print(n)

# def cube():
#     x = int(input("Enter a num : "))
#     print(x**3)


# cube()


# def cube():
#     x = int(input("Enter a num : "))
#     print(x**3)
#     return None


# a = cube()
# print(a)


# def cube():
#     x = int(input("Enter a num : "))
#     print(x**3)

# a = cube()
# print(a)


# tip 👉 : Statements after return are not executed in the function body.
def cube():
    x = int(input("Enter a num : "))
    print("Hi")
    return x**3
    print("hi")


n = cube()
print(n)


# tip 👉 : The inputs to the function are called parameters when defining the function.
# tip 👉 : Inputs to a function are called arguments when calling that function.


"""
🍀🍀 A few recommendations for functions: 
✅ First -> our functions are not found to have too many commands, maximum of twenty lines.
✅ Second -> its parameters should not be too many.
✅ Third -> the name of the function must be the same as the work of the function and point to it.
✅ Fourth -> to do one specific task, not several tasks.

"""
#  pass