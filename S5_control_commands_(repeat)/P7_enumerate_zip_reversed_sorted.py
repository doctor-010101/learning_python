# "enumerate()" function
# output : [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
print(list(enumerate(["a", "b", "c", "d"])))

first_list = ["a", "b", "c", "d"]
for i, h in enumerate(first_list, 3):
    print(i, ":", h)


# "zip()" function
name = ["Hassan", "Hossein", "Ali", "Zahra"]
age = [20, 10, 47, 19]
for a, b in zip(name, age):
    print("name :", a, "_", "age :", b)

print("\n")


# "reversed()" function
for z in reversed(name):
    print(z)

print("\n")


# "sorted()" function
for q in sorted(name):
    print(q)

print("\n")

for w in sorted(age):
    print(w)

print("\n\n")

for e in reversed(sorted(age)):
    print(e)

print("\n")

for r in reversed(sorted(name)):
    print(r)
