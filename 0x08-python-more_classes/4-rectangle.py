#!/usr/bin/python3
"""creating class"""


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
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate the area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width)

    def __str__(self):
        """print for str"""
        string = ""
        count = 0
        if self.__height == 0 or self.__width == 0:
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                string = string + "#"
            count = count + 1
            if count < self.__height:
                string = string + "\n"
        return string

    def __repr__(self):
        """edit repr output"""
        return f'Rectangle({self.__width}, {self.__height})'
