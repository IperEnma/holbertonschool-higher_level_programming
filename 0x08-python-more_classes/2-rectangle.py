#!/usr/bin/python3
"""creating rectangle class"""


class Rectangle:
    """define class"""

    def __init__(self, width=0, height=0):
        """initialize the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__widht

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("width must be >= 0")
        if value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
