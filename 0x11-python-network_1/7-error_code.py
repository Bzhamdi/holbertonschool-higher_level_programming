#!/usr/bin/python3
import requests
import sys
"""
error code
"""

try:
    response = requests.get(sys.argv[1])

        
    print(response.text)
    
except Exception as err:
    print("Error code: {}".format(response.status_code))
