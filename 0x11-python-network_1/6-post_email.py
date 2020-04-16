#!/usr/bin/python3
# POST request with requests package
import requests
from sys import argv as av


if __name__ == '__main__':
    url, data = av[1], {"email": av[2]}
    req = requests.post(url, data=data)
    print(req.text)
