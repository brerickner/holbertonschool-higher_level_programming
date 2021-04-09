#!/usr/bin/python3
'''Python script that fetches https://intranet.hbtn.io/status'''

import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print("\t- type: {}".format(r))
    print("\t- content: {}".format(r.text))
