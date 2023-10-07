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

    def area(self):
        """
            returns the area of square
        """
        return (self.__size * self.__size)
