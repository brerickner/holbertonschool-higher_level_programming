#!/usr/bin/python3
"""Module that adds and saves Python list to file"""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

addToFile = "add_item.json"
if path.exists(addToFile):
    pythonList = load_from_json_file(addToFile)
else:
    pythonList = []

args = sys.argv[1:]
pythonList.extend(args)

save_to_json_file(pythonList, 'add_item.json')
