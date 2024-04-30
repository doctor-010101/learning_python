# 1 -> "Normal" Syntax


def func(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)


func(1, 4, 5)


# -> "Default Value" Syntax


def func(a=10, b=11, c=12):
    print("a =", a)
    print("b =", b)
    print("c =", c)


func()
func(1, 4)
func(b=50)
func(1, 4, 5)


# "Normal and Default Value" Syntax


def func(a, b=11, c=12):
    print("a =", a)
    print("b =", b)
    print("c =", c)


func(10)


# "*name" Syntax


def func(a, b, *c, d):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)


func(10, 11, 12, 13, ["a", "b", "c"], 14, 15, d=16)


# "**name" Syntax


def func(a, b, *c, **d):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)


func(10, 11, 12, 13, ["a", "b", "c"], 14, 15, d=16, e=17)
