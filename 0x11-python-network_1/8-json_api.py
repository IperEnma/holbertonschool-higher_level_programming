#!/usr/bin/python3
"""JSON API PYTHON """
from sys import argv
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if (len(argv) > 1):
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    try:
        response = requests.post(url, data).json()
        if(len(response) == 0):
            print("No result")
        else:
            if (hasattr(response, 'id') and hasattr(response, 'name)')):
                print("[{}] {}".format(response['id'], response['name']))
    except Exception as e:
        print(e)
        print("Not a valid JSON")
