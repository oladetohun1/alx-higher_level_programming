#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    l_digit = number % 10
else:
    l_digit = ((number * -1) % 10) * -1  # last digit
if l_digit < 6 and l_digit != 0:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
else:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
