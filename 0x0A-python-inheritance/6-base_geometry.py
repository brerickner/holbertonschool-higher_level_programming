#!/usr/bin/python3
"""Module defining BaseGeometry class"""


class BaseGeometry:

    """Defines class BaseGeometry"""

    def area(self):
        """Method to raise Eception when area() not implemented"""
        raise Exception("area() is not implemented")
