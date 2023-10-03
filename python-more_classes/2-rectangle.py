#!/usr/bin/python3
"""
    This file contains a class representing a Rectangle with all it's atributes
    and methods.
"""


class Rectangle:

    """This class describes a Rectangle as well as all it's properties."""

    def __init__(self, width=0, height=0):
        """
            Method that initializes each instance of the class Rectangle, and
            __size is a private atribute. An error is risen if the size is not
            an integer or if it is less than 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
            Method that returns the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            Method that sets the size of the Rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
            Method that returns the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            Method that sets the height of the Rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """
            Method that returns the area of the Rectangle.
        """
        return self.__height * self.__width
    
    def perimeter(self):
        """
            Method that returns the perimeter of the Rectangle.
        """
        return self.__height * 2 + self.__width * 2
