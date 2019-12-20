#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    divis = sum([sec for one, sec in my_list])
    divid = sum([one * sec for one, sec in my_list])
    return divid / divis
