#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __le__(self, other):
        """less than"""
        return self.size <= other.size

    def __eq__(self, other):
        """equal"""
        return self.size == other.size

    def __ne__(self, other):
        """not equal"""
        return self.size != other.size

    def __gt__(self, other):
        """greater than"""
        return self.size > other.size

    def __ge__(self, other):
        """greater than or equal"""
        return self.size >= other.size
