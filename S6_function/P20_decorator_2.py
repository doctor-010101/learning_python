import functools



def plus(func):
    @functools.wraps(func)
    def inner(*x, **y):
        print("+" * 20)
        func(*x, **y)
        print("+" * 20)
    return inner


def exclamation(func):
    @functools.wraps(func)
    def inner(*x, **y):
        print("!" * 20)
        func(*x, **y)
        print("!" * 20)
    return inner


@plus
@exclamation
def message(msg):
    print("I love", msg)


message("py")


# The decorator formula
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
