#!/usr/bin/python3
"""
Base module
"""
import json
import csv


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
        """ Get id attribute """
        return self.__id

    @id.setter
    def id(self, value):
        """ Set of id attribute
        Args:
            value (int): value of id
        """
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method that returns the JSON string
            representation of list_dictionaries
        Args:
            list_dictionaries (list of dicts):
                List of dictionaries

        return: The JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string
            representation of list_objs to a file
        Args:
            cls: Class, maybe Rectangle or Square

        list_objs: a list of instances who inherits of Base
            - example: list of Rectangle or list of Square instances
        """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                dicts = [dic.to_dictionary() for dic in list_objs]
                file.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Method that returns the list of the
            JSON string representation json_string
        Args:
            json_string: a string representing a list of dictionaries

        Return: JSON string representation
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Method that returns an instance with all attributes already set
        Args:
            cls (class): Rectangle or Square
            **dictionary:
                can be thought of as a double pointer to a dictionary
        return: Instance
        """
        if cls.__name__ == "Rectangle":
            instance = cls(2, 4)  # create a new instance
        else:
            instance = cls(2)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ That returns a list of instances
        Args:
            cls (class): Rectangle or Square

            raises:
                IOError: return []

            Return: a list of instances or []
        """
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                ls_of_dic = Base.from_json_string(file.read())
                return [cls.create(**dics) for dics in ls_of_dic]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method thats serializes in CSV
        Args:
            cls (class): Rectangle or Square

        raises:
            IOError: return []

        Return:
            Rectangle - <id>,<width>,<height>,<x>,<y>
            Square - <id>,<size>,<x>,<y>
        """
        csvfile = '{}.csv'.format(cls.__name__)
        with open(csvfile, 'w', newline='') as csvf:
            if list_objs is None or list_objs == []:
                csvf.write('[]')
            else:
                if cls.__name__ == 'Square':
                    fields = ["id", "size", "x", "y"]
                if cls.__name__ == 'Rectangle':
                    fields = ["id", "width", "height", "x", "y"]
                doc = csv.DictWriter(csvf, fieldnames=fields)
                [doc.writerow(inst.to_dictionary()) for inst in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """ Method thats deserializes in CSV
        Args:
            cls (class): Rectangle or Square

        raises:
            IOError: return []

        Return:
            Rectangle - <id>,<width>,<height>,<x>,<y>
            Square - <id>,<size>,<x>,<y>
        """
        csvfile = '{}.csv'.format(cls.__name__)
        try:
            with open(csvfile, 'r', newline='') as csvf:
                if cls.__name__ == 'Square':
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                doc = csv.DictReader(csvf, fieldnames=fields)
                ls_of_dics = [{k: int(v) for k, v in dic.items()}
                              for dic in doc]
                return [cls.create(**dics) for dics in ls_of_dics]
        except IOError:
            return []
