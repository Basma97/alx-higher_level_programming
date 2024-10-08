#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ define a square"""

    def __init__(self, size=0):
        """ constructor"""
        self.__size = size

    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ property for the length of a side square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ method that  returns the current square area"""
        return (self.__size * self.__size)
