#!/usr/bin/python3
"""Module defining to_json_string method"""

import json


def to_json_string(my_obj):
    """Method that gets JSON repr of an onj(string)
        Args:
            my_obj: object to get JSON representation of
        Returns:
            JSON representation of object
        """
    return json.dumps(my_obj)
