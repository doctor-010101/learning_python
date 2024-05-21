# In Python, a lambda is an anonymous (unnamed) expression that allows you to define small, one-line functions. Lambda functions are typically used for simple operations in places where a full function definition is unnecessary. The general structure of a lambda expression is as follows:

# lambda arguments: expression

### Features of Lambda Functions in Python
# 1. Anonymous: Lambda functions do not require a name and can be used directly where they are defined.
# 2. Concise and One-liner: They are usually used for simple and short operations.
# 3. Usage in Other Functions: Lambda functions can be passed as arguments to other functions (such as sorting, filtering, etc.).

### Examples

#### Example 1: Simple Lambda Function
# In this example, a lambda function is defined to add two numbers:
add = lambda x, y: x + y
result = add(2, 3)
print(result)  # Output: 5
# Here, add is a lambda function that takes two arguments x and y and returns their sum.

#### Example 2: Using with map Function
# The map function applies a function to each item in a list:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
# Here, a lambda function is passed to map that squares each number.

#### Example 3: Using with filter Function
# The filter function is used to filter items in a list based on a condition:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]
# Here, a lambda function is passed to filter that selects only even numbers.

#### Example 4: Using with sorted Function
# The sorted function is used to sort a list. You can create a custom sorting function using a lambda:
points = [(2, 3), (1, 2), (4, 1), (3, 4)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(4, 1), (1, 2), (2, 3), (3, 4)]
# Here, a list of points is sorted based on their y-coordinate.

# Overall, lambda functions in Python are useful for quick and short operations, making the code more concise and readable.