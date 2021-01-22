#!/usr/bin/python3
"""This module contains the Rectangle class inherited from Base"""

Base = __import__('base').Base

class Rectangle(Base):
    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes rectangle with attrs width, height, x, y, id.
            Args:
                width: width of rectangle
                height: height of rectangle
                x = x coordinates
                y = y coordinates
                id = new rectangle id
            """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle.
            Args:
                value: int value assigned to width.
            """
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle
            Args:
                value: int value assigned to height.
            """
        self.__height = value

    @property
    def x(self):
        """Get x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate of Rectangle
            Args:
                value: int value assigned to x.
            """
        self.__x = value
    
    @property
    def y(self):
        """Get y coordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y coordinate of Rectangle
            Args:
                value: int value to assign to y
            """
        self.__y = value