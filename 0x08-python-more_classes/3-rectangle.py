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
        self.width = width
        self.height = height

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
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """Method to get area of rectangle.
        Return:
            area of rectangle
            """
        return self.__height * self.__width

    def perimeter(self):
        """Method to get perimeter of rectangle.
        Return:
            perimeter of rectangle, 0 when width or height 0
            """
        if self.__height is 0 or self.__width is 0:
            print("")
            return 0
        
       # copy = self.__perimeter[:]

        for i in range(self.__height):
            print("{}".format("#" * self.__width))
       # print("{}".format("#" * self.__width), end="")

            
        return ((self.__height * 2) + (self.__width * 2))
"""
        if self.__height is 0 or self.__width is 0:
            print("")
        for i in range(self.__width):
            print("{}".format("#" * self.__width))
            """