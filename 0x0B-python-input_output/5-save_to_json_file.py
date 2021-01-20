#!/usr/bin/python3
"""Module defining save_to_json_file method"""

import json


def save_to_json_file(my_obj, filename):
    """Method that writes an Object to a text file,
        using a JSON representation.
        Args:
            my_obj: obj to be written to text file
            filename: file to be written to
        """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
