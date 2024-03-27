x = 10.5
y = 15
string = "Hello world"
print(f"x is {x}\ny is {y}\nz is {2*10}") # Before string wite f or F
print(F"x is {x}\ny is {y}\nz is {2*10}")
print(F"x is {x:.2f}\ny is {y}\nz is {2*10}")
print(f"{{x}} is {x}") # output => {x} is 10.5
print(f"{{x}} is {{{x}}}") # output => {x} is {10.5}
print(f"{{{{x}}}} is {{{{{x}}}}}") # output => {{{x}} is {{10.5} Continue in the same way to add {}
print(f"My string : {string.upper()}") # output => My string : HELLO WORLD


name = "he"
age = 23

message = (

    f"name is {name}\n"
    f"age is {age}"
)

print(message)


# Formatting is the same as the previous method.
