#!/usr/bin/python3
"""
containes class Rectangle
"""
from models.rectangle import *


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ toString"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """size.get()"""
        return self.width

    @size.setter
    def size(self, size):
        """size.set()"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method """
        if len(args):
            for i, x in enumerate(args):
                if i == 0:
                    self.id = x
                elif i == 1:
                    self.size = x
                elif i == 2:
                    self.x = x
                elif i == 3:
                    self.y = x
        else:
            for i, x in kwargs.items():
                setattr(self, i, x)

    def to_dictionary(self):
        """dictionary representation"""
        dec = {}
        dec["id"] = self.id
        dec["x"] = self.x
        dec["size"] = self.height
        dec["y"] = self.y
        return dec
