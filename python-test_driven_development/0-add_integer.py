#!/usr/bin/python3
"""
    Add function, which adds two integers, the tests for this function are
    located on the tests folder
"""


def add_integer(a, b=98):
    """
        Returns the addition of two numbers if they are ints or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
