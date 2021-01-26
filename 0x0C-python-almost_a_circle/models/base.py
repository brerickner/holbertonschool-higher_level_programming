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

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes JSON str repr of list_obj to a file"""
        filename = cls.__name__ + ".json"
        jString = ""
        with open(filename, "w", encoding="utf-8") as f:
            for obj in list_objs:
                if list_objs is None:
                    f.write("[]")
                else:
                    objDict = obj.to_dictionary()
                    jString += Base.to_json_string(objDict)
            f.write(jString)

    """
    NEED TO WRITE TESTS FOR SAVE TO FILE FIRST
    @staticmethod
    def from_json_string(json_string):
        """Method to return list of JSON string repr json_string"""
    """ 

                