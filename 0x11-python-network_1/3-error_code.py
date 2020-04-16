#!/usr/bin/python3
# Handle HTTP errors
import urllib.request as request
import urllib.error as error
from sys import argv


if __name__ == '__main__':
    try:
        url = request.Request(argv[1])
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
