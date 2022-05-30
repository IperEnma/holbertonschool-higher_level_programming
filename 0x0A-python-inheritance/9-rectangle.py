#!/usr/bin/python3
"""module class rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """define class"""

    def __init__(self, width, height):
        """initialize class"""
        Rectangle.integer_validator(self.__init__, "width", width)
        Rectangle.integer_validator(self.__init__, "height", height)
        self.width = width
        self.height = height

    def area(self):
        """calculate area rectangule"""
        return self.width * self.height

    def __str__(self):
        """print information"""
        return f"[Rectangle] {self.width}/{self.height}"
