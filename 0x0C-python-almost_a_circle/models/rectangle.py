#!/usr/bin/python3
"""This module contains the Rectangle class inherited from Base"""

from models.base import Base


class Rectangle(Base):

    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes rectangle with attrs width, height, x, y, id.
            Args:
                width: width of rectangle
                height: height of rectangle
                x = x coordinates
                y = y coordinates
                id = new rectangle id
            """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle.
            Args:
                value: int value assigned to width.
            """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0 ")

        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle
            Args:
                value: int value assigned to height.
            """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0 ")
        self.__height = value

    @property
    def x(self):
        """Get x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate of Rectangle
            Args:
                value: int value assigned to x.
            """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y coordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y coordinate of Rectangle
            Args:
                value: int value to assign to y
            """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method that gives area of Rectangle.
            Return:
                area of Rectangle
            """
        return self.__width * self.__height

    def display(self):
        """Method to print Rectangle to stdout in # chars"""
        for down in range(self.y):
            print("")
        for rows in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """Method to override string representation of Rectangle.
            Return:
                new string representation of Rectangle
            """

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width,
                    self.height)

    def update(self, *args, **kwargs):
        """Method to assign argument to each attribute"""

        if len(args) != 0:
            argList = ["id", "width", "height", "x", "y"]

            for index, arg in enumerate(args):
                setattr(self, argList[index], args[index])

        else:
            for key, value in kwargs.items():
                if key is 'id' and value is None:
                    setattr(self, 'id', self.id)
                else:
                    setattr(self, key, value)
    
    def to_dictionary(self):
        """Method to return the dict repr of Rectangle"""
        return self.__dict__
