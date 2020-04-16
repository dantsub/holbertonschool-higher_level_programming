#!/usr/bin/python3
#
import requests
from sys import argv as av

if __name__ == '__main__':
    res = "" if len(av) == 1 else av[1]
    data = {"q": res}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
