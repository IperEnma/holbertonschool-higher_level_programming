#!/usr/bin/python3
"""sends a request to the URL"""
import sys
from urllib import request, parse
from urllib.error import URLError

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')

    try:
        request.urlopen(url, data)
    except URLError as e:
        print(e.reason)
