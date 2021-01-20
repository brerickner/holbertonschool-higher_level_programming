#!/usr/bin/python3
"""Module defining Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Class Square inherited from Rectangle"""

    def __init__(self, size):
        """Instantiation of width and height of square with +ints"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that returns area of square"""
        return self.__size ** 2
