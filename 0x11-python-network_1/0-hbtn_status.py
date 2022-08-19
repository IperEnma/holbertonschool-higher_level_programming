#!/usr/bin/python3
"""scrip that fetches"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    print("Body response:")
    html = response.read()
    print("   - type: {}".format(type(html)))
    print("   - content: {}".format(html))
    print("   - utf8 content: {}".format(html.decode()))
