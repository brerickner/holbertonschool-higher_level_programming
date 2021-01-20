#!/usr/bin/python3
"""Module defining Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Class Rectangle inherited from BaseGeomety"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
