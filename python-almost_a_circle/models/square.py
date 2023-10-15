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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Getter size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
            Setter size
        """
        self.__width = size
        self.__height = size

    def __str__(self):
        """
            Returns data related to the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
            updates the values of the square
        """
        if args and len(args) > 0:
            atr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atr[i], arg)

        else:
            for j, arg in kwargs.items():
                setattr(self, j, arg)
