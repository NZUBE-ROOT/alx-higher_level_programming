#!/usr/bin/python3
"""Defines a rectangle class that inherits from base."""
from models.base import Base


class Rectangle(Base):
    """Subclass Rectangle inheriting from Class Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of class rectangle.
        Args:
            1. width: Width of the rectangle.
            2. height: Height of the rectangle.
            3. x: x coordinate of the rectangle.
            4. y: y coordinate of the rectangle.
            5. id: id of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Gets the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle."""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Gets the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle."""
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Gets x coordinate of the rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets x coordinate of the rectangle."""
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Gets y coordinate of the rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets y coordinate of the rectangle."""
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Assigns an argument to atributes id, width, height, x and y."""
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """String rep of the rectangle object."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
