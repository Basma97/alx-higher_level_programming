#!/usr/bin/python3
"""define save to json"""


import json


def save_to_json_file(my_obj, filename):
    """write an obj to text"""
    with open(filename, 'w', encoding="utf-8") as o:
        json.dump(my_obj, o)
