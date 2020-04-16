#!/usr/bin/python3
# Handle errors HTTP with requests package
import requests
from sys import argv as av


if __name__ == '__main__':
    req = requests.get(av[1])

    if req.status_code > 399:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
