#!/usr/bin/python3
"""Student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Student instance to jason"""
        return self.__dict__
