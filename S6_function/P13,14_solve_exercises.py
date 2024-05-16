# 🍀 1 🍀
# def len_(it):
#     counter = 0
#     for _ in it:
#         counter += 1
#     return counter


# str = "python"
# l = [1, 3, 4, 5, 6]
# t = ("a", "b", "c")

# print(len_(str))
# print(len_(l))
# print(len_(t))


# 🍀 2 🍀
# def max_(*args):
#     m = float("-inf")
#     for i in args:
#         if i > m:
#             m = i
#     return m


# print(max_(10, 20, 65, 23, 10, -1))


# 🍀 3 🍀
# def sum_(it):
#     s = 0
#     for i in it:
#         s += i
#     return s


# print(sum_((10, 12, 11)))


# 🍀 4 🍀
# def square(n):
#     for i in range(1, n):
#         if i ** 2 == n:
#             print(f"Yes! {i} * {i} = {n}")
#             break
#     else:
#         print("No!")


# x = int(input("x: "))
# square(x)


# 🍀 5 🍀
# def discount(rate, price):
#     discount_rate = int(price * rate / 100)
#     new_price = price - discount_rate
#     print("discount_rate :", discount_rate)
#     print("new-price :", new_price)


# rate = int(input("rate: "))
# price = int(input("price: "))
# discount(rate, price)


# 🍀 6 🍀
def func(character):
    if 48 <= ord(character) <= 57:
        print("The character is number!")
    elif 65 <= ord(character) <= 90:
        print("The character is  uppercase letter!")
    elif 97 <= ord(character) <= 122:
        print("The character is lowercase letter!")
    else:
        print("Other!")


character = input("Enter a character : ")
func(character)
