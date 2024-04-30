# After the "*" indicator, the parameters are written as "Key value".


def func(a, *, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)


func(10, b=16, c=17)


# Parameters before "/" are written positionally.


def func(a, b, /, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)


func(10, 16, c=17)


# Composition


def func(a, b, /, c, d, *, e, f):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("e =", e)
    print("f =", f)


func(10, 16, 17, d=20, e=30, f=40)
