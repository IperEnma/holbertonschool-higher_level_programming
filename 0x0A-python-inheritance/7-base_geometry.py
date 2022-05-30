#!/usr/bin/python3
"""module BaseGeometry"""


class BaseGeometry:
    """class basegeometry"""

    def area(self):
        """instance in building"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
