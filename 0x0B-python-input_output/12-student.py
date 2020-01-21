#!/usr/bin/python3
"""
Class Student
"""


class Student():
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        """ Initialize Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that retrieves a dictionary
            representation of a Student instance
        """
        dicc = self.__dict__
        if (type(attrs) == list and 
                all(type(st) == str for st in attrs)):
            return {y: dicc[y] for y in dicc if y in attrs}
        return dicc
