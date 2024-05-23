# 1 Enumerate 🍀👇

def my_enumerate(secuence, start=0):
    c = start
    for i in secuence:
        yield c, i
        c += 1


list_ = ["ali", "hassan", "zahra"]
for i, j in my_enumerate(list_):
    print(i, j)


print("\n")


# 2 Fibonacci 🍀👇

def fibonacci():
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    while True:
        f3 = f2 + f1
        yield f3
        f1 = f2
        f2 = f3


fib = fibonacci()
for _ in range(50):
    print(next(fib))




# 3 Sum 🍀👇

def sum_generator(lst):
    s = 0
    for i in lst:
        s += i
        yield s


sg = sum_generator([1, 2, 3, 4])
for i in sg:
    print(i)


print("\n")



# 4 Sum 🍀👇

def rev_str(s):
    l = len(s)
    for i in range(l - 1, -1, -1):
        yield s[i]


rg = rev_str("python")
for ch in rg:
    print(ch)



print("\n")


# 5 Even or Odd 🍀👇

def my_gen(eve_or_odd="e"):
    c = 0
    if eve_or_odd == "o":
        c = 1
    while True:
        yield c
        c += 2

eo = my_gen("e")
for _ in range(10):
    print(next(eo))


print("\n")


#  6 🍀👇

def num_gen():
    c = 1
    while True:
        s = ""
        for i in range(1, c+1):
            s += f"{c}\t"
        yield s
        c += 1


n = num_gen()
for i in range(15):
    print(next(n))