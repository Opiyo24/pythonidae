#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
def last_dig(x):
    string_num = str(x)
    last_digit = len(string_num) - 1

    return (string_num[last_digit])

last_digit = int(last_dig(number))

if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")