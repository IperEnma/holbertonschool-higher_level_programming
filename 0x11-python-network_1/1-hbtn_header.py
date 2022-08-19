#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

from urllib import request, parse
import sys

url = sys.argv[1]
values = {'X-Request-Id': sys.argv[2]}

data = parse.urlencode(values)
url = url + '?' + data

with request.urlopen(url) as response:
    for key, value in response.info().items():
        if key == 'X-Request-Id':
            print(value)