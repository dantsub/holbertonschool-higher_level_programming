#!/usr/bin/python3
""" Peak Module """


def find_peak(list_of_integers):
    """
    find_peak function find a peak
    Args:
    list_of_integers
    """
    if type(list_of_integers) == list:
        if len(list_of_integers) == 0:
            return None
        return max(list_of_integers)
    return None
