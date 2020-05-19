#!/usr/bin/python3
"""Define class """


class Square:
    """ class square """
    def __init__(self, size=0):
        """ cons """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
