#!/usr/bin/python3
"""
    add area imp to class
"""


class BaseGeometry():
    """
        area added
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
