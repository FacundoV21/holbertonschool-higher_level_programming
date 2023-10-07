#!/usr/bin/python3
"""
    Defines a square
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """
            Class wich inherits from Rectangle
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
