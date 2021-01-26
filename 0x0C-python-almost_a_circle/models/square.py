#!/usr/bin/python3
"""This module contains the Square class inherited from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class inherited from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square with attrs size, x, y, id.
            Args:
                size = height * width
                x = x coordinates
                y = y coordinates
                id = new square id
            """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method to get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0 ")

        self.width = value
        self.height = value

    def __str__(self):
        """Method to override string representation of Square.
            Return:
                new string representation of Square
            """

        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Method to assign argument to each attribute"""
        if len(args) != 0:
            argList = ["id", "size", "x", "y"]

            for index, arg in enumerate(args):
                setattr(self, argList[index], args[index])

        else:
            for key, value in kwargs.items():
                if key is 'id' and value is None:
                    setattr(self, 'id', self.id)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method to return dictionary representation of Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
