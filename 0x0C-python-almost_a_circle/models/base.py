#!/usr/bin/python3
"""
module contains the Base
"""


import json
import os.path as path
import csv


class Base:
    " the Base class"
    __nb_objects = 0

    def __init__(self, id=None):
        "constroctor"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        dic = []
        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))
        with open(file_name, 'w') as file:
            file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            re = cls(1, 2)
        else:
            re = cls(1)
        re.update(**dictionary)
        return re

    @classmethod
    def load_from_file(cls):
        """returns a list of instances """
        filename = cls.__name__ + ".json"
        lines = []
        if path.exists(filename):
            with open(filename) as file:
                lines = cls.from_json_string(file.read())
            for i, e in enumerate(lines):
                lines[i] = cls.create(**lines[i])
        return lines

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save in csv return list of obj"""
        with open(cls.__name__ + ".csv", 'w') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    fnames = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    csv_writer.writerow(fnames)
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    fnamess = [obj.id, obj.size, obj.x, obj.y]
                    csv_writer.writerow(fnamess)

    @classmethod
    def load_from_file_csv(cls):
        """
        load from csv file method
        Returns:list of objects
        """
        if path.exists(cls.__name__ + ".csv") is False:
            return []
        with open(cls.__name__ + ".csv", 'r') as file:
            lst = []
            reader = csv.reader(file)
            for i in reader:
                if cls.__name__ is "Rectangle":
                    dic = {"id": int(i[0]),
                           "width": int(i[1]),
                           "height": int(i[2]),
                           "x": int(i[3]),
                           "y": int(i[4])}
                elif cls.__name__ is "Square":
                    dic = {"id": int(i[0]), "size": int(i[1]),
                           "x": int(i[2]), "y": int(i[3])}
                o = cls.create(**dic)
                lst.append(o)
        return lst
