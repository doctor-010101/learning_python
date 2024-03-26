x = 1
y = 1.123456789
print("x is : {}\ny is : {}\nz is : {}".format(x, y, 1 + 1))

print(
    "x is : {0}\ny is : {1}\nz is : {2}".format(x, y, 1 + 1)
)  # Numbering start from zero.
print(
    "x is : {1}\ny is : {0}\nz is : {2}".format(x, y, 1 + 1)
)  # There is nothing wrong with writing out of order
print(
    "x is : {0}\ny is : {0}\nz is : {0}".format(x, y, 1 + 1)
)  # There is nothing wrong with repetitive writing.


dic = {"x": 1, "y": 2, "z": 3}
print("x is : {x}\ny is : {y}\nz is : {z}".format(**dic))
print("x is : {z}\ny is : {x}\nz is : {y}".format(**dic))
print("x is : {z}\ny is : {z}\nz is : {z}".format(**dic))
print(
    "x is : {x}\ny is : {y}\nz is : {z}".format(x=dic["x"], y=dic["y"], z=dic["z"])
)  # We can write like this but it is not recommended
print("x is : {2}\ny is : {0}\nz is : {1}".format(*"abc"))
print("x is : {2}\ny is : {0}\nz is : {1}".format(*[5, 6, 7]))


print("x is : {}\ny is : {}\nz is : {}".format(*[5, 6, 7]))  # Field name is optional.
print("x is : {0!s}".format("python"))  # output => x is : python
print("x is : {0!r}".format("python"))  # output => x is : 'python'
print("x is : {0!a}".format("ƃ"))  # output => x is : '\u0183' (unicode)
print("x is : {0!a}".format("þ"))  # output => x is : '\xfe'
print("x is : {0!a}".format("+ƃ"))  # output => x is : '+\u0183'
print("x is : {0!s}".format("+ƃ"))  # output => x is : +ƃ


print("x is : {0:.5}".format(1.123456789))  # output => x is : 1.1235 (rounded) (decimal)
print("x is : {0:f}".format(1.123456789))  # output => x is : 1.123457 (type)
print("x is : {0:%}".format(1/3))  # output => x is : 33.333333%
print("x is : {0:.2%}".format(1/3))  # output => x is : 33.33%
print("x is : {0:_.2f}".format(1000000))  # output => x is : 1_000_000.00 (grouping optional)
print("x is : {0:15_.2f}".format(1000000))  # output => x is :    1_000_000.00 (width)
print("x is : {0:015_.2f}".format(1000000))  # output => x is : 0_001_000_000.00
print("x is : {0:b}".format(313))  # output => x is : 100111001 (binary)
print("x is : {0:o}".format(313))  # output => x is : 471 (octal)
print("x is : {0:#b}".format(313))  # output => x is : 0b100111001 (binary)
print("x is : {0:#o}".format(313))  # output => x is : 0o471 (octal)
print("x is : {0:#o}".format(313))  # output => x is : 0o471 (octal)

# There are many examples of this topic, for the sake of this article, it is avoided to give too many examples, those who are interested can refer to the following address for read.
# link => https://docs.python.org/3/library/string.html#format-string-syntax
