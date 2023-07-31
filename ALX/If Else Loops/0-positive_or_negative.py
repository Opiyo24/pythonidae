#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE

def num_sign(x):
    if x < 0:
        print(f"{x} is negative")
    elif x > 0:
        print(f"{x} is positive")
    else:
        print(f"{x} is zero")

num_sign(number)