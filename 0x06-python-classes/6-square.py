#!/usr/bin/python3
"""create class"""


class Square():
    """define class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize class"""
        self.__size = size
        self.__position = position

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
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @size.setter
    def position(self, value):
        """set position"""
        if not(isinstance(value[0], tuple)) or not(isinstance(value[1], tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not(isinstance(value[0], int)) or not(isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculating area"""
        return self.__size * self.__size

    def my_print(self):
        """print square"""
        if self.__size != 0:
            aux = self.__position
            if aux[1] > 0:
                for x in range(aux[1]):
                     print()
            for x in range(0, self.__size):
                for i in range(aux[0]):
                    print(" ", end="")
                for y in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
