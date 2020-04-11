#!/usr/bin/python3
""" Peak Module """


def find_peak(list_of_integers):
    """
    find_peak - function find a peak
    Args:
    list_of_integers
    """
    if list_of_integers == []:
        return None
    lenlist = len(list_of_integers)
    if lenlist == 1:
        return list_of_integers[0]
    if lenlist == 2:
        return max(list_of_integers)
    return list_of_integers[peak(list_of_integers, 0, lenlist - 1)]


def peak(listin, left, right):
    """
    peak - search the peak with recursion
    Args:
    listin: list of integer
    left: left of list
    right: right of list
    return: position of the peak
    """
    if left == right:
        return left
    mid = int((left + right) / 2)
    if listin[mid] > listin[mid + 1]:
        return peak(listin, left, mid)
    return peak(listin, mid + 1, right)
