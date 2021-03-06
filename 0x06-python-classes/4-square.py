#!/usr/bin/python3
"""Define class """


class Square:
    """class """
    def __init__(self, size=0):
        """cons """
        self.__size = size

    def area(self):
        """area """
        return self.__size ** 2

    @property
    def size(self):
        """the size """
        return self.__size

    @size.setter
    def size(self, value):
        """size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
