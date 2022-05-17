#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        if (not(type(value[0]) is int and type(value[1]) is int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size

    def my_print(self):
        if self.__size != 0:
            for x in range(0, self.__position[1]):
                print()
            for x in range(0, self.__size):
                for i in range(0, self.__position[0]):
                    print(" ", end="")
                for y in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
