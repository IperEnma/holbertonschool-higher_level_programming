#!/usr/bin/python3
"""crate square"""


class Square():
    """define class"""
    def __init__(self, size=0):
        """initialize class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculating area"""
        return self.__size * self.__size

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
