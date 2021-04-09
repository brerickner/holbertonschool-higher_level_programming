#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)'''

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {
        'email': email
    }
    data = urllib.parse.urlencode(values)
    data = value.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        meow = response.info()
        print(meow)
        theMeow = meow.data('email')
        print(theMeow, meow)
