#!/usr/bin/python3
"""This module contains the Base class"""

import json
from os import path


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
        jList = []
        with open(filename, "w", encoding="utf-8") as f:
            for obj in list_objs:
                if list_objs is None:
                    f.write("[]")
                else:
                    jList.append(obj.to_dictionary())
            jString = Base.to_json_string(jList)
            f.write(jString)

    @staticmethod
    def from_json_string(json_string):
        """Method to return list of JSON string repr json_string.
            Returns:
                Empty list when json_string is none.
                Else list represented by json_string
            """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method to return an instance with all attributes already set
            Return:
                instance with all attributes set already
            """
        if cls.__name__ == "Square":
            dummy = cls(6)
        if cls.__name__ == "Rectangle":
            dummy = cls(6, 6)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method to return a list of instances.
            Return:
                An empty list if file doesn't exist. Else list of instances
            """
        filename = cls.__name__ + ".json"
        instList = []

        if path.exists(filename) is False:
            return instList
        if path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                fromFile = f.read()
            dictList = cls.from_json_string(fromFile)
            for dict in dictList:
                instList.append(cls.create(**dict))
        return instList
