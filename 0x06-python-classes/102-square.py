#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ rep of a square class"""

    def __init__(self, size=0):
        """ constructor"""
        self.__size = size

        """ Getter the private attr size"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ method that  returns .."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ define the equal of a square area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equal a square area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """ define the greaterthan of a square area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """ comparison of a square area"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """ define the lessthan comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """ lessthanequal comparison of a square area"""
        return self.area() <= other.area()
