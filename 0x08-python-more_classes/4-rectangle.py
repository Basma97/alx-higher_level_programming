#!/usr/bin/python3
""" class module"""


class Rectangle:
    """rectangle class """
    def __init__(self, width=0, height=0):
        """ instantation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ the getter"""
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
        """ the getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance"""
        return self.__height * self.__width

    def perimeter(self):
        """ public"""
        if self.__height == 0 or self.__width == int(0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ the string"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec_print = []
        for i in range(self.__height):
            [rec_print.append("#") for j in range(self.width)]
            if i != self.height - 1:
                rec_print.append("\n")
        return ("".join(rec_print))

    def __repr__(self):
        """ string repo"""
        rect_rep = "Rectangle(" + str(self.__width)
        rect_rep += ", " + str(self.__height) + ")"
        return rect_rep
