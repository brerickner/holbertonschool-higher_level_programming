#!/usr/bin/python3
"""Module defining class Student"""

class Student():
    """Defining class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of first/last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Method that retrieves a dict repr of Student instance"""
        return self.__dict__