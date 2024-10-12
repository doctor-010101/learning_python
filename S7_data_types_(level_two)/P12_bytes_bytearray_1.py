# bytes Data Type

# The b/ytes data type is immutable, which means that once a bytes object is created, its content cannot be changed. This type is useful for representing binary data, such as the content of binary files.

# Creating a bytes Object

# You can create a bytes object in several ways:

# 1. From a string:

b = bytes("Hello, World!", "utf-8")
print(b)  # Output: b'Hello, World!'


# 2. From a list or tuple of integers:

b = bytes([72, 101, 108, 108, 111])
print(b)  # Output: b'Hello'


# bytes Methods

# Some important methods for bytes objects include:

# - decode(encoding='utf-8', errors='strict'): XThis method is used to convert the bytes object into a string using the specified encoding.

b = bytes("Hello, World!", "utf-8")
s = b.decode("utf-8")
print(s)  # Output: Hello, World!


# - split(separator=None, maxsplit=-1): This method is used to split the bytes object into a list of bytes objects based on a specified separator.

b = bytes("Hello, World! How are you?", "utf-8")
parts = b.split(b' ')
print(parts)  # Output: [b'Hello,', b'World!', b'How', b'are', b'you?']


# bytearray Data Type

# The bytearray data type is mutable, which means that you can change its content after creation. This type is also used for representing binary data.

# Creating a bytearray Object

# You can create a bytearray object in several ways:

# 1. From a string:


ba = bytearray("Hello, World!", "utf-8")
print(ba)  # Output: bytearray(b'Hello, World!')


# 2. From a list or tuple of integers:


ba = bytearray([72, 101, 108, 108, 111])
print(ba)  # Output: bytearray(b'Hello')


# bytearray Methods

# Some important methods for bytearray objects include:

# - append(item): This method appends an item to the end of the bytearray.

ba = bytearray([72, 101, 108, 108, 111])
ba.append(33)
print(ba)  # Output: bytearray(b'Hello!')


# - extend(iterable): This method extends the bytearray by appending elements from an iterable(like a list or tuple).


ba = bytearray([72, 101, 108, 108, 111])
ba.extend([32, 87, 111, 114, 108, 100])
print(ba)  # Output: bytearray(b'Hello World')


# - insert(index, item): This method inserts an item at the specified position.

ba = bytearray([72, 101, 108, 108, 111])
ba.insert(5, 32)  # Adding a space after Hello
print(ba)  # Output: bytearray(b'Hello ')


# - pop(index=-1): This method removes and returns an item at the specified position.


ba = bytearray([72, 101, 108, 108, 111, 33])
item = ba.pop()
print(ba)   # Output: bytearray(b'Hello')
print(item)  # Output: 33


# - remove(item): This method removes the first occurrence of the item.


ba = bytearray([72, 101, 108, 108, 111, 33])
ba.remove(108)  # Removing the first 108
print(ba)  # Output: bytearray(b'Helo!')
