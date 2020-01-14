#!/usr/bin/python3
"""  """
def text_indentation(text):
    """
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.rstrip()
    size = len(text)
    idx = 0

    while idx < size and ord(text[idx]) == 32:
        idx += 1

    while idx < size:
        if text[idx] in ".?:":
            print("{:s}".format(text[idx]), end="\n\n")
            while (idx + 1) < size and ord(text[idx + 1]) == 32:
                idx += 1
        else:
            print("{:s}".format(text[idx]), end="")

        idx += 1
