#!/usr/bin/python3
# takes in a letter and sends a POST request
import requests
from sys import argv as av


if __name__ == '__main__':
    req = requests.get('https://api.github.com/user', auth=(av[1], av[2]))
    print(req.json().get("id"))
