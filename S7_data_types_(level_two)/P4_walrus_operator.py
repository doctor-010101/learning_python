# walrus in loop
x = []
while (s := input("name (use q for quit): ").lower()) != "q":
    x.append(s)


print("names : ", x)
print("\n")

# walrus in condition
a = [1, 3, 4, 5, 6]
if (n := len(a)) > 3:
    print(n)
print("\n")


# walrus in functioin
def pow(a):
    print(a**2)


pow(z := 5)
print(z)
print("\n")


# example
b = [1, 3, 2, 4]
d = {
    "len": (l := len(b)),
    "sum": (s := sum(b)),
    "average": s / l
}

print(d)