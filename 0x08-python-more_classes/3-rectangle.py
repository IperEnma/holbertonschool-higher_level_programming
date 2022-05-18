#!/usr/bin/python3
"""creating rectangle class"""


class Rectangle:
    """define class"""

    def __init__(self, width=0, height=0):
        """initialize the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        string = ""
        count = 0
        if self.__height == 0 or self.__width == 0:
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                string = string + "#"
            count = count + 1
            if (count < self.__height):
                string = string + "\n"
        return string
