#!/usr/bin/python3
"""sends a request to the URL"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values, 'utf-8')
    full_url = url + '?' + data
    with request.urlopen(full_url) as response:
        if hasattr(response.info(), 'email'):
            print(response.info().get('email'))
