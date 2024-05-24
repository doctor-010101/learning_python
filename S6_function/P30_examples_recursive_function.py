# Example One "Timer" 😊💪

from time import sleep


def reverse(n):
    if n <= 0:
        return None
    sleep(1)
    print(n)
    n -= 1
    reverse(n)


# reverse(20)


# Example Two 😊💪

def mul5(n):
    if n == 0:
        return 1
    elif n % 10 < 5:
        return mul5(n // 10)
    else:
        return n % 10 * mul5(n // 10)


# print(mul5(5249))


# Example Three 😊💪

def func(n):
    if n < 3:
        return
    elif n % 3 == 0:
        print(n)
    func(n-1)


# func(10)

# Example Four 😊💪

def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)


# print(fib(6))