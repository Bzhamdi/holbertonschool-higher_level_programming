#!/usr/bin/python3
"""
crud get response get top 10 commit from github
"""

import requests
import sys

if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    repos = r.json()
    for x in repos[0:10]:
        print(
            "{}: {}".format(
                x.get('sha'),
                x.get('commit').get('author').get('name')))
