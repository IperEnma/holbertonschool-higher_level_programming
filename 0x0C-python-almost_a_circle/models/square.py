#!/usr/bin/python3
"""module with class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """define class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize class Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """rewriting method __str__"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """get size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update class square"""
        if args and args is not None:
            for count in range(len(args)):
                if count == 0:
                    self.id = args[count]
                if count == 1:
                    self.size = args[count]
                if count == 2:
                    self.x = args[count]
                if count == 3:
                    self.y = args[count]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
