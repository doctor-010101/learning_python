# --- 1 --- Tuples and lists are very similar.
#
# --- 2 --- Tuples are immutable.
#
# --- 3 --- Indexing and slicing in tuples like lists.


tuple1 = (1, 2, 3, ["a", "b"], ("aa", "bb"), "python", 4, 5)
tuple2 = 1, 2, 3, ["a", "b"], ("aa", "bb"), "python", 4, 5
print(tuple1, "\n", type(tuple), sep="")
print(tuple2, "\n", type(tuple2), sep="")


# Tuples in the list must be enclosed in parentheses
list = [1, 2, 3, ("a", "b")]


# The lists inside the tuple can be changed
tuple1[3][1] = "c"
print(tuple1, "\n", type(tuple), sep="")


# tuple or int
int = (1)  # int
int = (1,)  # tuple


# tuple()
tuple3 = tuple("python")
print(tuple3)  # output : ('p', 'y', 't', 'h', 'o', 'n')
