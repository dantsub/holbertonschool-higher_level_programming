#!/usr/bin/python3
# information about status url
import urllib.request as request


if __name__ == '__main__':
    with request.urlopen("https://intranet.hbtn.io/status") as reponse:
        page = reponse.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf-8')))
