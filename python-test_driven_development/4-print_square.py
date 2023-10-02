#!/usr/bin/python3
"""
    Say my name function, wich print the first and second name passed

"""


def print_square(size):
    """Prints a square"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
