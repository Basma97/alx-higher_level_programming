#!/usr/bin/python3
"""define append """


def append_write(filename="", text=""):
    """append file with utf"""
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
