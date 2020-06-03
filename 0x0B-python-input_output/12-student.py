#!/usr/bin/python3
"""Student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student instance to jason with filter
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        dict = {}
        for i in attrs:
            if i in self.__dict__:
                dict[i] = self.__dict__[i]
        return dict
