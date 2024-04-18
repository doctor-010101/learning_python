# for loop -> The for loop in the Python programming language is used to iterate over functions or datasets.
# This loop automatically traverses all elements of a dataset from beginning to end and accesses each element of the dataset in order.


"""
The difference between "while" and "for":

for loop:
The for loop is used to iterate over all elements of a dataset, which can be a list, a string, a dictionary, a tuple, or any other iterable object.
It automatically traverses all elements of the dataset from beginning to end and accesses each element of the dataset in order.
It is typically used when the number of iterations is known and limited, or when you want to examine all elements of a dataset.
while loop:
The while loop continues to iterate as long as a specific condition is true.
The condition in a while loop is evaluated at the beginning of each iteration, and the loop continues as long as the condition remains true.
It is usually used when the number of iterations may vary or when you want to repeat until a specific condition is met.
In summary, if the number of iterations is known and there is a dataset to iterate over, the for loop is typically used.
On the other hand, if the iteration is based on a specific condition and you want to repeat until that condition is met, the while loop is more appropriate.
"""

list_1 = [1, 3, 4, 6, 7, 8, 9]
string = "python"
tuple_1 = ("a", "b", "c")
dictionary = {"a": 20, "b": 30, "c": 40}


# for target in object ...
for i in list_1:
    print(i)

for i in string:
    print(i)

for i in tuple_1:
    print(i)

for i in dictionary:  # By default, keys are printed
    print(i)
print()


# Example 1 (Print character with code)
list_2 = [90, 87, 58, 63, 69, 113, 72]
for characters in list_2:
    print(chr(characters))


# for in while and while in for


# break, continue, else (As stated in "while")


# Example 2 (nested loop)
list_a = [1, 3, 4, 5, 788, 9, 7, 98, 6, 13, 95]
list_b = [91, 2, 1, 3, 11, 7, 7, 98, 61, 93, 95]
for i in list_a:
    for j in list_b:
        if i == j:
            print(i)


# Example 3
for a, b, *c in [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]]:
    print(a)
    print(b)
    print(c)



# Example 4
for key in dictionary.keys():
    print(key)


for value in dictionary.values():
    print(value)


for key, value in dictionary.items():
    print(key, ":", value)