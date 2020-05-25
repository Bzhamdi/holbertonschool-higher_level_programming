#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        s = ""
        if self.__width == 0 or self.__height == 0:
            return str
        s += "\n".join(str(self.print_symbol) * self.__width
                       for j in range(self.__height))
        return s

    def __repr__(self):
        """string_reproduction"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ notifiction when delete """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ the biggest rectangle's area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
