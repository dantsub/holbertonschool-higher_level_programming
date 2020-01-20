#!/usr/bin/python3
""" Return True or False
"""


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        otherwise False.
    Args:
        obj: a object
        a_class: a Class
        Return: True or False
    """
    tyob = type(obj)
    return True if issubclass(tyob, a_class) and tyob != a_class else False
