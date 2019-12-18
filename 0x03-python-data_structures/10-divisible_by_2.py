#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for idx in range(len(my_list)):
        if (new[idx] % 2 == 0):
            new[idx] = True
        else:
            new[idx] = False
    return new
