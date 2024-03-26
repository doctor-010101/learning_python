# First way => Traditional method: This method is old but not obsolete yet.
x = 5
y = 10.5
z = 11.5
print(
    "x is: %i\ny is: %f\nz is:%i\na is:%i" % (x, y, z, 2 + 10)
)  # i(integer), f(float)
# [(key)] [flag] [width] [.p] type => Only specifying the type is mandatory.


print(
    "character is: %c" % (72)
)  # output : character is: H (It is used when we want to find the unicode character).

print("character is: %c" % ("B"))  # output : character is: B

# print(
#     "character is: %c" % ("AB")
# )  # output : TypeError: %c requires int or char (You cannot write a string, it must be a character).

print("string is: %s" % ("I love python"))  # output => string is: I love python

print("integer is: %i" % (20))  # output => integer is: 20

print(
    "integer is: %i" % (20.5)
)  # output => integer is: 20 (float number becomes an integer)

print("integer is: %d" % (20))  # output => integer is: 20 (%d does %i work)

print("oct is: %o" % (20))  # output => oct is: 24 (It show octal)

print("hex is: %x" % (313313))  # output => hex is: 4c7e1 (It show hex, lowercase)

print("hex is: %X" % (313313))  # output => hex is: 4C7E1 (It show hex, uppercase)

print(
    "scientific symbol is: %e" % (313313)
)  # output => scientific symbol is: 3.133130e+05 (It shows numbers with scientific symbols, lowercase)

print(
    "scientific symbol is: %E" % (313313)
)  # output => scientific symbol is: 3.133130e+05 (It shows numbers with scientific symbols, uppercase)

print(
    "float is: %f" % (3.2)
)  # output => float is: 3.200000 (It shows numbers with six decimal places)

print(
    "float is: %f" % (3)
)  # output => float is: 3.000000 (It shows numbers with six decimal places)

print(
    "float is: %f" % (2e400)
)  # output => float is: inf (It shows numbers with six decimal places, lowercase)

print(
    "float is: %F" % (2e400)
)  # output => float is: INF (It shows numbers with six decimal places, uppercase)

print(
    "string is: %r" % ("I love python")
)  # output => string is: 'I love python' (It does X but with the difference that it puts the result in single quotes)

# The above 👆 was about typing, which is mandatory to specify
#
# We can control the decimal part 👇
print(
    "float: %.2f" % (2.128456789)
)  # output => float: 2.13 (Rounds the last number according to the next number)
print(
    "float: %.2f" % (2.123456789)
)  # output => float: 2.12 (Rounds the last number according to the next number)
print(
    "float: %.8f" % (2.123456789)
)  # output => float: 2.12345679 (Rounds the last number according to the next number)
print(
    "float: %.8f" % (2.123456789)
)  # output => float: 2.12345679 (Rounds the last number according to the next number)


# We can control the width of characters 👇

print("float: %2.4f" % (2.1234))  # output => float: 2.1234
print("float: %6.4f" % (2.1234))  # output => float: 2.1234
print(
    "float: %15.4f" % (2.1234)
)  # output => float:          2.1234 (Fills with spaces)

# Flags (+, -, 0)
print(
    "float: %+9.4f" % (2.1234), "+", sep=""
)  # output => float:   +2.1234+ (It show positive numbers)
print(
    "float: %-9.4f" % (2.1234), "+", sep=""
)  # output => float: 2.1234   + (It changes the order)
print(
    "float: %09.4f" % (2.1234), "+", sep=""
)  # output => float: 0002.1234+ (Fills the space with zero)

# Key()
dictionary = {"num1": 10, "num2": 20}
print("%(num1)i\n%(num2)i" % (dictionary))  # output => 10, 20
print("%(num2)i\n%(num1)i" % (dictionary))  # output => 20, 10
print("%(num1)i\n%(num2)i" % ({"num1": 10, "num2": 20}))  # output => 10, 20

# We will talk about dictionary later 💪
#
# We can make the user specify the decimal place and the width 👇

float = 2.2
decimal = int(input("Enter dicimal: "))
width = int(input("Enter width: "))

print("%0*.*f" % (width, decimal, float)) # output => 000002.200
