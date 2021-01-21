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
        copyDict = {}
        '''covers list not of type list or None'''
        if isinstance(attrs, list) is False:
            return self.__dict__
        '''checks if attrs listed are all strings'''
        if all(isinstance(attrSearch, str) for attrSearch in attrs) is True:
            '''if string in attrs is also an attribute name retrieve it'''
            for attName in attrs:
                if attName in self.__dict__:
                    copyDict[attName] = self.__dict__[attName]
            return copyDict

        '''else retrieve all attributes'''
        return self.__dict__
