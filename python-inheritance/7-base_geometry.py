#!/usr/bin/python3
"""
    add area  to class
"""


class BaseGeometry():
    """
        area assss
    """
    def area(self):
        raise Exception('area() is not implemented')

    """
        int validator addassssed
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
