#!/usr/bin/python3
def print_last_digit(number):
    digit = 0
    if (number < 0):
        number = number * -1

    digit = number % 10
    print("{}".format(digit), end="")
    return digit
