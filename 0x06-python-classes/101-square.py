#!/usr/bin/python3
""" a square"""


class Square():
    """ define A square"""

    def __init__(self, size=0, position=(0, 0)):
        """ constructor"""
        self.size = size
        self.position = position

        """Private attribute"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """make the value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Private instance attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """the area of the class obj"""
        return (self.__size * self.__size)

    def my_print(self):
        """Public instance method"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """string re square"""
        if self.__size != 0:
            [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print()
        return ("")
