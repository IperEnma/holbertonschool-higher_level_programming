#!/usr/bin/python3
"""creating class"""


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
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print square"""
        if (self.__size == 0):
            print()
            return
        for i in range(0, self.__size):
            for c in range(0, self.__size):
                print("#", end="")
            print()
