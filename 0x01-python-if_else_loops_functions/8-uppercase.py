#!/usr/bin/python3
def uppercase(str):
    for word in str:
        letter = ord(word)
        if (96 < letter < 123):
            letter = letter - 32
        print('{:c}'.format(letter), end='')
    print()
