"""
Number Types 👇

1. Integers:
   Integers are defined as whole numbers without decimals. For example:
   
   num1 = 10
   num2 = -5
   

2. Floats:
   Floats include numbers with decimals. For example:
   
   num3 = 3.14
   num4 = -0.5
   

3. Complex Numbers:
   Complex numbers consist of a real part and an imaginary part. For example:
   
   num5 = 2 + 3j
   num6 = -1.5 - 2j
   

4. Zero:
   Zero is also defined in Python and can be represented as follows:
   
   zero = 0


These functions are used to convert the type of numbers to each other 👇

    float()
    int()
    complex()

"""

"""
In mathematics, numbers can be classified based on the base used to represent them. These bases generally include base-10 (Decimal), base-2 (Binary), base-8 (Octal), and base-16 (Hexadecimal). Here is a detailed explanation of each of these number bases:

1. Base-10 (Decimal):
   - Decimal numbers range from 0 to 9.
   - Decimal representation uses digits from 0 to 9.
   - For example: 123, 456, 789

2. Base-2 (Binary):
   - Binary numbers consist of only 0s and 1s.
   - Binary representation uses digits 0 and 1.
   - For example: 101 (equivalent to decimal number 5)

3. Base-8 (Octal):
   - Octal numbers range from 0 to 7.
   - Octal representation uses digits from 0 to 7.
   - For example: 17 (equivalent to decimal number 15)

4. Base-16 (Hexadecimal):
   - Hexadecimal numbers range from 0 to F (where letters A to F are used as substitutes for numbers greater than 9).
   - Hexadecimal representation uses digits from 0 to F.
   - For example: 1A3 (equivalent to decimal number 419)


These functions are used to convert the basis of numbers to each other
    bin()
    oct()
    hex()

"""
# In Python, numbers can be separated by "_"
x = 1_000_000_000


# In Python, large numbers are represented by scientific notation
z = 5e4  # (5 * 10) ** 4

print(pow(2, 3))  # Use for exponentiation (**)

print(7/3) # Result : 2.3333333333333335

print(round((7 / 3), 3))  # Use for round numbers result : 2.333
