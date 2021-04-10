#!/usr/bin/python3
'''Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''

import requests
import sys
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    token = sys.argv[2]
    auth = HTTPBasicAuth(user, token)

    r = requests.get(url, auth=auth)

    try:
        print(r.json().get('id'))
    except BaseException:
        print("None")
