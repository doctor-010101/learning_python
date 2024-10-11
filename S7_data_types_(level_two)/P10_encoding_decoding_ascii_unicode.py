### 1. Encoding
# Encoding is the process of converting text (characters) into a binary format for storage or transmission. In Python, this is typically done using the encode() method.

#### Example:
text = "Hello"
encoded_text = text.encode('utf-8')
print(encoded_text)

# In this example, the string "Hello" is converted to a binary format using UTF-8 encoding.

### 2. Decoding
# Decoding is the process of converting binary data back into the original text. In Python, this is typically done using the decode() method.

#### Example:

encoded_text = b'Hello'
decoded_text = encoded_text.decode('utf-8')
print(decoded_text)

# In this example, the binary data is decoded using UTF-8 encoding to convert it back into the original string "Hello".

### 3. Unicode
# Unicode is a universal standard for representing characters that can cover most characters from different languages. In Python, strings are Unicode by default.

#### Example:

text = "Hello, سلام, 你好"
for char in text:
    print(char, ord(char))

# In this example, we have a string containing characters from different languages. The ord() function shows the Unicode code point for each character.

### 4. ASCII
# ASCII is a character encoding standard for representing English characters and some special characters, covering Unicode code points from 0 to 127. Characters outside this range cannot be represented in ASCII.

#### Example:

text = "Hello"
ascii_encoded = text.encode('ascii')
print(ascii_encoded)

# Trying to encode non-ASCII characters will result in an error
non_ascii_text = "سلام"
try:
    non_ascii_encoded = non_ascii_text.encode('ascii')
except UnicodeEncodeError as e:
    print(f"Error: {e}")

# In this example, the string "Hello" is encoded to ASCII successfully. However, attempting to encode the string "سلام" using ASCII results in an error because its characters are outside the ASCII range.

### Summary
# - Encoding: Converting text to binary.
# - Decoding: Converting binary back to text.
# - Unicode: A universal standard for character representation.
# - ASCII: A standard for encoding English characters and some special characters.

# These concepts help ensure the proper storage and transmission of text, especially in multilingual applications.