#!/usr/bin/python3

"""
    This module declarates the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
        Declaration of the Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Init of the Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            Setter width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
            Getter height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            Setter height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
            Getter x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            Setter x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
            Getter y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            Setter y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
