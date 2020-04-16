#!/usr/bin/python3
# print X-Request-Id of url pass to argument
import urllib.request as request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as reponse:
        headers = reponse.getheaders()
        x_id = [item[1] for item in headers if item[0] == "X-Request-Id"]
        try:
            print(x_id[0])
        except:
            print("None")
