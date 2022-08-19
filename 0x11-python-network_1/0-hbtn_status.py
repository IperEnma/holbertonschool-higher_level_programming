#!/usr/bin/python3
"""scrip that fetches"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    print("Bode response:")
    print("- type: {}".format(response.code))
    html = response.read()
    print("- content: {}".format(html))
    print("- utf8 content: {}".format(html.decode()))
