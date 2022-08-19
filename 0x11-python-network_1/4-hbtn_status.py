#!/usr/bin/python3
"""Python script that fetches"""
import requests


if __name__ == '__main__':

    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print("Bode response:")
    print("\t- type: {}".format(type(response.content.decode())))
    print("\t- content: {}".format(response.content.decode()))
