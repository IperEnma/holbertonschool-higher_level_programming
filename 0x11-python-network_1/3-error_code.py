#!/usr/bin/python3
"""handled errors"""
from sys import argv
from urllib import request
from urllib.error import HTTPError


if __name__ == '__main__':
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode())
    except HTTPError as error:
        print("Error code: {}".format(error.code))
