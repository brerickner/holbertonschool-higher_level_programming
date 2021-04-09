#!/usr/bin/python3
'''Python script that fetches https://intranet.hbtn.io/status'''

import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    meow = r.text
    print("Body response:")
    print("\t- type: {}".format(type(meow)))
    print("\t- content: {}".format(meow))
