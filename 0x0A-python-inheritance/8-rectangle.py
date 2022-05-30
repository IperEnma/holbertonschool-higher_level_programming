#!/usr/bin/python3
"""class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define class Rectangle"""

    def __init__(self, width, height):
        """initialize class"""
        Rectangle.integer_validator(self.__init__, "width", width)
        Rectangle.integer_validator(self.__init__, "height", height)
        self.__width = width
        self.__height = height
