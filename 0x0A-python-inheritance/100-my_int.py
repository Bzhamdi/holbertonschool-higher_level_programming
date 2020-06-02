#!/usr/bin/python3
"""Myint"""


class MyInt(int):
    """ class MyInt """

    def __eq__(self, other):
        """re__eq__"""
        return int(self) != int(other)

    def __ne__(self, other):
        """re__ne__"""
        return int(self) == int(other)
