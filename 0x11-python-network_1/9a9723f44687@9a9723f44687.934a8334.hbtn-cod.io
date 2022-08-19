#!/usr/bin/python3
"""sends a request to the URL"""
import sys
from urllib import request, parse
from urllib.error import HTTPError

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values, 'utf-8')
    url = url + '?' + data

    with request.urlopen(url) as response:
        html = response.read()
        print(html.decode('utf-8'))

