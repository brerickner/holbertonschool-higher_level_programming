#!/usr/bin/python3
"""Module defining class Student"""


def append_after(filename="", search_string="", new_string=""):
    """Method that inserts a line of txt after spec string"""
    with open(filename, encoding="utf-8") as f:
        text = []
        lineRead = f.readlines()
        if search_string in lineRead:
            text.append(new_string)

        for lineRead in text:
            f.write(lineRead)
