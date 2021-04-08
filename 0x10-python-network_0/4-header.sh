#!/bin/bash
# Bash script that takes in a URL as an argument and displays the body
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
