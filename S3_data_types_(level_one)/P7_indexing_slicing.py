# --- indexing => Each character in a string is called an index or andis.
#
# --- Cannot change an index of a string
# 
# --- For positive numbering of string indexes, we start from the first character and numbering is done from zero.
my_string = "hi world"  # So h = 0, i = 1, space = 2, w = 3, o = 4, r = 5, l = 6, d = 7


# --- For negative numbering of string indexes, we start from the last character and numbering is done from -1.
my_string = "hi world"  # So h = -8, i = -7, space = -6, w = -5, o = -4,  = -3, l = -2, d = -1


# --- For get indexes of strings we use "[]".
print(my_string[1]) # output = i
print(my_string[-3]) # output = r
# print(my_string[10]) # IndexError: string index out of range


# --- We can use "[]" for slicing.
# The end point is not considered.
print(my_string[4:6]) # output = or
print(my_string[1:-4]) # output = i w
print(my_string[-7:-2]) # output = i wor
print(my_string[4:2]) # output = print is empty, because the end point must be after the start point not before it.
print(my_string[-1:2]) # output = print is empty, because the end point must be after the start point not before it.
print(my_string[-1:-5]) # output = print is empty, because the end point must be after the start point not before it.
print(my_string[5:]) # output = rld
print(my_string[:5]) # output = hi wo
print(my_string[:]) # output = hi world
print(my_string[:5] + my_string[5:]) # output = hi world


# --- We can specify the steps of slicing
print(my_string[0:5:2]) # output = h o (two by two)
print(my_string[0:5:10]) # output = h (because the steps are more than the string indexes, it prints until the end).
print(my_string[6:2:-1]) # output = lrow 
print(my_string[::-1]) # output = dlrow ih (Reverses the indexes of the string) 


# --- The len(string) function is used to get the number of characters in a string.
print(len(my_string)) # output = 8 
# print(my_string[len(my_string)]) # output = IndexError: string index out of range becouse : 👇
# (The length of the string is different from the number of its indexes. Length start form 1 but indexes numbering start from 0).

print(my_string[len(my_string) - 1]) # output = d

