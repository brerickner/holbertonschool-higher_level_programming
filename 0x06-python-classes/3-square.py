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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """Public instance area method
        Args:
            self: object
        Return: 
            square area
        """
        return self.__size ** 2