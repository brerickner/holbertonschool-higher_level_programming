#!/usr/bin/python3
"""Module defining class Student"""


class Student():

    """Defining class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of first/last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dict repr of Student instance
            Args:
                attrs: attributes
            """
        if isinstance(attrs, list) is False:
            return self.__dict__

        if all(isinstance(stuff, str) for stuff in attrs) is False:
                
            print("stuff string")
            print(self.__dict__[stuff])
            return self.__dict__
               
            