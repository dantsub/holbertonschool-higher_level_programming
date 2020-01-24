#!/usr/bin/python3
"""
Base module
"""
import json


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__+ '.json'
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                dicts = [dic.to_dictionary() for dic in list_objs]
                file.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Square":
                instance = cls(2)
            else:
                instance = cls(2, 4)
            instance.update(**dictionary)
            return instance
