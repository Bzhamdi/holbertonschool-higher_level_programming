#!/usr/bin/python3
"""Define class """
import math


class MagicClass:
    """class """

    def __init__(self, radius=0):
        """cons"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ar """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """cirxy"""
        return 2 * math.pi * self.__radius
