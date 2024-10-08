#!/usr/bin/python3
"""class module"""


class Rectangle:
    """ the rectangle class """
    def __init__(self, width=0, height=0):
        """ instantation of class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ the getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
