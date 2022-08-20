#!/usr/bin/python3
"""credential git"""
import requests
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    token = argv[2]
    response = requests.get("https://api.github.com/user", auth=(user, token)).json()

    print(response['id'])
