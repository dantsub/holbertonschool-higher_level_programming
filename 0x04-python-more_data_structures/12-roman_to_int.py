#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
        rm = [s for s in roman_string]
        res = 0
        l = len(rm)
        for idx in range(l):
            if idx < l - 1 and rom.get(rm[idx]) < rom.get(rm[idx + 1]):
                res -= rom.get(rm[idx])
            else:
                res += rom.get(rm[idx])
        return res
    return 0
