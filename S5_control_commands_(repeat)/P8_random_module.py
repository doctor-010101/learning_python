from random import random, seed

print(random())  # Generates a random number between zero and one [0,1)

print("\n")

"""

Seed or seed is an initial value used in random number generation algorithms.
This value serves as the starting point for generating a sequence of random numbers.
In Python, the seed() function is employed to set this seed, allowing the program to produce the same random sequence each time it's run, ensuring result reproducibility.
The use of seed in random number generation algorithms enables result reproducibility, which is particularly useful for experiments requiring consistency, such as scientific experiments or code testing.

"""
# Run once
seed(100)
print(random())  # output : 0.1456692551041303
print(random())  # output : 0.45492700451402135
print(random())  # output : 0.7707838056590222
print(random())  # output : 0.705513226934028
print(random())  # output : 0.7319589730332557

print("\n")

# Run for the second time
seed(100)
print(random())  # output : 0.1456692551041303
print(random())  # output : 0.45492700451402135
print(random())  # output : 0.7707838056590222
print(random())  # output : 0.705513226934028
print(random())  # output : 0.7319589730332557


print("\n")


# If the seed() input is empty, it selects the system time as input, and since the time changes every moment, the random numbers will not be repeated.
seed()
print(random())  # output : 0.9719809075126528
