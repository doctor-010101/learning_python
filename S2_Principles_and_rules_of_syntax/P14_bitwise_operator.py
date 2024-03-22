"""

Bitwise operators in the Python programming language are used to perform bitwise operations on integers.
Below are some of the bitwise operators in Python along with examples for each 👇

"""

""" 1. & (Bitwise AND):
   - This operator compares each bit of two numbers and returns the bitwise AND result.
   - Example 👇
"""

a = 10  # 1010 in binary
b = 6  # 0110 in binary
result = a & b
print(result)  # Output: 2 (0010 in binary)

"""
2. | (Bitwise OR):
   - This operator compares each bit of two numbers and returns the bitwise OR result.
   - Example 👇
"""
a = 10  # 1010 in binary
b = 6  # 0110 in binary
result = a | b
print(result)  # Output: 14 (1110 in binary)

"""
3. ^ (Bitwise XOR):
   - This operator compares each bit of two numbers and returns the bitwise XOR result.
   - Example 👇
"""
a = 10  # 1010 in binary
b = 6  # 0110 in binary
result = a ^ b
print(result)  # Output: 12 (1100 in binary)

"""
4. ~ (Bitwise NOT):
   - This operator flips all the bits of a number; i.e., it changes every 1 bit to 0 and every 0 bit to 1.
   - Example 👇
"""
a = 10  # 1010 in binary
result = ~a
print(result)  # Output: -11 (1101...101 in binary)

"""
5. << (Left Shift):
   - This operator shifts all the bits of a number to the left and pads with zeros.
   - Example 👇
"""
a = 5  # 0101 in binary
result = a << 2
print(result)  # Output: 20 (10100 in binary)

"""
6. >> (Right Shift):
   - This operator shifts all the bits of a number to the right and pads with zeros.
   - Example 👇
"""
a = 20  # 10100 in binary
result = a >> 2
print(result)  # Output: 5 (0101 in binary)


# These operators allow you to perform complex operations on the bits of integer numbers in Python.
# "bin(integer)" function is used to get the binary number of integers
print(bin(10))  # Result => 0b1010 (0b is the binary sign of the number)
