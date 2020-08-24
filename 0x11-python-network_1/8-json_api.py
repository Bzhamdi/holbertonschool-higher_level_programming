#!/usr/bin/python3
"""
post and a response as json
"""
import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    src = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=src)
    try:
        res_json = response.json()
        id = res_json.get('id')
        name = res_json.get('name')
        if res_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_json.get('id'), res_json.get('name')))
    except BaseException:
        print("Not a valid JSON")
