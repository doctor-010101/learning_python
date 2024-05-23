# First Example 🍀👇
from time import perf_counter
from functools import wraps
passwords = {
    "ali": "1234",
    "hassan": "544254",
    "reza": "43435",
    "akin": "123734534",
    "sasan": "43733",
    "saed": "7367367",
    "mahdi": "7353543",
    "ana": "54164",
    "he ri": "213514654"
}

black_list = {
    "akin"
}


def ban(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args[0] in black_list:
            print("This user is blocked !!!")
        else:
            func(*args, **kwargs)
    return inner


@ban
def get_password(username):
    print(username, ":", passwords[username])


@ban
def change_password(username, new_password):
    passwords[username] = new_password
    print(username, ":", passwords[username])


get_password("akin")
change_password("ana", "1242")
get_password("ana")


# Second Example 🍀👇

def time_calculation(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("The run time of : ", func.__name__, "is:", run_time)
        return value
    return wrapper_decorator

@time_calculation
def A(y):
    s = 0
    for i in range(y):
        s += i**2


@time_calculation
def B(x):
    fact = 0
    for i in range(1, x + 1):
        fact *= i


A(10000000)
B(500000)