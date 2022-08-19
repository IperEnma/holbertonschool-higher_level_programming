#!/usr/bin/python3
"""scrip that fetches"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    print("Body response:")
    html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode()))
