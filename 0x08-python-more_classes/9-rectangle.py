#!/usr/bin/python3
"""Simple class defining a rectangle"""


class Rectangle:

    """Defining a class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height of rectangle.
        Args:
            width(int): Private attribute for width of rectangle.
            height(int): Private attribute for height of rectangle.
        Return:
            None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return 0

        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Method to print string of a rectangle."""
        printStr = ""
        printOcto = str(self.print_symbol) * self.__width
        printNL = "\n"
        if self.__height is 0 or self.__width is 0:
            return printStr
        for i in range(self.__height - 1):
            printStr += printOcto + printNL
        printStr += printOcto
        return printStr

    def __repr__(self):
        """String representation of rectangle"""
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """Method that prints message when rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        rects = [str(rect_1.area()), str(rect_2.area())]
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return square as rectangle"""
        return Rectangle(size, size)
