#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = 0

if (number < 0):
    temp = number * -1
else:
    temp = number

if (temp % 10 > 5):
    print(f"Last digit of {number} is {temp % 10} and is greater than 5")

if (temp % 10 == 0):
    print(f"Last digit of {number} is {temp % 10} and is 0")

if (temp % 10 < 6):
    if (temp % 10 > 0):
        print(f"Last digit of {number} is {temp % 10} and is less than 6 and \
not 0")
