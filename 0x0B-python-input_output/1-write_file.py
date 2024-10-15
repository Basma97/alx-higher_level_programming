#!/usr/bin/python3
"""define write file"""


def write_file(filename="", text=""):
    """reads filename"""
    with open(filename, "w", encoding='utf-8') as c:
        return c.write(text)
