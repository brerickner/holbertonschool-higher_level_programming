#!/usr/bin/python3
"""Module defining load_from_json_file method"""

import json


def load_from_json_file(filename):
    """Method that creates obj from a "JSON file"
        Args:
            filename: file to load
        """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
