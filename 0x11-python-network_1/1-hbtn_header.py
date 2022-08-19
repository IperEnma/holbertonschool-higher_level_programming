#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys


url = sys.argv[1]
""" values = {'X-Request-Id': sys.argv[2]}
data = parse.urlencode(values)
url = url + '?' + data"""
with urllib.request.urlopen(url) as response:
    """for key, value in response.info().items():
        if key == 'X-Request-Id':
            print(value)"""
    print(response.info()['X-Request-Id'])
