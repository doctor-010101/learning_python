# In Python, iterators and iterables are essential components of the iteration protocol, which allows you to traverse items in a collection (like lists, tuples, and dictionaries).

# An iterable is an object that implements the iter() method, which returns an iterator.

# An iterator is an object that implements two methods: iter() (which returns the iterator object itself) and next() (which returns the next value from the collection or raises StopIteration when there are no more items).


# Creating an Iterable and an Iterator

# Let’s create a custom iterable and its corresponding iterator. We’ll design an iterable class MyRange that mimics Python's built-in range() function, allowing iteration over a sequence of numbers.

# Step 1: Create the Iterator Class

# First, we’ll create an iterator class that handles the logic of iteration.

# class MyRangeIterator:
#     def init(self, start, stop):
#         self.current = start
#         self.stop = stop

#     def iter(self):
#         return self  # The iterator object itself

#     def next(self):
#         if self.current >= self.stop:
#             raise StopIteration  # Signal that there are no more items
#         else:
#             current_value = self.current
#             self.current += 1  # Move to the next value
#             return current_value

# Step 2: Create the Iterable Class

# Next, we’ll create the iterable class that uses the iterator.

# class MyRange:
#     def init(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def iter(self):
#         return MyRangeIterator(self.start, self.stop)  # Return an instance of the iterator

# Step 3: Using the Custom Iterable

# Now that we have our MyRange class, we can use it in a for loop or convert it to a list to see the results.

# # Create an instance of MyRange
# my_range = MyRange(1, 5)

# # Using the custom iterable in a for loop
# for num in my_range:
#     print(num)  # Output: 1, 2, 3, 4

# # Convert to a list
# numbers = list(my_range)
# print(numbers)  # Output: [1, 2, 3, 4]

# Explanation of the Example

# 1. Iterator Class (MyRangeIterator):

# The init method initializes the current value and the stopping condition.

# The iter method returns the iterator object itself.

# The next method checks if the current value is less than the stop value. If it is, it returns the current value and increments it. If not, it raises StopIteration.



# 2. Iterable Class (MyRange):

# The init method initializes the start and stop values.

# The iter method returns a new instance of MyRangeIterator, allowing iteration over the specified range.



# 3. Usage:

# When we create an instance of MyRange and use it in a for loop, Python calls the iter method of MyRange, which returns an iterator. Then, it repeatedly calls next on the iterator to get values until StopIteration is raised.




# Summary

# An iterable is an object that can return an iterator. It implements the iter() method.

# An iterator is an object that keeps track of the current state of iteration. It implements the iter() and next() methods.

# By creating your own iterable and iterator classes, you can control how objects are iterated in your Python programs.


# This approach is very powerful and can be used to create complex data structures that can still be iterated over using Python's familiar for-loop syntax.
