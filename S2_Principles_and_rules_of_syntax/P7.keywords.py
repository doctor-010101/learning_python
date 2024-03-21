# 1 => Keywords, also known as reserved words, are a type of predefined tokens in a programming language that have special meanings and purposes.
#
# 2 => The number of keywords in Python is 35.
#
# The following commands are used to get keywords 👇

help("keywords")  # First Way

import keyword

print(keyword.kwlist)  # Second Way
print(
    keyword.iskeyword("word")
)  # This command is used to know whether a word is a keyword or not
