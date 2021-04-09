#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).'''

import urllib.request
import sys
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            meow = response.read()
            print(meow.decode(encoding="UTF-8"))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
