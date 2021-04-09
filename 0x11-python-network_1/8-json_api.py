#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    try:
        q = sys.argv[1]
    except BaseException:
        q = ""

    jsonIn = {'q': q}
    try:
        r = requests.post(url, data=jsonIn).json()
        if not r:
            print("No result")
        else:
            theId = r.get('id')
            name = r.get('name')
            print("[{}] {}".format(theId, name))
    except BaseException:
        print("Not a valid JSON")
