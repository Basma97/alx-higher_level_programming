#!/usr/bin/python3
"""a square"""


class Square():
    """define square"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        self.size = size
        self.position = position

        """Private attribute"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """make the value of the set meet a standard"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """constructor"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position 2 positive integers")
        self.__position = value

    def area(self):
        """method that return .."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print ...."""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
