#!/usr/bin/python3
"""
    This file contains a class representing a square with all it's atributes
    and methods.
"""


class Square:

    """This class describes a square as well as all it's properties."""

    def __init__(self, size):
        """
            Method that initializes each instance of the class square, and
            __size is a private atribute. An error is risen if the size is not
            an integer or if it is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
