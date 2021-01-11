#!/usr/bin/python3
"""Simple class defining a rectangle"""


class Rectangle:

    """Defining a class rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height of rectangle.
        Args:
            width(int): Private attribute for width of square.
            height(int): Private attribute for height of square.
        Return:
            None
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter to retrieve width of rectangle.
        Return:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to retrieve width of rectangle.
        Args:
            value(int): int object.
        """
        if isinstance(value, int) and value >= 0:
            self.__width = value

        elif isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter to retrieve height of rectangle.
        Return:
            self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to retrieve height of rectangle.
        Args:
            value(int): int object.
        """
        if isinstance(value, int) and value >= 0:
            self.__height = value

        elif isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
