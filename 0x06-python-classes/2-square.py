#!/usr/bin/python3
"""A simple module that defines a class square"""


class Square:

    """Defines a square"""

    def __init__(self, size=0):
        """Initialize the square.
        Args:
            size(int): Private attribute for size of square.
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
