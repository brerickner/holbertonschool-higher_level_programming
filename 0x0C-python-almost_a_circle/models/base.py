#!/usr/bin/python3
"""This module contains the Base class"""


class Base:

    """Base class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization with public instance attribute id.
            Args:
                id: assumed int
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
