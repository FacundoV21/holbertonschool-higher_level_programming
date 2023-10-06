#!/usr/bin/python3
"""
    Defines a rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class wich inherits from Base Geometry
    """
    def __init__(self, width, height):
        """
            Initializes a Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
