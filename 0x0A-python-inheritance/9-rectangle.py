#!/usr/bin/python3
"""Module defining Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Class Rectangle inherited from BaseGeomety"""

    def __init__(self, width, height):
        """Instantiation of width and height of Rectangle with pos ints"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
