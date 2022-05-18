#!/usr/bin/python3
"""create class"""


class Rectangle:
    """define class"""

    number_of_instances = 0
    """counter"""

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the class"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """print rectangle"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            count = 0
            for x in range(self.__height):
                for y in range(self.__width):
                    string = string + str(self.print_symbol)
                count += 1
                if count < self.__height:
                    string = string + "\n"
        return string

    def __repr__(self):
        """print string representation"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """say goodbye"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger or equal"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
