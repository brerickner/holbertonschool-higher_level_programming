#!/usr/bin/python3
"""Module defining from_json_string method"""

import json


def from_json_string(my_str):
    """Method that gets an obj representation by a JSON string
        Args:
            my_str: str to represent as JSON object
        Returns:
            an obj(Python data stucture) repr by a JSON string
        """
    return json.loads(my_str)
    