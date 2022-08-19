#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
values = {'X-Request-Id': sys.argv[2]}

data = urllib.parse.urlencode(values)
url = url + '?' + data

with urllib.request.urlopen(url) as response:
    for key, value in response.info().items():
        if key == 'X-Request-Id':
            print(value)
