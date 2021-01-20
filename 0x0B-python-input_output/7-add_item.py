#!/usr/bin/python3
"""Module that adds and saves Python list to file"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
if path.exists("add_item.json")
    pythonList = load_from_json_file('add_item.json')
else:
    pythonList = []

pythonList.extend(args)

save_to_json_file(pythonList, 'add_item.json')
