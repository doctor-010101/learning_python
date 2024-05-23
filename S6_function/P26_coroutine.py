def my_gen():
    print("start :)")
    while True:
        name = yield
        print("My name is ", name)


gen = my_gen()
next(gen)
next(gen)
gen.send("python")
