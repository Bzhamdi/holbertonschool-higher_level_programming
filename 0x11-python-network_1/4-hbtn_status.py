#!/usr/bin/python3
"""Paython script that fetches https://intranet.hbtn.io/status
with urllib
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read().decode()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
