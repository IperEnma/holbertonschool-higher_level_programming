#!/usr/bin/python3
"""sends a request to the URL and display"""
from sys import argv
import requests
from requests.exceptions import HTTPError


if __name__ == '__main__':
    url = argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.content.decode())
    except HTTPError as error:
        if(error.response.status_code >= 400):
            print(error.response.status_code)
