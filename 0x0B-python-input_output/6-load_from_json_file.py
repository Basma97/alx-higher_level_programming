#!/usr/bin/python3
"""creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """creats an obj from json"""
    with open(filename, 'r', encoding="utf-8") as j:
        return json.load(j)
