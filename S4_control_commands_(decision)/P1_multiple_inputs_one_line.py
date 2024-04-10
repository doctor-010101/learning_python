# Taking multiple inputs from the user in one line
# ---- The number of inputs and variables must be equal
# x, y, z = input("x, y, z : ").split(" ")
# print("x : ", x, "\ny : ", y, "\nz : ", z)


# We can take many inputs by thid way 👇
list = input("Enter a list of numbers: ").split(",")
print(list)
