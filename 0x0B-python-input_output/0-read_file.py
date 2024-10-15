#!/usr/bin/python3
"""defining readfile"""


def read_file(filename=""):
    """red filename with utf"""
    with open(filename, encoding='utf-8') as u:
        print(u.read(), end="")
