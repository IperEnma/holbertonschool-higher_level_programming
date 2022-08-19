#!/usr/bin/python3
"""get send parameter"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    data = {'email': argv[2]}
    response = requests.post(url, data)
    print(response.content.decode())
