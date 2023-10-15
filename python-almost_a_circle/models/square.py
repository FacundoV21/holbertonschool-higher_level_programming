#!/usr/bin/python3

"""
    This module declarates the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Declaration of the Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Init of the Square class
        """
        super().__init__(id)
        self.size
        self.x = x
        self.y = y

    @property
    def size(self):
        """
            Getter size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
            Setter size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.__size = size

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

    def area(self):
        """
            function to retrieve the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
            function to print the rectangle
        """
        for i in range(0, self.__y):
            print()
        for j in range(0, self.__size):
            for k in range(0, self.__x):
                print(" ", end="")
            for ln in range(0, self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """
            Returns data related to the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.__size}"

    def update(self, *args, **kwargs):
        """
            updates the values of the rectangle
        """
        if args and len(args) > 0:
            atr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atr[i], arg)

        else:
            for j, arg in kwargs.items():
                setattr(self, j, arg)
