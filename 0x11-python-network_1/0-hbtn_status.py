#!/usr/bin/python3
"""scrip that fetches"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    print("Body response:")
    html = response.read()
    print("{}- type: {}".format(11, type(html)))
    print("{}- content: {}".format(11, html))
    print("{}- utf8 content: {}".format(11, html.decode()))
