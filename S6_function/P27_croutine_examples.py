def cen_gen(words):
    print("start :)")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * len(word)


generator = cen_gen(["cow", "bear"])
next(generator)
print(generator.send("python"))
print(generator.send("cow"))
print(generator.send("js"))


print("\n")



def split_gen(delimiter=" "):
    print("start")
    s = None
    while True:
        line = yield s
        s = line.split(delimiter)

g = split_gen("-")
next(g)
print(g.send("ali-hassan-reza-heydar"))