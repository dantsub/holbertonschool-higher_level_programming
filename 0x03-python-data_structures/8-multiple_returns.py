#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tuple1 = (0, None)
    else:
        tuple1 = (len(sentence), sentence[0])
    return tuple1
