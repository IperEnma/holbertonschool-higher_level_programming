#!/usr/bin/python3
"""create class"""


class Square:
    """define class"""
    def __init__(self, size=0):
        """initiaize class"""
        if (not(type(size) == int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """calculating area"""
        return self.__size * self.__size
