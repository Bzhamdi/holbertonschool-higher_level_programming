#!/usr/bin/python3
"""
authentification + crud get response
"""

import requests
import sys
if __name__ == '__main__':
    s = requests.Session()
    s.auth = (sys.argv[1], sys.argv[2])
    r = s.get('https://api.github.com/user')
    print(r.json().get('id'))
