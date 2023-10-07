#!/usr/bin/python3
"""
    Defines a square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """
            Class wich inherits Rectangle
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
