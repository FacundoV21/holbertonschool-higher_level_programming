#!/usr/bin/python3
"""
    This file contains a class representing a square with all it's atributes
    and methods.
"""


class Square:

    """This class describes a square as well as all it's properties."""

    def __init__(self, size=0):
        """
            Method that initializes each instance of the class square, and
            __size is a private atribute. An error is risen if the size is not
            an integer or if it is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            Method that returns the area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
            Method that returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Method that sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        side = self.__size
        for i in range(0, side):
            for j in range(0, side):
                print("#", end="")
            print()
