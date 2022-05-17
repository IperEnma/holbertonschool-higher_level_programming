#!/usr/bin/python3
"""create class"""


class Square:
    """define classs"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize class"""
        self.size = size
        self.position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position value"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            position = self.__position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for i in range(self.size):
                print(" " * position[0] + "#" * self.size)
