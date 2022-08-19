#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
