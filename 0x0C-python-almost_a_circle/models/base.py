#!/usr/bin/python3
"""This module contains the Base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to return JSON str representation of list_dictionaries.
            Args:
                list_dictionaries: list of dicts
            Return:
                "[]" if list_dictionaries is None or Empty.
                Else JSON representation of list_dictionaries
            """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
