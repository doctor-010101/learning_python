print(range(10))  # output : range(0, 10)
print(type(range(10)))  # output : <class 'range'>
print(list(range(10)))   # output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    print(i)


print("\n")

# start, end
for a in range(2, 11):
    print(a)


print("\n")

# start, end, ste
for b in range(2, 11, 3):
    print(b)

print("\n")

for c in range(-100, -200, -20):
    print(c)

print("\n")

# Example 1
input_list = input("Enter the names : ").split("-")
for name in range(0, len(input_list)):
    print(name, input_list[name])


# Example 2 : Find the factorial
number = int(input("Enter a number : "))
d = 1
for number in range(1, number + 1):
    d *= number
print("factorial :", d)


# Example 3 : Reverse the input numbe
num = input("Enter a num : ")
for z in range(len(num)-1, -1, -1):
    print(num[z], end="")


# Example 4
rows = int(input("rows : "))
for x in range(1, rows + 1):
    for y in range(1, x+1):
        print(y, end="")
    print()
for x in range(rows - 1, 0, -1):
    for y in range(1, x+1):
        print(y, end="")
    print()
