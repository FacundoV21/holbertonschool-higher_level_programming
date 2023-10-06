#!/usr/bin/python3
"""
    add area implementation to class
"""


class BaseGeometry():
    """
        area added
    """
    def area(self):
        raise Exception('area() is not implemented')

    """
        int validator added
    """
    def integer_validator(self, name, value):
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
