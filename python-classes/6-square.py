#!/usr/bin/python3
"""
    This file contains a class representing a square with all it's atributes
    and methods.
"""


class Square:

    """This class describes a square as well as all it's properties."""

    def __init__(self, size=0, position=(0, 0)):
        """
            Method that initializes each instance of the class square, and
            __size and __psoition are private atributes. An error is risen
            if the size is not an integer or if it is less than 0, the same
            with each field of the position.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for i in position:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 positive\
 integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for i in value:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 positive\
 integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        side = self.__size
        for lj in range(0, self.position[1]):
            print()
        for i in range(0, side):
            for s in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, side):
                print("#", end="")
            print()
