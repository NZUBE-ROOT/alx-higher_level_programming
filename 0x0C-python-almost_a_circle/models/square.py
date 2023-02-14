#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A sub class square that inherits from the class rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the class square.
        Args:
            1. size: The length of the square.
            2. x: x coordinate.
            3. y: y coordinate.
            4. id: id of the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes.
        Attributes:
           *args: Non key-word arguments
                1. id: id
                2. size: size
                3. x: x coordinate
                4. y: y coordinate
            *kwargs: Key-word arguments
        """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(id)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Str rep of a square obj."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)
