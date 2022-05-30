#!/usr/bin/python3
"""module class rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """define class"""

    def __init__(self, width, height):
        """initialize class"""
        Rectangle.integer_validator(self.__init__, "width", width)
        self.width = width
        Rectangle.integer_validator(self.__init__, "height", height)
        self.height = height

    def area(self):
        """calculate area rectangule"""
        return self.height * self.width

    def __str__(self):
        """print information"""
        return "[Rectangle] " + str(self.width) + "/" + str(self.height)
