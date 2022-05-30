#!/usr/bin/python3
"""module class"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """define class"""

    def __init__(self, size):
        """initialize class"""
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """print information"""
        return f"[Square] {self.__size}/{self.__size}"
