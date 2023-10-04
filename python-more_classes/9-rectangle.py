#!/usr/bin/python3
"""
    This file contains a class representing a Rectangle with all it's atributes
    and methods.
"""


class Rectangle:

    """This class describes a Rectangle as well as all it's properties."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Method that initializes each instance of the class Rectangle, and
            __size is a private atribute. An error is risen if the size is not
            an integer or if it is less than 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        n_str = ""
        if self.__height == 0 or self.__width == 0:
            return n_str

        for i in range(self.__height):
            for j in range(self.__width):
                n_str += str(f"{self.print_symbol}")
            n_str = n_str + '\n'
        n_str = n_str[:-1]
        return n_str

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
