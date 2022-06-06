#!/usr/bin/python3
"""module with class rectangle"""

from models.base import Base


class Rectangle(Base):
    """define class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """validators"""

    def validator_size(self, name, value):
        """validator size"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validator_position(self, name, value):
        """validator position"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    """ setters and getters"""

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width with validator"""
        self.validator_size("width", value)
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validator_size("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator_position("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator_position("y", value)
        self.__y = value

    """methods that do calculations"""

    def area(self):
        """calculate area rectangle"""
        return self.__width * self.__height

    """methods display"""

    def display(self):
        """display rectangle"""
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            for y in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """rewriting method __str__"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    """update"""

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if args and args is not None:
            for count in range(len(args)):
                if count == 0:
                    self.id = args[count]
                if count == 1:
                    self.width = args[count]
                if count == 2:
                    self.height = args[count]
                if count == 3:
                    self.x = args[count]
                if count == 4:
                    self.y = args[count]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
