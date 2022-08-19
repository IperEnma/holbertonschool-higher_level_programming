#!/usr/bin/python3
"""sends a request to the URL"""

from urllib import parse, request
import sys

url = sys.argv[1]
with request.urlopen(url) as response:
    for key, value in response.info().items():
        if key == 'X-Request-Id':
            print(value)
