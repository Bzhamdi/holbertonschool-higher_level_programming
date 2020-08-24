#!/usr/bin/python3
"""error code
"""
import urllib.request
import sys
import urllib.error



if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:        
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
