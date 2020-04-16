#!/usr/bin/python3
# POST Request
import urllib.request as request
import urllib.parse as parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    data = {"email": argv[2]}

    post = parse.urlencode(data).encode("utf-8")
    req = request.Request(url, post)

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
