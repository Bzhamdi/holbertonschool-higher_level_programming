#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """height.getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height.setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width.getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width.setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ rectangle.area """
        return self.__height * self.__width

    def perimeter(self):
        """ rectangle.perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ printable string """
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        str += "\n".join("#" * self.__width
                         for j in range(self.__height))
        return str

    def __repr__(self):
        """string_reproduction"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ notifiction when delete """
        print("Bye rectangle...")
