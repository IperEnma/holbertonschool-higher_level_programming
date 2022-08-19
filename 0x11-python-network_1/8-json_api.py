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
    response = requests.post(url, data)
    result = response.content.decode()
    result_dict = eval(result)
    if(type(result_dict) != dict):
        print("Not a valid JSON")
    elif(len(result_dict) == 0):
        print("No result")
    else:
        print("[{}] {}".format(result_dict['id'], result_dict['name']))
