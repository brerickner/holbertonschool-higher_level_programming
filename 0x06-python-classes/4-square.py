#!/usr/bin/python3
"""A simple module that defines a class square"""


class Square:

    """Defines a square"""

    def __init__(self, size=0):
        """Initialize the square.
        Args:
            size(int): Private attribute for size of square.
        Return:
            None
        """

        self.__size = size

    @property
    def size(self):
        """Getter function to retrieve size attribute.
        Return:
            size of obj.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to validate size
        Args:
            value(int): int object
        """

        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance area method
            Args:
                self: object
            Return:
                current square area
        """
        return self.__size ** 2
