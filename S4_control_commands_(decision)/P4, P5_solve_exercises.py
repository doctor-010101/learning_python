# 1 - Take a number from the user and check if it is divisible by both 2 and 5 or not?
number = int(input("Enter a number : "))
if number % 5 == 0 and number % 2 == 0:
    print("Yes")
else:
    print("No")


# 2 - Triangles
side1 = int(input("Enter first side : "))
side2 = int(input("Enter second side : "))
side3 = int(input("Enter third side : "))

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print("Triangles can be made with these sides!")
    if side1 == side2 and side2 == side3:
        print("The triangle is equilateral!")
    if side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles!")
    if side1 != side2 and side2 != side3 and side1 != side3:
        print("The triangle is different sided!")
    if side1 ** 2 == side2 ** 2 + side3 ** 2 and side2 ** 2 == side1 ** 2 + side3 ** 3 and side3 ** 2 == side1 ** 2 + side2 ** 2:
        print("The triangle is right-angled")
else:
    print("A triangle is not created")


# 3 - Get a character from the user and check it is a number or a character or other symbol.
character = input("Enter a character : ")
if 48 <= ord(character) <= 57:
    print("The character is number!")
elif 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
    print("The character is letter!")
else:
    print("Other!")
