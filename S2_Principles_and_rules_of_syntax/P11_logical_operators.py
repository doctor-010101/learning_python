"""
Logical operators are operators used to perform logical operations between two logical expressions or values.
 In programming and mathematics, logical operators include AND, OR, and NOT operators.

1. AND operator: This operator is used when both input expressions or logical values are true.
 In other words, the result of the AND operator is true only when both inputs are true.

2. OR operator: This operator is used when at least one of the two input expressions or logical values is true.
 The result of the OR operator is true if at least one of the inputs is true.

3. NOT operator: This operator is used to negate the input logical value or expression.
 In other words, if the input is true, the result of the NOT operator will be false and vice versa.

These logical operators have various applications in programming, algorithms, computer logic, and other fields.
"""

x = 10
y = 5

# and
print(
    x > y and (x / 2) == y and x == (y * 2)
)  # Because all the expression are true, then the result is true.
print(
    x > y and x <= y and x == (y * 2)
)  # Because one of the expression is false, then the result is false.

# or
print(
    x > y or x == y or (x / 2) > y
)  # Because one of the expression is true, the result is also true.
print(
    x <= y or x == y or (x / 2) > y
)  # Because all expression are false, the result is also false.

# not reverse the result

print(
    not (x == y and x > y)
)  # Because the expression inside the parenthesis is false, true is printed.
print(
    not (x != y)
)  # Because the expression inside the parenthesis is true, false is printed.

print(not True)
print(not False)
