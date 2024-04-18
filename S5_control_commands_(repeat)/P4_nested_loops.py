# Example 1
# first loop 👇
i = 1
while i <= 10:
    # second loop 👇
    a = 1
    while a <= 10:
        print("\t", a)
        a += 1
    print(i)
    i += 1


# Example 2
list = input("name : ").split("-")
i = 0
while i < len(list):
    word = list[i]
    a = 0
    while a < len(word):
        if a % 2 == 0:
            print(word[a].upper(), end="")
        else:
            print(word[a], end="")
        a += 1
    print()
    i += 1


# Example 3
i = 1
while i <= 10:
    b = 1
    while b <= 10:
        print(i * b, end="\t")
        b += 1
    print()
    i += 1


# Example 4
i = 1
while i <= 5:
    j = 0
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
